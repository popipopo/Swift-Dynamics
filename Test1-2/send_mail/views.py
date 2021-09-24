from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
import sendgrid
import os
import smtplib, ssl,os,json,sys,re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Create your views here.



class NewTextForm(forms.Form):
    tasks = forms.CharField(label="New Task:")

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = os.path.join(SETTINGS_PATH, 'templates\\index.html')

@csrf_protect


def index(request):

    result = {"Welcome":"you can use http://127.0.0.1:8000/send_mail/sendmail for sending e-mail "}
        
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

def sendmail(request):
    try:
        if request.method != 'POST':
            result = {"status":"ER","errorMessage":"Invalid method"}
            return result

        data = json.loads(request.body)

        if "send_to" not in data or "password" not in data or "send_from" not in data or  "subject" not in data or "meassage" not in data :
            result = {"status":"ER","errorMessage":"please input send_to , password , send_from , subject , meassage"}
            return result

        send_to = data["send_to"]
        password = data["password"]
        send_from = data["send_from"]
        subject = data["subject"]
        meassage = data["meassage"]

        if not (re.fullmatch(regex, send_to)):
            result = {"status":"ER","errorMessage":"Invalid send_to please input email "}
            return result

        if not (re.fullmatch(regex, send_from)):
            result = {"status":"ER","errorMessage":"Invalid send_from please input email "}
            return result

        result = send_mail(send_from,send_to,password,subject,meassage)

        
    except Exception as e:
        result = {"status":"ER","errorMessage":"sendmail function --> "+ str(e) + debug_row(e)}
    finally:
        return HttpResponse(json.dumps(result), content_type="application/json")

def send_mail(sender_email,receiver_email,password,subject,body):
    try:
        port = 587  # For starttls
        smtp_server = "smtp.gmail.com"

        message = """\
        Subject: """ + subject  + """
        
        """

        message += body

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        result = {"status":"OK","result":"Mail Sent"}
    except Exception as e:
        result = {"status":"ER","errorMessage":"send_mail function --> "  + str(e) + debug_row(e)}
    finally:
        return result
