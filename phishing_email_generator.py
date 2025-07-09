def generate_phishing_email(sender, recipient, subject, message):
    template = f"""
From: {sender}
To: {recipient}
Subject: {subject}
MIME-Version: 1.0
Content-Type: text/plain

{message}

--
This message was generated for educational purposes only.
"""
    return template


def main():
    print("=== Phishing Email Generator (Educational Use Only) ===")
    sender = input("Enter spoofed sender email: ").strip()
    recipient = input("Enter recipient email: ").strip()
    subject = input("Enter subject: ").strip()
    message = input("Enter the phishing message: ").strip

    email = generate_phishing_email(sender, recipient, subject, message)
    print("\n--- Generated Email ---")
    print(email)

    with open("generated_phishing_email.txt", "w") as file:
        file.write(email)
        print("\n[*] Email saved to 'generated_phishing_email.txt'")


if __name__ == "__main__":
    main()
