# Generated by Django 4.2.1 on 2023-08-10 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('naudotojo_profilis', '0001_initial'),
        ('irankis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nuomosfaktas',
            name='nuomininkas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nuomininko_nuomos_faktai', to='naudotojo_profilis.naudotojoprofilis'),
        ),
        migrations.AddField(
            model_name='nuomosfaktas',
            name='nuomotojas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nuomotojo_nuomos_faktai', to='naudotojo_profilis.naudotojoprofilis'),
        ),
        migrations.AddField(
            model_name='irankis',
            name='kategorijos',
            field=models.ManyToManyField(to='irankis.kategorija'),
        ),
        migrations.AddField(
            model_name='irankis',
            name='naudotojas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naudotojo_profilis.naudotojoprofilis'),
        ),
        migrations.AddField(
            model_name='irankiovienetas',
            name='irankis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='irankis.irankis'),
        ),
        migrations.AddField(
            model_name='irankioatsiliepimas',
            name='irankis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='irankis.irankis'),
        ),
        migrations.AddField(
            model_name='irankioatsiliepimas',
            name='naudotojas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
