import requests

API_KEY = "api_key" 
base_url = "https://us3.api.insight.rapid7.com/idr/v1/rules/_search"

headers = {
    "X-Api-Key": API_KEY,
    "Accept": "application/json",
    "Accept-version": "strong-force-preview",
    "Content-Type": "application/json"
}

params = {
    "size": 1,
    "position": None,
    "include_counts": "NONE"
}

body = {
    "filters": [
        {
            "type": "IN",
            "target": "rule_set",
            "values": ["Legacy UBA"]
        }
    ],
    "sortFieldOrders": [
        {
            "target": "rrn",
            "order": "ASC"
        }
    ]
}

response = requests.post(base_url, headers=headers, params=params, json=body)

if response.status_code == 200:
    data = response.json()
    if data.get("data"):
        print("First Filtered Rule:")
        print(data["data"][0])
    else:
        print("No Legacy UBA rules found.")
else:
    print(f"Failed to retrieve rules: {response.status_code} - {response.text}")
