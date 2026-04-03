import requests
import json
import os

API_KEY = os.environ.get("API_KEY")

company = ["MSTR", "MARA", "XXI", "MTPLF", "CEPO", "BLSH", "RIOT", "COIN", "HUT", "CLSK"]

for c in company:
    response = requests.get(
        f"https://playground.bitcointreasuries.net/api/v1/companies/{c}/history?api_key={API_KEY}&limit=1000"
    )
    data = response.json()
    with open(f'{c}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)