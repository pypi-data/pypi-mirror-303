#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""LISA GW Response module."""

import importlib_metadata

from .response import Response
from .response import ReadResponse
from .response import ResponseFromStrain
from .response import ReadStrain
from .response import GalacticBinary
from .response import VerificationBinary
from .stochastic import StochasticPointSource
from .stochastic import StochasticBackground

from . import psd


try:
    metadata = importlib_metadata.metadata('lisagwresponse').json
    __version__ = importlib_metadata.version('lisagwresponse')
    __author__ = metadata['author']
    __email__ = metadata['author_email']
except importlib_metadata.PackageNotFoundError:
    pass
