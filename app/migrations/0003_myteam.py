# Generated by Django 4.1.3 on 2022-12-03 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players', models.ManyToManyField(to='app.player')),
            ],
        ),
    ]