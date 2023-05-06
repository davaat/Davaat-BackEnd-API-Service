from kavenegar import *
from core.settings import Kavenegar_API, EMAIL_HOST_USER
from random import randint
from . import models
import datetime
import time
import random
import string
import json
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone



def otpsend(phone, otp):
    try:
        api = KavenegarAPI(Kavenegar_API)
        params = {
          'receptor': phone,
          'template': 'verify',
          'token': otp,
          'type': 'sms',
          }
        response = api.verify_lookup(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)






def get_random_otp():
    return  randint(10000, 99999)






def check_otp_expiration(phone):
    try:
        user = models.User.objects.get(phone=phone)
        now = timezone.now()
        otp_time = user.otp_create_time
        diff_time = now - otp_time
        print('OTP TIME: ', diff_time)

        if diff_time.seconds > 120:
            return False
        return True

    except models.User.DoesNotExist:
        return False





def check_send_otp(phone):
    user = models.User.objects.get(phone=phone)
    now = timezone.now()
    otp_time = user.otp_create_time
    diff_time = now - otp_time

    if diff_time.seconds > 120:
        return True
    return False







def email_send_code(user, password):
    subject = 'Davaat account password'
    message = f'Hi {user.first_name}, Thank you for using our service. Your password is: {password}'
    from_email = EMAIL_HOST_USER
    recipient_list = [user.email, ]
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, recipient_list)
        except BadHeaderError:
            return 0
            #return HttpResponse('Invalid header found.')
        return 1
        #return HttpResponseRedirect('/contact/thanks/')
    else:
        return 0
        #return HttpResponse('Make sure all fields are entered and valid.')

