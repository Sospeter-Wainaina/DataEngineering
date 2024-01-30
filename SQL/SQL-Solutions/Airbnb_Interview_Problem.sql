/* Find the room types that are searched most no of times output the room type alongside the number of searches for it
 If the  filter for the room types has more than one room type consider each unique room type as separate row
 Sort the result based on the number of searches in descending order*/
--create table airbnb_searches 
--(
--user_id int,
--date_searched date,
--filter_room_types varchar(200)
--);
--delete from airbnb_searches;
--insert into airbnb_searches values
--(1,'2022-01-01','entire home,private room')
--,(2,'2022-01-02','entire home,shared room')
--,(3,'2022-01-02','private room,shared room')
--,(4,'2022-01-03','private room')
--;