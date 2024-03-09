# Homework

## Setting up

In order to get a static set of results, we will use historical data from the dataset.

## Question 0

_This question is just a warm-up to introduce dynamic filter, please attempt it before viewing its solution._

What are the dropoff taxi zones at the latest dropoff times?

For this part, we will use the [dynamic filter pattern](https://docs.risingwave.com/docs/current/sql-pattern-dynamic-filters/).

## Question 1

Create a materialized view to compute the average, min and max trip time **between each taxi zone**.

Note that we consider the do not consider `a->b` and `b->a` as the same trip pair.
So as an example, you would consider the following trip pairs as different pairs:

```plaintext
Yorkville East -> Steinway
Steinway -> Yorkville East
```

From this MV, find the pair of taxi zones with the highest average trip time.
You may need to use the [dynamic filter pattern](https://docs.risingwave.com/docs/current/sql-pattern-dynamic-filters/) for this.

Bonus (no marks): Create an MV which can identify anomalies in the data. For example, if the average trip time between two zones is 1 minute,
but the max trip time is 10 minutes and 20 minutes respectively.

Options:

1. **Yorkville East, Steinway**
2. Murray Hill, Midwood
3. East Flatbush/Farragut, East Harlem North
4. Midtown Center, University Heights/Morris Heights

p.s. The trip time between taxi zones does not take symmetricity into account, i.e. `A -> B` and `B -> A` are considered different trips. This applies to subsequent questions as well.

### Solution

```sql
--HOMEWORK Q1
CREATE MATERIALIZED VIEW max_trip_duration AS
with T AS (
SELECT
    z.zone AS pickup_zone,
    x.zone AS dropoff_zone,
    EXTRACT(EPOCH FROM (t.tpep_dropoff_datetime - t.tpep_pickup_datetime)) / 60 AS trip_duration_minutes
FROM
    trip_data t
INNER JOIN
    taxi_zone z ON t.PULocationID = z.location_id
INNER JOIN
    taxi_zone x ON t.DOLocationID = x.location_id
)

SELECT pickup_zone,dropoff_zone, ROUND(AVG(trip_duration_minutes),2) AS AVG_MINS,ROUND(MAX(trip_duration_minutes),2) AS MAX_MINS,ROUND(MIN(trip_duration_minutes),2) AS MIN_MINUTES
FROM T
GROUP BY pickup_zone,dropoff_zone
ORDER BY AVG(trip_duration_minutes) DESC LIMIT 1;
```

## Question 2

Recreate the MV(s) in question 1, to also find the **number of trips** for the pair of taxi zones with the highest average trip time.

Options:

1. 5
2. 3
3. 10
4. **1**

### Solution

```sql
---HOMEWORK Q2

CREATE MATERIALIZED VIEW max_trip_duration_with_count AS
WITH T AS (
    SELECT
        z.zone AS pickup_zone,
        x.zone AS dropoff_zone,
        EXTRACT(EPOCH FROM (t.tpep_dropoff_datetime - t.tpep_pickup_datetime)) / 60 AS trip_duration_minutes
    FROM
        trip_data t
    INNER JOIN
        taxi_zone z ON t.PULocationID = z.location_id
    INNER JOIN
        taxi_zone x ON t.DOLocationID = x.location_id
)

SELECT
    pickup_zone,
    dropoff_zone,
    ROUND(AVG(trip_duration_minutes), 2) AS avg_mins,
    ROUND(MAX(trip_duration_minutes), 2) AS max_mins,
    ROUND(MIN(trip_duration_minutes), 2) AS min_mins,
    COUNT(*) AS trip_count
FROM
    T
GROUP BY
    pickup_zone,
    dropoff_zone
ORDER BY
    avg_mins DESC
LIMIT 1;
```

## Question 3

From the latest pickup time to 17 hours before, what are the top 3 busiest zones in terms of number of pickups?
For example if the latest pickup time is 2020-01-01 17:00:00,
then the query should return the top 3 busiest zones from 2020-01-01 00:00:00 to 2020-01-01 17:00:00.

HINT: You can use [dynamic filter pattern](https://docs.risingwave.com/docs/current/sql-pattern-dynamic-filters/)
to create a filter condition based on the latest pickup time.

NOTE: For this question `17 hours` was picked to ensure we have enough data to work with.

Options:

1. Clinton East, Upper East Side North, Penn Station
2. **LaGuardia Airport, Lincoln Square East, JFK Airport**
3. Midtown Center, Upper East Side South, Upper East Side North
4. LaGuardia Airport, Midtown Center, Upper East Side North

### Solution

```sql
----HOMEWORK Q3

CREATE MATERIALIZED VIEW busiest_zones_17hr_before AS

WITH latest_pickup_time as (
SELECT MAX(T.tpep_pickup_datetime) as latest_pickup_time
	FROM trip_data t
    INNER JOIN
        taxi_zone z ON t.PULocationID = z.location_id)
    SELECT
        taxi_zone.ZONE,count(*) AS cnt
    FROM
        trip_data c
    INNER JOIN latest_pickup_time l
                ON c.tpep_pickup_datetime > l.latest_pickup_time - interval '17 hour'
    INNER JOIN taxi_zone
                ON c.PULocationID = taxi_zone.location_id
GROUP BY taxi_zone.ZONE ORDER BY COUNT(*) DESC LIMIT 3;
```
