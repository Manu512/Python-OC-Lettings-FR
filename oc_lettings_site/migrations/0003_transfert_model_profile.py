# Generated by Django 3.0 on 2021-08-23 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_transfert_model_lettings'),
    ]

    database_operations = [migrations.AlterModelTable('Profile', 'profiles_profile'),
                           ]

    state_operations = [migrations.DeleteModel('Profile'),
                        ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]
