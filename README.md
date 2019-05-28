# GWAS Deposition Service App


## Description   
A demo app to use for development of the GWAS Submission app. The Deposition Service app provides endpoints for submitting data and monitoring file validation of the GWAS submission files. A light-weight SQLite database is used to store submission data, note this is an initial prototype since this data will eventually be retrieved by GOCI web services when the submission table is added to the GWAS schema.

## Dependencies
See `requirements.txt` file.

## Usage
Set-up the SQLite database by running:  
`python database_setup.py`

Add demo data to the database as:  
`python add_submissions.py`

Run the app as:  
`python app.py`