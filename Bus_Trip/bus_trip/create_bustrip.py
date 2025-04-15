#İNTİZAR GÜZELÇAY
#18.05.2024


import mysql.connector as sql

class Bustrip:

    def __init__(self, connection):
        self.connection = sql.connect(**connection)

    def add_firm(self, firm_name):
        cursor = self.connection.cursor()
        query = "INSERT INTO firms(firm_name) VALUES (%s)"
        cursor.execute(query, (firm_name,))
        self.connection.commit()
        cursor.close()

    def add_route(self, route):
        cursor = self.connection.cursor()
        query = "INSERT INTO routes(route) VALUES(%s)"
        cursor.execute(query, (route,))
        self.connection.commit()
        cursor.close()

    def add_trips(self, direction, route_id, trips_name):
        cursor = self.connection.cursor()
        query = "INSERT INTO trips(direction, route_id, trips_name) VALUES(%s, %s, %s)"
        cursor.execute(query, (direction, route_id, trips_name))
        self.connection.commit()
        cursor.close()

    def add_trip(self, trips_id, firm_id, trip_time):
        cursor = self.connection.cursor()
        
        cursor.execute("SELECT EXISTS(SELECT 1 FROM trips WHERE Id = %s)", (trips_id,))
        if not cursor.fetchone()[0]:
            print("Trips ID bulunamadı")
            return

        cursor.execute("SELECT EXISTS(SELECT 1 FROM firms WHERE Id = %s)", (firm_id,))
        if not cursor.fetchone()[0]:
            print("Firm ID bulunamadı")
            return

        query = "INSERT INTO trip(trips_id, firm_id, trip_time) VALUES (%s, %s, %s)"
        cursor.execute(query, (trips_id, firm_id, trip_time))
        self.connection.commit()
        cursor.close()
        print("Trip added successfully.")

    def generate_trip_file(self):
        destination = input("Enter where you want to go: ")
        cursor = self.connection.cursor()
        query = """
            SELECT trips.trips_name, trip.trip_time, firms.firm_name
            FROM trip
            JOIN trips ON trip.trips_id = trips.Id
            JOIN firms ON trip.firm_id = firms.Id
            WHERE trips.trips_name LIKE %s
        """
        cursor.execute(query, ("%" + destination + "%",))
        
        found = False
        print("Trip name, Trip time, Firm name")
         
        for (trip_name, trip_time, firm_name) in cursor:
            print(f"{trip_name}, {trip_time}, {firm_name}")
            found = True

        if not found:
            print(f"No trips found for destination: {destination}")

        cursor.close()

    def __del__(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Connection to the database is closed.")

   
