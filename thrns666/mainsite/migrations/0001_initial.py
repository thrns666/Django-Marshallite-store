# Generated by Django 4.2.1 on 2023-06-21 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=115)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('contacts', models.CharField(blank=True, max_length=150)),
                ('photo', models.ImageField(upload_to='photos/%y/')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('main_cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainsite.maincategory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=115)),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%y/')),
                ('price', models.CharField(default='0', max_length=20)),
                ('availability', models.BooleanField(default=True)),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mainsite.subcategories')),
            ],
        ),
    ]
