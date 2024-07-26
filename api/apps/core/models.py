from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


# class SoftDeleteManager(models.Manager):
#     def get_by_natural_key(self, id):
#         return self.get(id=id)
#
#     def get_queryset(self):
#         return super().get_queryset().filter(is_deleted=False)
#
#     def all_with_deleted(self):
#         return super().get_queryset()
#
#     def delete(self, *args, **kwargs):
#         self.update(is_deleted=True)
#
#     def hard_delete(self):
#         super().get_queryset().delete()
