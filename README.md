# Logs Analysis Tool
this project was created for the third project in my fullstack developer nanodegree course.  
it was written in python and uses postgreSQL for the database.  
this shows my ability to use the psycopg2 library to connect my advanced sql querys to my python code.  
python code was verified with PEP8 to ensure readability.  
this program was tested using postgresql v9.5.10, psycopg2 v2.7.3.2, and python v2.7.12  

# Running it
- installs the required dependencies  
`apt-get install postgresql`  
`apt-get install python python-pip`  
`pip2 install --upgrade pip`  
`pip2 install psycopg2`  
- setup the database  
`su postgres -c 'createuser -dRS developer'`  
`su developer -c 'createdb'`  
`su developer -c 'createdb news'`  
`su developer -c 'psql -d news -f newsdata.sql'`  
`su developer -c 'psql -d news -f newsviews.sql'`  
- run the program  
`python tool.py`  
