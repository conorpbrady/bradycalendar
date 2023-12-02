from django.db import models

# Create your models here.

class Event(models.Model):
    event_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    is_anniversary = models.BooleanField(default=False)
    name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64, blank=True, null=True)

    MONTHS = (
            (1, 'January'),
            (2, 'February'),
            (3, 'March'),
            (4, 'April'),
            (5, 'May'),
            (6, 'June'),
            (7, 'July'),
            (8, 'August'),
            (9, 'September'),
            (10, 'October'),
            (11, 'November'),
            (12, 'Decemeber')
            )

    month = models.IntegerField(choices=MONTHS)

    def __str__(self):
        output_string = self.name
        if self.is_anniversary:
            output_string = f'(A) {output_string}'
        return output_string
