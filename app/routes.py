from flask import render_template, redirect
from app.update import update_folder_list
from app.iw import change, make
import json
from app import app
from app.forms import SapForm
from app.sap import plot_struc, mbom

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/iw')
def iw():
    folder_list = update_folder_list()
    #form = IWForm()
    return render_template('iw.html', folder_list=folder_list)

@app.route('/iw/new')
def new_folder():
    print('new folder?')
    return render_template('iw.html', folder_list=folder_list)

@app.route('/iw/<folder>')
def change_folder(folder):
    change(folder)
    print('ran folder?')
    return redirect('/index')

@app.route('/sap', methods=['GET', 'POST'])
def handle_sap():
    form = SapForm()
    if form.validate_on_submit():
        if form.plotstruc.data:
            print('ran plotstruc')
            plot_struc(form.material.data)
        elif form.mbom.data:
            print('ran mbom')
            mbom(form.material.data)
    return render_template('sap.html', form=form)
    
