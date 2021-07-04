# Generated by Django 3.1.2 on 2021-07-04 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20210704_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalbed',
            name='occupied_patient',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='patients.patient'),
        ),
    ]
