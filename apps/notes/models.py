from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User=get_user_model()

#Custom manager for fetch active notes only
class ActiveNoteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)
    
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes", null=False, blank=False)
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=models.Manager()
    active_notes=ActiveNoteManager()

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return self.title