# Panversion

panversion is a tool to manage and compare versions.


## Philosophy

As a simple tool, panversion is pure-python. You can use a simple library or take its
unque file to integrate it in your project.


## Known versions

Panversion aims to be able to work a maximal number of version systems.

Right now, panversion is able to work with:

* [Semantic Version](https://semver.org/)
* [Version Specifiers](https://packaging.python.org/en/latest/specifications/version-specifiers/)


## Usage

Comparison:

    >>> from panversion import Version
    >>> Version("1.0.3-alpha") < Version("1.0.3")   # Semantic form
    True
    >>> Version("1.0-a8") < Version("1.0-post1")   # Version specifiers form
    True

Sorting:

    >>> from panversion import Version
    >>> sorted(["1.0.0-alpha", "1.0.0-beta", "1.0.0-rc.1", "1.0.0-alpha.beta", "1.0.0"], key=Version)
    ['1.0.0-alpha', '1.0.0-alpha.beta', '1.0.0-beta', '1.0.0-rc.1', '1.0.0']
    >>> sorted(["0.9", "1.0rc1", "1.0a2", "1.0", "1.0a1", "1!0.8", "1.1a1", "1.0b1"], key=Version)
    ['0.9', '1.0a1', '1.0a2', '1.0b1', '1.0rc1', '1.0', '1.1a1', '1!0.8']

Normalization:

    >>> from panversion import Version
    >>> Version("1.2-rev.12")
    1.2.post12

