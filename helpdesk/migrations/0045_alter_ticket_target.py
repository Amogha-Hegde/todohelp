# Generated by Django 3.2.9 on 2022-01-19 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0044_auto_20220119_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdesk.role', verbose_name='Organisation'),
        ),
    ]
