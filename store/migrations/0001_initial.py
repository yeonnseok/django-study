# Generated by Django 3.0.7 on 2020-06-20 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('stock_quantity', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='store.Author')),
            ],
        ),
        migrations.CreateModel(
            name='MemberBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='store.Book')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='accounts.Member')),
            ],
        ),
    ]
