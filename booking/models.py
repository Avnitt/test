from django.db import models
from service.models import Subservice, Addon
from customauth.models import User
from staff.models import Professional, Slot

class Appointment(models.Model):
    user = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='appointments')
    subservice = models.ForeignKey(Subservice,
                                   on_delete=models.CASCADE,
                                   related_name='appointments')
    addons = models.ManyToManyField(Addon,
                                    blank=True)
    professional = models.ForeignKey(Professional,
                                     on_delete=models.CASCADE,
                                     related_name='appointments')
    slot = models.OneToOneField(Slot,
                                on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id