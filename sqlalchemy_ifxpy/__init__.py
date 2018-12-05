# sqlalchemy_ifxpy/__init__.py
# Copyright (C) 2005-2013 the SQLAlchemy authors and contributors <see AUTHORS file>
#
# This module is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php
__version__ = '0.1.0'

import os
from sqlalchemy_ifxpy import base, ifxpy
from sqlalchemy.dialects import registry

os.environ['DELIMIDENT'] = 'Y' # Allow double quoted sql identifiers

base.dialect = ifxpy.dialect

registry.register("informix", "sqlalchemy_ifxpy.ifxpy", "InformixDialect_ifxpy")
registry.register("informix.ifxpy", "sqlalchemy_ifxpy.ifxpy", "InformixDialect_ifxpy")
