import psycopg2

DB_NAME = "news"


# What are the most popular three articles of all time?
# when limit == -1 then there is no limit, default 3
def get_top_articles(limit=3):

    db = psycopg2.connect("dbname=%s" % DB_NAME)
    cursor = db.cursor()
    cursor.execute("select * from top_articles;")
    if limit == -1:
        return cursor.fetchall()
    else:
        return cursor.fetchmany(abs(limit))
    db.close()


# Who are the most popular article authors of all time?
# when limit == -1 then there is no limit, default -1
def get_top_authors(limit=-1):

    db = psycopg2.connect("dbname=%s" % DB_NAME)
    cursor = db.cursor()
    cursor.execute("select * from top_authors;")
    if limit == -1:
        return cursor.fetchall()
    else:
        return cursor.fetchmany(abs(limit))
    db.close()


# On which days did more than 1% of requests lead to errors?
# when limit == -1 then there is no limit, default 1
def get_worst_days(limit=-1):

    db = psycopg2.connect("dbname=%s" % DB_NAME)
    cursor = db.cursor()
    cursor.execute("select * from bad_days where percent > 1;")
    if limit == -1:
        return cursor.fetchall()
    else:
        return cursor.fetchmany(abs(limit))
    db.close()


top_articles = get_top_articles()
top_authors = get_top_authors()
worst_days = get_worst_days()

print "What are the most popular three articles of all time?"
for article in top_articles:
    print "\"%s\" - %s views" % (article[0], str(article[1]))

print "\nWho are the most popular article authors of all time?"
for author in top_authors:
    print "%s - %s views" % (author[0], author[1])

print "\nOn which days did more than 1% of requests lead to errors?"
for day in worst_days:
    data = (day[0].strftime("%B %d, %Y"), "{0:.2f}%".format(day[1]))
    print "%s - %s errors" % data
