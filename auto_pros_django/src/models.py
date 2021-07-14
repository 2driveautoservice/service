from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.deletion import SET_NULL
from django.db.models import Avg, Func, FloatField
from django.conf import settings

from PIL import Image
from datetime import datetime

from .managers import CustomUserManager

# Functions

# (# to round, # of digits)
class Round(Func):
  function = 'ROUND'
  arity = 2

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)

    REQUIRED_FIELDS = [name, code]

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    REQUIRED_FIELDS = [name]

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    managing_user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=SET_NULL)

    def __str__(self):
        return self.name

    def get_rating(self):
        if not self.rating_set.all():
            return 0
        else:
            return self.rating_set.aggregate(rounded_rating_avg=Round(Avg('rating'), 1, output_field=FloatField()))['rounded_rating_avg']
    
    def get_recent_rating(self):
        if not self.rating_set.all():
            return datetime.min
        else:
            return self.rating_set.all().order_by('-date_created')[0].date_created
    
    def get_general_profile(self):
        try:
            return self.general_profile
        except:
            return False
    
    def get_business_profile(self):
        try:
            general_profile = self.get_general_profile()
            return general_profile.business_profile
        except:
            return False
    
    def get_image(self):
        try:
            return self.get_general_profile().get_image()
        except:
            return False
    
    def get_description(self):
        try:
            return self.get_business_profile().description
        except:
            return False

    REQUIRED_FIELDS = [name]

class Location(models.Model):
    address = models.CharField(max_length=150)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='locations', on_delete=models.CASCADE)

    REQUIRED_FIELDS = [address]

    def __str__(self):
        return self.address

    def get_region(self):
        return str(self.region)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('Email Address'), unique=True)
    employer = models.ManyToManyField(Company, blank=True)
    is_active = models.BooleanField(('active'), 
    default=True, 
    help_text=('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    is_staff = models.BooleanField(
        default=False,
        help_text=('Designates whether the user is a staff member.'),
        verbose_name='staff status'
    )
    is_active = models.BooleanField(
        default=True,
        help_text=(
            'Designates whether this user should be treated as active.'
            'Unselect this instead of deleting accounts.'
        ),
        verbose_name='active status'
    )
    is_business_owner = models.BooleanField(
        default=False,
        help_text=(
            'Designates whether the user is a business_owner'
        ),
        verbose_name='business_owner status')
    is_business_user = models.BooleanField(
        default=False,
        help_text=(
            'Designates whether the user is a business_user'
        ),
        verbose_name='business_user status')
    is_consumer_user = models.BooleanField(
        default=False,
        help_text=(
            'Designates whether the user is a consumer/normal user'
        ),
        verbose_name='consumer_user status')
    
    date_created = models.DateTimeField(auto_now_add=True)


    ordering = ('email',)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    REQUIRED_FIELDS = ['is_business_owner', 'is_business_user', 'is_consumer_user']

class GeneralProfile(models.Model):
    phone = models.CharField(max_length=15, unique=True)
    image = models.ImageField(
        upload_to='uploads/', 
        blank=True, 
        null=True, 
        default='default_profile_image.png')
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    company = models.OneToOneField(
        Company,
        related_name='general_profile',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    #reformat for be static size?
    def get_image(self):
        if self.image:
            return str(settings.HOST_DOMAIN) + self.image.url
        return False
    
    def __str__(self):
        if self.user is not None:
            return 'User: ' + self.user.email
        elif self.company is not None:
            return 'Company: ' + self.company.name
        else:
            return 'Profile id: ' + self.id
    
class BusinessOwnerProfile(models.Model):
    description = models.TextField(default='', max_length=255)

    profile = models.OneToOneField(
        GeneralProfile,
        related_name='business_profile',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        profile_string = str(self.profile)
        if 'Profile id' in profile_string:
            return 'Profile id: ' + self.id
        else:
            return profile_string

class BusinessUserProfile(models.Model):
    title = models.CharField(max_length=10)

    profile = models.OneToOneField(
        GeneralProfile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        profile_string = str(self.profile)
        if 'Profile id' in profile_string:
            return 'Profile id: ' + self.id
        else:
            return profile_string

class ConsumerUserProfile(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
        
    profile = models.OneToOneField(
        GeneralProfile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        profile_string = str(self.profile)
        if 'Profile id' in profile_string:
            return 'Profile id: ' + self.id
        else:
            return profile_string

class Rating(models.Model):
    RATING_CHOICES = [(i+1,i+1) for i in range(5)]
    rating = models.IntegerField(choices=RATING_CHOICES)
    review = models.TextField(default='')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    REQUIRED_FIELDS = [rating]

class Service(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=SET_NULL)
    company = models.ManyToManyField(Company, blank=True, related_name='services')
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    REQUIRED_FIELDS = [name]

    def __str__(self):
        return self.name
    
    def get_companies(self):
        company_objects = self.company.all()
        return company_objects.values_list('id', flat=True)
        










