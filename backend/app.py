from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from verify import addEFTRecord, createForm
from report import Report, PLCE
from offsiteList import parseChecklist, dropdownHandler
from models import queryEquipment, addTodo, addUser, queryUser, removeUser, addRequest
from werkzeug import secure_filename
import subprocess
import os
import json

# Set base path for file uploads
UPLOAD_FOLDER = './assets/files'
ALLOWED_EXTENSIONS = set(['docx'])

# Set up flask app
app = Flask(__name__,
            static_folder='../dist/static',
            template_folder='../dist',
            )

# Add CORS for development with Vue frontend
CORS(app)

# Config app
app.config['SECRET_KEY'] = 'N7SDGLAK293JBDGALKDF99H1K3B'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Views

# catchall to let Vue router do the rendering.
@app.route('/', methods=['GET', 'POST'], defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # productName = request.form['productName']
    # print(productName)
    return render_template("index.html")

# APIS

# EMC Report Generation
@app.route('/submit/report', methods=['GET', 'POST'])
def submitReport():
    if request.method == 'POST':
        reportData = request.get_json()
        product = reportData['productName']
        company = reportData['companyName']
        class_ = reportData['class_']
        setup = reportData['setup']
        data = reportData['dataLocation']
        standard = reportData['standard']
        equipment = {
            'SpecA': reportData['specA'],
            'LISN': reportData['lisn']
        }
        print(reportData['productName'])
        print(reportData['companyName'])
        print(reportData['dataLocation'])
        print(reportData['standard'])
        print(reportData['setup'])
        print(reportData['power'])
        print(reportData['class_'])
        print(reportData['lisn'])
        print(reportData['specA'])

        output = '/Users/jadonbull/Documents/EMC Hub Output/EMC Reports/' + product + '.docx'
        report = Report(product, company, class_, setup, data, standard, equipment, output, PLCE=PLCE)
        report.reportOutput()

        return 'Finished'

# EFT Verification
@app.route('/submit/eftverification', methods=['GET', 'POST'])
def submitEFTVerification():
    if request.method == 'POST':
        EFTData = request.get_json()

        date = EFTData['date']
        assetNumber = EFTData['asset']
        engineer = EFTData['engineer']
        formGeneration = EFTData['form']
        peakValue = float(EFTData['peakValue'])
        riseTime = float(EFTData['riseTime'])
        fallTime = float(EFTData['fallTime'])
        burstPeriod = float(EFTData['burstPeriod'])
        burstDuration = float(EFTData['burstDuration'])
        filesFolder = './assets/files/'
        fileName = './assets/files/verificationOutput.docx'

        print(EFTData['date'])
        print(EFTData['engineer'])
        print(EFTData['form'])
        print(EFTData['asset'])
        print(EFTData['peakValue'])
        print(EFTData['riseTime'])
        print(EFTData['fallTime'])
        print(EFTData['burstPeriod'])
        print(EFTData['burstDuration'])

        addEFTRecord(date, assetNumber, engineer, peakValue, riseTime, fallTime, filesFolder)

        if formGeneration == 'true':
            createForm(date, assetNumber, engineer, peakValue, riseTime, fallTime, burstPeriod, burstDuration, filesFolder, fileName)

        return 'Finished'

# Search Equipment Database
@app.route('/query/equipment', methods=['POST'])
def getEquipment():
    if request.method == 'POST':
        filters = request.get_json()
        print(filters)
        result = queryEquipment(filters)
        return jsonify(result)

# Add Todo List Item to Database
@app.route('/add/todo/equipment', methods=['POST'])
def addTodoItem():

    # Axios request will be post
    if request.method == 'POST':
        # Todo object passed from Vue via Axios
        todo = request.get_json()
        print(todo)

        # Set new Todo db entry params
        name = todo['id']
        category = 'Individual Test Equipment'
        type_ = todo['type_']

        # Create Todo in db. This will be a new Todo object
        addTodo(name, category, type_)

        # Return the Todo object to Vue
        return 'OK'


# Offsite List Upload
@app.route('/submit/offsiteList', methods=['POST'])
def uploadList():
    if request.method == 'POST':
        f = request.files['file']
        filename = f.filename
        filename = secure_filename(filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify(dropdownHandler(parseChecklist(os.path.join(app.config['UPLOAD_FOLDER'], filename))))

# File Explorer Open
@app.route('/submit/fileopen', methods=['POST'])
def fileExplorer():
    subprocess.call(['/usr/bin/open', '../../../EMC Hub Output'])
    return 'OK'


if __name__ == "__main__":
    app.run(debug=True)
