# Generated by Django 5.0.4 on 2024-06-13 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mother', '0006_mother_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='meal_images_path',
            field=models.CharField(blank=True, choices=[('meat', 'images/meat.jpg'), ('milk', 'images/milk.jpg'), ('sandwich', 'images/sandwich.jpg'), ('nuggets', 'images/nuggets.jpg'), ('burger', 'images/burger.jpg'), ('pasta', 'images/pasta.jpg'), ('pie', 'images/pie.jpg'), ('pizza', 'images/pizza.jpg'), ('pancake', 'images/pancake.jpg'), ('waffle', 'images/waffle.jpg')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='child',
            name='meal',
            field=models.CharField(blank=True, choices=[('meat', 'meat'), ('milk', 'milk'), ('sandwich', 'sandwich'), ('nuggets', 'nuggets'), ('burger', 'burger'), ('pasta', 'pasta'), ('pie', 'pie'), ('pizza', 'pizza'), ('pancake', 'pancake'), ('waffle', 'waffle')], max_length=200, null=True),
        ),
    ]