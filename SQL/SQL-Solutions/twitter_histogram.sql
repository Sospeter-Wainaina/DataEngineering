--PROBLEM STATEMENT
/*
 Assume you're given a table Twitter tweet data, write a query to obtain a histogram of tweets posted per user in 2022. Output the tweet count per user as the bucket and the number of Twitter users who fall into that bucket.
 
 In other words, group the users by the number of tweets they posted in 2022 and count the number of users in each group.*/
-- SOLUTION
with tweet_count as (
    SELECT user_id,
        count(tweet_id) as users_num
    FROM tweets
    where EXTRACT(
            'YEAR'
            FROM tweet_date
        ) = 2022
    group by user_id
)
select users_num as tweet_bucket,
    count(users_num)
from tweet_count
group by users_num