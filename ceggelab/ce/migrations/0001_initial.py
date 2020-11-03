# Generated by Django 3.1.3 on 2020-11-03 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name_en', models.CharField(max_length=200)),
                ('student_name_th', models.CharField(max_length=200)),
                ('student_ID', models.IntegerField(default=0)),
                ('student_level', models.CharField(choices=[('M', 'Master programs'), ('D', 'Doctoral programs'), ('P', 'Postdoctorate'), ('R', 'Researcher')], max_length=30)),
            ],
        ),
    ]
