# Generated by Django 3.1.6 on 2021-02-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('category', models.CharField(choices=[('MEAT', '육류'), ('FISH', '어류'), ('EGG', '난류'), ('MILK', '우유'), ('ETC', '기타')], max_length=4)),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
            },
        ),
    ]
