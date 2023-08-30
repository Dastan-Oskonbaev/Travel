from django.contrib.auth.models import AbstractUser, UserManager
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser(AbstractUser):
    first_name = models.CharField(
        _("First Name"),
        max_length=150,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        _("Last Name"),
        max_length=150,
        blank=True,
        null=True

    )
    email = models.EmailField(
        _("Email"),
        unique=True
    )
    phone_number = PhoneNumberField(
        _("Phone Number"),
        null=True,
        blank=True,
        unique=True
    )
    date_of_birth = models.DateField(
        _("Date of Birth"),
        null=True,
        blank=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
