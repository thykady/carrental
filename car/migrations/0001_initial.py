# Generated by Django 4.2.7 on 2023-11-09 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carmodel', '0001_initial'),
        ('carmark', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(default='default_image.jpg', upload_to='car_images/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carmark.brand')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carmodel.model')),
            ],
        ),
    ]
