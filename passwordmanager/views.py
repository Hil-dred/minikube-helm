from django.http import HttpResponse
from django.shortcuts import redirect
import json
from os.path import exists
from django.shortcuts import render
from .entrypoint import Auth, Form

def index(request):
    return redirect(auth)

def dashboard(request):
    return render(request, "dashboard.html")

def view_all(request):
    filename = '{}.json'.format(request.session['data']["account_name"])
    if exists(filename):
            input_file = open (filename)
            cred_object = json.load(input_file)

    return render(request, "view-all.html", {'apps': cred_object['cred']})

def create_or_add(request):
    form = Form(request.POST)
    session = request.session['data']
    details = {"username": "", "password": "", "app_name": ""}
    cred_object = None

    if form.is_valid():
        details["username"] = form.cleaned_data.get("user_name")
        details["password"] = form.cleaned_data.get("password")
        details["app_name"] = form.cleaned_data.get("app_name")

        filename = '{}.json'.format(session["account_name"])
        if exists(filename):
            input_file = open (filename)
            cred_object = json.load(input_file)

        if cred_object == None:
            cred_object = {"master":session["master_password"], "cred": []}

        if details["username"] != '' and details["password"] != '':
            cred_object["cred"].append(details)
            
            json_object = json.dumps(cred_object, indent=4)
            with open(filename, "w") as outfile:
                outfile.write(json_object)
            return redirect(auth)

    return render(request, "index.html", {'form': form})

def auth(request):
    data = {'account_name':'', 'master_password':''}
    form = Auth(request.POST) # A form bound to the POST data

    if form.is_valid():
        data['account_name']= form.cleaned_data.get("account_name")
        data['master_password']= form.cleaned_data.get("master_password")

        filename = '{}.json'.format(data["account_name"])
        if exists(filename):
            input_file = open (filename)
            cred_object = json.load(input_file)
            
            if(cred_object["master"] != data['master_password']):
                return redirect(auth)

        if(data["account_name"]!=''):
            request.session['data'] = data
            return redirect(dashboard)

    return render(request, "index.html", {'form': form})