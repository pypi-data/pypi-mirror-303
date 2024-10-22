from contextlib import contextmanager
from dataclasses import dataclass
from typing import Dict, Any

from dbt_common.exceptions import (
    DbtConfigError,
    DbtRuntimeError
)
from dbt.adapters.contracts.connection import Credentials, AdapterResponse

from dbt.adapters.sql import SQLConnectionManager
from dbt.adapters.events.logging import AdapterLogger

from odps import ODPS
import odps.dbapi

from dbt.adapters.maxcompute.context import set_dbt_default_schema
from dbt.adapters.maxcompute.wrapper import ConnectionWrapper

logger = AdapterLogger("MaxCompute")

@dataclass
class MaxComputeCredentials(Credentials):
    endpoint: str
    accessId: str
    accessKey: str

    _ALIASES = {
        'project': 'database',
        'ak': 'accessId',
        'sk': 'accessKey',
    }

    @property
    def type(self):
        return "maxcompute"

    @property
    def unique_field(self):
        return self.endpoint + '_' + self.database

    def _connection_keys(self):
        return ("project", "database")


class MaxComputeConnectionManager(SQLConnectionManager):
    TYPE = "maxcompute"

    @classmethod
    def open(cls, connection):
        if connection.state == 'open':
            logger.debug('Connection is already open, skipping open.')
            return connection

        credentials = connection.credentials

        o = ODPS(
            credentials.accessId,
            credentials.accessKey,
            project=credentials.database,
            endpoint=credentials.endpoint,
        )
        o.schema = credentials.schema
        set_dbt_default_schema(credentials.schema)

        try:
            o.get_project().reload()
        except Exception as e:
            raise DbtConfigError(f"Failed to connect to MaxCompute: {str(e)}") from e

        handle = ConnectionWrapper(odps=o, hints={'odps.sql.submit.mode': 'script', 'odps.sql.allow.cartesian':'true'})
        connection.state = 'open'
        connection.handle = handle
        return connection

    @classmethod
    def get_response(cls, cursor):
        # FIXME：we should get 'code', 'message', 'rows_affected' from cursor
        logger.info("Current instance id is " + cursor._instance.id)
        return AdapterResponse(_message="OK")

    def set_query_header(self, query_header_context: Dict[str, Any]) -> None:
        # no query header will better
        pass

    @contextmanager
    def exception_handler(self, sql: str):
        try:
            yield
        except Exception as exc:
            logger.debug("Error while running:\n{}".format(sql))
            logger.debug(exc)
            if len(exc.args) == 0:
                raise
            thrift_resp = exc.args[0]
            if hasattr(thrift_resp, "status"):
                msg = thrift_resp.status.errorMessage
                raise DbtRuntimeError(msg)
            else:
                raise DbtRuntimeError(str(exc))

    def cancel(self, connection):
        connection.handle.cancel()

    def add_begin_query(self):
        pass

    def add_commit_query(self):
        pass
