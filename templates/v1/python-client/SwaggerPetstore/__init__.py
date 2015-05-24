#!/usr/bin/env python
"""Add all of the modules in the current directory to __all__"""
import os

# import models into package

from .models.register_response import RegisterResponse


# import apis into package

from .default_api import DefaultApi


# import ApiClient
from .swagger import ApiClient

__all__ = []

for module in os.listdir(os.path.dirname(__file__)):
  if module != '__init__.py' and module[-3:] == '.py':
    __all__.append(module[:-3])
