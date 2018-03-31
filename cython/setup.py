from distutils.core import setup
from distutils.core import Extension
from Cython.Build import cythonize

extensions = [Extension("*", ["*.pyx"])]

setup(
    ext_modules = cythonize(extensions, annotate=True)
)


if __name__ == '__main__':
    print()