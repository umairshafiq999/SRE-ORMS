from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=191)
    phone_no = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    password = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Items(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=191)
    picture = models.CharField(max_length=191)
    rental_price = models.IntegerField()
    description = models.CharField(max_length=191)
    keywords = models.CharField(max_length=191)
    status = models.CharField(max_length=191)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class UsersRentedItems(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_rented_items'


class UsersRequestedItems(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_requested_items'
