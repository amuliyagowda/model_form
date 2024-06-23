from django.db import models
from django import forms
# Create your models here.

#should start with a
def validate_for_a(value):
    if value[0]!='a':
        raise forms.ValidationError('should  start with a')

# lenght should be less than given value 
def validate_for_len(value):
    if len(value)>5:
        raise forms.ValidationError('lenght should be less than 5')

#should not  be third character as n  
def validate_for_n(value):
    if value[3]=='n':
        raise forms.ValidationError('third character should not be n')

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True,validators=[validate_for_a])
    
    def __str__(self):
        return self.topic_name

class  Webpages(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,validators=[validate_for_n])
    url=models.URLField()
    game=models.CharField(max_length=100,default='cricket')
    email=models.EmailField()

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100,validators=[validate_for_len])

    def __str__(self):
        return self.author