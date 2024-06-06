# Generated by Django 5.0.6 on 2024-06-06 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('publicado_em', models.DateField()),
                ('isbn', models.CharField(max_length=13, unique=True)),
            ],
        ),
    ]