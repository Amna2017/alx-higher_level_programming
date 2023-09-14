#!/usr/bin/python3
import MySQLdb

# Function to list all states
def list_states(username, password, database):
        # Connect to MySQL server
            db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

                # Create a cursor object to execute queries
                    cursor = db.cursor()

                        # Execute the query to fetch all states
                            cursor.execute("SELECT * FROM states ORDER BY id ASC")

                                # Fetch all rows
                                    rows = cursor.fetchall()

                                        # Display the results
                                            for row in rows:
                                                        print(row)

                                                            # Close the cursor and database connection
                                                                cursor.close()
                                                                    db.close()

                                                                    # Call the function with the provided arguments
                                                                    list_states("your_mysql_username", "your_mysql_password", "hbtn_0e_0_usa")
