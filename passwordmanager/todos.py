from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
import json
from os.path import exists
from django.shortcuts import render
from .entrypoint import Form

def index(request):
    form_data = {'todo':''}
    form = Form(request.POST) # A form bound to the POST data

    filename = 'todos.json'
    todos_obj = {"todos":[]}
    if exists(filename):
        input_file = open (filename)
        todos_obj = json.load(input_file)
   
    if form.is_valid():
        form_data['todo']= form.cleaned_data.get("todo")

    if form_data['todo'] != '':
        todos_obj["todos"].append(form_data['todo'])
            
        json_object = json.dumps(todos_obj, indent=4)
        with open(filename, "w") as outfile:
            outfile.write(json_object)

        return HttpResponseRedirect('/')

    return render(request, "index.html", {'form': form, 'todos':todos_obj['todos']})