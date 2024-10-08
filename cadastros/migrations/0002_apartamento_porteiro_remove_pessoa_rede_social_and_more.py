# Generated by Django 4.2.13 on 2024-07-08 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cadastros", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Apartamento",
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
                ("numero", models.IntegerField()),
                ("bloco", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Porteiro",
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
                ("nome", models.CharField(max_length=150)),
                ("turno", models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name="pessoa",
            name="rede_social",
        ),
        migrations.RemoveField(
            model_name="pessoa",
            name="salario",
        ),
        migrations.CreateModel(
            name="Visita",
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
                ("motivo", models.CharField(max_length=255)),
                ("data_hora_entrada", models.DateTimeField()),
                ("data_hora_saida", models.DateTimeField(blank=True, null=True)),
                (
                    "visita",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cadastros.pessoa",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Morador",
            fields=[
                (
                    "pessoa_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="cadastros.pessoa",
                    ),
                ),
                ("possui_animais", models.BooleanField(default=False)),
                (
                    "apartamento",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="morador",
                        to="cadastros.apartamento",
                    ),
                ),
            ],
            bases=("cadastros.pessoa",),
        ),
        migrations.CreateModel(
            name="Carro",
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
                ("placa", models.CharField(max_length=10)),
                ("modelo", models.CharField(max_length=50)),
                ("cor", models.CharField(max_length=20)),
                (
                    "apartamento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="carros",
                        to="cadastros.apartamento",
                    ),
                ),
            ],
        ),
    ]
