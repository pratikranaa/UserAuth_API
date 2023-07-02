from django.core.mail import EmailMessage
from django.core.mail.backends.smtp import EmailBackend
from user_api.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS
from django.core.mail import send_mail
from rest_framework import status

""" Send email function """
def send_email(subject, message, mail_to, mail_from=None, attachement=None):
    try:
        backend = EmailBackend(host=EMAIL_HOST, port=EMAIL_PORT, username=EMAIL_HOST_USER, 
                            password=EMAIL_HOST_PASSWORD, use_tls=EMAIL_USE_TLS)
        
        if mail_from is None: mail_from = EMAIL_HOST_USER
        sent = EmailMessage(subject, message, mail_from, [mail_to], connection=backend)
        print(mail_to, mail_from)
        if attachement: sent.attach_file(attachement)
        try : 
            print("demo")
            status = sent.send()
            return status
        except Exception as err:
            raise ValueError(err)
    except Exception as err:
        raise ValueError(err)

## Uniform api response
def success(count):
    response = {
                    'inserted': str(count)+" row(s) inserted successfully",
                    "status" : "success",
                    "code"   : status.HTTP_200_OK
                }
    return response

def error(msg):
    response = {
                    "message": msg,
                    "status" : "error",
                    "code"   : status.HTTP_400_BAD_REQUEST
                }
    return response

def success_def(count,defective_data):
    response = {
                    'inserted': str(count)+" row(s) inserted successfully",
                    "status" : "success",
                    "rejected_records" : defective_data,
                    "code"   : status.HTTP_200_OK
                }
    return response

def success_msg(msg):
    response = {
                    "message": msg,
                    "status" : "success",
                    "code"   : status.HTTP_201_CREATED
                }
    return response

#*************** Encode API Name **************
def encode_api_name(value):
    value=str(value)
    lowercase = value.lower()
    value = lowercase.replace(" ", "_")
    return value

#*************** Decode API name ***************
def decode_api_name(value):
    captalize = value.title()
    value = captalize.replace("_", " ")
    return value
