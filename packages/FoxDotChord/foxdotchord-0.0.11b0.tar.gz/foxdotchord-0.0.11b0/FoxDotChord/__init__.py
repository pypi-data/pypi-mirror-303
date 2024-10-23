"""Chord for foxdot."""

from ._chord import Chord
from ._pattern import PChord, c
from ._require import require

__all__ = ['Chord', 'PChord', 'c']

FoxDotCode = require('Code').FoxDotCode

FoxDotCode.namespace['c'] = c
FoxDotCode.namespace['PChord'] = PChord
