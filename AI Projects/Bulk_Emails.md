# Automated Training Compliance Email System

## Overview
This project automates the process of notifying employees and their managers about upcoming and overdue training requirements. It reads a weekly Excel report, analyzes deadlines, and sends personalized, professional emails with a summary table and the original report attached.

---

## Features
- Reads a training report from an Excel file
- Groups all trainings by employee and sends a single, consolidated email per employee
- Highlights upcoming and breached (overdue) trainings in professional HTML tables
- CCs the manager if any training is overdue
- Attaches the original Excel report to each email
- Prompts for the sender's email password only once per session
- Uses secure SMTP (TLS) for sending emails

---

## How It Works
1. **Data Input:** Reads the Excel file ("Weekly Trainning Report.xlsx") with columns: Employee, From, Manager, Training Name, Training Due Date.
2. **Grouping:** Groups all rows by employee so each employee receives one email with all their trainings.
3. **Logic:**
   - If a training due date is in the future, it is listed as "Upcoming Due" (highlighted in yellow).
   - If a training due date is in the past, it is listed as "Breached" and the manager is CC'd.
4. **Email Body:**
   - Uses HTML tables with a light blue header and bold column names for clarity.
   - Includes a professional message about compliance and next steps.
5. **Attachment:**
   - Attaches the original Excel report to each email for reference.
6. **Security:**
   - Prompts for the sender's password only once per session and does not store it anywhere.

---

## Code Walkthrough

### 1. Import Libraries
```python
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
import os
```
- **pandas**: For reading and processing the Excel file.
- **smtplib**: For sending emails via SMTP.
- **email.mime**: For constructing email messages and attachments.
- **datetime**: For date calculations.
- **os**: For file path handling.

### 2. Read and Prepare Data
```python
excel_path = 'd:/Python/python-learnings/AI Projects/Weekly Trainning Report.xlsx'
df = pd.read_excel(excel_path)
df.columns = [col.strip().lower() for col in df.columns]
```
- Reads the Excel file and normalizes column names to lowercase for consistency.

### 3. SMTP Setup
```python
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
```
- Sets up the Gmail SMTP server and port for secure email sending.

### 4. Group by Employee
```python
employee_groups = df.groupby('employee')
```
- Groups all training records by employee so each gets a single email.

### 5. Main Loop
```python
for employee, group in employee_groups:
    from_email = group.iloc[0]['from']
    manager = group.iloc[0]['manager']
    ...
```
- For each employee, retrieves the sender and manager email addresses.
- Prompts for the sender's password only once per session.

### 6. Split Trainings
```python
upcoming = group[pd.to_datetime(group['training due date']).dt.date > now]
breached = group[pd.to_datetime(group['training due date']).dt.date <= now]
```
- Splits the employee's trainings into upcoming and breached based on the due date.

### 7. Compose Email
- Builds a professional HTML email body with:
  - A greeting and compliance message
  - A table of upcoming trainings (yellow highlight for due date)
  - A table of breached trainings (manager included)
  - A closing message

### 8. Attach Excel File
```python
with open(excel_path, 'rb') as f:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(excel_path)}"')
    msg.attach(part)
```
- Attaches the original Excel report to the email.

### 9. Send Email
```python
server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
server.starttls()
server.login(from_email, password)
server.sendmail(from_email, recipients, msg.as_string())
server.quit()
```
- Connects to the SMTP server, logs in, and sends the email to the employee (and manager if needed).

---

## Impact
- **Effort Saved:** Automates hours of manual tracking and emailing each week.
- **Increased Efficiency:** Ensures timely notifications, improving training completion rates.
- **Project Manager Value:** Reduces compliance risk, provides auditability, and supports a culture of accountability.

---

## Usage
1. Update the Excel file path if needed.
2. Run the script in your Python environment.
3. Enter the sender's email password when prompted (use an App Password for Gmail).
4. Emails will be sent to all employees with their training status and the report attached.

---

## Screenshot / Visual
![Automated Email System Illustration](https://github.com/sid-dev7/python-learnings/blob/main/AI%20Projects/Email.pic.png)    

---

## License
This project is open source and free to use for educational and professional purposes.
