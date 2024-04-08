## Business Overview
### Objective: Develop a solution to ensure accurate and up-to-date COVIDcast data by identifying and correcting discrepancies between the epimetric_latest and epidata_full tables.

### Timeline:
Effort Estimation: 2 hours
### Technical Overview
Data manipulation in Python and SQL. 

### Solution Design:
Develop a correction script (fix_data.py) to identify and correct discrepancies between epimetric_latest and epidata_full tables. The whole process is done in Jupyter notebook, including data quality check and validation of the data_latest. 

### Data Sources:
1. epimetric_latest: Holds the most recent update for each time value.
2. epidata_full: Holds all updates and values received from the source.
Level of Data: Epidemiological data.
### Source Data Quality:
Check unique, duplicate, null and data type. 

### Data Model:
Updated epimetric_latest table.

### Target Data Quality:
Ensure accuracy and consistency between epimetric_latest and epidata_full tables.

### Solution Detail
Detail Explanation of Solution:
I follow this logic to conduct the codes and logic. (Data transformation logic Diagram)
1.Identify offending entries in epimetric_latest table. 
2.Retrieve actual latest values from epidata_full table.
3. Update epimetric_latest table with the latest values.
4. Validate the correctness of the fix. (from the jupyter notebook: Is_latest.ipynb)


