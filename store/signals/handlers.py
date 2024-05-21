from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import Customer

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_customer_for_new_user(sender, **kwargs):
    if kwargs['created']:
        Customer.objects.create(user=kwargs['instance'])
    
