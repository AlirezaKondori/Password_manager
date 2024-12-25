# Password Manager

This Password Manager is a simple and secure application for storing and managing your passwords locally. It ensures the confidentiality of your sensitive information by encrypting stored passwords using a master key.

## Features

- **Master Key:**
  - Generates a secure master key for encrypting and decrypting passwords.
  - Ensures your data remains confidential.

- **Add Passwords:**
  - Securely store passwords for different services.

- **Retrieve Passwords:**
  - Decrypt and display stored credentials for a specific service.

- **List Services:**
  - View all the services for which passwords are stored.

- **SQLite Database:**
  - Uses a lightweight local database for persistence.

## Requirements

- Python 3.6 or higher
- Required Python libraries:
  - `cryptography`
  - `sqlite3` (built-in with Python)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd password-manager
   ```

2. Install the required libraries:
   ```bash
   pip install cryptography
   ```

3. Run the application:
   ```bash
   python password_manager.py
   ```

## Usage

### Options

1. **Generate Master Key**:
   - Generates a new master key for encrypting passwords.
   - **Important:** Save this key securely. Losing the master key will result in the loss of access to your stored passwords.

2. **Set Master Key**:
   - Set the master key to decrypt and encrypt passwords.

3. **Add Password**:
   - Add a new password for a specific service.

4. **Retrieve Password**:
   - Decrypt and display the username and password for a specific service.

5. **List Services**:
   - View all the services for which passwords are stored.

6. **Exit**:
   - Safely close the application.

### Example Workflow

1. Generate a master key:
   ```
   Your master key (save this securely): e.g., b'X4VAv2...u6k='
   ```

2. Add a password:
   - Enter service name, username, and password when prompted.

3. Retrieve a password:
   - Provide the service name to view the stored credentials.

4. List services:
   - View all stored service names.

## Security Considerations

- **Master Key Security:**
  - The master key must be securely stored by the user.
  - If the master key is lost, all stored passwords will be unrecoverable.

- **Encryption:**
  - Uses the `cryptography` library's `Fernet` symmetric encryption for strong encryption.

- **Local Storage:**
  - Passwords are stored in an SQLite database on your local machine.

## Future Enhancements

- Support for changing the master key while preserving access to old passwords.
- Adding a password strength generator.
- Building a graphical user interface (GUI).
- Cross-device synchronization.

## Author

Alireza Kondori
