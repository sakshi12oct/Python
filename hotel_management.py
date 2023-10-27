pip install mysql-connector-python
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hotel_management"
)

# Create a cursor object to interact with the database
cursor = db.cursor()
# Initialize the database schema for rooms
cursor.execute("""
    CREATE TABLE IF NOT EXISTS rooms (
        room_number INT PRIMARY KEY,
        occupant VARCHAR(255),
        rate DOUBLE(10, 2)
    )
""")
cursor.execute("""
   
    insert into rooms values (106,null,150);
""")
# Function to display room availability
def display_room_availability():
    cursor.execute("SELECT * FROM rooms")
    rooms = cursor.fetchall()

    if not rooms:
        print("No rooms available.")
    else:
        print("Room Availability:")
        for room in rooms:
            room_number, occupant, rate = room
            if occupant is None:
                print(f"Room {room_number} is available at ${rate} per night.")
            else:
                print(f"Room {room_number} is occupied by {occupant}.")

# Function to check-in a guest
def check_in_guest(room_number, guest_name):
    cursor.execute("SELECT occupant FROM rooms WHERE room_number = %s", (room_number,))
    result = cursor.fetchone()
    if result is not None and result[0] is None:
        cursor.execute("UPDATE rooms SET occupant = %s WHERE room_number = %s", (guest_name, room_number))
        db.commit()
        print(f"{guest_name} has checked into Room {room_number}.")
    else:
        print("Invalid room number or room is already occupied.")

# Function to check-out a guest
def check_out_guest(room_number):
    cursor.execute("SELECT occupant FROM rooms WHERE room_number = %s", (room_number,))
    result = cursor.fetchone()
    if result is not None and result[0] is not None:
        occupant = result[0]
        cursor.execute("UPDATE rooms SET occupant = NULL WHERE room_number = %s", (room_number,))
        db.commit()
        print(f"{occupant} has checked out from Room {room_number}.")
    else:
        print("Invalid room number or room is not occupied.")

# Main program
while True:
    print("\nHotel Management System")
    print("1. Display Room Availability")
    print("2. Check-in Guest")
    print("3. Check-out Guest")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_room_availability()
    elif choice == "2":
        room_number = input("Enter room number: ")
        guest_name = input("Enter guest name: ")
        check_in_guest(room_number, guest_name)
    elif choice == "3":
        room_number = input("Enter room number: ")
        check_out_guest(room_number)
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# Close the cursor and database connection
cursor.close()
db.close()


'''

output:

Hotel Management System
1. Display Room Availability
2. Check-in Guest
3. Check-out Guest
4. Exit
Enter your choice:  1
Room Availability:
Room 101 is available at $100.0 per night.
Room 102 is available at $110.0 per night.
Room 103 is available at $120.0 per night.
Room 104 is occupied by Sakshi.
Room 105 is available at $150.0 per night.
Room 106 is available at $150.0 per night.

Hotel Management System
1. Display Room Availability
2. Check-in Guest
3. Check-out Guest
4. Exit
Enter your choice:  2
Enter room number:  103
Enter guest name:  Parv
Parv has checked into Room 103.

Hotel Management System
1. Display Room Availability
2. Check-in Guest
3. Check-out Guest
4. Exit
Enter your choice:  1
Room Availability:
Room 101 is available at $100.0 per night.
Room 102 is available at $110.0 per night.
Room 103 is occupied by Parv.
Room 104 is occupied by Sakshi.
Room 105 is available at $150.0 per night.
Room 106 is available at $150.0 per night.

Hotel Management System
1. Display Room Availability
2. Check-in Guest
3. Check-out Guest
4. Exit
'''
