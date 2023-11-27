
-- {{ config(materialized='view') }}

with source_data as (

    SELECT *
    FROM {{ref('spi_matches_latest')}}

)

SELECT *
FROM source_data
