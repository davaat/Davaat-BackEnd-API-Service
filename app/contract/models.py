from django.db import models
from django.db.models import Model
from authentication.models import User
from tag.models import Tag



class Category(models.Model):
    name = models.CharField(max_length=256, unique=True, verbose_name='دسته بندی')
    creator_company = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_company')

    def __str__(self):
        return str(self.name)



class ContractFile(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploader', verbose_name='uploader')
    name = models.CharField(max_length=256)
    file = models.FileField(upload_to='files')

    def __str__(self):
        return str(self.name)


class ContractFileSettings(models.Model):
    contract_file = models.OneToOneField(ContractFile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.contract_file)






class Contract(Model):
    title = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', verbose_name='creator')
    contracting_party = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contracting_party', verbose_name='طرف قرارداد')
    CHOICES = (('تکمیل شده', 'تکمیل شده'),
               ('تدوین قرارداد', 'تدوین قرارداد'),
               ('منتظر تایید', 'منتظر تایید'),
               ('منتظر امضا', 'منتظر امضا'),
               ('پایان مهلت امضا', 'پایان مهلت امضا'))
    status = models.CharField(max_length=256, choices=CHOICES, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='category')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True, related_name='tag')
    #questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, null=True, blank=True, related_name='questionnaire')
    body = models.TextField(max_length=1000)
    conclusion_date = models.CharField(max_length=256, null=True, blank=True, verbose_name='تاریخ انعقاد')
    end_date = models.CharField(max_length=256, null=True, blank=True, verbose_name='تاریخ پایان')
    file = models.ForeignKey(ContractFile, on_delete=models.CASCADE, related_name='ContractFile', verbose_name='ContractFile')
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)





class Questionnaire(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='contract')

class Question(models.Model):
    question = models.CharField(max_length=256)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='questionnaire')





class GeneralSettings(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    public_approvers = models.ManyToManyField(User, related_name='public_approvers_GeneralSettings')
    dedicated_approvers = models.ManyToManyField(User, related_name='dedicated_approvers_GeneralSettings')

    def __str__(self):
        return str(self.contract)



class CustomSettings(models.Model):
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    public_approvers = models.ManyToManyField(User, related_name='public_approvers_CustomSettings')
    dedicated_approvers = models.ManyToManyField(User, related_name='dedicated_approvers_CustomSettings')

    def __str__(self):
        return str(self.contract)


