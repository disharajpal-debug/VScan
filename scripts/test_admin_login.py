import requests

TOKEN = "dev-admin-token-1234"
EMAIL = "admin@c4i4.org"

s = requests.Session()
try:
    r = s.post(
        "http://127.0.0.1:5000/admin_login",
        data={"token": TOKEN, "email": EMAIL},
        allow_redirects=False,
        timeout=10,
    )
    print("POST /admin_login ->", r.status_code)
    print("Location:", r.headers.get("Location"))
    r2 = s.get("http://127.0.0.1:5000/admin", timeout=10)
    print("GET /admin ->", r2.status_code)
    open("admin_page2.html", "w", encoding="utf8").write(r2.text)
    print("Saved admin_page2.html")
except Exception as e:
    print("Error:", e)
