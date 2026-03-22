home = open("templates/home.html", encoding="utf-8").read()
start = home.find("HOW IT WORKS")
print(repr(home[start:start+2000]))