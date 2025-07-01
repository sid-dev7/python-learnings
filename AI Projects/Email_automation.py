import pandas as pd
import win32com.client as win32

# Load Excel file
file_path = 'emails.xlsx'  # Update with your actual file path
df = pd.read_excel(file_path)

# Initialize Outlook
outlook = win32.Dispatch('Outlook.Application')

# Loop through each row and send email
for index, row in df.iterrows():
    try:
        mail = outlook.CreateItem(0)  # Create a new mail item
        mail.To = row['Email']
        mail.Subject = row['Subject']
        mail.Body = row['Body']
        
        # mail.Send()     # Uncomment this to actually send
        mail.Display()     # Use this for testing (opens email draft)

        print(f"Email prepared for: {row['Email']}")
    except Exception as e:
        print(f"Error sending to {row['Email']}: {str(e)}")
