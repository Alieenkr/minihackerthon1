# Generated by Django 2.2 on 2019-05-25 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editorweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=30)),
                ('professor', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Country',
        ),
    ]