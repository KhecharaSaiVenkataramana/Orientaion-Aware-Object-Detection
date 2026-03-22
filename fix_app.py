content = open("app.py", encoding="utf-8").read()
print("HAS csv route:", "download_report_csv" in content)
print("HAS pdf route:", "download_report_pdf" in content)
print("Total lines:", len(content.split('\n')))