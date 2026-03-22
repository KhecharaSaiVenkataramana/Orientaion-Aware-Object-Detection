import re
content = open("app.py", encoding="utf-8").read()

# Replace the image embedding line to resize images before adding to PDF
old = """                story.append(RLImage(fpath, width=16*cm, height=10*cm, kind="proportional"))"""

new = """                # Compress image before embedding
                try:
                    from PIL import Image as PILImage
                    with PILImage.open(fpath) as pil_img:
                        pil_img = pil_img.convert("RGB")
                        # Resize to max 800px wide to reduce PDF size
                        max_w = 800
                        if pil_img.width > max_w:
                            ratio = max_w / pil_img.width
                            new_h = int(pil_img.height * ratio)
                            pil_img = pil_img.resize((max_w, new_h), PILImage.LANCZOS)
                        import tempfile, os as _os
                        tmp = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
                        pil_img.save(tmp.name, "JPEG", quality=60, optimize=True)
                        tmp.close()
                        story.append(RLImage(tmp.name, width=16*cm, height=10*cm, kind="proportional"))
                        _os.unlink(tmp.name)
                except Exception:
                    story.append(RLImage(fpath, width=16*cm, height=10*cm, kind="proportional"))"""

if old in content:
    content = content.replace(old, new)
    with open("app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Done! Image compression added to PDF route.")
else:
    print("Line not found — checking:")
    for i, line in enumerate(content.split('\n')):
        if 'RLImage' in line and 'fpath' in line:
            print(f"{i+1}: {repr(line)}")
