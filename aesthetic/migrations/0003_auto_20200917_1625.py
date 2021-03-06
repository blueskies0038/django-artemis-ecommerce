# Generated by Django 3.0.8 on 2020-09-17 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aesthetic', '0002_auto_20200914_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionimage',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='aesthetic.Collection'),
        ),
        migrations.AlterField(
            model_name='collectionimage',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name='CollectionPreview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preview_images', to='aesthetic.Collection')),
            ],
        ),
    ]
