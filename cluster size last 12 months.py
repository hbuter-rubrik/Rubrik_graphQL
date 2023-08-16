""" 
Python Script that logs into your Rubrik Security Cloud and create a capacity report based on the last 52 weeks
Define: 
    rubrik_cluster_id - CLuster ID where your like to get the report from
    csv_file_location - Path where you want to store the CSV File

Cluster UUID Location RSC --> Data Protection --> Cluster view --> Cluster Details --> UUID
"""

import requests
import json
import csv
import datetime
import connect_RSC

# Section for date today to be used as a variable and calculate 52 weeks back for start variable
# Get the current date
date_today = datetime.date.today()
# Calculate the date 52 weeks ago
date_52_weeks_ago = str(date_today - datetime.timedelta(weeks=52))
date_today = str(date_today)

# Variables needed for this script to run
rubrik_cluster_id = '[YOUR CLUSTER ID]' # Change into your Rubrik cluster ID in RSC
csv_file_location = '[YOUR_PATH]/cluster_last12months_' + date_today + '.csv'

# Main Script, please don't edit any lines below

# Token imported from connect_RSC module
bearer_key = connect_RSC.api_token

# GraphQL endpoint URL
url = connect_RSC.rsc_url + '/api/graphql'

# Variables for the query
variables = {
    'unit': 'Week',
    'timeRange': {
        'start': date_52_weeks_ago, # Change to start week 52 weeks ago
        'end': date_today # Change to date today
    },
    'clusterId': rubrik_cluster_id
}

# Authorization header, 
headers = {
    'Authorization': 'Bearer '+ bearer_key 
}

# GraphQL query
query = '''
    query ClusterCapacityTimelineQuery($unit: TimeUnitEnum!, $timeRange: TimeRangeInput, $clusterId: UUID!) {
      clusterConnection(filter: {id: [$clusterId]}) {
        nodes {
          metricTimeSeries(unit: $unit, timeRange: $timeRange) {
            metric {
              usedCapacity
              totalCapacity
              snapshotCapacity
              liveMountCapacity
              miscellaneousCapacity
              availableCapacity
              __typename
            }
            timeInfo {
              ... on TimeRangeWithUnit {
                start
                end
                __typename
              }
              __typename
            }
            __typename
          }
          __typename
        }
        __typename
      }
    }
'''

# Make the GraphQL request
response = requests.post(url, json={'query': query, 'variables': variables}, headers=headers)

# Handle the response

if response.status_code == 200:
    data = response.json()

    # Extract necessary data from the response
    metric_data = data['data']['clusterConnection']['nodes'][0]['metricTimeSeries']
    
    # Define CSV file path
    csv_file_path = csv_file_location

# Save response data as CSV
    with open(csv_file_path, 'w', newline='', encoding='UTF8') as csvfile:
        fieldnames = ['Date', 'Total Capacity', 'Used Capacity', 'Snapshot Capacity']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for entry in metric_data:
            metric_entry = entry['metric']
            date_info = entry['timeInfo']
            writer.writerow({
                'Date': date_info['start'],
                'Total Capacity': metric_entry['totalCapacity'],
                'Used Capacity': metric_entry['usedCapacity'],
                'Snapshot Capacity': metric_entry['snapshotCapacity']
            })

    print(f'Response data saved as {csv_file_path}')
else:
    print('Request failed with status code:', response.status_code)