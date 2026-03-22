home = open("templates/home.html", encoding="utf-8").read()

# Fix Step 1 default background
home = home.replace(
    'style="background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:20px;\n                    padding:36px 32px;text-align:center;position:relative;z-index:1;\n                    transition:transform 0.3s,border-color 0.3s,box-shadow 0.3s;"',
    'style="background:var(--bg-card,#0d0b22);border:1px solid rgba(102,68,255,0.2);border-radius:20px;\n                    padding:36px 32px;text-align:center;position:relative;z-index:1;\n                    transition:transform 0.3s,border-color 0.3s,box-shadow 0.3s;"'
)

# Fix ALL hardcoded dark card backgrounds in home.html
home = home.replace("background:#0d0b22;", "background:var(--bg-card,#0d0b22);")
home = home.replace("background: #0d0b22;", "background:var(--bg-card,#0d0b22);")
home = home.replace("background:#0d0b22'", "background:var(--bg-card,#0d0b22)'")
home = home.replace("':\'#0d0b22\'", "':getComputedStyle(document.body).getPropertyValue('--bg-card')||'#0d0b22\'")

# Fix hover onmouseover/onmouseout to use CSS variable
import re
home = re.sub(
    r"this\.style\.background=lm\?'#fff':'#0d0b22'",
    "this.style.background=''",
    home
)

with open("templates/home.html", "w", encoding="utf-8") as f:
    f.write(home)
print("Done!")