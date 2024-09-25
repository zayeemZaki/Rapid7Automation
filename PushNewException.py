import requests

API_KEY = "api_key"
rule_rrn = "rule_rrn"
url = f"https://us.api.insight.rapid7.com/idr/v1/rules/{rule_rrn}/rule-exceptions/create"

headers = {
    "X-Api-Key": API_KEY,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "name": "Exception Name",
    "rule_action": "OFF",
    "note": "This is a note for the new exception.",
    "priority_level": "LOW",
    "type": "LEQL",
    "value": "from(event_type = 'process_start_event') where osType = 'example_os'"
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    print("Exception created successfully!")
else:
    print(f"Failed to create exception: {response.status_code} - {response.text}")
