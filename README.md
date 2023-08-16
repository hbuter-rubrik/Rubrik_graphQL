# Python scripts to use with GraphQL and Rubrik Security Cloud (RSC)
In this repository I'll be adding python scripts that I've created for our customers. 

connect_RSC.PY - Script to generate a token needed for the scripts to authenticate using a Service Account with Rubrik Security Cloud. I prefer to import this script as a module into my scripts

You'll need to define the following in the script prior to running:
   * rsc_url - RSC_URL Customer name so it matches your company RSC URL
   * client_id - Service Account client ID
   * client_secret - Service Account Client Secret

# Reporting script
cluster size last 12 months.py - Script to provide a capacity report for the last 52 weeks, it imports connect_RSC.py to authenticate. 
You will need to define the following prior to running the script: 
  * rubrik_cluster_id  - cluster ID of the particular cluster which can be gained via RSC --> Data Protection --> Cluster view --> Cluster Details --> UUID
  * csv_file_location - Path where you want to store the CSV File

Screenshot of output of the script (output is in bytes)
![Screenshot of csv file output](https://github.com/hbuter-rubrik/images/blob/main/12months.png)

