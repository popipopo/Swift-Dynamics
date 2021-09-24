from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from todolist.models import *
import os,json,sys,uuid
from datetime import datetime
# Create your views here.

task_to_do = []

class NewTextForm(forms.Form):
    tasks = forms.CharField(label="New Task:")

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = os.path.join(SETTINGS_PATH, 'templates\\index.html')

@csrf_protect


def index(request):
    try:
        
        result = {"task_to_do":task_to_do}
        
    except Exception as e:
        result = {"status":"ER","errorMessage":"index error --> " + debug_row(e)}
    finally:
        return HttpResponse(json.dumps(result), content_type="application/json")

def add(request):
    try:
        if request.method != 'POST':
            result = {"status":"ER","errorMessage":"Invalid method"}
            return result
        
        data = json.loads(request.body)

        if "task_header" not in data or "task_body" not in data:
            result = {"status":"ER","errorMessage":"please input task_header , task_body"}
            return result

        task_header = data["task_header"]
        task_body = data["task_body"]
        id = str(uuid.uuid4())
        last_update = str(datetime.now())

        if not isinstance((task_header), str) or not isinstance((task_body), str) :
            result = {"status":"ER","errorMessage":"task_header , task_body must be str"}
            return result

        if task_header == "" and task_body == "":
            result = {"status":"ER","errorMessage":"please input data task_header , task_body"}
            return result
        
        payload = { "task_header":task_header,
                    "task_body":task_body,
                    "id":id,
                    "last_update":last_update
                    }
        task_to_do.append(payload)

        result = {"task":task_to_do}

    except Exception as e:
        result = {"status":"ER","errorMessage":"add function --> "+ str(e) + debug_row(e)}
    finally:
        return HttpResponse(json.dumps(result), content_type="application/json")

def remove(request):
    try:
        if request.method != 'POST':
            result = {"status":"ER","errorMessage":"Invalid method"}
            return result
        
        data = json.loads(request.body)

        id = data["id"]
        
        for i in task_to_do:
            if i['id'] == id:
                task_to_do.remove(i)

        result = {"task":task_to_do}

    except Exception as e:
        result = {"status":"ER","errorMessage":"remove function --> "+ str(e) + debug_row(e)}
    finally:
        return HttpResponse(json.dumps(result), content_type="application/json")


def edit(request):
    try:
        if request.method != 'POST':
            result = {"status":"ER","errorMessage":"Invalid method"}
            return result
        
        data = json.loads(request.body)

        if "new_header" not in data or "new_body" not in data:
            result = {"status":"ER","errorMessage":"please input new_header , new_body"}
            return result

        id = data["id"]
        new_header = data["new_header"]
        new_body = data["new_body"]
        last_update = str(datetime.now())

        if not isinstance((new_header), str) or not isinstance((new_body), str) :
            result = {"status":"ER","errorMessage":"new_header , new_body must be str"}
            return result

        if new_header == "" and new_body == "":
            result = {"status":"ER","errorMessage":"please input data new_header , new_body"}
            return result
        
        for i in task_to_do:
            if i['id'] == id:
                i["task_header"] = new_header
                i["task_body"] = new_body
                i["last_update"] =last_update

        result = {"task":task_to_do}

    except Exception as e:
        result = {"status":"ER","errorMessage":"remove function --> " + str(e) + debug_row(e)}
    finally:
        return HttpResponse(json.dumps(result), content_type="application/json")



def debug_row(e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    error_type = exc_type
    error_file = fname
    error_line = exc_tb.tb_lineno
    error_message = e
    result = str(error_file) + " " + str(error_line)
    print(exc_type, fname, exc_tb.tb_lineno, e)
    return result