# Generated by Django 2.1.5 on 2019-01-10 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workedYears', models.FloatField()),
                ('salaryBrutto', models.FloatField(null=True)),
            ],
        ),
    ]
