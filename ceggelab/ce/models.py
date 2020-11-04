from django.db import models

# Create your models here.
class Studentrecord(models.Model):
    student_name_en = models.CharField(max_length=200)
    student_name_th = models.CharField(max_length=200)
    student_ID = models.IntegerField(default=0)
    type = (('M','Master programs'),
        ('D','Doctoral programs'),
        ('P','Postdoctorate'), 
        ('R','Researcher'))

    student_level = models.CharField(max_length=30, choices= type)

    def __str__(self):
        return self.student_name_en +' '+ str(self.student_ID) +' '+ self.student_level
