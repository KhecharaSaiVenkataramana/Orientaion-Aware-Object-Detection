import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_USER     = "team.ravendetections@gmail.com"
SMTP_PASSWORD = "qpye xwcy ndfh pcbk"
TEAM_EMAIL    = "team.ravendetecctions@gmail.com"

try:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "[RAVEN] Test suggestion email"
    msg["From"]    = SMTP_USER
    msg["To"]      = TEAM_EMAIL
    body = "<html><body><h2>Test email from RAVEN</h2><p>If you see this, email is working!</p></body></html>"
    msg.attach(MIMEText(body, "html"))

    print("Connecting to Gmail SMTP...")
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        print("TLS started...")
        server.login(SMTP_USER, SMTP_PASSWORD)
        print("Logged in!")
        server.sendmail(SMTP_USER, TEAM_EMAIL, msg.as_string())
        print("Email sent successfully!")

except smtplib.SMTPAuthenticationError as e:
    print("AUTH ERROR:", e)
    print("App password is wrong or 2FA not enabled on this Gmail.")
except Exception as e:
    print("ERROR:", type(e).__name__, e)