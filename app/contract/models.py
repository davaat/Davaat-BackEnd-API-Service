from django.db import models
from django.db.models import Model
from authentication.models import User





class Category(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name='دسته بندی')

    def __str__(self):
        return str(self.name)







class Contract(Model):
    title = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    contracting_party = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contracting_party', verbose_name='طرف قرارداد')
    CHOICES = (('تکمیل شده', 'تکمیل شده'),
               ('تدوین قرارداد', 'تدوین قرارداد'),
               ('منتظر تایید', 'منتظر تایید'),
               ('منتظر امضا', 'منتظر امضا'),
               ('پایان مهلت امضا', 'پایان مهلت امضا'))
    status = models.CharField(max_length=256, choices=CHOICES, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    body = models.TextField(max_length=1000)
    conclusion_date = models.CharField(max_length=256, null=True, blank=True, verbose_name='تاریخ انعقاد')
    end_date = models.CharField(max_length=256, null=True, blank=True, verbose_name='تاریخ پایان')
    file = models.FileField(upload_to='files', null=True, blank=True, verbose_name="فایل های ضمیمه شده")
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
