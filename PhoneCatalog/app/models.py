from django.db import models

class phone_catalog(models.Model):
    Name = models.CharField(max_length=20)
    RegDate = models.DateField(auto_now_add=True)
    Address = models.CharField(max_length=110)
    Phone = models.CharField(max_length=30)
    def __str__(self):
        return self.Name+" "+self.Address + " " +str(self.RegDate)+ " "+self.Phone