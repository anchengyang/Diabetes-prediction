from django.db import models

# Create your models here.
class PredResults(models.Model):

    pregnancies = models.IntegerField()
    glucose = models.FloatField()
    blood_pressure = models.FloatField()
    skin_thickness = models.FloatField()
    insulin = models.FloatField()
    bmi = models.FloatField()
    diabetes_pedigree_function = models.FloatField()
    age = models.IntegerField()
    classification = models.CharField(max_length=30)

    def __str__(self):
        return self.classification