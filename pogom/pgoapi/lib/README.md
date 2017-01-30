[PokéLibs](https://github.com/pokelibs)

# pgoapi-libs
[![license](https://img.shields.io/github/license/pokelibs/pgoapi-libs.svg?maxAge=2592000?style=flat-square)](https://github.com/pokelibs/pgoapi-libs/blob/master/LICENSE.md)

## Table of Contents

* [What is it?](#what-is-it)
* [Installation](#installation)
* [Documentation](#documentation)
* [Contributing](#contributing)
  * [Core Maintainers](#core-maintainers)
* [Licensing](#licensing)

## What is it?
`pgoapi-libs` is the official source repository for all hashing, encrypt and future libraries that need to be shipped with various API implementations.

## Installation
Simply checkout this repository as a submodule for your project at the desired tagged release.
Please make sure that the SHA256SUMS match up with the sums for each file to assure it hasn't been tampered with.
The latest sums are:

```
b8f62a0fbb301eabbe4cb83bab2c17f35360116b46e196fd53ef5da1d7d1395d  libniahash-freebsd-i386.so
3ffbc2f64ffda74c82cefeff94a7d3aeba72efcc890b847ff2732c308768e6dd  libniahash-freebsd-x86-64.so
e1eff1af978b0fda2b883d38c53290c15de3ca4274b4bd8690d41eab8558843b  libniahash-linux-arm32.so
8fcb0424682df55684410ebb078adc467842f2cf4d2c1b5cc757e461388671df  libniahash-linux-arm64.so
c194a4207eabf0f3e2b418e39747dabeb63aba397a73b27c64eb064e9b344d83  libniahash-linux-i386.so
dd1e9510e58f2793f3f92ec352c8d301e797be473c8aa00d731e5d931f0f76b2  libniahash-linux-x86-64.so
c6985404f10dd5daab8458c80432ae773b4ac2d8129fcbd05c25668e199d5882  libpcrypt-freebsd-i386.so
a6f9e9b45ce7ac6d7475c69abc4f763ea3195cce10f1cbff65bf9f09c1cf868a  libpcrypt-freebsd-x86-64.so
6fd47cc98534065ace055e378746492bbb4b07807d35c8639df9f56f895878cc  libpcrypt-linux-arm32.so
4bf2131e82cd95d2a48f6807af42cbe6540238ac417529d9e3d82cac3a28e5d4  libpcrypt-linux-arm64.so
f3110263ac01788edb580e1a96d0bc52a355720298876b4c66d5ce089b0cc7de  libpcrypt-linux-i386.so
49d86fcea6d40371c7194acc494b715e06a0733ab28ed4460496629e83d9d01d  libpcrypt-linux-x86-64.so
549cbc22d4fdee557706ceb70f10c935e995509b2f230272c6c6384c7eb6f925  libniahash-macos-i386.dylib
bfd97a9028a30e711ac5db7967e425f298ca710b5f3c3878c85ffa47df40da76  libniahash-macos-x86-64.dylib
62d87ca447fac6e9d366119c3974ba5016feaeb6aa886eda4fbc8aa3e85e456d  libpcrypt-macos-i386.dylib
def6546280ee3d5117e04856532bd81517424695036d4bb60887c8d06412cd32  libpcrypt-macos-x86-64.dylib
663bec4e8987923c2f82f4aa99c9039c04cf67be6c9eeaec628861ce839c573f  libniahash-windows-i686.dll
c0f9197c67a82b0920293b1a8e2c0a74e1125236c0da7c9d53ab6b7d2b72c70f  libniahash-windows-x86-64.dll
dbf76869afde7fed4f40118f72e4bfa68ea50c20bc32397921f9a04e1e948c56  libpcrypt-windows-i686.dll
b6d11b185384a5df02a48c064b6005074a90b14dfbec05b8539d2bba987a33cc  libpcrypt-windows-x86-64.dll
```

## Documentation
More detailed instructions on how to compile the given libraries will be updated soon, for now a roughy guideline is given below.

* Checkout https://github.com/laverdet/pcrypt-c (Thanks a lot to @marcel)
* Use `make all`
* Checkout https://gist.github.com/Noctem/018c107d6a6297c24e36a00d4da046c9 (Thanks a lot to @Waryas, @marcel, @HatchingEgg, @Apoc)
* Make the file according to the following flags: (Thanks a lot to @noctem)
```
Linux:
	cc -fPIC -O3 -shared niahash.c -o libniahash-linux-x86-64.so
macOS:
	clang -march=core2 -shared -fPIC -mmacosx-version-min=10.7 -O3 niahash.c -o libniahash-macos-x86-64.dylib
Windows:
	x86_64-w64-mingw32-gcc -O3 -fPIC -shared niahash.c -o libniahash-windows-x86-64.dll
```

## Licensing
[MIT](https://github.com/pokelibs/pgoapi-libs/blob/master/LICENSE)

### Third Party Licenses
    None

## Contributing
Currently, you can contribute to this project by visiting and discussing with us in Discord
