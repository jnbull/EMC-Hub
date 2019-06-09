from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from flask_cors import CORS
from verify import addEFTRecord, addESDRecord, createForm
from report import Report, PLCE, Template, File
import subprocess
import json

app = Flask(__name__,
            static_folder = '../dist/static',
            template_folder = '../dist',
            )
CORS(app)
app.config['SECRET_KEY'] = 'N7SDGLAK293JBDGALKDF99H1K3B'

# Views

# catchall to let Vue router do the rendering.
@app.route('/', methods = ['GET', 'POST'], defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # productName = request.form['productName']
    # print(productName)
    return render_template("index.html")

# APIS

# EMC Report Generation
@app.route('/submit/report', methods = ['GET','POST'])
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
            'SpecA' : reportData['specA'],
            'LISN' : reportData['lisn']
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

        output = './assets/files/reportOutput.docx'
        report = Report(product, company, class_, setup, data, standard, equipment, output, PLCE = PLCE)
        report.reportOutput()

        return 'Finished'

@app.route('/submit/eftverification', methods = ['GET','POST'])
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

# File Explorer Open
@app.route('/submit/fileopen', methods = ['POST'])
def fileExplorer():
    subprocess.call(['/usr/bin/open', '../../../EMC Hub Output'])
    return 'OK'

if __name__ == "__main__":
    app.run(debug=True)