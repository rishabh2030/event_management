from django.db import models

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    created_at = models.DateTimeField(auto_now_add=True,help_text="when instance was created")
    updated_at = models.DateTimeField(auto_now=True,help_text="when instance was last updated")

    class Meta:
        abstract = True