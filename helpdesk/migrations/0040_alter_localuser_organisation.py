# Generated by Django 3.2.9 on 2022-01-14 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0039_auto_20220114_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localuser',
            name='organisation',
            field=models.ForeignKey(help_text='Name of the organisation that the user belongs to', null=True, on_delete=django.db.models.deletion.CASCADE, to='helpdesk.organisation'),
        ),
    ]
