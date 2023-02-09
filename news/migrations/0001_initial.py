# Generated by Django 4.1.6 on 2023-02-09 11:39

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
            name="Post",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="uploads/% Y/% m/% d/")),
                (
                    "post_category",
                    models.CharField(
                        choices=[
                            ("BLOCK", "BlockChain News"),
                            ("CRYPT", "Crypto News"),
                            ("PR", "Press Release"),
                        ],
                        default="BLOCK",
                        max_length=5,
                    ),
                ),
                ("content", models.TextField()),
                ("highlighted", models.TextField()),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="snippets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="Comments",
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
                ("email", models.EmailField(max_length=254)),
                ("comment", models.TextField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="news.post",
                    ),
                ),
            ],
            options={
                "ordering": ["-created_on"],
            },
        ),
    ]
