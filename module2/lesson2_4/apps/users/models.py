from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import BaseModel
from apps.users.managers import CustomUserManager


class User(AbstractUser, BaseModel):
    class UserLanguages(models.TextChoices):
        ENGLISH = "en", _("English")
        RUSSIAN = "ru", _("Russian")
        UZBEK = "uz", _("Uzbek")

    username = None
    first_name = None
    last_name = None

    phone_number = PhoneNumberField(_("Phone number"), max_length=13, unique=True)
    full_name = models.CharField(_("full name"), max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(_("Date of birth"), null=True, blank=True)
    photo = models.ImageField(_("Image"), upload_to='photo/%Y/%m', null=True, blank=True)
    language = models.CharField(_("Language"), choices=UserLanguages.choices, default=UserLanguages.RUSSIAN)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def token(self):
        token = RefreshToken.for_user(self)
        return {"access": str(token.access_token), "refresh": str(token)}

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return f'{self.phone_number}'
