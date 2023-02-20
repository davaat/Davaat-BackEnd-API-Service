from django.db import models
from django.db.models import Model
from authentication.models import User



class Signature(Model):
    name = models.CharField(max_length=256, verbose_name='نام امضا')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000, verbose_name='توضیحات')
    image = models.ImageField(upload_to='user/signature', default='user/signature/default.png')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    def img(self):
        return format_html("<img style='width:30px;border-radius:10%;' src='{}'>".format(self.image.url))
