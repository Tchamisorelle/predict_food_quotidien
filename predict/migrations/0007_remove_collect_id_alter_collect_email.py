# Generated by Django 4.2.1 on 2023-06-03 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0006_alter_collect_boisson_alter_collect_fruit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collect',
            name='id',
        ),
        migrations.AlterField(
            model_name='collect',
            name='email',
            field=models.EmailField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]