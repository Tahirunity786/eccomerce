from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from core_account.manager import CustomUserManager

class Addresses(models.Model):
    address_text = models.TextField(db_index=True, null=True)



class User(AbstractUser):
    GENDER = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Not confirmed", "Not confirmed"),
    )

    profile = models.ImageField(upload_to="profile/images", blank=True, null=True)
    full_name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(db_index=True, unique=True)
    date_of_birth = models.DateField(default=None, null=True)
    gender = models.CharField(max_length=100, choices=GENDER, null=True, db_index=True)
    mobile_number = models.BigIntegerField(null=True)
    otp = models.PositiveIntegerField(null=True)
    otp_limit = models.IntegerField(null=True)
    otp_delay = models.TimeField(auto_now=True)
    last_login = models.DateTimeField(default=None, null=True)
    is_blocked = models.BooleanField(default=False, null=True)
    is_verified = models.BooleanField(default=False)
    address = models.ManyToManyField(Addresses, db_index=True)
    groups = models.ManyToManyField(Group, related_name='user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions', blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 
    objects = CustomUserManager()

    def __str__(self):
        return self.email  # Or any other field you prefer as representation
