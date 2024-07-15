from __database__ import connector

# connect to a local database on localhost as root
connection = connector.inventory_database()
cursor = connection.cursor()


def overview():
    cursor.execute(f"SELECT device, surname FROM employees, devices, relations WHERE devices.iddevices = relations.iddevices and employees.idEmployees = relations.idEmployees")
    for row in cursor.fetchall():
        print(row)

def search_employee():
    employee = input("What's the name of the employee? ")
    cursor.execute(f"SELECT device FROM employees, devices, relations WHERE devices.iddevices = relations.iddevices and employees.idEmployees = relations.idEmployees and surname = '{employee}'")
    for row in cursor.fetchall():
        print(row)

def add_device():
    device_name = input("What's the name of the device? ")
    device_type = input("What's the type of the device? ")
    cursor.execute(f"INSERT INTO devices(device, `device kind`) VALUES('{device_name}', '{device_type}')")
    connection.commit()

# main loop of the program
while True:
    choice = int(input("""Hello. Please make a choice: 
               1. I want an overview
               2. I am searching for an employee
               3. I want to add a device
               4. I want to quit immediately
    """))

    if choice == 1:
        overview()
    elif choice == 2:
        search_employee()
    elif choice == 3:
        add_device()
    elif choice == 4:
        connection.close()
        break
