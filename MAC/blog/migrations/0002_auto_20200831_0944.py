# Generated by Django 3.1 on 2020-08-31 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='chead0',
            field=models.CharField(default='', max_length=5000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead1',
            field=models.CharField(default='  ', max_length=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chead2',
            field=models.CharField(default=1, max_length=3000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head0',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head1',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='head2',
            field=models.CharField(max_length=50),
        ),
    ]