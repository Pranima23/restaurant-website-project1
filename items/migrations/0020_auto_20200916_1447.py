# Generated by Django 3.1 on 2020-09-16 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20200827_2239'),
        ('items', '0019_auto_20200827_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='order',
            name='reservation_detail',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.customer'),
        ),
        migrations.AlterField(
            model_name='item',
            name='about_item',
            field=models.TextField(blank=True, default='', max_length=200, null=True),
        ),
    ]
