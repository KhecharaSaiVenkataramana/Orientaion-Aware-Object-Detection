layout = open("templates/layout.html", encoding="utf-8").read()

reset_js = """
                document.querySelectorAll('.step-card,.feature-card,.card,.dataset-card').forEach(function(el){
                    el.style.background='';
                    el.style.boxShadow='';
                    el.style.borderColor='';
                });"""

old_add = "document.body.classList.add('light-mode');"
old_remove = "document.body.classList.remove('light-mode');"

if old_add in layout:
    layout = layout.replace(
        old_add,
        old_add + reset_js
    )
    print("Add patched!")

if old_remove in layout:
    layout = layout.replace(
        old_remove,
        old_remove + reset_js
    )
    print("Remove patched!")

with open("templates/layout.html", "w", encoding="utf-8") as f:
    f.write(layout)
print("Done!")