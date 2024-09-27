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
            "position": position if position else None,
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
    
    with open("rules_output.txt", "w") as file:
        for i, entry in enumerate(entries):
            name = entry.get('rule', {}).get('name', 'N/A')
            rrn = entry.get('rrn', 'N/A')

            file.write(f"Rule {i + 1}:\n")
            file.write(f"   Name: {name}\n")
            file.write(f"   RRN: {rrn}\n\n")

    print(f"Successfully wrote {len(entries)} rules to 'rules_output.txt'.")

except requests.exceptions.RequestException as e:
    print(f"Error retrieving RRNs: {e}")
