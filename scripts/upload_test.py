import requests
import sys

url = "http://localhost:5000/upload?extract_only=1"
cookie_value = "eyJfcGVybWFuZW50IjpmYWxzZSwibmFtZSI6IkRpc2hhIFJhanBhbCIsInVzZXIiOiJkaXNoYS5yYWpwYWxAYzRpNC5vcmcifQ.aSQWdg.imAMIke-xq36xY1snbLJwP64628"
file_path = r"uploads\test.jpg"

print('Posting file:', file_path)
try:
    with open(file_path, 'rb') as f:
        files = {'file': ('camera-capture.jpg', f, 'image/jpeg')}
        r = requests.post(url, cookies={'session': cookie_value}, files=files, timeout=60)
        print('Status:', r.status_code)
        print('Headers:', r.headers)
        try:
            print('JSON response:', r.json())
        except Exception:
            print('Text response:', r.text)
except FileNotFoundError:
    print('File not found:', file_path)
    sys.exit(2)
except Exception as e:
    print('Request failed:', e)
    sys.exit(1)
