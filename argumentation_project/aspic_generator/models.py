from django.db import models

class Literal(models.Model):
    name = models.CharField(max_length=100)
    is_negative = models.BooleanField()

    def __str__(self):
        return f"¬{self.name}" if self.is_negative else self.name

class Rule(models.Model):
    premises = models.ManyToManyField(Literal, related_name='premises')
    conclusion = models.ForeignKey(Literal, on_delete=models.CASCADE, related_name='conclusion')
    is_defeasible = models.BooleanField()
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        premises_str = ', '.join(str(literal) for literal in self.premises.all())
        return f"{self.name}: {premises_str} ⇒ {self.conclusion}"

class Argument(models.Model):
    top_rule = models.ForeignKey(Rule, on_delete=models.CASCADE, related_name='top_rule')
    sub_arguments = models.ManyToManyField('self', symmetrical=False, blank=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
