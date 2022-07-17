
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.



from django.db import models
from django.template.defaultfilters import slugify


from django.urls import reverse
from django.contrib.auth.models import User

from IsraelAPI.I4G006635NH1.links.managers import ActiveLinkManager

# Create your models here.
class link(models.Model):
    target_url=models.URLField(max_lenght=200)
    description=models.CharField
    identifier=models.SlugField(blank=True,unique=True,max_lenght=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateField()
    active=models.BooleanField(default=True)

    
    objects = models.Manager()
    public = ActiveLinkManager()