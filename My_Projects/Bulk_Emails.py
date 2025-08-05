import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import os

# Read the Excel file (update the path if needed)
excel_path = 'd:/Python/python-learnings/AI Projects/Weekly Trainning Report.xlsx'
df = pd.read_excel(excel_path)
df.columns = [col.strip().lower() for col in df.columns]
print('Excel columns:', df.columns.tolist())

# SMTP server details (example for Gmail)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Get today's date
now = datetime.now().date()

# Store passwords for each sender
passwords = {}

# Group all trainings by employee
employee_groups = df.groupby('employee')

for employee, group in employee_groups:
    from_email = group.iloc[0]['from']
    manager = group.iloc[0]['manager']
    password = passwords.get(from_email)
    if not password:
        password = input(f"Enter password for {from_email}: ")
        passwords[from_email] = password

    # Split trainings into upcoming and breached
    upcoming = group[pd.to_datetime(group['training due date']).dt.date > now]
    breached = group[pd.to_datetime(group['training due date']).dt.date <= now]

    # Compose email
    to_email = employee
    cc = manager if not upcoming.empty and not breached.empty else None
    subject = "Weekly Training Compliance Report"
    body = f"""
    <p>Dear {employee},</p>
    <p>This is your weekly training compliance report as part of our company's ongoing commitment to professional development and regulatory compliance. Please review your training status below and take the necessary actions to ensure you remain compliant with company policy.</p>
    """
    # Add upcoming trainings table
    if not upcoming.empty:
        body += "<h3 style='color:#0074D9;'>Upcoming Due Trainings</h3>"
        body += "<p>Please complete the following trainings before their due dates to avoid compliance breaches:</p>"
        body += "<table style='border-collapse:collapse;'>"
        body += "<tr style='background-color:#e6f2ff;font-weight:bold;'>"
        body += "<th style='border:1px solid #ccc;padding:6px;'>Training Name</th>"
        body += "<th style='border:1px solid #ccc;padding:6px;'>Training Due Date</th>"
        body += "</tr>"
        for _, row in upcoming.iterrows():
            body += f"<tr><td style='border:1px solid #ccc;padding:6px;'>{row['training name']}</td>"
            body += f"<td style='border:1px solid #ccc;padding:6px;background-color:yellow;'><b>{row['training due date']}</b></td></tr>"
        body += "</table><br>"
    # Add breached trainings table
    if not breached.empty:
        body += "<h3 style='color:#d9534f;'>Breached Trainings</h3>"
        body += "<p>The following trainings have missed their deadlines. As per company policy, your account may be disabled due to non-compliance. Please contact your manager for further assistance.</p>"
        body += "<table style='border-collapse:collapse;'>"
        body += "<tr style='background-color:#e6f2ff;font-weight:bold;'>"
        body += "<th style='border:1px solid #ccc;padding:6px;'>Training Name</th>"
        body += "<th style='border:1px solid #ccc;padding:6px;'>Training Due Date</th>"
        body += "<th style='border:1px solid #ccc;padding:6px;'>Manager</th>"
        body += "</tr>"
        for _, row in breached.iterrows():
            body += f"<tr><td style='border:1px solid #ccc;padding:6px;'>{row['training name']}</td>"
            body += f"<td style='border:1px solid #ccc;padding:6px;'><b>{row['training due date']}</b></td>"
            body += f"<td style='border:1px solid #ccc;padding:6px;'>{row['manager']}</td></tr>"
        body += "</table><br>"
    body += "<p>This report is generated automatically to help you stay on track with your professional development and to ensure compliance with our company’s standards and regulatory requirements. If you have any questions, please reach out to your manager or the HR department.</p>"
    body += "<p>Best regards,<br>Compliance Team</p>"

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    if cc:
        msg['Cc'] = cc
    msg.attach(MIMEText(body, 'html'))

    # Attach the Excel file
    with open(excel_path, 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(excel_path)}"')
        msg.attach(part)

    recipients = [to_email]
    if cc:
        recipients.append(cc)

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(from_email, password)
        server.sendmail(from_email, recipients, msg.as_string())
        print(f"Email sent from {from_email} to {to_email} (cc: {cc if cc else 'None'})")
        server.quit()
    except Exception as e:
        print(f"Failed to send email from {from_email} to {to_email}: {e}")
