content = open("app.py", encoding="utf-8").read()

content = content.replace(
    'SMTP_USER     = "PLACEHOLDER_EMAIL"',
    'SMTP_USER     = "team.ravendetections@gmail.com"'
)

with open("app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Done! Verifying...")
for line in open("app.py", encoding="utf-8").read().split('\n'):
    if any(x in line for x in ['SMTP_USER', 'SMTP_PASS', 'TEAM_EMAIL']):
        if '==' not in line and 'login' not in line and 'sendmail' not in line and 'From' not in line and 'To' not in line:
            print(repr(line))