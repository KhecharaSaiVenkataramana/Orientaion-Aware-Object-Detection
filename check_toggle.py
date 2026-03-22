layout = open("templates/layout.html", encoding="utf-8").read()
idx = layout.find("light-mode")
while idx != -1:
    line_start = layout.rfind('\n', 0, idx)
    line_end = layout.find('\n', idx)
    print(f"pos {idx}: {repr(layout[line_start:line_end])}")
    idx = layout.find("light-mode", idx+1)
    if idx > 0 and layout.count("light-mode") > 10:
        break