from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from sqlalchemy import create_engine, asc, desc, func
from sqlalchemy.orm import sessionmaker

from werkzeug import secure_filename

import sys
sys.path.append('./database')
import database_setup
from database_setup import Base, Submission, User


app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/submissions": {"origins": "http://localhost:port"}})

# Connect to database and create database session
engine = create_engine('sqlite:///gwas_submissions.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/submissions')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def show_submissions():
    '''
    Lists submissions found in the Submissions database table.
    '''
    submissions = session.query(Submission).all()
    print "** Subs: ", submissions
    return jsonify(allSubmissions=[sub.serialize for sub in submissions])


@app.route('/fileValidation/<int:submission_id>',  methods = ['GET', 'POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def file_validation(submission_id):
    '''
    Sets or returns the file validation status.
    '''
    # TODO: Add authentication if needed
    if request.method == 'GET':
        file_validation_status = session.query(Submission).filter_by(id=submission_id).one()
        print jsonify(file_validation_status)
        # return jsonify(file_validation_status)
        return True


# TODO: Specify file directory to save to
@app.route('/uploader', methods = ['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def uploader():
    '''
    Uploads file to server.
    '''
    if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
