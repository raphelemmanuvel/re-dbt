
-- {{ config(materialized='view') }}

with source_data as (

    SELECT *
    FROM {{ref('spi_global_rankings')}}

)

SELECT *
FROM source_data
