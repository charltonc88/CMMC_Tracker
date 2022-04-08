# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from sys import maxsize
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

LEVEL_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)


FAMILY_CHOICES = (
    ("Access Control (AC)", "Access Control (AC)"),
    ("Identification and Authentication (IDA)", "Identification and Authentication (IDA)"),
    ("Media Protection (MP)", "Media Protection (MP)"),
    ("Physical Protection (PP)", "Physical Protection (PP)"),
    ("System and Communications Protection (SCP)", "System and Communications Protection (SCP)"),
    ("System and Information Integrity (SII)", "System and Information Integrity (SII)"),
    ("Awareness and Training (AT)", "Awareness and Training (AT)"),
    ("Audit and Accountability (AA)", "Audit and Accountability (AA)"),
    ("Security Assessment (SAS)", "Security Assessment (SAS)"),
    ("Configuration Management (CM)", "Configuration Management (CM)"),
    ("Incident Response (IA)", "Incident Response (IA)"),
    ("Maintenance (MA)", "Maintenance (MA)"),
    ("Personnel Security (PS)", "Personnel Security (PS)"),
    ("Recovery (RE)", "Recovery (RE)"),
    ("Risk Management (RM)", "Risk Management (RM)"),
    ("Asset Management (AM)", "Asset Management (AM)"),
    ("Situational Awareness (SA)","Situational Awareness (SA)"),
)

STATUS_CHOICES = (
    ("Non-Compliant", "Non-Compliant"),
    ("Compliant", "Compliant"),
    ("Non-Applicable", "Non-Applicable"),
)


class Organization(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, default = None)
    description = models.CharField(max_length=500, default = None)
    cui_description = models.CharField(max_length=500, default = None)
    level = models.CharField(
        max_length=3,
        choices = LEVEL_CHOICES,
        default = '3'
    )

    def __str__(self):
        return self.name



class Control(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default = None)
    control_id = models.CharField(max_length=15, default = None)
    level = models.CharField(
        max_length=3,
        choices = LEVEL_CHOICES,
        default = '3'
    )
    family = models.CharField(
        max_length=100,
        choices = FAMILY_CHOICES,
        default = None
    )
    description = models.CharField(max_length=500, default = None)
    status = models.CharField(
        max_length=25,
        choices = STATUS_CHOICES,
        default = 'Non-Compliant'
    )
    notes = models.CharField(max_length=500, default = None)

    def __str__(self):
        return self.control_id

    def get_status(self):
        return self.status
    
    def get_choices(self):
        return STATUS_CHOICES


class Users(models.Model):
     organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default = None)
     username = models.CharField(max_length=50, default = None)
     password = models.CharField(max_length=30, default = None)
     email = models.CharField(max_length=50, default = None)

     def __str__(self):
         return self.username
