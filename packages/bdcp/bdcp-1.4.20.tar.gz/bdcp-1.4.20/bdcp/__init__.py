#!/usr/bin/env python
# -*- coding:utf-8 -*-
__version__ = "1.4.10"


from . import connections
Connect = connect = Connection =connections.Connection

__all__ = [
    "Connect",
    "Connection",
    "connect",
    "__version__",
]