from django.db import models
from django.utils import timezone

class AdminUser(models.Model):
    admin_name = models.CharField(max_length=50)
    admin_user = models.CharField(max_length=100)
    admin_pw = models.CharField(max_length=30)
    #user_id = models.ForeignKey('User')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.admin_user

class UserType(models.Model):
    user_type_desc = models.CharField(max_length=45)
    user_type_status = models.IntegerField()

class UserAreaType(models.Model):
    user_area_name = models.CharField(max_length=45)

class User(models.Model):
    user_name = models.CharField(max_length=45)
    user_nickname = models.CharField(max_length=45)
    user_type_id = models.ForeignKey(UserType)
    user_country_code = models.CharField(max_length=45)
    user_phone = models.CharField(max_length=45)
    user_area = models.ForeignKey(UserAreaType)
    user_kakaoid = models.CharField(max_length=45)
    user_desc = models.TextField()
    user_has_car = models.IntegerField()
    user_available = models.IntegerField()
    user_sendbird_token = models.CharField(max_length=45)
    user_sendbird_token2 = models.CharField(max_length=45)
    user_sendbird_room = models.TextField()
    user_hashkey = models.TextField()
    user_is_del = models.IntegerField()
    user_email = models.CharField(max_length=45)
    #user_sendbird_id
    #user_publisher
    user_status = models.IntegerField()
    user_password = models.CharField(max_length=45)
    user_memo = models.TextField()
    user_created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_name
