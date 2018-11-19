import psycopg2


    def Execute_query(query):

   #Establishing connection to the database

    db = psycopg2.connect("news")
    c = db.cursor()
    c.execute(query)

    # fetch results from the cursor

    query_results = c.fetchall()
    db.close()
    return query_results

    # Query 1. The most popular three articles of all time:
def get_popular_articles():
 query = """
        SELECT articles.title, COUNT(*) AS num
                FROM articles
                JOIN log
                ON log.path LIKE concat('/article/%', articles.slug)
                GROUP BY articles.title
                ORDER BY num DESC
                LIMIT 3;
    """

  results = Execute_query(query)

    print('Three most popular articles of all time are' )

    for i in results:
        print('"{title}" - {count} views'
              .format(title=i[0], count=i[1]))
                print()

              return

 # Query 2. The most popular article authors of all time:

def get_popular_authors():
query = """
        SELECT authors.name, COUNT(*) AS num
                FROM authors
                JOIN articles
                ON authors.id = articles.author
                JOIN log
                ON log.path like concat('/article/%', articles.slug)
                GROUP BY authors.name
                ORDER BY num DESC
                LIMIT 3;
        """
         results = Execute_query(query)

           print('Most popular authors of all time')
           for i in results:
                           print('{author} - {count} views'
                            .format(author=i[0], count=i[1]))
             print()
             return


 # Query 3. On which days did more than 1% of requests lead to errors?:

def get_dates_with_errors():
query = """
            SELECT TO_CHAR(date, 'FMMonth FMDD, YYYY'), err/total AS ratio
                    FROM (SELECT time::date AS date,
                                COUNT(*) AS total,
                                SUM((status != '200 OK')::int)::float AS err
                                FROM log
                                GROUP BY date) as errors
                    WHERE err/total > 0.01;
                    """

  results = Execute_query(query)

   print(' more than 1% of requests lead to errors filtered by dates')

    for i in results:
                     print('{date:%B %d, %Y} - {error_rate:.1f}% errors'.format(
                    date=i[0],
                    error_rate=i[1]))
            print()
              return

    # Functions execution

        get_popular_articles()
        get_popular_authors()
        get_dates_with_errors()