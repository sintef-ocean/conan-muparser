[![GCC Conan](https://github.com/sintef-ocean/conan-muparser/workflows/GCC%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-muparser/actions?query=workflow%3A"GCC+Conan")
[![Clang Conan](https://github.com/sintef-ocean/conan-muparser/workflows/Clang%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-muparser/actions?query=workflow%3A"Clang+Conan")
[![MSVC Conan](https://github.com/sintef-ocean/conan-muparser/workflows/MSVC%20Conan/badge.svg)](https://github.com/sintef-ocean/conan-muparser/actions?query=workflow%3A"MSVC+Conan")
[![Download](https://api.bintray.com/packages/sintef-ocean/conan/muparser%3Asintef/images/download.svg)](https://bintray.com/sintef-ocean/conan/muparser%3Asintef/_latestVersion)

## Conan package recipe for [*muparser*](https://beltoforion.de/en/muparser/)

Fast Math Parser Library

The packages generated with this **conanfile** can be found on [Bintray](https://bintray.com/sintef-ocean/conan/muparser%3Asintef).

## For Users

### Basic setup

    $ conan install muparser/2.3.2@sintef/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    muparser/2.3.2@sintef/stable

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.


## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create . conan/stable


### Available Options
| Option        | Default | Possible Values  |
| ------------- |:----------------- |:------------:|
| shared      | False |  [True, False] |
| fPIC      | True |  [True, False] |


## Add Remote

Conan Community has its own Bintray repository, however, we are working to distribute all package in the Conan Center:

    $ conan remote add sintef https://api.bintray.com/conan/sintef-ocean/conan


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package muparser.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](LICENSE)
