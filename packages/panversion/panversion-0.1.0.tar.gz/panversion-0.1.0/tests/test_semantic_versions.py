import pytest

from panversion import Version
from tests.utils import sorting_comparison


def test_semantic_error():
    with pytest.raises(ValueError):
        Version("foobar")


def test_semantic_representation():
    assert str(Version("1.0.0")) == "1.0.0"
    assert str(Version("1.0.0-alpha")) == "1.0.0-alpha"
    assert str(Version("1.0.0-alpha+build")) == "1.0.0-alpha+build"
    assert str(Version("1.0.0+build")) == "1.0.0+build"


def test_semantic_equality():
    assert Version("1.0.0") == Version("1.0.0")
    assert Version("1.0.0-alpha") == Version("1.0.0-alpha+build")


def test_semantic_non_equality():
    assert Version("1.0.0") != Version("1.0.1")
    assert Version("1.0.0-alpha") != Version("1.0.1-alpha+build")


def test_semantic_lesser_than_major():
    assert Version("1.0.0") < Version("2.0.0")


def test_semantic_lesser_than_minor():
    assert Version("1.0.0") < Version("1.1.0")
    assert Version("1.8.0") < Version("1.10.0")


def test_semantic_lesser_than_patch():
    assert Version("1.0.0") < Version("1.0.1")
    assert Version("1.0.8") < Version("1.0.10")


def test_semantic_lesser_than_prerelease():
    assert Version("1.0.0-rc.1") < Version("1.0.0")
    assert Version("1.0.0-alpha") < Version("1.0.0-alpha.1")
    assert Version("1.0.0-alpha.1") < Version("1.0.0-alpha.beta")
    assert Version("1.0.0-0.3.7") < Version("1.0.0-alpha.beta")
    assert Version("1.0.0-alpha.beta") < Version("1.0.0-x.7.z.92")
    assert Version("1.0.0-x.7.z.92") < Version("1.0.0-x-y-z.--")
    assert Version("1.0.0-alpha.beta") < Version("1.0.0-rc.1")


def test_semantic_lesser_than_or_equal():
    assert Version("1.0.0") <= Version("1.0.0")
    assert Version("1.0.0+build") <= Version("1.0.0")
    assert Version("1.0.0") <= Version("2.0.0")
    assert Version("1.0.0") <= Version("1.1.0")
    assert Version("1.8.0") <= Version("1.10.0")
    assert Version("1.0.0") <= Version("1.0.1")
    assert Version("1.0.8") <= Version("1.0.10")
    assert Version("1.0.0-rc.1") <= Version("1.0.0")
    assert Version("1.0.0-alpha") <= Version("1.0.0-alpha+build")
    assert Version("1.0.0-alpha") <= Version("1.0.0-alpha.1")
    assert Version("1.0.0-alpha.1") <= Version("1.0.0-alpha.beta")
    assert Version("1.0.0-0.3.7") <= Version("1.0.0-alpha.beta")
    assert Version("1.0.0-alpha.beta") <= Version("1.0.0-x.7.z.92")
    assert Version("1.0.0-x.7.z.92") <= Version("1.0.0-x-y-z.--")
    assert Version("1.0.0-alpha.beta") <= Version("1.0.0-rc.1")
    assert Version("1.0.0-alpha") <= Version("1.0.0-alpha")


def test_semantic_greater_than():
    assert Version("1.0.0") > Version("1.0.0-rc.1")
    assert Version("1.0.0-alpha.1") > Version("1.0.0-alpha")
    assert Version("1.0.0-alpha.beta") > Version("1.0.0-alpha.1")
    assert Version("1.0.0-alpha.beta") > Version("1.0.0-0.3.7")
    assert Version("1.0.0-x.7.z.92") > Version("1.0.0-alpha.beta")
    assert Version("1.0.0-x-y-z.--") > Version("1.0.0-x.7.z.92")
    assert Version("1.0.0-rc.1") > Version("1.0.0-alpha.beta")


def test_semantic_greater_than_or_equal():
    assert Version("1.0.0") >= Version("1.0.0")
    assert Version("1.0.0") >= Version("1.0.0+build")
    assert Version("2.0.0") >= Version("1.0.0")
    assert Version("1.1.0") >= Version("1.0.0")
    assert Version("1.10.0") >= Version("1.8.0")
    assert Version("1.0.1") >= Version("1.0.0")
    assert Version("1.0.10") >= Version("1.0.8")
    assert Version("1.0.0") >= Version("1.0.0-rc.1")
    assert Version("1.0.0-alpha") >= Version("1.0.0-alpha+build")
    assert Version("1.0.0-alpha.1") >= Version("1.0.0-alpha")
    assert Version("1.0.0-alpha.beta") >= Version("1.0.0-alpha.1")
    assert Version("1.0.0-alpha.beta") >= Version("1.0.0-0.3.7")
    assert Version("1.0.0-x.7.z.92") >= Version("1.0.0-alpha.beta")
    assert Version("1.0.0-x-y-z.--") >= Version("1.0.0-x.7.z.92")
    assert Version("1.0.0-rc.1") >= Version("1.0.0-alpha.beta")


def test_simple_versions():
    sorting_comparison(
        [
            "1.1.0",
            "2.1.0",
            "3.1.0",
        ]
    )


def test_big_sub_versions():
    sorting_comparison(
        [
            "1.8.0",
            "1.9.0",
            "1.12.0",
        ]
    )


def test_semantic_versions():
    sorting_comparison(
        [
            "1.0.0-alpha",
            "1.0.0-alpha.1",
            "1.0.0-alpha.beta",
            "1.0.0-beta",
            "1.0.0-beta.2",
            "1.0.0-beta.11",
            "1.0.0-rc.1",
            "1.0.0",
        ]
    )


def test_semantic_versions_of_semver():
    sorting_comparison(
        [
            "1.0.0-beta",
            "1.0.0",
            "2.0.0-rc.1",
            "2.0.0-rc.2",
            "2.0.0",
        ]
    )
