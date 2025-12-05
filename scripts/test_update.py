import requests, json

SESSION_COOKIE = "eyJfcGVybWFuZW50IjpmYWxzZSwibmFtZSI6IkRpc2hhIFJhanBhbCIsInVzZXIiOiJkaXNoYS5yYWpwYWxAYzRpNC5vcmcifQ.aSQWdg.imAMIke-xq36xY1snbLJwP64628"
BASE = "http://localhost:5000"

cookies = {"session": SESSION_COOKIE}

try:
    r = requests.get(f"{BASE}/cards", cookies=cookies, timeout=10)
    print("GET /cards ->", r.status_code)
    try:
        data = r.json()
    except Exception as e:
        print("Failed to decode JSON from /cards:", e)
        print("Body preview:", r.text[:1000])
        raise SystemExit(1)

    cards = data.get("cards", [])
    if not cards:
        print("No cards returned (cards list empty)")
        raise SystemExit(0)

    first = cards[0]
    card_id = first.get("_id")
    print("First card id:", card_id)

    # Attempt to update website to a scheme-less URL
    new_website = "www.araiindia.com"
    payload = {"website": new_website}
    put = requests.put(f"{BASE}/update_card/{card_id}", json=payload, timeout=10)
    print("PUT /update_card ->", put.status_code)
    try:
        print("Response JSON:", put.json())
    except Exception:
        print("Response body:", put.text[:1000])

except Exception as e:
    print("Test script error:", e)
