# Generated by Django 4.1.6 on 2023-04-11 15:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=300)),
                ('brand', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=300)),
                ('cost', models.FloatField()),
                ('release_date', models.DateField()),
                ('description', models.TextField(max_length=5000)),
                ('averagerating', models.FloatField(default=0)),
                ('photo', models.ImageField(default='default.jpg', upload_to='product_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('comment', models.TextField()),
                ('date_time', models.DateField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_reviews', to='products.product')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
