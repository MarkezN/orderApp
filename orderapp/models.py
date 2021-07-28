from django.db import models


class Pdfs(models.Model):

	title = models.CharField(max_length=250)
	autor = models.CharField(max_length=250)
	fajlovi = models.FileField(upload_to="docs/pdfs/")


	def __str__(self):   
		return self.title



	def delete(self, *args, **kwargs):  
		self.fajlovi.delete()
		super().delete(*args, **kwargs)



	
