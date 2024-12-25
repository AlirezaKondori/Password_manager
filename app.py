import os
import sqlite3
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self, db_path="passwords.db"):
        self.db_path = db_path
        self.master_key = None
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self._setup_database()

    def _setup_database(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            username TEXT NOT NULL,
            password BLOB NOT NULL
        )
        """)
        self.conn.commit()

    def set_master_key(self, key):
        if not isinstance(key, bytes):
            raise ValueError("Master key must be bytes.")
        self.master_key = Fernet(key)

    def generate_master_key(self):
        key = Fernet.generate_key()
        print("Your master key (save this securely):", key.decode())
        self.set_master_key(key)

    def add_password(self, service, username, password):
        if self.master_key is None:
            raise ValueError("Master key not set.")
        encrypted_password = self.master_key.encrypt(password.encode())
        self.cursor.execute("""
        INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)
        """, (service, username, encrypted_password))
        self.conn.commit()

    def retrieve_password(self, service):
        if self.master_key is None:
            raise ValueError("Master key not set.")
        self.cursor.execute("SELECT username, password FROM passwords WHERE service = ?", (service,))
        result = self.cursor.fetchone()
        if result:
            username, encrypted_password = result
            decrypted_password = self.master_key.decrypt(encrypted_password).decode()
            return username, decrypted_password
        else:
            print("No entry found for service.")
            return None

    def list_services(self):
        self.cursor.execute("SELECT service FROM passwords")
        services = self.cursor.fetchall()
        return [service[0] for service in services]

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    print("Welcome to the Password Manager!")
    manager = PasswordManager()

    while True:
        print("\nOptions:")
        print("1. Generate master key")
        print("2. Set master key")
        print("3. Add password")
        print("4. Retrieve password")
        print("5. List services")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            manager.generate_master_key()
        elif choice == "2":
            key = input("Enter your master key: ").encode()
            try:
                manager.set_master_key(key)
                print("Master key set successfully.")
            except ValueError as e:
                print(e)
        elif choice == "3":
            service = input("Enter service name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                manager.add_password(service, username, password)
                print("Password added successfully.")
            except ValueError as e:
                print(e)
        elif choice == "4":
            service = input("Enter service name: ")
            try:
                result = manager.retrieve_password(service)
                if result:
                    username, password = result
                    print(f"Username: {username}, Password: {password}")
            except ValueError as e:
                print(e)
        elif choice == "5":
            services = manager.list_services()
            print("Stored services:")
            for service in services:
                print(service)
        elif choice == "6":
            manager.close()
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")
