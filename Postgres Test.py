import psycopg2

try:
    connection = psycopg2.connect(user = "urik",
                                  password = "5544",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "urik_database")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    #cursor.execute("SELECT version();")
    cursor.execute('select * from "Nationalities";')
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection. jjjj
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")