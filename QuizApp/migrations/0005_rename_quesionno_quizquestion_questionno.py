# Generated by Django 3.2.8 on 2021-10-31 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuizApp', '0004_remove_quizquestion_currentques'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizquestion',
            old_name='quesionNo',
            new_name='questionNo',
        ),
    ]
