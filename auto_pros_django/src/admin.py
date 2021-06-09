from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class UserAdminCustom(UserAdmin):
   list_display = ('id','email', 'is_business_owner', 'is_business_user', 'is_consumer_user', 'is_staff', 'is_superuser', 'is_active')
   list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_business_owner', 'is_business_user', 'is_consumer_user')
   search_fields = ('id', 'email',)
   ordering = ('id', 'email',)
   readonly_fields = ('id',)

class CompanyAdmin(admin.ModelAdmin):
   list_display = ('id', 'name')
   readonly_fields = ('id',)
   search_fields = ('id', 'name',)
   ordering = ('id', 'name',)

class RatingAdmin(admin.ModelAdmin):
   list_display = ('company', 'rating', 'user', 'date_created')
   search_fields = ('user', 'company', 'rating', 'date_created',)
   ordering = ('company', 'rating', 'user', 'date_created',)

class ServiceAdmin(admin.ModelAdmin):
   list_display = ('name', 'parent')
   search_fields = ('name', 'parent',)
   ordering = ('name', 'parent', 'id',)

class CountryAdmin(admin.ModelAdmin):
   list_display = ('name', 'code')
   search_fields = ('name', 'code',)

class RegionAdmin(admin.ModelAdmin):
   list_display = ('name', 'get_country')
   search_fields = ('name', 'get_country',)

   def get_country(self, obj):
        return obj.country.name
   get_country.admin_order_field  = 'country'  #Allows column order sorting
   get_country.short_description = 'Country'  #Renames column head

class LocationAdmin(admin.ModelAdmin):
   list_display = ('address', 'get_region', 'get_company')
   search_fields = ('address', 'get_region', 'get_company',)

   def get_region(self, obj):
        return obj.region.name
   get_region.admin_order_field  = 'region'  #Allows column order sorting
   get_region.short_description = 'Region'  #Renames column head

   def get_company(self, obj):
        return obj.company.name
   get_company.admin_order_field  = 'company'  #Allows column order sorting
   get_company.short_description = 'Company'  #Renames column head

admin.site.register(CustomUser, UserAdminCustom)
admin.site.register(Company, CompanyAdmin)
admin.site.register(GeneralProfile)
admin.site.register(BusinessOwnerProfile)
admin.site.register(BusinessUserProfile)
admin.site.register(ConsumerUserProfile)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Location, LocationAdmin)



