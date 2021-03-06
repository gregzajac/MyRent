# Generated by Django 3.0.3 on 2020-03-02 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyRent', '0004_tenant_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agreement',
            old_name='agreement_description',
            new_name='info',
        ),
        migrations.RenameField(
            model_name='flat',
            old_name='flat_description',
            new_name='info',
        ),
        migrations.RenameField(
            model_name='tenant',
            old_name='tenant_description',
            new_name='info',
        ),
        migrations.AddField(
            model_name='operation',
            name='info',
            field=models.TextField(null=True, verbose_name='Dodatkowe info'),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Najemca'),
        ),
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='Imię')),
                ('last_name', models.CharField(max_length=64, verbose_name='Nazwisko')),
                ('phone', models.CharField(max_length=16, null=True, verbose_name='Telefon')),
                ('email', models.CharField(max_length=64, null=True, verbose_name='E-mail')),
                ('info', models.TextField(null=True, verbose_name='Dodatkowe info')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Właściciel')),
            ],
        ),
        migrations.AddField(
            model_name='flat',
            name='landlord',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MyRent.Landlord', verbose_name='Właściciel'),
        ),
    ]
