Business Overview
Requirement Description in One Sentence:
Develop a solution to ensure accurate and up-to-date COVIDcast data by identifying and correcting discrepancies between the epimetric_latest and epidata_full tables.

Timeline:
Effort Estimation: 2 hours
Technical Overview
Business Research:
No specific data science research conducted.


Solution Design:
Develop a correction script (fix_data.py) to identify and correct discrepancies between epimetric_latest and epidata_full tables.
Utilize Python and pandas library for data processing and checking data quality. 
Validate the correctness and completeness of the fix.
Data Research:
Data Sources:
epimetric_latest: Holds the most recent update for each time value.
epidata_full: Holds all updates and values received from the source.
Description:
SLAs: No specific SLAs provided.
Level of Data: Epidemiological data.
Source Data Quality:


Data Model:
Updated epimetric_latest table.

Target Data Quality:
Ensure accuracy and consistency between epimetric_latest and epidata_full tables.
Solution Detail
Detail Explanation of Solution:
Utilize the fix_data.py script to:1.Identify offending entries in epimetric_latest table. 
                                  2.Retrieve actual latest values from epidata_full table.
                                  3. Update epimetric_latest table with the latest values.
                                  4. Validate the correctness of the fix. (from the jupyter notebook: Is_latest.ipynb)
Data Flow Diagram:

SLA:
No specific SLAs provided.
Quality Assurance:
Validate the correctness and completeness of the fix using test cases and data validation techniques.