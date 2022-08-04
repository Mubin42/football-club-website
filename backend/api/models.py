from django.db import models

# Create your models here.
class Player(models.Model):
    POSITION_CHOICE_GOALKEEPER = 'G'
    POSITION_CHOICE_DEFENDER   = 'D'
    POSITION_CHOICE_MIDFIELDER = 'M'
    POSITION_CHOICE_ATTACKER   = 'A'
    
    POSITION_CHOICE = [
        (POSITION_CHOICE_GOALKEEPER, 'Goalkeeper'),
        (POSITION_CHOICE_DEFENDER,   'Defender'),
        (POSITION_CHOICE_MIDFIELDER, 'Midfielder'),
        (POSITION_CHOICE_ATTACKER,    'Attacker'),
    ]

    CONTRACT_STATUS_FIRST_TEAM = 'F'
    CONTRACT_STATUS_SUBSTITUTE = 'S'
    CONTRACT_STATUS_BENCH      = 'B'
    CONTRACT_STATUS_ACADEMIY   = 'A'
    CONTRACT_STATUS_UNDEFINED  = 'U'


    CONTRACT_STATUS = [
        (CONTRACT_STATUS_FIRST_TEAM, 'First Team'),
        (CONTRACT_STATUS_SUBSTITUTE, 'Substitue'),
        (CONTRACT_STATUS_BENCH,      'Bench'),
        (CONTRACT_STATUS_ACADEMIY,   'Academy'),
        (CONTRACT_STATUS_UNDEFINED,  'Undefined'),
    ]

    name            = models.CharField(max_length=255)
    nationality     = models.CharField(max_length=255)
    age             = models.IntegerField()
    date_of_birth   = models.DateField()
    position        = models.CharField(max_length=1, choices=POSITION_CHOICE)
    player_salary   = models.IntegerField()
    contract_status = models.CharField(max_length=1, choices=CONTRACT_STATUS)

class Coach(models.Model):
    pass

class Staff(models.Model):
    pass

class User(models.Model):
    pass

class Merch(models.Model):
    title = models.CharField(max_length=255)
    inventory = models.IntegerField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    description = models.TextField()