import requests
import os
import csv

def fetch_datadog_rum_data(api_key, app_key, from_ts, to_ts):
    url = "https://api.datadoghq.com/api/v2/logs/events/search"
    headers = {
        "DD-API-KEY": api_key,
        "DD-APPLICATION-KEY": app_key,
        "Content-Type": "application/json"
    }
    body = {
        "filter": {
            "from": from_ts,
            "to": to_ts,
            "query": "@type:rum @session.type:user"
        },
        "group_by": ["@browser.name", "@device.type"],
        "page": {"limit": 1000}
    }
    response = requests.post(url, headers=headers, json=body)
    return response.json()
