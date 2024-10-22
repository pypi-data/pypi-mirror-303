import threading

DBT_DEFAULT_SCHEMA = "__dbt_default__"

schema_lock = threading.Lock()


def set_dbt_default_schema(schema):
    global DBT_DEFAULT_SCHEMA
    with schema_lock:
        DBT_DEFAULT_SCHEMA = schema


def get_dbt_default_schema():
    global DBT_DEFAULT_SCHEMA
    with schema_lock:
        return DBT_DEFAULT_SCHEMA
