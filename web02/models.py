from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class ClassInfo(models.Model):
    major_name = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.major_name
    
class StudentInfo(models.Model):
    name = models.CharField(max_length=100,blank=False)
    student_num = models.CharField(max_length=11)
    major = models.ForeignKey(ClassInfo,on_delete=models.CASCADE)
    the_1st_judge = models.CharField(max_length=100,blank=True)
    the_2nd_judge = models.CharField(max_length=100,blank=True)
    the_3rd_judge = models.CharField(max_length=100,blank=True)
    the_4th_judge = models.CharField(max_length=100,blank=True)
    the_5th_judge = models.CharField(max_length=100,blank=True)
    the_6th_judge = models.CharField(max_length=100,blank=True)
    the_7th_judge = models.CharField(max_length=100,blank=True)
    the_8th_judge = models.CharField(max_length=100,blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    def to_dict(self):
        major_name = ClassInfo.objects.filter(major_name=self.major)
        return {
            'name':self.name,
            'student_num':self.student_num,
            'major':major_name[0].major_name,
            'the_1st_judge':self.the_1st_judge,
            'the_2nd_judge':self.the_2nd_judge,
            'the_3rd_judge':self.the_3rd_judge,
            'the_4th_judge':self.the_4th_judge,
            'the_5th_judge':self.the_5th_judge,
            'the_6th_judge':self.the_6th_judge,
            'the_7th_judge':self.the_7th_judge,
            'the_8th_judge':self.the_8th_judge,
            'created':self.created,
            'updated':self.updated,
        }

