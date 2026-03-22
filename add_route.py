content = open("app.py", encoding="utf-8").read()

if 'send_suggestion' in content:
    print("Route already exists.")
else:
    new_route = '''
@app.route("/send-suggestion", methods=["POST"])
def send_suggestion():
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    SMTP_USER     = "PLACEHOLDER_EMAIL"
    SMTP_PASSWORD = "PLACEHOLDER_PASSWORD"
    TEAM_EMAIL    = "team.raven.ai@outlook.com"

    category     = request.form.get("category", "General")
    message      = request.form.get("message", "").strip()
    sender_email = session.get("username", "Anonymous")

    if not message:
        return jsonify({"status": "error", "msg": "Message cannot be empty"}), 400

    if SMTP_USER == "PLACEHOLDER_EMAIL":
        print(f"[SUGGESTION] From: {sender_email} | Category: {category} | Msg: {message}")
        return jsonify({"status": "ok", "msg": "Suggestion received!"})

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"[RAVEN] {category} from {sender_email}"
        msg["From"]    = SMTP_USER
        msg["To"]      = TEAM_EMAIL
        msg["Reply-To"] = sender_email
        body = f"""<html><body style="font-family:Arial;background:#07051a;color:#eee;padding:30px;">
        <h2 style="color:#00cfff;">New RAVEN Suggestion</h2>
        <p><b>From:</b> {sender_email}</p>
        <p><b>Category:</b> {category}</p>
        <p><b>Message:</b> {message}</p>
        </body></html>"""
        msg.attach(MIMEText(body, "html"))
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, TEAM_EMAIL, msg.as_string())
        return jsonify({"status": "ok", "msg": "Suggestion sent!"})
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")
        return jsonify({"status": "error", "msg": "Failed to send. Try again later."})

'''

    old = 'if __name__ == "__main__":'
    content = content.replace(old, new_route + old)
    with open("app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Done! send_suggestion route added.")