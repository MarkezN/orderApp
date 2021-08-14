from django.db import models
from django.conf import settings

class Pdfs(models.Model):

	title = models.CharField(max_length=250)
	autor = models.CharField(max_length=250)
	fajlovi = models.FileField(upload_to="docs/pdfs/")
	broj_stranica = models.IntegerField(blank=False, null=True)
	cena_stranica = models.IntegerField(null=True)


	def __str__(self):   
		return self.title



	def delete(self, *args, **kwargs):  
		self.fajlovi.delete()
		super().delete(*args, **kwargs)


	@property 
	def ukupno(self):   
		return self.broj_stranica * self.cena_stranica   

class Comment(models.Model): 

	autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	headline = models.CharField(max_length=150)
	tekst = models.TextField()


	def __str__(self):
		return self.headline











	
