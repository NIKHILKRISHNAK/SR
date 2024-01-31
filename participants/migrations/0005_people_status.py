# Generated by Django 4.2.1 on 2024-01-10 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0004_alter_people_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Finished', 'Finished'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50),
        ),
    ]