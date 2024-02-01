import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_personalized_email(sender_email, sender_password, recipient, subject, body):
    try:
        # Set up the SMTP server
        smtp_server = smtplib.SMTP('your_smtp_server', your_smtp_port)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)

        # Create message container
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient
        message['Subject'] = subject

        # Attach body to the message
        message.attach(MIMEText(body, 'plain'))

        # Send the email
        smtp_server.send_message(message)

        # Quit the server
        smtp_server.quit()

        print(f"Email sent successfully to {recipient}")

    except Exception as e:
        print(f"Error sending email to {recipient}: {str(e)}")

def main():
    # Sender credentials
    sender_email = 'your_email@example.com'
    sender_password = 'your_email_password'

    # Recipient list with personalized details
    recipients = [
        {'email': 'recipient1@example.com', 'subject': 'Subject 1', 'body': 'Body 1'},
        {'email': 'recipient2@example.com', 'subject': 'Subject 2', 'body': 'Body 2'},
        # Add more recipients as needed
    ]

    # Iterate through the recipient list and send personalized emails
    for recipient_info in recipients:
        send_personalized_email(
            sender_email,
            sender_password,
            recipient_info['email'],
            recipient_info['subject'],
            recipient_info['body']
        )

if __name__ == "__main__":
    main()