from django.db import models

# Create your models here.
class BusinessProfile(models.Model):
    companyType = models.CharField(max_length=250)
    registeredName = models.CharField(max_length=250)
    companyName = models.CharField(max_length=250)
    dateFiled = models.DateTimeField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    zipCode = models.IntegerField()

    def __str__(self):
        return '%s %s %s %s %s %s %s %s' % (self.companyType,
                self.registeredName, self.companyName, self.dateFiled,
                self.address, self.city, self.state, self.zipCode,)

#TODO: create a model for exception URLs from the scraper

