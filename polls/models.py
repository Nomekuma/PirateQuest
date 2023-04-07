from django.db import models
class Save(models.Model):
    max_level = models.TextField(blank=True, null=True)  # This field type is a guess.
    max_health = models.TextField(blank=True, null=True)  # This field type is a guess.
    cur_health = models.TextField(blank=True, null=True)  # This field type is a guess.
    coins = models.TextField(blank=True, null=True)  # This field type is a guess.
    # name = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'save'


