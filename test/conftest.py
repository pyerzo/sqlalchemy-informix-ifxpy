from sqlalchemy.dialects import registry

registry.register("informix", "sqlalchemy_ifxpy.ifxpy", "InformixDialect_ifxpy")
registry.register("informix.ifxpy", "sqlalchemy_ifxpy.ifxpy", "InformixDialect_ifxpy")

from sqlalchemy.testing.plugin.pytestplugin import *
