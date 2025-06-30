## Advanced Credential Harvester

This Python script is a simulated credential harvester tool designed for educational and red team development purposes. It prompts the user to input mock credentials (username and password) and saves them securely into a log file

### Features
- Prompts for username and password
- Timestamped credential logging
- Stores data in a structured `.txt` file
- Modular code for easy future upgrades
- No real network or malicious activity - for ethical use only

### How It Works

1. Prompts the user with a realistic credential input message.
2. Saves each login attempt with a time stamp.
3. Logs stored in `harvested_credential.txt`.

### Getting Started
```bash
python3 advanced_credential_harvester.py

### Example Output

[2025-07-01 18:40:02] Username: admin | Password: hunter2
[2025-07-01 18:43:10] Username: guest | Password: 1234

### Disclaimer

THIS TOOL IS INTENDED FOR EDUCATIONAL AND TRAINING PURPOSES ONLY. DO NOT USE IT FOR UNAUTHORIZED ACCESS OR ILLEGAL ACTIVITIES.
