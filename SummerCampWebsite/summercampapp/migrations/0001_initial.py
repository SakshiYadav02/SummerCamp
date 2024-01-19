# Generated by Django 3.1.7 on 2021-06-07 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityEvent',
            fields=[
                ('EventId', models.AutoField(primary_key=True, serialize=False)),
                ('EventName', models.CharField(max_length=100)),
                ('Date', models.CharField(max_length=10)),
                ('City', models.CharField(max_length=50)),
                ('VenuAddress', models.TextField()),
                ('Description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=45)),
                ('Email', models.CharField(max_length=45, null=True)),
                ('Phone', models.CharField(max_length=10)),
                ('Question', models.TextField()),
                ('Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('FeedbackId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=45)),
                ('Email', models.CharField(max_length=45)),
                ('Program_name', models.CharField(max_length=100)),
                ('Date', models.DateField()),
                ('FeedbackText', models.TextField()),
                ('Rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='JobDescription',
            fields=[
                ('JobId', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('PostName', models.CharField(max_length=30)),
                ('NoOfSeats', models.IntegerField()),
                ('LastDateToApply', models.DateField()),
                ('PostDate', models.DateField()),
                ('Description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Program_Management',
            fields=[
                ('Programid', models.AutoField(primary_key=True, serialize=False)),
                ('ProgramName', models.CharField(max_length=100)),
                ('Duration', models.CharField(max_length=20)),
                ('Fees', models.CharField(default='', max_length=30)),
                ('StartDate', models.DateField(default='')),
                ('EndDate', models.DateField(default='')),
                ('Description', models.TextField()),
                ('AgeGroup', models.CharField(max_length=20)),
                ('TeachingMode', models.CharField(max_length=20)),
            ],
        ),
    ]
