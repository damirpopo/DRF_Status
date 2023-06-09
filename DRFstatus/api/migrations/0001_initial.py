# Generated by Django 4.1.7 on 2023-03-16 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TitleJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titlejob', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('surname2', models.CharField(max_length=20)),
                ('login', models.CharField(max_length=20)),
                ('photo', models.URLField()),
                ('titleJob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.titlejob')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.IntegerField()),
                ('time_order', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.status')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.workers')),
            ],
        ),
    ]
