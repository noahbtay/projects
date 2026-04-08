from plyer import notification
import smtplib
from email.mime.text import MIMEText

EMAIL = "your_email@example.com"
PASSWORD = "your_email_password"
TO_EMAIL = "your_email@gmail.com"

def send_desktop_alert(ip):
    notification.notify(
        title=" VPN LEAK DETECTED!",
        message=f"Your VPN has leaked! Detected IP: {ip}",
        timeout=5
    )

def send_email_alert(ip):
    msg = MIMEText(f"Your VPN has leaked! Detected IP: {ip}")
    msg['Subject'] = "VPN Leak Alert"
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)

