# Generated by Django 4.2.1 on 2023-08-10 16:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('naudotojo_profilis', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='naudotojas',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='naudotojas',
            name='username',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='naudotojas',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]