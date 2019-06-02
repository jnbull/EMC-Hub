from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
from flask_cors import CORS
# from forms import EFTForm, ESDForm, ReportForm
# from verify import addEFTRecord, addESDRecord, createForm
from report import Report, PLCE, Template, File
import json

app = Flask(__name__,
            static_folder = '../dist/static',
            template_folder = '../dist',
            )
CORS(app)
app.config['SECRET_KEY'] = 'N7SDGLAK293JBDGALKDF99H1K3B'

@app.route('/', methods = ['GET', 'POST'], defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # productName = request.form['productName']
    # print(productName)
    return render_template("index.html")

@app.route('/submit/report', methods = ['POST'])
def submitReport():
    reportData = request.get_json()
    print(reportData['productName'])
    print(reportData['companyName'])
    print(reportData['data'])
    return 'OK'

if __name__ == "__main__":
    app.run(debug=True)