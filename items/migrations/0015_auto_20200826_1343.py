# Generated by Django 3.1 on 2020-08-26 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0014_auto_20200826_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='reservation_detail',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='items.reservation'),
        ),
    ]