# Generated by Django 3.0.3 on 2020-03-04 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyRent', '0007_auto_20200303_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agreement',
            options={'verbose_name': 'Umowa', 'verbose_name_plural': 'Umowy'},
        ),
        migrations.AlterModelOptions(
            name='flat',
            options={'verbose_name': 'Mieszkanie', 'verbose_name_plural': 'Mieszkania'},
        ),
        migrations.AlterModelOptions(
            name='landlord',
            options={'verbose_name': 'Właściciel', 'verbose_name_plural': 'Właściciele'},
        ),
        migrations.AlterModelOptions(
            name='operation',
            options={'verbose_name': 'Operacja finansowa', 'verbose_name_plural': 'Operacje finansowe'},
        ),
        migrations.AlterModelOptions(
            name='operationdict',
            options={'verbose_name': 'Typ operacji finansowej', 'verbose_name_plural': 'Typy operacji finansowych'},
        ),
        migrations.AlterModelOptions(
            name='tenant',
            options={'verbose_name': 'Najemca', 'verbose_name_plural': 'Najemcy'},
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='pictures/None/no-img.png', upload_to='pictures/')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyRent.Flat')),
            ],
            options={
                'verbose_name': 'Zdjęcie',
                'verbose_name_plural': 'Zdjęcia',
            },
        ),
    ]
