# Generated by Django 4.2.1 on 2023-07-24 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irankis', '0004_remove_irankis_aprasymas_remove_irankis_galia_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kategorija',
            name='pavadinimas',
        ),
        migrations.AddField(
            model_name='kategorija',
            name='name',
            field=models.CharField(default='kazkas', max_length=255, verbose_name='name'),
            preserve_default=False,
        ),
    ]
