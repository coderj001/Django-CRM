# Generated by Django 3.2.2 on 2021-05-20 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20210520_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='leads.agent'),
        ),
    ]
