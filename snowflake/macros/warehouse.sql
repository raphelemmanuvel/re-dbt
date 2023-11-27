{% macro resume_warehouse() %}

  alter warehouse {{ env_var('SNOWFLAKE_WAREHOUSE') }} resume

{% endmacro %}


{% macro suspend_warehouse() %}

  alter warehouse {{ env_var('SNOWFLAKE_WAREHOUSE') }} suspend

{% endmacro %}
