from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Custom UserManager
class UserManager(BaseUserManager):
    def create_user(self, email, name, tc, password=None, password2=None):
        """
        Creates and saves a User with the given email, name , tc
         and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            tc=tc,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, tc, password=None):
        """
        Creates and saves a User with the given email, name , tc
        and password.
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
            tc=tc,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=200)
    tc = models.BooleanField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "tc"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.IntegerField()
    imageurl = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=50)
    createdDate = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    cartId = models.IntegerField()
    username = models.CharField(max_length=100)
    product = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.IntegerField()
    imageurl = models.CharField(max_length=500)
    createdDate = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    product = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.IntegerField()
    imageurl = models.CharField(max_length=500)
    createdDate = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    img = models.ImageField(upload_to="images", blank=True)
