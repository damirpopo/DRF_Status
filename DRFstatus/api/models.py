from django.db import models


class Status(models.Model):
    status=models.CharField(max_length=30)

    def __str__(self):
        return self.status

class TitleJob(models.Model):
    titlejob=models.CharField(max_length=40)

    def __str__(self):
        return self.titlejob

class Workers(models.Model):
    name=models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    surname2 = models.CharField(max_length=20)
    login = models.CharField(max_length=20)
    photo= models.URLField()
    titleJob=models.ForeignKey(TitleJob,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    table=models.IntegerField()
    worker=models.ForeignKey(Workers,on_delete= models.CASCADE)
    time_order=models.DateTimeField()
    status=models.ForeignKey(Status,on_delete= models.CASCADE)
    price = models.IntegerField()



