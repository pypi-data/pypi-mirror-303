/* For examples of how to fill out the macros please refer to the postgres adapter and docs
postgres adapter macros: https://github.com/dbt-labs/dbt-core/blob/main/plugins/postgres/dbt/include/postgres/macros/adapters.sql
dbt docs: https://docs.getdbt.com/docs/contributing/building-a-new-adapter
*/

{% macro maxcompute__truncate_relation(relation) -%}
{% if relation.schema -%}
    truncate table {{ relation.database }}.{{ relation.schema }}.{{ relation.identifier }};
{%- else -%}
    truncate table {{ relation.database }}.{{ relation.identifier }};
{%- endif -%}
{% endmacro %}

{% macro maxcompute__rename_relation(from_relation, to_relation) -%}
{% if from_relation.schema -%}
    {% if from_relation.is_view -%}
        alter view {{ from_relation.database }}.{{ from_relation.schema }}.{{ from_relation.identifier }} rename to {{ to_relation.identifier }};
    {%- else -%}
        alter table {{ from_relation.database }}.{{ from_relation.schema }}.{{ from_relation.identifier }} rename to {{ to_relation.identifier }};
    {%- endif -%}
{%- else -%}
    {% if from_relation.is_view -%}
        alter view {{ from_relation.database }}.{{ from_relation.identifier }} rename to {{ to_relation.identifier }}
    {%- else -%}
        alter table {{ from_relation.database }}.{{ from_relation.identifier }} rename to {{ to_relation.identifier }};
    {%- endif -%}
{%- endif -%}
{% endmacro %}


{% macro maxcompute__alter_column_type(relation,column_name,new_column_type) -%}
{% if relation.schema -%}
    alter table {{ relation.database }}.{{ relation.schema }}.{{ relation.identifier }} change {{ column_name }} {{ column_name }} {{ new_column_type }};
{%- else -%}
    alter table {{ relation.database }}.{{ relation.identifier }} change {{ column_name }} {{ column_name }} {{ new_column_type }};
{%- endif -%}
{% endmacro %}


{% macro maxcompute__copy_grants() -%}
    {{ return(True) }}
{% endmacro %}

/* {# override dbt/include/global_project/macros/relations/table/create.sql #} */
{% macro maxcompute__create_table_as(temporary, relation, sql) -%}
{% if relation.schema -%}
  create table if not exists {{ relation.database }}.{{ relation.schema }}.{{ relation.identifier }} as (
      {{ sql }}
  )
{%- else -%}
  create table if not exists {{ relation.database }}.default.{{ relation.identifier }} as (
      {{ sql }}
  )
{%- endif -%}
{% if temporary %}
    lifecyclie 1
{%- endif -%}
;
{%- endmacro %}

/* {# override dbt/include/global_project/macros/relations/view/create.sql #} */
{% macro maxcompute__create_view_as(relation, sql) -%}
{% if relation.schema -%}
  create or replace view {{ relation.database }}.{{ relation.schema }}.{{ relation.identifier }} as (
         {{ sql }}
         );
{%- else -%}
  create or replace view {{ relation.database }}.default.{{ relation.identifier }} as (
         {{ sql }}
         );
{%- endif -%}
{%- endmacro %}

