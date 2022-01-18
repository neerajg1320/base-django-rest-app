import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database ...')
        connected = False
        db_conn = None
        while not connected:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Connection Error: Database unavailable, waiting 1 second')
                time.sleep(1)

            if db_conn:
                try:
                    cursor = db_conn.cursor()

                    # Mark the database connected
                    connected = True

                    cursor.close()
                    db_conn.close()
                except OperationalError:
                    self.stdout.write('Cursor Error: Database unavailable, waiting 1 second')
                    time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
