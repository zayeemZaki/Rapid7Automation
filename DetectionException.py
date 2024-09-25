import requests
import pandas as pd

API_KEY = "api key"
url = "https://us3.api.insight.rapid7.com/idr/v1/rules/rule-exceptions"

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

structured_data = []
for exception in rule_exceptions:
    create_date = exception.get("create_date")
    created_by = exception.get("created_by")
    name = exception.get("name")
    rule_action = exception.get("rule_action")
    
    entity = exception.get("entity", {})
    entity_name = entity.get("name")
    entity_rule_action = entity.get("rule_action")

    structured_data.append({
        "exception_create_date": create_date,
        "detection_name": entity_name,
        "detection_rule_action": entity_rule_action,

        "exception_name": name,
        "exception_rule_action": rule_action,
        "created_by": created_by,

    })

df = pd.DataFrame(structured_data)
df.to_csv('rule_exceptions_output.txt', sep='\t', index=False)
df.to_csv('rule_exceptions_output.csv', index=False)
