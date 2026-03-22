content = open("templates/history.html", encoding="utf-8").read()
print("EXTENDS LAYOUT:", "extends" in content)
print("HAS OWN NAVBAR:", '<div class="navbar">' in content)
print("FIRST 100:", repr(content[:100]))