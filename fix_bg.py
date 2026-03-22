import urllib.request
import os

url = "https://eoimages.gsfc.nasa.gov/images/imagerecords/79000/79765/dnb_land_ocean_ice.2012.3600x1800.jpg"
save_path = r"C:\Users\khech\OAOD Project\website\static\ui\aerial.jpg"

print("Downloading NASA Earth at Night image...")
urllib.request.urlretrieve(url, save_path)
size = os.path.getsize(save_path)
print(f"Downloaded! Size: {round(size/1024/1024, 1)} MB")
print("Saved to:", save_path)