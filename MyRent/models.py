from django.contrib.auth.models import User
from django.db import models
from datetime import datetime, timedelta


class Landlord(models.Model):
    first_name = models.CharField(max_length=64, verbose_name="Imię")
    last_name = models.CharField(max_length=64, verbose_name="Nazwisko")
    phone = models.CharField(max_length=16, verbose_name="Telefon", null=True)
    email = models.CharField(max_length=64, verbose_name="E-mail", null=True)
    info = models.TextField(verbose_name="Dodatkowe info", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name="Właściciel")

    class Meta:
        verbose_name = u'Właściciel'
        verbose_name_plural = u'Właściciele'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Flat(models.Model):
    street = models.CharField(max_length=128, verbose_name="Ulica")
    block_number = models.CharField(max_length=64, verbose_name="Nr domu")
    flat_number = models.CharField(max_length=64, verbose_name="Nr mieszkania", null=True)
    post_code = models.CharField(max_length=16, verbose_name="Kod pocztowy")
    city = models.CharField(max_length=64, verbose_name="Miasto")
    info = models.TextField(verbose_name="Dodatkowe info", null=True, blank=True)
    landlord = models.ForeignKey(Landlord, verbose_name="Właściciel", on_delete=models.CASCADE, null=True)
    is_for_rent = models.BooleanField(default=True, verbose_name="Czy jest do wynajęcia")

    class Meta:
        verbose_name = u'Mieszkanie'
        verbose_name_plural = u'Mieszkania'

    def __str__(self):
        if self.flat_number:
            block_flat_number = f"{self.block_number}/{self.flat_number}"
        else:
            block_flat_number = f"{self.block_number}"
        return f"{self.street} {block_flat_number}, {self.post_code} {self.city}"

    def get_active_agreement(self):
        lst = self.agreement_set.filter(date_from__lte=datetime.now().date(), date_to__gte=datetime.now().date())
        if lst.count() > 0:
            return lst[0]

    def available_from(self):
        active_agreement = self.get_active_agreement()
        if active_agreement:
            return active_agreement.date_to + timedelta(days=1)
        return datetime.now().date()


class Tenant(models.Model):
    first_name = models.CharField(max_length=64, verbose_name="Imię")
    last_name = models.CharField(max_length=64, verbose_name="Nazwisko")
    phone = models.CharField(max_length=16, verbose_name="Telefon", null=True)
    email = models.CharField(max_length=64, verbose_name="E-mail", null=True)
    info = models.TextField(verbose_name="Dodatkowe info", null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name="User login")

    class Meta:
        verbose_name = u'Najemca'
        verbose_name_plural = u'Najemcy'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agreement(models.Model):
    code = models.CharField(max_length=32, verbose_name="Identyfikator umowy", unique=True)
    agreement_date = models.DateField(verbose_name="Data podpisania umowy")
    date_from = models.DateField(verbose_name="Data początku najmu")
    date_to = models.DateField(verbose_name="Data końca najmu")
    mth_payment_value = models.FloatField(verbose_name="Miesięczny koszt wynajmu")
    mth_payment_deadline = models.SmallIntegerField(verbose_name="Termin miesięcznej opłaty")
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, verbose_name="Najemca")
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, verbose_name="Wynajmowane mieszkanie")
    info = models.TextField(verbose_name="Dodatkowe info", null=True, blank=True)

    class Meta:
        verbose_name = u'Umowa'
        verbose_name_plural = u'Umowy'

    def __str__(self):
        return f"{self.code}, {self.agreement_date}"

    def is_active(self):
        return self.date_from <= datetime.now().date() <= self.date_to


class OperationDict(models.Model):
    PLUS_MINUS = (
        (1, "PLUS"),
        (2, "MINUS")
    )
    name = models.CharField(max_length=32, verbose_name="Operacja finansowa")
    plus_minus = models.SmallIntegerField(choices=PLUS_MINUS, verbose_name="Wpływ na saldo rozliczeń")

    class Meta:
        verbose_name = u'Typ operacji finansowej'
        verbose_name_plural = u'Typy operacji finansowych'

    def __str__(self):
        return self.name


class Operation(models.Model):
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE, verbose_name="Umowa najmu")
    type = models.ForeignKey(OperationDict, on_delete=models.CASCADE, verbose_name="Typ operacji finansowej")
    date = models.DateField(verbose_name="Data operacji")
    value = models.FloatField(verbose_name="Kwota operacji")
    info = models.TextField(verbose_name="Dodatkowe info", null=True, blank=True)

    class Meta:
        verbose_name = u'Operacja finansowa'
        verbose_name_plural = u'Operacje finansowe'

    def __str__(self):
        return f"{self.type} | {self.date} | {self.value}"


class Image(models.Model):
    picture = models.ImageField(default="no-img.png", verbose_name="Zdjęcie")
    info = models.CharField(max_length=128, null=True, blank=True, verbose_name="Opis zdjęcia")
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, verbose_name="Mieszkanie dot. zdjęcia")

    class Meta:
        verbose_name = u'Zdjęcie'
        verbose_name_plural = u'Zdjęcia'

    def __str__(self):
        return f"{self.flat} | {self.info}"
