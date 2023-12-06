# Generated by Django 4.2.4 on 2023-12-06 00:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("gestorVehiculos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tipo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="vehiculo",
            name="tipo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="gestorVehiculos.tipo"
            ),
        ),
    ]