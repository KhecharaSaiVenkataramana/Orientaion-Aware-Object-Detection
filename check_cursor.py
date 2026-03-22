css = open("static/style.css", encoding="utf-8").read()
start = css.find(".cursor-dot")
if start == -1:
    print("Not in style.css either!")
else:
    print("Found in style.css:")
    print(repr(css[start:start+300]))