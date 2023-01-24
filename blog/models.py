from django.db import models

class Student(models.Model):
	name=models.CharField(max_length=15)
	email=models.CharField(max_length=15)
	mobile=models.IntegerField()
	

	def __str__(self):
		s=str(self.id)+self.name+self.name+str(self.mobile)
		return s
		
