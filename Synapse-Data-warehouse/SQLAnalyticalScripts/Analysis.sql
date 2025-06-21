--Count no of athletes by country
select country, count(*) as totalathletes from Athletes
group by Country
order by totalathletes desc

--count total no of medals won by each country
select TeamCountry, sum(Gold) as TotalGold,sum(Silver) as TotalSilver,sum(Bronze) as Totalbronze from Medals
group by TeamCountry
order by TotalGold desc
--calculate the average no of entries by gender for each discipline
select Discipline,avg(Female) As Avg_Female,avg(Male) as Avg_male
from EntriesGender
group by Discipline