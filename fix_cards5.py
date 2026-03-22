import re

home = open("templates/home.html", encoding="utf-8").read()

# Remove ALL background settings from onmouseover/onmouseout on step cards
# Replace the hover handlers to NOT touch background at all
home = re.sub(
    r"onmouseover=\"var lm=document\.body\.classList\.contains\('light-mode'\);this\.style\.transform='translateY\(-8px\)';this\.style\.borderColor='#6644ff';this\.style\.background=lm\?'#fff':'#0d0b22';this\.style\.boxShadow=lm\?'0 20px 40px rgba\(102,68,255,0\.12\)':'0 20px 40px rgba\(102,68,255,0\.2\)'\"",
    "onmouseover=\"this.style.transform='translateY(-8px)';this.style.borderColor='#6644ff';this.style.boxShadow='0 20px 40px rgba(102,68,255,0.25)'\"",
    home
)

home = re.sub(
    r"onmouseout=\"var lm=document\.body\.classList\.contains\('light-mode'\);this\.style\.transform='none';this\.style\.borderColor='rgba\(102,68,255,0\.2\)';this\.style\.background=lm\?'#fff':'#0d0b22';this\.style\.boxShadow='none'\"",
    "onmouseout=\"this.style.transform='none';this.style.borderColor='rgba(102,68,255,0.2)';this.style.boxShadow='none'\"",
    home
)

with open("templates/home.html", "w", encoding="utf-8") as f:
    f.write(home)

# Verify
c = open("templates/home.html", encoding="utf-8").read()
print("Background in hover:", "this.style.background" in c[c.find("step-card"):c.find("step-card")+500] if "step-card" in c else "step-card not found")
print("Done!")