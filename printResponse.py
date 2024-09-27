import requests

API_KEY = "api_key"
base_url = "https://us3.api.insight.rapid7.com/idr/v1/rules"

headers = {
    "X-Api-Key": API_KEY,
    "Accept": "application/json",
    "Accept-version": "strong-force-preview",
    "Content-Type": "application/json"
}

def get_filtered_rules(base_url, headers):
    filters = {
        "filters": [
            {
                "type": "EQ",
                "target": "rule_set",
                "values": ["UBA"]
            }
        ],
        "size": 1
    }

    response = requests.post(f"{base_url}/_search", headers=headers, json=filters)

    if response.status_code == 200:
        data = response.json()
        print("Filtered Rules Response:")
        print(data)
    else:
        print(f"Failed to retrieve rules: {response.status_code} - {response.text}")

try:
    get_filtered_rules(base_url, headers)

except requests.exceptions.RequestException as e:
    print(f"Error retrieving filtered rules: {e}")
