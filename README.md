# conan-gsl
[Conan.io](http://conan.io/) package for [GSL](https://github.com/Microsoft/GSL) library.

The packages generated with this conanfile can be found in conan.io.

# Export package

```sh
conan export anonymouz/stable
```

# Upload packages to server

```sh
conan upload gsl/2016-01-04@anonymouz/stable --all
```

## Basic setup

# Reuse the packages

Download conan client from [Conan.io](http://conan.io) and run:

```sh
conan install gsl/2016-01-04@anonymouz/stable
```

## Project setup

If you handle multiple dependencies in your project is better to add a conanfile.txt

```ini
[requires]
gsl/2016-01-04@anonymouz/stable
```

Complete the installation of requirements for your project running:

```sh
conan install .
```

