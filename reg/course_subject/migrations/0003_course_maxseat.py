# Generated by Django 4.1.1 on 2022-09-10 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_subject', '0002_course_semester_course_state_course_year_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='maxSeat',
            field=models.IntegerField(null=True),
        ),
    ]
