# Generated by Django 4.1.7 on 2023-03-21 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('questions', models.JSONField()),
                ('form_id', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.JSONField()),
                ('form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.form')),
            ],
        ),
    ]
