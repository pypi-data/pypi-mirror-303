"""Error classes for Kingbase error codes
"""

# ksycopg/errors.py - SQLSTATE and DB-API exceptions


def lookup(code):
    """Lookup an error code and return its exception class.

    Raise `!KeyError` if the code is not found.
    """
    from ksycopg2._ksycopg import sqlstate_errors   # avoid circular import
    return sqlstate_errors[code]
