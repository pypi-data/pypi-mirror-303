from itertools import zip_longest
import re


version_pattern = re.compile(
    # regex for Semantic Versions : https://semver.org/
    r"^(?P<semantic>"
    r"(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)"
    r"(?P<prerelease>-[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*)?"
    r"(?P<buildmetadata>\+[0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*)?"
    r")$"
    r"|"
    # regex for Version specifiers : https://packaging.python.org/en/latest/specifications/version-specifiers
    r"^(?P<PEP440>"
    r"\s*"
    r"v?"
    r"(?:(?P<epoch>[0-9]+)!)?"
    r"(?P<release>\d*)"
    r"(?P<subreleases>(\.\d+)*)"
    r"(?:[._-]?(?P<prerelease_signifier>(alpha|a|beta|b|c|preview|pre|rc))(?:[._-]?(?P<prerelease_numeral>[0-9]+))?)?"
    r"([._-]?(?P<postrelease_signifier>(post|rev|r))[._-]?(?P<postrelease_numeral>[0-9]+)?|(?P<postrelease_signifier2>-)[._-]?(?P<postrelease_numeral2>[0-9]+))?"
    r"(?:[._-]?(?P<devrelease_signifier>dev)(?:[._-]?(?P<devrelease_numeral>[0-9]+))?)?"
    r"(\+(?P<local>[0-9A-Za-z]+([._-][0-9A-Za-z]+)*))?"
    r"\s*"
    r")$",
    re.I,
)

SIGNIFIERS = {
    # prerelease signifiers
    "a": "a",
    "alpha": "a",
    "b": "b",
    "beta": "b",
    "c": "rc",
    "pre": "rc",
    "preview": "rc",
    "rc": "rc",
}


class Version:
    def __init__(self, version):
        self.is_semantic = False
        self.is_pep440 = False
        self.epoch = 0
        self.release = []
        self.prerelease = []
        self.postrelease = []
        self.devrelease = []
        self.local = []
        self.buildmetadata = ""

        # Parsing verison for comparisons
        parts = version_pattern.match(version)
        if parts is None:
            raise ValueError
        if parts.group("semantic") is not None:
            self.is_semantic = True
            self.release = [
                int(parts.group("major") or "0"),
                int(parts.group("minor") or "0"),
                int(parts.group("patch") or "0"),
            ]
            if parts.group("prerelease") is None:
                self.prerelease = []
            else:
                self.prerelease = parts.group("prerelease")[1:].split(".")
            self.buildmetadata = parts.group("buildmetadata") or ""
        elif parts.group("PEP440") is not None:
            self.is_pep440 = True
            self.epoch = int(parts.group("epoch") or "0")
            self.release = [int(parts.group("release") or "0")]
            for idx, subrelease in enumerate(parts.group("subreleases")[1:].split(".")):
                if subrelease != "":
                    self.release.append(int(subrelease))
            if (parts.group("prerelease_signifier") or "").lower() in SIGNIFIERS:
                self.prerelease.append(
                    SIGNIFIERS[parts.group("prerelease_signifier").lower()]
                )
                self.prerelease.append(parts.group("prerelease_numeral") or "0")
            if parts.group("postrelease_signifier"):
                self.postrelease.append("post")
                self.postrelease.append(parts.group("postrelease_numeral") or "0")
            if parts.group("postrelease_signifier2"):
                self.postrelease.append("post")
                self.postrelease.append(parts.group("postrelease_numeral2") or "0")
            if parts.group("devrelease_signifier"):
                self.devrelease.append("dev")
                self.devrelease.append(parts.group("devrelease_numeral") or "0")
            if parts.group("local"):
                self.local = re.split(r"[._-]", parts.group("local"))

    def compare_releases(self, releases):
        for release in releases:
            self_release = int(release[0])
            other_release = int(release[1])
            if self_release < other_release:
                return -1
            elif self_release > other_release:
                return 1
        return 0

    def compare_semantic_prereleases(self, prereleases):
        # https://semver.org/#spec-item-11
        for prerelease in prereleases:
            try:
                self_prerelease = int(prerelease[0])
            except (ValueError, TypeError):
                self_prerelease = prerelease[0]
            try:
                other_prerelease = int(prerelease[1])
            except (ValueError, TypeError):
                other_prerelease = prerelease[1]
            # Identifiers consisting of only digits are compared numerically.
            # Identifiers with letters or hyphens are compared lexically in ASCII sort
            # order.
            if type(self_prerelease) == type(other_prerelease):
                if self_prerelease < other_prerelease:
                    return -1
                elif self_prerelease > other_prerelease:
                    return 1
            else:
                # Numeric identifiers always have lower precedence than non-numeric
                # identifiers.
                if isinstance(self_prerelease, int) and isinstance(
                    other_prerelease, str
                ):
                    return -1
                if isinstance(self_prerelease, str) and isinstance(
                    other_prerelease, int
                ):
                    return 1
                # A larger set of pre-release fields has a higher precedence than a
                # smaller set, if all of the preceding identifiers are equal.
                if self_prerelease is None:
                    return -1
                if self_prerelease is not None:
                    return 1
        return 0

    def compare_pep440_prereleases(self, prereleases):
        # https://packaging.python.org/en/latest/specifications/version-specifiers/#pre-releases
        for prerelease in prereleases:
            try:
                self_prerelease = int(prerelease[0])
            except (ValueError, TypeError):
                self_prerelease = prerelease[0]
            try:
                other_prerelease = int(prerelease[1])
            except (ValueError, TypeError):
                other_prerelease = prerelease[1]
            # Pre-releases for a given release are ordered first by phase (alpha, beta,
            # release candidate) and then by the numerical component within that phase.
            if self_prerelease < other_prerelease:
                return -1
            elif self_prerelease > other_prerelease:
                return 1
        return 0

    def compare_pep440_postreleases(self, postreleases):
        # https://packaging.python.org/en/latest/specifications/version-specifiers/#post-releases
        for postrelease in postreleases:
            try:
                self_postrelease = int(postrelease[0])
            except (ValueError, TypeError):
                self_postrelease = postrelease[0]
            try:
                other_postrelease = int(postrelease[1])
            except (ValueError, TypeError):
                other_postrelease = postrelease[1]
            # Post-releases are ordered by their numerical component, immediately
            # following the corresponding release, and ahead of any subsequent release.
            if self_postrelease < other_postrelease:
                return -1
            elif self_postrelease > other_postrelease:
                return 1
        return 0

    def __lt__(self, other):
        if self.epoch < other.epoch:
            return True
        if self.epoch > other.epoch:
            return False
        # Semantic Version
        # Precedence is determined by the first difference when comparing each of these
        # identifiers from left to right as follows: Major, minor, and patch versions
        # are always compared numerically.
        # PEP440 Version
        # Comparison and ordering of release segments considers the numeric value of
        # each component of the release segment in turn. When comparing release
        # segments with different numbers of components, the shorter segment is
        # padded out with additional zeros as necessary.
        if (
            self.compare_releases(
                zip_longest(self.release, other.release, fillvalue="0")
            )
            < 0
        ):
            return True
        if (
            self.compare_releases(
                zip_longest(self.release, other.release, fillvalue="0")
            )
            > 0
        ):
            return False
        if self.is_semantic:
            # When major, minor, and patch are equal, a pre-release version has lower
            # precedence than a normal version
            if len(self.prerelease) > 0 and len(other.prerelease) == 0:
                return True
            if len(self.prerelease) == 0 and len(other.prerelease) > 0:
                return False
            # Precedence for two pre-release versions with the same major, minor, and
            # patch version MUST be determined by comparing each dot separated
            # identifier from left to right until a difference is found as follows.
            if (
                self.compare_semantic_prereleases(
                    zip_longest(self.prerelease, other.prerelease)
                )
                < 0
            ):
                return True
            if (
                self.compare_semantic_prereleases(
                    zip_longest(self.prerelease, other.prerelease)
                )
                > 0
            ):
                return False
        if self.is_pep440:
            if len(self.prerelease) > 0 and len(other.prerelease) == 0:
                return True
            if len(self.prerelease) == 0 and len(other.prerelease) > 0:
                return False
            # Pre-releases for a given release are ordered first by phase (alpha, beta,
            # release candidate) and then by the numerical component within that phase.
            if (
                self.compare_pep440_prereleases(
                    zip_longest(self.prerelease, other.prerelease)
                )
                < 0
            ):
                return True
            if (
                self.compare_pep440_prereleases(
                    zip_longest(self.prerelease, other.prerelease)
                )
                > 0
            ):
                return False
            if len(self.postrelease) == 0 and len(other.postrelease) > 0:
                return True
            if len(self.postrelease) > 0 and len(other.postrelease) == 0:
                return False
            # Post-releases are ordered by their numerical component, immediately
            # following the corresponding release, and ahead of any subsequent release.
            if (
                self.compare_pep440_postreleases(
                    zip_longest(self.postrelease, other.postrelease)
                )
                < 0
            ):
                return True
            if (
                self.compare_pep440_postreleases(
                    zip_longest(self.postrelease, other.postrelease)
                )
                > 0
            ):
                return False
        return False

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        if self.epoch > other.epoch:
            return True
        if self.epoch < other.epoch:
            return False
        # Semantic Version
        # Precedence is determined by the first difference when comparing each of these
        # identifiers from left to right as follows: Major, minor, and patch versions
        # are always compared numerically.
        if (
            self.compare_releases(
                zip_longest(self.release, other.release, fillvalue="0")
            )
            > 0
        ):
            return True
        if (
            self.compare_releases(
                zip_longest(self.release, other.release, fillvalue="0")
            )
            < 0
        ):
            return False
        if self.is_semantic:
            # When major, minor, and patch are equal, a pre-release version has lower
            # precedence than a normal version
            if len(self.prerelease) == 0 and len(other.prerelease) > 0:
                return True
            if len(self.prerelease) > 0 and len(other.prerelease) == 0:
                return False
            # Precedence for two pre-release versions with the same major, minor, and
            # patch version MUST be determined by comparing each dot separated
            # identifier from left to right until a difference is found as follows.
            if (
                self.compare_semantic_prereleases(
                    zip_longest(self.prerelease, other.prerelease)
                )
                > 0
            ):
                return True
            if (
                self.compare_semantic_prereleases(
                    zip_longest(self.prerelease, other.prerelease)
                )
                < 0
            ):
                return False
        if self.is_pep440:
            if len(self.prerelease) == 0 and len(other.prerelease) > 0:
                return True
            if len(self.prerelease) > 0 and len(other.prerelease) == 0:
                return False
            # Pre-releases for a given release are ordered first by phase (alpha, beta,
            # release candidate) and then by the numerical component within that phase.
            if (
                self.compare_pep440_prereleases(
                    zip_longest(self.prerelease, other.prerelease)
                )
                > 0
            ):
                return True
            if (
                self.compare_pep440_prereleases(
                    zip_longest(self.prerelease, other.prerelease)
                )
                < 0
            ):
                return False
            if len(self.postrelease) > 0 and len(other.postrelease) == 0:
                return True
            if len(self.postrelease) == 0 and len(other.postrelease) > 0:
                return False
            # Post-releases are ordered by their numerical component, immediately
            # following the corresponding release, and ahead of any subsequent release.
            if (
                self.compare_pep440_postreleases(
                    zip_longest(self.postrelease, other.postrelease)
                )
                > 0
            ):
                return True
            if (
                self.compare_pep440_postreleases(
                    zip_longest(self.postrelease, other.postrelease)
                )
                < 0
            ):
                return False
        return False

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __eq__(self, other):
        return (
            self.epoch == other.epoch
            and self.compare_releases(
                zip_longest(self.release, other.release, fillvalue="0")
            )
            == 0
            and self.prerelease == other.prerelease
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        version = ".".join(map(str, self.release))
        if self.is_semantic:
            if len(self.prerelease) > 0:
                version = f"{version}-" + ".".join(self.prerelease)
            if self.buildmetadata != "":
                version = f"{version}{self.buildmetadata}"
        if self.is_pep440:
            if len(self.prerelease) > 0:
                version = f"{version}" + "".join(self.prerelease)
            if len(self.postrelease) > 0:
                version = f"{version}." + "".join(self.postrelease)
            if len(self.devrelease) > 0:
                version = f"{version}." + "".join(self.devrelease)
            if len(self.local) > 0:
                version = f"{version}+" + ".".join(self.local)

        return version
