import BrickPi3Lib

from distutils.core import setup
from distutils.extension import Extension

setup(
  name = 'BrickPi3Lib',
  version=BrickPi3Lib.__version__,
  description="For use with the BrickPi3",
  author="Emil Jimenez",
  packages=['BrickPi3Lib'],
)