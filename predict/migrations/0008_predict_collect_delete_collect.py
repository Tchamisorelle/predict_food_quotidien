# Generated by Django 4.2.1 on 2023-06-05 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0007_remove_collect_id_alter_collect_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='predict_collect',
            fields=[
                ('nom', models.CharField(max_length=30)),
                ('aliment', models.CharField(max_length=50)),
                ('boisson', models.CharField(blank=True, max_length=30, null=True)),
                ('fruit', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'predict_collect',
            },
        ),
        migrations.DeleteModel(
            name='collect',
        ),
    ]
