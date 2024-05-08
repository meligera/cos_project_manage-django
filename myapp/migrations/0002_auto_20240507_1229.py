from datetime import datetime
from django.db import migrations, connection
from myapp.models import Project

def load_projects_data(apps, schema_editor):
    # Load data from your PostgreSQL database here
    sql = """
        SELECT id, activity, stage, status, basis, representive, foreigh_manager, analytic, creation_date, modify_date
        FROM projects
    """
    with connection.cursor() as cursor:
        cursor.execute(sql)
        projects_data = [(
            row[0], row[1], row[2], row[3], row[4],
            row[5] if row[5] else '',  # Replace NULL with an empty string
            row[6], row[7],
            datetime.strptime(row[8], '%d.%m.%Y').date() if row[8] else None,  # Convert creation_date
            datetime.strptime(row[9], '%d.%m.%Y').date() if row[9] else None,  # Convert modify_date
        ) for row in cursor.fetchall()]

    Project.objects.bulk_create([
        Project(
            id=id,
            activity=activity,
            stage=stage,
            status=status,
            basis=basis,
            representive=representive,
            foreigh_manager=foreigh_manager,
            analytic=analytic,
            creation_date=creation_date,
        )
        for id, activity, stage, status, basis, representive, foreigh_manager, analytic, creation_date, modify_date in projects_data
    ])

def unload_projects_data(apps, schema_editor):
    Project.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0001_initial'),  # Replace with the actual previous migration
    ]

    operations = [
        migrations.RunPython(load_projects_data, reverse_code=unload_projects_data),
    ]