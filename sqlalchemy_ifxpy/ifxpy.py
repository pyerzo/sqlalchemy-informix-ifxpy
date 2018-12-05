# sqlalchemy_ifxpy/ifxpy.py
# Copyright (C) 2005-2013 the SQLAlchemy authors and contributors <see AUTHORS file>
# Copyright (C) 2018 Tim Powell Modified to work with the ifxpy DBAPI interface
#
# This module is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

"""
Support for the ifxpy DBAPI.

ifxpy is available at:

    https://github.com/ifxdb/PythonIfxDB/

Connecting
^^^^^^^^^^

Sample informix connection using this dialect::

    engine = create_engine('informix+ifxpy://user:password@host/dbname')

"""

import re

from sqlalchemy_ifxpy.base import InformixDialect
from sqlalchemy.engine import default

import IfxPyDbi as ifxpydbi

VERSION_RE = re.compile(r'(\d+)\.(\d+)(.+\d+)')


class InformixExecutionContext_ifxpy(default.DefaultExecutionContext):

    def post_exec(self):
        if self.isinsert:
            self._lastrowid = self.cursor._get_last_identity_val
    #def post_exec(self):
    #    if self._select_lastrowid:
    #        # Massive hack to get the last inserted serial (sqlca.sqlerrd1) or bigserial
    #        # Apparently both are never set
    #        cursor = self.create_cursor()
    #        cursor.execute("SELECT dbinfo('sqlca.sqlerrd1'), dbinfo('bigserial') FROM sysmaster:\"informix\".sysdual")
    #        result = cursor.fetchone()
    #        assert(not all(result))
    #        self._lastrowid = result[0] + result[1]

    #    return super().post_exec()


    def get_lastrowid(self):
        return self._lastrowid


class InformixDialect_ifxpy(InformixDialect):
    driver = 'ifxpy'
    execution_ctx_cls = InformixExecutionContext_ifxpy

    @classmethod
    def dbapi(cls):
        return ifxpydbi

    def create_connect_args(self, url):
        """ Return a tuple of *args,**kwargs for creating a connection.

        The IfxPyDbi connection constructor looks like this:

            connect(ConnStr, user='', password='',
                    host='', database='', conn_options=None)

        This method translates the values in the provided url
        into args and kwargs needed to instantiate a connection.

        Because all but conn_options can also be included in the ConnStr,
        we prefer that to kwargs.

        """
        opts = url.translate_connect_args(username='uid', password='pwd',
                host='server', port='service') # Are these safe renames?
        connstr = ";".join(['%s=%s' % (k.upper(), v) for k, v in opts.items()])
        opt = {}

        return ([connstr], opt)

    def _get_server_version_info(self, connection):
        #return connection.connection.server_info()[1]
        v = VERSION_RE.split(connection.connection.dbms_ver)
        return (int(v[1]), int(v[2]), v[3])

    def is_disconnect(self, e, connection, cursor):
        if isinstance(e, self.dbapi.OperationalError):
            return 'closed the connection' in str(e) \
                    or 'connection not open' in str(e)
        else:
            return False


dialect = InformixDialect_ifxpy
