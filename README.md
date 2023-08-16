# Python scripts to use with GraphQL and Rubrik Security Cloud (RSC)
In this repository I'll be adding python scripts that I've created for our customers. 

connect_RSC.PY - Script to generate a token needed for the scripts to authenticate using a Service Account with Rubrik Security Cloud. I prefer to import this script as a module into my scripts

# Reporting script
cluster size last 12 months.py - Script to provide a capacity report for the last 52 weeks, it imports connect_RSC.py to authenticate. You will need to add cluster ID of the particular cluster which can be gained via RSC --> Data Protection --> Cluster view --> Cluster Details --> UUID

Screenshot of output of the script (output is in bytes)
![Screenshot of csv file output](https://github.com/hbuter-rubrik/images/blob/main/12months.png)

