import requests

BASE = "http://127.0.0.1:5000"
LOGIN = BASE + "/login"
CARDS = BASE + "/cards"

s = requests.Session()
resp = s.get(LOGIN)
print("GET /login status", resp.status_code)
# perform login
r = s.post(
    LOGIN,
    data={"email": "admin@c4i4.org", "password": "AdminPass123!"},
    allow_redirects=True,
)
print("POST /login status", r.status_code)
print("Login response length", len(r.text))
# fetch cards
c = s.get(CARDS)
print("GET /cards status", c.status_code)
try:
    print(c.json())
except Exception as e:
    print("Failed to parse JSON:", e)
    print("Response text:", c.text[:1000])

# fetch filtered cards by a sample scanner (replace with existing scanner email)
sample_scanner = "pranav.pankhawala@c4i4.org"
cf = s.get(CARDS, params={"scanned_by": sample_scanner})
print(f"GET /cards?scanned_by={sample_scanner} status", cf.status_code)
try:
    data = cf.json()
    print("Filtered count:", len(data.get("cards", [])))
    # print first item if any
    if data.get("cards"):
        print("First filtered card scanned_by:", data["cards"][0].get("scanned_by"))
except Exception as e:
    print("Failed to parse filtered JSON:", e)
    print("Response text:", cf.text[:1000])
