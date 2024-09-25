import requests

API_KEY = "api key"
url = "https://us.api.insight.rapid7.com/idr/v1/rules/rule-exceptions"

headers = {
    "X-Api-Key": API_KEY,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

params = {
    "size": 100,  
    "position": None 
}

def get_all_rule_exceptions():
    exceptions = []
    while True:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            break
       
        data = response.json()
        exceptions.extend(data.get("data", []))
       
        position = data.get("position")
        if not position:
            break
        params["position"] = position
   
    return exceptions


rule_exceptions = get_all_rule_exceptions()
for exception in rule_exceptions:
    print(exception)