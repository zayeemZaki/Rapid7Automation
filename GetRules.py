import requests

API_KEY = "api_key"
base_url = "https://us3.api.insight.rapid7.com/idr/v1/rules"

headers = {
    "X-Api-Key": API_KEY,
    "Accept": "application/json",
    "Accept-version": "strong-force-preview"
}

def get_all_rules(base_url, headers):
    rules = []
    position = ''
    size = 100

    while True:
        params = {
            "size": size,
            "position": position,
            "include_counts": "NONE"
        }
        response = requests.get(base_url, headers=headers, params=params)

        if response.status_code != 200:
            print(f"Failed to retrieve rules: {response.status_code} - {response.text}")
            break

        data = response.json()
        rules.extend(data.get('data', []))

        position = data.get('position', None)
        if not position:
            break

    return rules

try:
    entries = get_all_rules(base_url, headers)
    for i, entry in enumerate(entries):
        print("Rule ", i + 1)
        print("   RRN: ", entry['rrn'])
        print("   Name: ", entry['rule']['name'])
        print()

except requests.exceptions.RequestException as e:
    print(f"Error retrieving RRNs: {e}")