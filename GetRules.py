import requests
import csv

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
    
    with open("rules_output.csv", "w", newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["Rule Number", "Name", "RRN", "Type", "Migrated"])

        for i, entry in enumerate(entries):
            name = entry.get('rule', {}).get('name', 'N/A')
            rrn = entry.get('rrn', 'N/A')
            event_types = entry.get('event_types', [])
            event_type_str = ", ".join(event_types) if event_types else "N/A"
            
            threats = entry.get('threats', [])
            uba_migrated = next((threat.get('uba_migrated', 'N/A') for threat in threats if 'uba_migrated' in threat), 'N/A')

            writer.writerow([i + 1, name, rrn, event_type_str, uba_migrated])

    print(f"Successfully wrote {len(entries)} rules to 'rules_output.csv'.")

except requests.exceptions.RequestException as e:
    print(f"Error retrieving RRNs: {e}")
