import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Read the Excel file (update the path if needed)
df = pd.read_excel('d:/Python/python-learnings/AI Projects/emails.xlsx')
df.columns = [col.strip().lower() for col in df.columns]
print('Excel columns:', df.columns.tolist())

# SMTP server details (example for Gmail)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Loop through each row in the Excel file
for index, row in df.iterrows():
    to_email = row['to']
    from_email = row['from']
    subject = row['subject']
    body = row['note']
    # Prompt for password or use a secure method to get it
    password = input(f"Enter password for {from_email}: ")

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        print(f"Email sent from {from_email} to {to_email}")
        server.quit()
    except Exception as e:
        print(f"Failed to send email from {from_email} to {to_email}: {e}")
