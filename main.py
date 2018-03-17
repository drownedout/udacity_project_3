import psycopg2

db = psycopg2.connect("dbname=news")

cursor = db.cursor()

f = open('output.txt', 'w')

"""
To get the page count, I joined the two tables on the slug (which is a url
in human readable format) and the article title - which were more or
less the same. To reconcile the extra content in the slug url, I used
substring patterns.
(https://www.postgresql.org/docs/9.3/static/functions-matching.html)
"""

f.write("What are the most popular three articles of all time?" + "\n" * 2)

cursor.execute("SELECT articles.title, "
               "count(*) AS num "
               "FROM articles "
               "JOIN log ON log.path "
               "LIKE '%' || articles.slug || '%' "
               "GROUP BY articles.title "
               "ORDER BY num "
               "DESC LIMIT 3;")

for row in cursor:
    f.write("\"" + str(row[0]) + "\"" + " - " + str(row[1]) + " views" + '\n')

f.write("\n" * 2)

"""
	I followed a similar method with the first query but joined
  the articles table with the authors table on author id.
"""

f.write("Who are the most popular article authors of all time?" + "\n" * 2)

cursor.execute("SELECT authors.name, "
               "count(*) AS num "
               "FROM authors "
               "INNER JOIN articles ON articles.author = authors.id "
               "INNER JOIN log on log.path LIKE '%' || articles.slug || '%' "
               "GROUP BY authors.name ORDER BY num DESC;")

for row in cursor:
    f.write(str(row[0]) + " - " + str(row[1]) + " views" + '\n')

f.write("\n" * 2)

"""
	To aggregate all the times that the response was 404, I used the
  filter expression and divided it over total responses.
  Intially, I was using a conditional but that didn't work - so
  I refered to the documentation and used FILTER instead
  (https://www.postgresql.org/docs/9.4/static/sql-expressions.html).
"""

f.write("On which days did more than 1% of "
        "requests lead to errors?" + ("\n" * 2))

cursor.execute(
    "SELECT date_trunc('day',log.time) as d, "
    "COUNT(*) FILTER (WHERE status = '404 NOT FOUND')::NUMERIC * 100"
    "/ COUNT(*) "
    "from log group by d;")

for row in cursor:
    if round(row[1], 2) > 1.0:
        f.write(str(row[0].strftime("%B %d %Y")) + " - " +
                str(round(row[1], 2)) + "% errors" + '\n')

f.close()
