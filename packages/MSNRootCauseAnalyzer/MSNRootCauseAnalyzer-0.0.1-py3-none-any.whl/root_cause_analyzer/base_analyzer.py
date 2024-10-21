# base_analyzer.py

import warnings
from abc import ABC, abstractmethod
from numbers import Integral, Real

import numpy as np
import scipy.sparse as sp

class BaseAnalyzer:
    """
    base class for root cause analyzer
    """
    _parameter_constraints: dict = {
        "verbose": ["verbose"],
        "random_state": ["random_state"],
    }

    def __init__(
        self,
        top_n_factors,
        verbose
    ):
        self.top_n_factors = top_n_factors
        self.verbose = verbose

    def analyze(self, data):
        """
        analyze the data and return the root cause
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def format_output(self, result):
        """
        format the output
        """
        raise NotImplementedError("Subclasses should implement this method.")
