import pytest

from panversion import Version
from tests.utils import sorting_comparison


def notest_PEP440_error():
    with pytest.raises(ValueError):
        Version("foobar")


def test_PEP440_normalization():
    assert str(Version("1.0.0")) == "1.0.0"
    assert str(Version("1.0alpha")) == "1.0a0"
    assert str(Version("1.1.a1")) == "1.1a1"
    assert str(Version("1.1-a1")) == "1.1a1"
    assert str(Version("1.0a.1")) == "1.0a1"
    assert str(Version("1.1alpha1")) == "1.1a1"
    assert str(Version("1.1beta2")) == "1.1b2"
    assert str(Version("1.1c3")) == "1.1rc3"
    assert str(Version("1.2-post2")) == "1.2.post2"
    assert str(Version("1.2post2")) == "1.2.post2"
    assert str(Version("1.0-r4")) == "1.0.post4"
    assert str(Version("1.2.post")) == "1.2.post0"
    assert str(Version("1.2-rev.12")) == "1.2.post12"
    assert str(Version("1.0-1")) == "1.0.post1"
    assert str(Version("1.2-dev2")) == "1.2.dev2"
    assert str(Version("1.2dev2")) == "1.2.dev2"
    assert str(Version("1.2.dev")) == "1.2.dev0"
    assert str(Version("1.0+ubuntu-1")) == "1.0+ubuntu.1"
    assert str(Version("\t\r 1.0+ubuntu-1\n")) == "1.0+ubuntu.1"


def test_PEP440_equality():
    assert Version("1.0") == Version("1.0.0")
    assert Version("1.0a") == Version("1.0-alpha0")
    assert Version("1.0A") == Version("1.0-aLPha0")
    assert Version("2016!1.0-alpha1.dev2") == Version("2016!1.0a1.dev2")
    assert Version("1.1.a1") == Version("1.1-a1")
    assert Version("1.2a") == Version("1.2-a.0")


def test_PEP440_non_equality():
    assert Version("1.0.0") != Version("1.0.1")
    assert Version("3.14.0a1") != Version("3.14.0.a")


def test_PEP440_lesser_than_major():
    assert Version("1.0") < Version("2.0")


def test_PEP440_lesser_than_minor():
    assert Version("1.0") < Version("1.1")
    assert Version("1.8") < Version("1.10")


def test_PEP440_lesser_than_patch():
    assert Version("1.0.0.0") < Version("1.0.1.0")
    assert Version("1.0.8.0") < Version("1.0.10.0")


def test_PEP440_lesser_than_prerelease():
    assert Version("1.0-rc.1") < Version("1.0")
    assert Version("1.0-alpha") < Version("1.0-alpha.1")
    assert Version("1.0-alpha.1") < Version("1.0-beta")
    assert Version("1.0-beta") < Version("1.0-rc.1")


def test_PEP440_lesser_than_postrelease():
    assert Version("1.0-0") < Version("1.0-1")
    assert Version("1.0-post") < Version("1.0-post.1")
    assert Version("1.0-post.8") < Version("1.0-post.10")
    assert Version("1.0") < Version("1.0-post")


def test_PEP440_lesser_than_or_equal():
    assert Version("1.0") <= Version("1.0")
    assert Version("1.0.0+build") <= Version("1.0.0")
    assert Version("1.0") <= Version("2.0")
    assert Version("1.0") <= Version("1.1")
    assert Version("1.8") <= Version("1.10")
    assert Version("1.0.0.0") <= Version("1.0.1.0")
    assert Version("1.0.8.0") <= Version("1.0.10.0")
    assert Version("1.0-rc.1") <= Version("1.0")
    assert Version("1.0-alpha") <= Version("1.0-alpha+build")
    assert Version("1.0-alpha") <= Version("1.0-alpha.1")
    assert Version("1.0-alpha.1") <= Version("1.0-beta")
    assert Version("1.0-beta") <= Version("1.0-rc.1")


def test_PEP440_greater_than():
    assert Version("1.0") > Version("1.0-rc.1")
    assert Version("1.0-alpha.1") > Version("1.0-alpha")
    assert Version("1.0-alpha.10") > Version("1.0-alpha.8")
    assert Version("1.0-beta") > Version("1.0-alpha")
    assert Version("1.0-rc.1") > Version("1.0-beta")
    assert Version("1.0-post.1") > Version("1.0-post")
    assert Version("1.0-post") > Version("1.0")


def test_PEP440_greater_than_or_equal():
    assert Version("1.0") >= Version("1.0")
    assert Version("1.0") >= Version("1.0+build")
    assert Version("2.0") >= Version("1.0")
    assert Version("1.1") >= Version("1.0")
    assert Version("1.10") >= Version("1.8")
    assert Version("1.0.1.0") >= Version("1.0.0.0")
    assert Version("1.0.10.0") >= Version("1.0.8.0")
    assert Version("1.0") >= Version("1.0-rc.1")
    assert Version("1.0-alpha") >= Version("1.0-alpha+build")
    assert Version("1.0-alpha.1") >= Version("1.0-alpha")
    assert Version("1.0-beta") >= Version("1.0-alpha.1")
    assert Version("1.0-rc") >= Version("1.0-alpha0")
    assert Version("1.0-rc.1") >= Version("1.0-alpha")
    assert Version("1!1.0") >= Version("1.0")


def test_PEP440_simple_major_minor():
    sorting_comparison(
        [
            "0.1",
            "0.4",
            "0.6",
            "0.10",
            "1.0",
            "1.1",
        ]
    )


def test_PEP440_release_segments_with_different_size():
    sorting_comparison(
        [
            "0",
            "0.1",
            "0.1.2",
            "0.1.2.3",
            "0.1.2.3.4",
            "0.1.2.3.4.5",
            "1.0",
            "1.0.3",
            "1.1",
            "2020.12.2",
        ]
    )


def test_PEP440_simple_major_minor_micro():
    sorting_comparison(
        [
            "1.1.0",
            "1.1.1",
            "1.1.6",
            "1.1.10",
            "1.2.0",
        ]
    )


def test_PEP440_major_minor_with_prerelease():
    sorting_comparison(
        [
            "0.9",
            "1.0a1",
            "1.0a4",
            "1.0a10",
            "1.0b1",
            "1.0rc1",
            "1.0",
            "1.1a1",
        ]
    )


def test_PEP440_final_release():
    sorting_comparison(
        [
            "0.9",
            "0.9.1",
            "0.9.2",
            "0.9.10",
            "0.9.10.1",
            "0.9.11",
            "1",
            "1.0.1",
            "1.1",
            "2.0",
            "2.0.1",
        ]
    )

def test_PEP440_date_based():
    sorting_comparison(
        [
            "2012.4",
            "2012.7",
            "2012.10",
            "2013.1",
            "2013.6",
        ]
    )



def test_PEP440_versions_1():
    sorting_comparison(
        [
            "0.9",
            "1.0a1",
            "1.0a2",
            "1.0b1",
            "1.0rc1",
            "1.0",
            "1.1a1",
            "1!0.8",
        ]
    )
