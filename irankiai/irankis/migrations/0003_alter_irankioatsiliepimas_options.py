# Generated by Django 4.2.1 on 2023-06-14 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irankis', '0002_remove_irankiovienetas_vietove_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='irankioatsiliepimas',
            options={'ordering': ['-date_created'], 'verbose_name': 'Atsiliepimas', 'verbose_name_plural': 'Atsiliepimai'},
        ),
    ]
