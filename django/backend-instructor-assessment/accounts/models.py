# from django.contrib.auth.models import AbstractUser
# from django.db import models
#
#
# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         db_table = "CustomUser"
#         get_latest_by = ['-created_at', 'updated_at']
#         verbose_name = "CustomUser"
#         verbose_name_plural = "CustomUsers"
#
#     def __str__(self):
#         return self.username
