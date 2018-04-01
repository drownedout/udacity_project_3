#! /usr/bin/env python3
import psycopg2

def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except BaseException:
        print("Database did not connect properly")


def query_one():
    db, cursor = connect()

    query = "SELECT title, " \
            "count(*) AS views " \
            "FROM log join articles ON log.path = concat('/article/', articles.slug) " \
            "GROUP BY title ORDER BY views DESC LIMIT 3;"

    cursor.execute(query)

    for row in cursor:
        f.write("\"" + str(row[0]) + "\"" + " - " +
                str(row[1]) + " views" + '\n')

    db.close()


def query_two():
    db, cursor = connect()

    query = "SELECT authors.name, " \
            "count(*) AS num FROM authors " \
            "INNER JOIN articles ON articles.author = authors.id " \
            "INNER JOIN log ON log.path = concat('/article/', articles.slug) " \
            "GROUP BY authors.name ORDER BY num DESC;"

    cursor.execute(query)

    for row in cursor:
        f.write(str(row[0]) + " - " + str(row[1]) + " views" + '\n')

    db.close()


def query_three():
    db, cursor = connect()

    query = "SELECT * FROM (SELECT date_trunc('day',log.time) as d, " \
            "COUNT(*) FILTER (WHERE status = '404 NOT FOUND')::NUMERIC * 100 / COUNT(*) as var " \
            "FROM log GROUP BY d) AS fof WHERE fof.var > 1.0;"

    cursor.execute(query)

    for row in cursor:
        f.write(str(row[0].strftime("%B %d %Y")) + " - " +
                str(round(row[1], 2)) + "% errors" + '\n')

    db.close()


if __name__ == '__main__':
    f = open('output.txt', 'w')
    f.write("What are the most popular three articles of all time?" + "\n" * 2)
    query_one()
    f.write("\n" * 2)
    f.write("Who are the most popular article authors of all time?" + "\n" * 2)
    query_two()
    f.write("\n" * 2)
    f.write("On which days did more than 1% of "
            "requests lead to errors?" + ("\n" * 2))
    query_three()
    f.close()
