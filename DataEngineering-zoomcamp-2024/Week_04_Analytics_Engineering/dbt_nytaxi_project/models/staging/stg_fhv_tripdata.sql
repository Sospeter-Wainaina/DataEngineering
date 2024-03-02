{{
    config(
        materialized='view'
    )
}}

with tripdata as 
(
  select *,
    row_number() over(order by pickup_datetime) as rn
  from {{ source('staging','fhv_tripdata') }}
),
select
 {{ dbt.safe_cast("dispatching_base_num", api.Column.translate_type("varchar")) }} as dispatching_base_num
cast(pickup_datetime as timestamp) as pickup_datetime,
cast(dropoff_datetime as timestamp) as dropoff_datetime,
{{ dbt.safe_cast("pulocationid", api.Column.translate_type("integer")) }} as pickup_locationid,
{{ dbt.safe_cast("dolocationid", api.Column.translate_type("integer")) }} as dropoff_locationid,
cast('SR_Flag' as Float) as SR_Flag,
 {{ dbt.safe_cast("Affiliated_base_number", api.Column.translate_type("varchar")) }} as Affiliated_base_number
 from tripdata
