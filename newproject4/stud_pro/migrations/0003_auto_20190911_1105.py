# Generated by Django 2.2.5 on 2019-09-11 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stud_pro', '0002_auto_20190911_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='parent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stud_pro.Parent'),
        ),
    ]
