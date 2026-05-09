from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('fundador', models.CharField(max_length=100)),
                ('data_fundacao', models.DateField()),
                ('animal_simbolo', models.CharField(max_length=100)),
            ],
        ),
    ]
