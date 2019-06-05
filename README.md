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

Run the app locally as:  
`python app.py`

Run on the server using the "deploy" script. This contains some non-public information so it's not listed here.


## Endpoints
All endpoints return JSON by default. There are no options to return XML.
### List all Submissions (GET)
- Returns a JSON object with a list of all submissions.
- Signature: `/submissions`

### List submission (GET)
- Returns a single submission based on the submission id
- Signature: `/submission/<int:submission_id>`

### Update Filename (POST)
- Adds the template filename to the database.
- Signature: `/updateSubmission/<string:file_name>/submission_id/<int:submission_id>`


### Update File validataion status (POST)
- Adds the file validataion status to the database.
- Signature: `/updateFileValidationStatus/submissionId/<int:submission_id>/status/<string:status>/message/<string:message>`