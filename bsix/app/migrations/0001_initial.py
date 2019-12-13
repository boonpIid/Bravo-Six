# Generated by Django 3.0 on 2019-12-13 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BenefitProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('info', models.TextField(max_length=65535)),
                ('baseForm', models.CharField(max_length=255)),
                ('applicationForm', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.ApplicationForm')),
                ('requirements', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.Requirements')),
            ],
        ),
    ]