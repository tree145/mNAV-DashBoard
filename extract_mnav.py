import requests
import json

company = ["MSTR", "MARA", "XXI", "MTPLF", "CEPO", "BLSH", "RIOT", "COIN", "HUT", "CLSK"]

for c in company:
    response = requests.get(
        f"https://playground.bitcointreasuries.net/api/v1/companies/{c}/history?api_key=bt_bd64f8b453cf879a62230464be154554849c7c3c&limit=1000"
    )
    data = response.json()
    with open(f'{c}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)  # indent 让格式更美观