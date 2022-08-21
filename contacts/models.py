from django.db import models
from datetime import datetime

class contacts(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 12)
    message = models.TextField(blank = True)
    contact_date  = models.DateTimeField(default = datetime.now)
    user_id = models.CharField(max_length = 230 ) #blank = True

    def __str__(self):
       # return self.listing_id
         return self.name