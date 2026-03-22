home = open("templates/home.html", encoding="utf-8").read()

# Replace all hardcoded card backgrounds with empty string
# and let CSS classes handle the color
home = home.replace(
    'background:var(--bg-card,#0d0b22);border:1px solid rgba(102,68,255,0.2);border-radius:20px;',
    'border:1px solid rgba(102,68,255,0.2);border-radius:20px;'
)
home = home.replace(
    'background:#0d0b22;border:1px solid rgba(102,68,255,0.2);border-radius:20px;',
    'border:1px solid rgba(102,68,255,0.2);border-radius:20px;'
)

# Add step-card class to all 3 cards
home = home.replace(
    'class="reveal reveal-delay-1"\n             style="border:1px solid rgba(102,68,255,0.2);border-radius:20px;',
    'class="reveal reveal-delay-1 step-card"\n             style="border:1px solid rgba(102,68,255,0.2);border-radius:20px;'
)
home = home.replace(
    'class="reveal reveal-delay-2"\n             style="border:1px solid rgba(102,68,255,0.2);border-radius:20px;',
    'class="reveal reveal-delay-2 step-card"\n             style="border:1px solid rgba(102,68,255,0.2);border-radius:20px;'
)
home = home.replace(
    'class="reveal reveal-delay-3"\n             style="border:1px solid rgba(102,68,255,0.2);border-radius:20px;',
    'class="reveal reveal-delay-3 step-card"\n             style="border:1px solid rgba(102,68,255,0.2);border-radius:20px;'
)

with open("templates/home.html", "w", encoding="utf-8") as f:
    f.write(home)
print("Done!")