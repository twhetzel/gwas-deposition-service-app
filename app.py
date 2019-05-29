from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine, asc, desc, func
from sqlalchemy.orm import sessionmaker

from werkzeug import secure_filename

import os.path
import sys
sys.path.append('./database')
import database_setup
from database_setup import Base, Submission, User


# http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
UPLOAD_FOLDER = './gwas_upload_files'
ALLOWED_EXTENSIONS = set(['txt', 'xls'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/submissions": {"origins": "http://localhost:port"}})

# Connect to database and create database session
engine = create_engine('sqlite:///gwas_submissions.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/submissions', methods = ['GET'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def show_submissions():
    '''
    Lists submissions found in the Submissions database table.
    '''
    submissions = session.query(Submission).all()
    print "** Subs: ", submissions
    return jsonify(allSubmissions=[sub.serialize for sub in submissions])


@app.route('/fileValidationStatus/<int:submission_id>',  methods = ['GET', 'POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def file_validation_status(submission_id):
    '''
    Sets or returns the file validation status.
    '''
    # TODO: Add authentication if needed
    if request.method == 'GET':
        file_validation_status = session.query(Submission).filter_by(id=submission_id).one()
        print jsonify(file_validation_status)
        # return jsonify(file_validation_status)
        return True


@app.route('/startFileValidation/<string:file_name>/submission_id/<int:submission_id>',  methods = ['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def start_file_validation(file_name=None, submission_id=None):
    '''
    Given a submission_id and a filename, starts the file validataion process.
    '''
    if request.method == 'POST':
        print "** File validatation process started for: "+file_name+" SubmissionID: "+str(submission_id)
        return 'testing'



@app.route('/uploader', methods = ['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def uploader():
    '''
    Uploads file to server.
    '''
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'file uploaded successfully'


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
