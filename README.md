# COVIDcast Data Correction

## Overview
This repository contains scripts and data for identifying and correcting discrepancies in the COVIDcast data between the `epimetric_latest` and `epidata_full` tables. The goal is to ensure that the latest updates are accurately reflected in the `epimetric_latest` table.

## Problem Description
Due to the dynamic nature of epidemiological data, discrepancies can arise where the latest update in the `epimetric_latest` table does not match the actual latest values in the `epidata_full` table. This can lead to inaccuracies in the data representation.

## Solution Approach
To address this issue, we have developed a methodology outlined in the correction script (`fix_data.py`). This script identifies offending entries in the `df_latest` table, retrieves the actual latest values from the `df_full` table, and updates the `df_latest` table accordingly. The script also includes validation steps to ensure the correctness and completeness of the fix.

## File Structure
- `epimetric_full.csv`: Contains data similar to the `df_full` table.
- `epimetric_latest.csv`: Contains data similar to the `df_latest` table.
- `fix_data.py`: Python script for correcting discrepancies in the data.
- `fixed_epimetric_latest.csv`: Output CSV file containing the fixed version of the `epimetric_latest_fixed` table.

## Usage: 1. Python 
1. Clone this repository to your local machine.
2. Navigate to the repository directory.
3. Run the `fix_data.py` script to execute the correction process.
4. Verify the correctness of the fixed `epimetric_latest.csv` file or use it directly in your database.
5. Process data manipulation using python, jupyter notebook and SQL on docker.

## Data flow diagram: 
![Screenshot](https://github.com/chihlinc/data_fix/blob/main/Screenshot%202024-04-08%20at%205.26.37%20PM.png)
## Requirements
- Python 3.x
- pandas library
- Jupyter notebook 
- ydata-profiling
- matplotlib 



## Usage: 2. SQL 
## Start the database with the following command:
    docker run --rm -p 3307:3307 -e MYSQL_ROOT_PASSWORD=strong_password -e MYSQL_DATABASE=delphi -e MYSQL_USER=foo -e MYSQL_PASSWORD=bar -v $(pwd)/database/init/:/run/init -v $(pwd)/data/:/run/init/data -v $(pwd)/database/my.cnf:/etc/mysql/my.cnf --name delphi_db mysql:latest
## In a seperate terminal, run:
    docker exec delphi_db /bin/sh -c 'chmod +x /run/init/initialize_database.sh && ./run/init/initialize_database.sh'

## Lastly, run this command to get into the MySQL CLI:
    docker exec -it delphi_db mysql --user=foo --password=bar

## Identify the outdated data from epimetric_latest:
Using SQL to indentify the outdated data from epimetric_latest and generate the SQL named after get_outdate_from_el.sql. 



