from .mingus import *
from mingus.core.chords import *
from mt_exceptions import NoteFormatError, FormatError
import sys

if __name__ == '__main__':
  print(
    mingus.core.chords.triad('E')
#	core.chords.augmented_major_seventh("C")
  )
