# Generated by Django 4.1.7 on 2023-04-02 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PredResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancies', models.IntegerField()),
                ('glucose', models.FloatField()),
                ('blood_pressure', models.FloatField()),
                ('skin_thickness', models.FloatField()),
                ('insulin', models.FloatField()),
                ('bmi', models.FloatField()),
                ('diabetes_pedigree_function', models.FloatField()),
                ('age', models.IntegerField()),
                ('classification', models.CharField(max_length=30)),
            ],
        ),
    ]
