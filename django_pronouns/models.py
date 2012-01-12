from django.db import models

class Pronoun(models.Model):
    name = models.CharField(max_length='30')
    description = models.CharField(max_length=256)

    subject = models.CharField(max_length='10', help_text="He, she, it")
    object = models.CharField(max_length='10', help_text="Her, him, it")
    reflexive = models.CharField(max_length='15', help_text="Itself, himself, herself")
    possessive_pronoun = models.CharField(max_length='10', help_text="Hers, his, its")
    possessive_determiner = models.CharField(max_length='10', help_text="His, her, its")

    def she_he(self): return self.subject
    def he_she(self): return self.subject
    def em(self): return self.subject

    def him_her(self): return self.object
    def her_him(self): return self.object
    def ey(self): return self.object

    def himself_herself(self): return self.reflexive
    def herself_himself(self): return self.reflexive
    def emself(self): return self.reflexive

    def his_hers(self): return self.possessive_pronoun
    def hers_his(self): return self.possessive_pronoun
    def eir(self): return self.possessive_pronoun

    def his_her(self): return self.possessive_determiner
    def her_his(self): return self.possessive_determiner
    def eirs(self): return self.possessive_determiner

    def __unicode__(self):
        return self.name
