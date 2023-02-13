from kavenegar import *
from core.settings import Kavenegar_API
from random import randint
from . import models
import datetime
import time
import random
import string
import json




def otpsend(phone, otp):
    try:
        api = KavenegarAPI(Kavenegar_API)
        params = {
          'receptor': phone,
          'template': 'RPTaxiVerify',
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
        now = datetime.datetime.now()
        otp_time = user.otp_create_time
        diff_time = now - otp_time
        print('OTP TIME: ', diff_time)

        if diff_time.seconds > 120:
            return False
        return True

    except models.User.DoesNotExist:
        return False





def check_send_otp(mobile):
    user = models.User.objects.get(mobile=mobile)
    now = datetime.datetime.now()
    otp_time = user.otp_create_time
    diff_time = now - otp_time

    if diff_time.seconds > 120:
        return True
    return False
