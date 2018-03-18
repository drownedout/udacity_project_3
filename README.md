# Log Analysis

## A simple python script to analyze a website's data logs.

### How to use

To run this code, you will need to install Postgresql and the python module, psycopg2.

Information on how install and utilize the components.

 * [Posgresql Installation (Windows)](http://www.postgresqltutorial.com/install-postgresql/)
 * [Posgresql Installation (OSX)](https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb)
 * [psycopg2](http://www.psychopy.org/)

You will then need to create the database 'news' and run the sql file:

```createdb news```

```psql -d news -f newsdata.sql```

The sql file, ```newsdata.sql```, can be downloaded [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

After this has been completed, in your terminal while inside your working directory, run ```python3 main.py```

Once you have done this a text file, **'output.txt'**, will have generated with the appropriate data.

### Process
##### These were originally included in main.py but were rejected by the auto-linter.

Query 1: To get the page count, I joined the two tables on the slug (which is a url in human readable format) and the article title - which were more or less the same. To reconcile the extra content in the slug url, I used
substring patterns. (https://www.postgresql.org/docs/9.3/static/functions-matching.html)

Query 2: I followed a similar method with the first query but joined the articles table with the authors table on author id.

Query 3: To aggregate all the times that the response was 404, I used the filter expression and divided it over total responses. Initially, I was using a conditional but that didn't work - so I referred to the documentation and used FILTER instead (https://www.postgresql.org/docs/9.4/static/sql-expressions.html).