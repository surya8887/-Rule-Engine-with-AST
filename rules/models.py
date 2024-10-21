from django.db import models

class Rule(models.Model):
    rule_name = models.CharField(max_length=100, unique=True, default='Unnamed Rule')  # Add default value
    rule_string = models.TextField()

    def __str__(self):
        return self.rule_name
