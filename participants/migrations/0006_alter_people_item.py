# Generated by Django 4.2.1 on 2024-03-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0005_people_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='item',
            field=models.CharField(choices=[('Song', 'Song'), ('Dance', 'Dance'), ('Skit', 'Skit'), ('Mimicry', 'Mimicry'), ('Mono Act', 'Mono Act'), ('Thiruvathira', 'Thiruvathira')], max_length=50),
        ),
    ]
