# Generated by Django 4.1.5 on 2023-02-07 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactions",
            name="card",
            field=models.TextField(max_length=12),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="cpf",
            field=models.TextField(max_length=11),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="date",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="hour",
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="name",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="owner",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="value",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
