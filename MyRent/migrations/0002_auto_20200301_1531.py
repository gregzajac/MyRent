# Generated by Django 3.0.3 on 2020-03-01 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyRent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='Imię')),
                ('last_name', models.CharField(max_length=64, verbose_name='Nazwisko')),
                ('phone', models.CharField(max_length=16, null=True, verbose_name='Telefon')),
                ('email', models.CharField(max_length=64, null=True, verbose_name='E-mail')),
                ('tenant_description', models.TextField(null=True, verbose_name='Dodatkowe info')),
            ],
        ),
        migrations.RemoveField(
            model_name='flat',
            name='description',
        ),
        migrations.AddField(
            model_name='flat',
            name='flat_description',
            field=models.TextField(null=True, verbose_name='Dodatkowe info'),
        ),
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=32, unique=True, verbose_name='Identyfikator umowy')),
                ('agreement_date', models.DateField(verbose_name='Data podpisania umowy')),
                ('date_from', models.DateField(verbose_name='Data początku najmu')),
                ('date_to', models.DateField(verbose_name='Data końca najmu')),
                ('mth_payment_value', models.FloatField(verbose_name='Miesięczny koszt wynajmu')),
                ('mth_payment_deadline', models.SmallIntegerField(verbose_name='Termin miesięcznej opłaty')),
                ('agreement_description', models.TextField(null=True, verbose_name='Dodatkowe info')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyRent.Flat', verbose_name='Wynajmowane mieszkanie')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyRent.Tenant', verbose_name='Najemca')),
            ],
        ),
    ]
