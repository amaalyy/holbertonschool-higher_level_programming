-- script that lists the number of records with the same score in the table
SELECT score, COUNT(score) as score
FROM second_table
GROUP BY score;
