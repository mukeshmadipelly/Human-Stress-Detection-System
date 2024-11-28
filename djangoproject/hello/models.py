from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
import joblib
import os
import tensorflow as tf


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class HealthData(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    heart_rate = models.FloatField()
    snoring_rate = models.FloatField()
    respiratory_rate = models.FloatField()
    body_temperature = models.FloatField()
    limb_movements = models.FloatField()
    blood_oxygen = models.FloatField()
    eye_movement = models.FloatField()
    sleep_hours = models.FloatField()
    result = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

# Load the model and scaler 
model_path = r'C:\Users\mukes\Desktop\myproject\djangoproject\hello\models\stress_detection_ann_model.h5' 
scaler_path = r'C:\Users\mukes\Desktop\myproject\djangoproject\hello\models\scaler.pkl' 
model = tf.keras.models.load_model(model_path)
scaler = joblib.load(scaler_path) 
def predict_stress(parameters): 
    scaled_features = scaler.transform([parameters]) 
    prediction = model.predict(scaled_features) 
    return 'Stressed' if prediction[0][0] > 0.5 else 'Not Stressed'

