import requests

API_KEY = "api_key"
base_url = "https://us3.api.insight.rapid7.com/idr/v1/rules"

headers = {
    "X-Api-Key": API_KEY,
    "Accept": "application/json",
    "Accept-version": "strong-force-preview"
}

def get_first_response(base_url, headers):
    size = 100

    params = {
        "size": size,
        "include_counts": "NONE"
    }
    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Failed to retrieve rules: {response.status_code} - {response.text}")
        return None

    data = response.json()
    
    print("Full Response: ", data)
    
    return data.get('data', [])

get_first_response(base_url, headers)



"""
{
  "data": [
    {
      "rule_set": "CDR",
      "rrn": "rrn:cba:us:f43e689c-d914-4207-ada1-8fc8b6eec42d:custom-rule:KX6EM4G24959",
      "rrn_revision": "rrn:cba:us:f43e689c-d914-4207-ada1-8fc8b6eec42d:custom-rule:version:CK7F4VFBNKTM",
      "obsolete": false,
      "invalid": false,
      "create_date": "2021-02-31T17:01:24.466136Z",
      "state": {
        "value": "ACTIVE"
      },
      "event_types": [
        "process_start_event"
      ],
      "event_subtypes": [],
      "detection_count": 0,
      "threats": [],
      "last_modified_date": "2021-03-07T12:19:49.53251Z",
      "exception_count": 5,
      "activated_date": "2021-02-31T17:01:24.466136Z",
      "score": 0,
      "total_exception_matches_month": 0,
      "assessment": [
        {
          "type": "CUSTOM_RULE",
          "id": "rrn:cba:us:f43e629c-d914-4277-ada1-4fc8b6eec42d:report:OMBAYD3WTF13",
          "status": "COMPLETE",
          "report": {
            "start": "2021-03-07T12:19:49.53251",
            "stop": "2021-03-07T13:19:49.53251",
            "detections": 0,
            "throttles": 0,
            "score": 0
          },
          "schema": 1
        }
      ],
      "rule": {
        "schema": 2,
        "name": "Example Rule 2",
        "rule_action": "OFF",
        "priority_level": "LOW",
        "condition": {
          "type": "LEQL",
          "value": "from(event_type = \"process_start_event\")where(osType = \"example\")"
        },
        "tactics": [],
        "techniques": [],
        "labels": [],
        "throttle": {
          "count": 10,
          "timespan": "1m"
        }
      }
    }
  ],
  "position": "RXhhbXBsZSBSdWxlIDJLWDZFTTRHMjQ5NTk",
  "metadata": {
    "size": 1,
    "rule_counts": {
      "total": 2,
      "rule_set_counts": {
        "DR": 0,
        "CDR": 2
      },
      "rule_priority_counts": {
        "LOW": 2,
        "INHERITED": 0,
        "MEDIUM": 0,
        "HIGH": 0,
        "CRITICAL": 0
      },
      "rule_action_counts": {
        "OFF": 1,
        "CREATES_INVESTIGATIONS": 1,
        "TRACKS_NOTABLE_EVENTS": 0,
        "CREATES_ALERTS": 0,
        "ASSESS_ACTIVITY": 0
      },
      "event_type_counts": {
        "process_start_event": 2,
        "asset_auth": 0,
        "cloud_service_activity": 0,
        "cloud_service_admin": 0,
        "dns": 0,
        "firewall": 0,
        "flow": 0,
        "ids": 0,
        "ingress_auth": 0,
        "third_party_alert": 0,
        "virus": 0,
        "web_proxy": 0
      },
      "event_subtype_counts": {
        "endpoint_activity:sysmon": 0,
        "anomalous_data_transfer:anomalous_data_transfer_subtype": 0
      },
      "threat_counts": {
        "Example Threat 1": 0
      },
      "tactic_counts": {},
      "assessment_counts": {
        "COMPLETE": 1
      }
    },
    "cdr": {
      "limit": 20,
      "used": 2,
      "remaining": 18
    }
  },
  "options": {
    "filters": [
      {
        "name": "activated_date",
        "type": "DATE_TIME"
      },
      {
        "name": "assessment_status",
        "type": "TEXT"
      },
      {
        "name": "create_date",
        "type": "DATE_TIME"
      },
      {
        "name": "description",
        "type": "TEXT"
      },
      {
        "name": "detection_count",
        "type": "NUMBER"
      },
      {
        "name": "event_subtypes",
        "type": "TEXT"
      },
      {
        "name": "event_types",
        "type": "TEXT"
      },
      {
        "name": "exception_count",
        "type": "NUMBER"
      },
      {
        "name": "total_exception_matches_month",
        "type": "NUMBER"
      },
      {
        "name": "labels",
        "type": "TEXT"
      },
      {
        "name": "last_detected_date",
        "type": "DATE_TIME"
      },
      {
        "name": "last_modified_date",
        "type": "DATE_TIME"
      },
      {
        "name": "name",
        "type": "TEXT"
      },
      {
        "name": "obsolete",
        "type": "BOOLEAN"
      },
      {
        "name": "rule_priority",
        "type": "TEXT"
      },
      {
        "name": "responsibility",
        "type": "TEXT"
      },
      {
        "name": "rrn",
        "type": "TEXT"
      },
      {
        "name": "rrn_revision",
        "type": "TEXT"
      },
      {
        "name": "rule_action",
        "type": "TEXT"
      },
      {
        "name": "rule_set",
        "type": "TEXT"
      },
      {
        "name": "score",
        "type": "NUMBER"
      },
      {
        "name": "state",
        "type": "BOOLEAN"
      },
      {
        "name": "tactic_code",
        "type": "TEXT"
      },
      {
        "name": "tactic",
        "type": "TEXT"
      },
      {
        "name": "technique_code",
        "type": "TEXT"
      },
      {
        "name": "technique",
        "type": "TEXT"
      },
      {
        "name": "threat",
        "type": "TEXT"
      },
      {
        "name": "uba_migrated",
        "type": "BOOLEAN"
      },
      {
        "name": "workflows",
        "type": "TEXT"
      }
    ],
    "sorts": {
      "activated_date": [
        "ASC",
        "DESC"
      ],
      "create_date": [
        "ASC",
        "DESC"
      ],
      "description": [
        "ASC",
        "DESC"
      ],
      "detection_count": [
        "ASC",
        "DESC"
      ],
      "exception_count": [
        "ASC",
        "DESC"
      ],
      "total_exception_matches_month": [
        "ASC",
        "DESC"
      ],
      "last_detected_date": [
        "ASC",
        "DESC"
      ],
      "last_modified_date": [
        "ASC",
        "DESC"
      ],
      "name": [
        "ASC",
        "DESC"
      ],
      "rule_priority": [
        "ASC",
        "DESC"
      ],
      "rule_action": [
        "ASC",
        "DESC"
      ],
      "score": [
        "ASC",
        "DESC"
      ],
      "threat": [
        "ASC",
        "DESC"
      ]
    }
  }
}
"""

