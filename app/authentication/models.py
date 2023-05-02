from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.custom_usermanager import UserManager
from django.utils.html import format_html
from shortuuid.django_fields import ShortUUIDField







#------------------------------------------------------------------------------
class City(models.Model):
    name = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return str(self.name)





class User(AbstractUser):
    username = None
    is_company = models.BooleanField(default=False, verbose_name="شرکت می باشد")
    company_name = models.CharField(max_length=256, null=True, blank=True, verbose_name="نام شرکت")
    company_display_name = models.CharField(max_length=256, null=True, blank=True, verbose_name="نام شرکت")
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=256, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=256, null=True, blank=True, unique=True)
    national_code = models.CharField(max_length=256, unique=True, null=True, blank=True)
    #father_name = models.CharField(max_length=256, null=True, blank=True)
    #birth_date = models.CharField(max_length=256, null=True, blank=True)
    otp = models.PositiveIntegerField(blank=True, null=True)
    otp_create_time = models.DateTimeField(auto_now=True)
    otp_confirmed = models.BooleanField(default=False)
    #email_confirmed = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='user/photo', default='user/photo/default.png')
    invitation_referral = ShortUUIDField(length=8, max_length=15, alphabet="abcdefg1234", editable=False)
    referral = models.CharField(max_length=256, null=True, blank=True)
    status = models.CharField(max_length=256, null=True, blank=True)
    status_set_time = models.DateTimeField(null=True, blank=True)
    CHOICES = (("don't clear", "don't clear"), ("30 min", "30 min"), ("1 hour", "1 hour"),("24 hour", "24 hour"),("this week", "this week") )
    status_clear_after = models.CharField(max_length=256, choices=CHOICES, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    def __str__(self):
        return str(self.phone)

    def img(self):
        return format_html("<img style='width:30px;border-radius:50%;' src='{}'>".format(self.photo.url))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



