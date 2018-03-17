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

Please note the sql file, ```newsdata.sql```, was too large to include.

After this has been completed, in your terminal while inside your working directory, run ```python3 main.py```

Once you have done this a text file, **'output.txt'**, will have generated with the appropriate data.