from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings



# class UserManager(BaseUserManager):    
    
#     use_in_migrations = True

#     def create_user(self, username, password):        
         
#         user = self.model(            
#             username = username,
#             password = password,
#             nickname = '기본',
#             birthdate = '2000-01-01'
#         )        
#         user.set_password(password)        
#         user.save(using=self._db)        
#         return user
      
#     def create_superuser(self, username, password):        
       
#         user = self.create_user(   
#             username = username,            
#             password = password,
#             nickname = '기본',
#             birthdate = '2000-01-01'     
#         )        
#         user.is_admin = True        
#         user.is_superuser = True        
#         user.is_staff = True        
#         user.save(using=self._db)        
#         return user


class User(AbstractUser):
    GENDER_CHOICES = [
        (1, '남'),
        (2, '여')
    ]

    stars = models.ManyToManyField('self', symmetrical=False, related_name='fans', through='Relationship')
    nickname = models.CharField(max_length=20, null=False, default='nickname')
    birthdate = models.DateField(null=False, auto_now_add=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=1)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.username


class Group(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_groups')
    name = models.CharField(max_length=20, default='기본', null=False)

    def __str__(self):
        return self.name


class Relationship(models.Model): # follow
    fan = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_stars')
    star = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_fans')
    group = models.ForeignKey(Group, on_delete=models.SET_DEFAULT, default=1, related_name='group_stars')

    def __str__(self):
        return f'{self.fan}이 {self.star}을 {self.group}그룹에 넣음'