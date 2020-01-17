# Generated by Django 2.2.7 on 2019-11-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id_color', models.AutoField(primary_key=True, serialize=False)),
                ('color_name', models.CharField(max_length=45)),
                ('price_coef', models.IntegerField(default=None, null=True)),
            ],
        ),
    ]
