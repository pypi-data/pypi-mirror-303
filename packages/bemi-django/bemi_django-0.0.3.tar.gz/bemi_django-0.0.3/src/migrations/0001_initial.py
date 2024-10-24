from django.db import migrations
from bemi import Bemi

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.RunSQL(
            sql=Bemi.migration_up_sql,
            reverse_sql=Bemi.migration_down_sql
        ),
    ]
