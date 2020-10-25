from django.db import models

# Create your models here.

def pid_validation(PID):
    if PID in KW.objects.filter(ID==PID):
        return True
    else:
        return False


class KW(models.Model):
    keyword = models.CharField(blank=False, max_length=50)
    _id = models.IntegerField(auto_created=True,primary_key=True)
    PID = models.IntegerField(blank=False,default=0,validators=[pid_validation])


