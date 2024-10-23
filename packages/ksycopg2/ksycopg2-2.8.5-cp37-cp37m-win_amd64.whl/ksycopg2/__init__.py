"""A Python driver for Kingbase

ksycopg is a Kingbase database adapter for the Python_ programming
language.

Homepage: https://help.kingbase.com.cn/v9/index.html

:Groups:
  * `Connections creation`: connect
  * `Value objects constructors`: Binary, Date, DateFromTicks, Time,
    TimeFromTicks, Timestamp, TimestampFromTicks
"""
# ksycopg/__init__.py - initialization of the ksycopg module
#
# Import the DBAPI-2.0 stuff into top-level module.

from ksycopg2._ksycopg import (                     # noqa
    BINARY, NUMBER, STRING, DATETIME, ROWID,

    Binary, Date, Time, Timestamp,
    DateFromTicks, TimeFromTicks, TimestampFromTicks,

    Error, Warning, DataError, DatabaseError, ProgrammingError, IntegrityError,
    InterfaceError, InternalError, NotSupportedError, OperationalError,

    _connect, apilevel, threadsafety, paramstyle,
    __version__, __libkci_version__,
)

from ksycopg2 import tz                             # noqa


# Register default adapters.

from ksycopg2 import extensions as _ext
_ext.register_adapter(tuple, _ext.SQL_IN)
_ext.register_adapter(type(None), _ext.NoneAdapter)

# Register the Decimal adapter here instead of in the C layer.
# This way a new class is registered for each sub-interpreter.
# See ticket #52
from decimal import Decimal                         # noqa
from ksycopg2._ksycopg import Decimal as Adapter    # noqa
_ext.register_adapter(Decimal, Adapter)
del Decimal, Adapter


def connect(dsn=None, connection_factory=None, cursor_factory=None, **kwargs):
    """
    Create a new database connection.

    The connection parameters can be specified as a string:

        conn = ksycopg2.connect("dbname=test user=kingbase password=secret")

    or using a set of keyword arguments:

        conn = ksycopg2.connect(database="test", user="kingbase", password="secret")

    Or as a mix of both. The basic connection parameters are:

    - *dbname*: the database name
    - *database*: the database name (only as keyword argument)
    - *user*: user name used to authenticate
    - *password*: password used to authenticate
    - *host*: database host address (defaults to UNIX socket if not provided)
    - *port*: connection port number (defaults to 54321 if not provided)

    Using the *connection_factory* parameter a different class or connections
    factory can be specified. It should be a callable object taking a dsn
    argument.

    Using the *cursor_factory* parameter, a new default cursor factory will be
    used by cursor().

    Using *async*=True an asynchronous connection will be created. *async_* is
    a valid alias (for Python versions where ``async`` is a keyword).

    Any other keyword parameter will be passed to the underlying client
    library: the list of supported parameters depends on the library version.

    """
    kwasync = {}
    if 'async' in kwargs:
        kwasync['async'] = kwargs.pop('async')
    if 'async_' in kwargs:
        kwasync['async_'] = kwargs.pop('async_')

    if dsn is None and not kwargs:
        raise TypeError('missing dsn and no parameters')

    dsn = _ext.make_dsn(dsn, **kwargs)
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
    if cursor_factory is not None:
        conn.cursor_factory = cursor_factory

    return conn
