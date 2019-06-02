from flask import Flask, render_template, url_for, flash, redirect, request, jsonify
# from forms import EFTForm, ESDForm, ReportForm
# from verify import addEFTRecord, addESDRecord, createForm
from report import Report, PLCE, Template, File

app = Flask(__name__,
            static_folder = '../dist/static',
            template_folder = '../dist',
            )
app.config['SECRET_KEY'] = 'N7SDGLAK293JBDGALKDF99H1K3B'

@app.route('/', methods = ['GET', 'POST'], defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")