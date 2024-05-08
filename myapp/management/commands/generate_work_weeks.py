from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from myapp.models import WorkWeek

class Command(BaseCommand):
    help = 'Generate work weeks for the given year'

    def add_arguments(self, parser):
        parser.add_argument('year', type=int, help='The year for which to generate work weeks')

    def handle(self, *args, **options):
        year = options['year']
        start_date = datetime(year, 1, 1)
        end_date = datetime(year, 12, 31)

        current_date = start_date - timedelta(days=start_date.weekday())  # Start from the previous Monday
        week_number = 1

        while True:
            start_day = current_date
            end_day = start_day + timedelta(days=4)  # Adjust if needed (e.g., for weekends)

            if start_day.year == year:
                WorkWeek.objects.create(
                    year=year,
                    week_number=week_number,
                    start_date=start_day,
                    end_date=end_day
                )
                week_number += 1

            if end_day > end_date:
                break

            current_date += timedelta(days=7)

        self.stdout.write(self.style.SUCCESS('Work weeks generated successfully for %s' % year))