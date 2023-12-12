#!/usr/bin/python3

import psutil
import smtplib
from email.mime.text import MIMEText

# Function to save information to a .txt file
def save_to_txt(cpu_info, file_path="cpu_info.txt"):
    with open(file_path, 'w') as file:
        for name, value in cpu_info.items():
            file.write(f"{name}: {value} seconds\n")

# Function to send email using Outlook SMTP server
def send_email(file_path):
    sender_email = "rcodelab@outlook.com"
    receiver_email = "rcodelab@outlook.com"
    subject = "CPU Information"
    body = "Please find attached the CPU information."

    with open(file_path, 'r') as file:
        content = file.read()

    message = MIMEText(body + "\n\n" + content)
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Use Outlook SMTP server
    smtp_server = "smtp.office365.com"
    smtp_port = 587
    smtp_username = "rcodelab@outlook.com"
    smtp_password = "YourOutlookPassword"  # Replace with your Outlook password

    # Start TLS for security
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Login with Outlook credentials
    server.login(smtp_username, smtp_password)

    # Send email
    server.sendmail(sender_email, [receiver_email], message.as_string())

    # Quit SMTP server
    server.quit()

def get_cpu_times(information_type=None):
    # Same as before...

if __name__ == "__main__":
    try:
        cpu_info = get_cpu_times()
        if cpu_info is not None:
            for seq_num, (name, value) in enumerate(cpu_info.items(), start=1):
                print(f"{seq_num}. {name}: {value} seconds  # Time spent in {name} mode")

            # Save to .txt file
            save_to_txt(cpu_info)

            # Send email
            send_email("cpu_info.txt")

        user_time = get_cpu_times("user")
        if user_time is not None:
            print(f"User time: {user_time} seconds  # Time spent by normal processes in user mode")

    except Exception as error:
        print(f"Error occurred: {error}")
