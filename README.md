# Logs Analysis Tool
This project was created for the third project in my Full Stack Web Developer Nanodegree Program.  
This is written in python and uses postgreSQL for the database.  
This shows my ability to use the psycopg2 library to connect my advanced SQL querys to my python code.  
The python code was verified with PEP8 to ensure readability.  
Program was tested using postgresql v9.5.10, psycopg2 v2.7.3.2, and python v2.7.12  
  
# Running it on Ubuntu 16.04
- installs the required dependencies  
`apt-get install unzip`  
`apt-get install postgresql`  
`apt-get install python python-pip`  
`pip2 install --upgrade pip`  
`pip2 install psycopg2`  
`unzip newsdata.zip`  
- setup the database  
`su postgres -c 'createuser -dRS developer'`  
`su developer -c 'createdb'`  
`su developer -c 'createdb news'`  
`su developer -c 'psql -d news -f newsdata.sql'`  
`su developer -c 'psql -d news -f newsviews.sql'`  
- run the program  
`python2.7 tool.py`  
# Views  
For the code used to create the SQL views, see newsviews.sql  
  
# Expected output  
`What are the most popular three articles of all time?`  
`"Candidate is jerk, alleges rival" - 338647 views`  
`"Bears love berries, alleges bear" - 253801 views`  
`"Bad things gone, say good people" - 170098 views`  
   
`Who are the most popular article authors of all time?`  
`Ursula La Multa - 507594 views`  
`Rudolf von Treppenwitz - 423457 views`  
`Anonymous Contributor - 170098 views`  
`Markoff Chaney - 84557 views`  
  
`On which days did more than 1% of requests lead to errors?`  
`July 17, 2016 - 2.28% errors`  
