from datetime import datetime
from decimal import Decimal

from dbt.adapters.events.logging import AdapterLogger
from odps.dbapi import Cursor, Connection
from odps.errors import ODPSError
import re

class ConnectionWrapper(Connection):

    def cursor(self, *args, **kwargs):
        return CursorWrapper(
            self, *args, use_sqa=self._use_sqa,
            fallback_policy=self._fallback_policy,
            hints=self._hints, **kwargs
        )

logger = AdapterLogger("MaxCompute")

class CursorWrapper(Cursor):
    def execute(self, operation, parameters=None, **kwargs):
        def replace_sql_placeholders(sql_template, values):
            if not values:
                return sql_template
            if operation.count('%s') != len(parameters):
                raise ValueError("参数数量与SQL模板中的占位符数量不匹配")
            return operation % tuple(parameters)

        def param_normalization(params):
            if not params:
                return None
            normalized_params = []
            for param in params:
                if isinstance(param, Decimal):
                    normalized_params.append(f"{param}BD")
                elif isinstance(param, datetime):
                    normalized_params.append(f"TIMESTAMP_NTZ'{param.strftime('%Y-%m-%d %H:%M:%S')}'")
                elif isinstance(param, str):
                    normalized_params.append(f"'{param}'")
                else:
                    normalized_params.append(f"{param}")
            return normalized_params

        def remove_comments(input_string):
            logger.debug(f"remove_comments: {input_string}")
            # 使用正则表达式匹配 /* 开始和 */ 结束之间的内容，并将其替换为空字符串
            result = re.sub(r'/\*[^+].*?\*/', '', input_string, flags=re.DOTALL)
            return result

        operation = remove_comments(operation)
        parameters = param_normalization(parameters)
        operation = replace_sql_placeholders(operation, parameters)

        # retry three times
        for i in range(4):
            try:
                super().execute(operation)
                self._instance.wait_for_success()
                return
            except ODPSError as e:
                # 0130201: view not found, 0110061, 0130131: table not found
                if e.code == "ODPS-0130201" or e.code == "ODPS-0110061" or e.code == "ODPS-0130131":
                    logger.info("retry when execute sql: %s, error: %s", operation, e)
                    continue
                else:
                    raise e

