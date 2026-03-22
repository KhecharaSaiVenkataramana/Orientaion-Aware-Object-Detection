layout = open("templates/layout.html", encoding="utf-8").read()

# Remove the cursor dot entirely from CSS and JS — replace with cleaner version
import re

# Replace cursor dot CSS
layout = re.sub(
    r'\.cursor-dot \{[^}]+\}',
    '''.cursor-dot {
    position: fixed;
    width: 8px;
    height: 8px;
    background: #00cfff;
    border-radius: 50%;
    pointer-events: none;
    z-index: 99999;
    top: 0;
    left: 0;
    opacity: 0;
    box-shadow: 0 0 10px #00cfff, 0 0 20px rgba(0,207,255,0.4);
    will-change: transform;
    transition: opacity 0.2s;
}''',
    layout
)

# Replace cursor JS — use transform instead of left/top for smoothness
old_cursor_block = re.search(
    r'// ── CURSOR DOT ──.*?}\)\(\);',
    layout, re.DOTALL
)

new_cursor_js = '''// ── CURSOR DOT ──────────────────────────────────────────────
(function() {
    var dot = document.getElementById('cursor-dot');
    if (!dot) return;
    var x = window.innerWidth / 2;
    var y = window.innerHeight / 2;

    document.addEventListener('mousemove', function(e) {
        x = e.clientX;
        y = e.clientY;
        dot.style.opacity = '1';
        dot.style.transform = 'translate(' + (x - 4) + 'px, ' + (y - 4) + 'px)';
    });
    document.addEventListener('mouseleave', function() {
        dot.style.opacity = '0';
    });
})();'''

if old_cursor_block:
    layout = layout.replace(old_cursor_block.group(), new_cursor_js)
    print("Cursor block replaced")
else:
    # Just append the fix before </script>
    layout = layout.replace(
        '// ── BUTTON RIPPLE',
        new_cursor_js + '\n\n// ── BUTTON RIPPLE'
    )
    print("Cursor JS injected")

with open("templates/layout.html", "w", encoding="utf-8") as f:
    f.write(layout)

# Verify
content = open("templates/layout.html", encoding="utf-8").read()
print("HAS translate transform:", "translate(' + (x - 4)" in content)
print("Done! Restart: python app.py")