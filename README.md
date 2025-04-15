###  🚌 Obilet Route and Trip Management System ### 

This is a simple object-oriented Python project that simulates a bus trip management system using MySQL. The project allows you to add bus companies (firms), routes, trips, and individual trip times. It also provides a search functionality to find trips based on destination keywords.

---

## 📁 Project Structure

Bus_Trip / └── pycache/ # Python cache files └──bus_trip │ └──pycache/  │ │ ├── create_obilet.py # Obilet class (database operations) │ │ ├── add_data_obilet.py 

---

## 💾 Technologies Used

- **Python **
- **MySQL** (via XAMPP)
- **mysql-connector-python** library

---

## ⚙️ Setup Instructions

1. **Install XAMPP** and start MySQL server.
2. **Create a database** named `bus_trip` in phpMyAdmin.
3. **Create the following tables** and relations inside the `obilet` database:



---

🧠 How the Code Works (Short Summary)


1. A class named  is created to handle all database operations.

2. It connects to the MySQL database using the provided credentials.

3. add_firm, add_route, add_trips, and add_trip methods are used to insert data into their respective tables.

4. generate_trip_file allows users to search trips by destination and shows trip name, time, and firm.

5. At the end, several firms, routes, trips, and trip times are added, and the user is prompted to search for a trip.

6. Database connection is closed automatically when the object is deleted.

---



**📊 Database Schema**

![Database Schema] (.\database.png)




```sql
CREATE TABLE firms (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    firm_name VARCHAR(100)
);

CREATE TABLE routes (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    route VARCHAR(255)
);

CREATE TABLE trips (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    direction INT,
    route_id INT,
    trips_name VARCHAR(255),
    FOREIGN KEY (route_id) REFERENCES routes(Id)
);

CREATE TABLE trip (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    trips_id INT,
    firm_id INT,
    trip_time VARCHAR(10),
    FOREIGN KEY (trips_id) REFERENCES trips(Id),
    FOREIGN KEY (![Ekran görüntüsü 2024-05-18 101246](https://github.com/user-attachments/assets/83448355-8a10-4f91-8c94-37d012b207d5)
firm_id) REFERENCES firms(Id)
);


---
