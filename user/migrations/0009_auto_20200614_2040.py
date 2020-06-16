# Generated by Django 3.0.7 on 2020-06-14 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20200613_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='house',
            name='img',
            field=models.ImageField(upload_to='house_id/'),
        ),
        migrations.AlterField(
            model_name='room',
            name='img',
            field=models.ImageField(upload_to='room_id/'),
        ),
    ]