import os, re
BASE = r"C:\Users\khech\OAOD Project\website"

# Fix in home.html — replace onmouseover/onmouseout on step cards
# with light-mode aware versions
home = open(os.path.join(BASE, "templates", "home.html"), encoding="utf-8").read()

# Replace all step card onmouseover/onmouseout with light-mode aware JS
old1 = """onmouseover="this.style.transform='translateY(-8px)';this.style.borderColor='#6644ff';this.style.boxShadow='0 20px 40px rgba(102,68,255,0.2)'"
             onmouseout="this.style.transform='none';this.style.borderColor='rgba(102,68,255,0.2)';this.style.boxShadow='none'">"""

new1 = """onmouseover="var lm=document.body.classList.contains('light-mode');this.style.transform='translateY(-8px)';this.style.borderColor='#6644ff';this.style.background=lm?'#fff':'#0d0b22';this.style.boxShadow=lm?'0 20px 40px rgba(102,68,255,0.12)':'0 20px 40px rgba(102,68,255,0.2)'"
             onmouseout="var lm=document.body.classList.contains('light-mode');this.style.transform='none';this.style.borderColor='rgba(102,68,255,0.2)';this.style.background=lm?'#fff':'#0d0b22';this.style.boxShadow='none'">"""

old2 = """onmouseover="this.style.transform='translateY(-8px)';this.style.borderColor='#00cfff';this.style.boxShadow='0 20px 40px rgba(0,207,255,0.15)'"
             onmouseout="this.style.transform='none';this.style.borderColor='rgba(102,68,255,0.2)';this.style.boxShadow='none'">"""

new2 = """onmouseover="var lm=document.body.classList.contains('light-mode');this.style.transform='translateY(-8px)';this.style.borderColor='#00cfff';this.style.background=lm?'#fff':'#0d0b22';this.style.boxShadow=lm?'0 20px 40px rgba(0,207,255,0.08)':'0 20px 40px rgba(0,207,255,0.15)'"
             onmouseout="var lm=document.body.classList.contains('light-mode');this.style.transform='none';this.style.borderColor='rgba(102,68,255,0.2)';this.style.background=lm?'#fff':'#0d0b22';this.style.boxShadow='none'">"""

old3 = """onmouseover="this.style.transform='translateY(-8px)';this.style.borderColor='#6644ff';this.style.boxShadow='0 20px 40px rgba(102,68,255,0.2)'"
             onmouseout="this.style.transform='none';this.style.borderColor='rgba(102,68,255,0.2)';this.style.boxShadow='none'">
            <div style="width:72px;height:72px;border-radius:50%;
                        background:linear-gradient(135deg,#6644ff,#00cfff);"""

new3 = """onmouseover="var lm=document.body.classList.contains('light-mode');this.style.transform='translateY(-8px)';this.style.borderColor='#6644ff';this.style.background=lm?'#fff':'#0d0b22';this.style.boxShadow=lm?'0 20px 40px rgba(102,68,255,0.12)':'0 20px 40px rgba(102,68,255,0.2)'"
             onmouseout="var lm=document.body.classList.contains('light-mode');this.style.transform='none';this.style.borderColor='rgba(102,68,255,0.2)';this.style.background=lm?'#fff':'#0d0b22';this.style.boxShadow='none'">
            <div style="width:72px;height:72px;border-radius:50%;
                        background:linear-gradient(135deg,#6644ff,#00cfff);"""

count = 0
if old1 in home:
    home = home.replace(old1, new1)
    count += 1
    print("Fixed step card 1 hover")
if old2 in home:
    home = home.replace(old2, new2)
    count += 1
    print("Fixed step card 2 hover")
if old3 in home:
    home = home.replace(old3, new3)
    count += 1
    print("Fixed step card 3 hover")

if count == 0:
    print("Patterns not matched — using regex replacement")
    # Generic fix: add light mode check to all onmouseover with background color
    home = re.sub(
        r"onmouseover=\"(this\.style\.transform='translateY\(-8px\)';this\.style\.borderColor='([^']+)';this\.style\.boxShadow='([^']+)')\"",
        r"onmouseover=\"var lm=document.body.classList.contains('light-mode');\1;this.style.background=lm?'#fff':'#0d0b22'\"",
        home
    )
    home = re.sub(
        r"onmouseout=\"(this\.style\.transform='none';this\.style\.borderColor='rgba\(102,68,255,0\.2\)';this\.style\.boxShadow='none')\"",
        r"onmouseout=\"var lm=document.body.classList.contains('light-mode');\1;this.style.background=lm?'#fff':'#0d0b22'\"",
        home
    )
    print("Regex replacement applied")

with open(os.path.join(BASE, "templates", "home.html"), "w", encoding="utf-8") as f:
    f.write(home)
print("home.html saved!")

# Also fix about.html and discuss.html cards
for fname in ["about.html", "discuss.html"]:
    fpath = os.path.join(BASE, "templates", fname)
    content = open(fpath, encoding="utf-8").read()
    content = re.sub(
        r"onmouseover=\"this\.style\.borderColor='#6644ff';this\.style\.transform='translateY\(-6px\)'\"",
        "onmouseover=\"var lm=document.body.classList.contains('light-mode');this.style.borderColor='#6644ff';this.style.transform='translateY(-6px)';this.style.background=lm?'#fff':'#0d0b22'\"",
        content
    )
    content = re.sub(
        r"onmouseout=\"this\.style\.borderColor='rgba\(102,68,255,0\.18\)';this\.style\.transform='none'\"",
        "onmouseout=\"var lm=document.body.classList.contains('light-mode');this.style.borderColor='rgba(102,68,255,0.18)';this.style.transform='none';this.style.background=lm?'#fff':'#0d0b22'\"",
        content
    )
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{fname} hover fixed!")

print("\nDone! Restart: python app.py")