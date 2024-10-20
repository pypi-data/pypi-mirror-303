"""Top-level package for BG RefSeq Accession File Utils."""

__author__ = """Jaideep Sundaram"""
__email__ = 'sundaram.baylorgenetics@gmail.com'
__version__ = '0.1.0'

from .parser import Parser as RefSeqAccessionFileParser
from .record import Record as RefSeqAccessionRecord
from .writer import Writer as RefSeqAccessionFileWriter
