"""Top-level package for BG Review File Utils."""

__author__ = """Jaideep Sundaram"""
__email__ = 'sundaram.baylorgenetics@gmail.com'
__version__ = '0.1.0'

from .parser import Parser as ReviewParser
from .record import Record as ReviewRecord
from .writer import Writer as ReviewWriter
