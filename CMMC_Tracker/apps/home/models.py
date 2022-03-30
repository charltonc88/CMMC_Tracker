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
)

FAMILY_CHOICES = (
    ("access_control", "Access Control (AC)"),
    ("identification_and_authentication", "Identification and Authentication (IDA)"),
    ("media_protection", "Media Protection (MP)"),
    ("physical_protection", "Physical Protection (PP)"),
    ("system_and_communications_protection", "System and Communications Protection (SCP)"),
    ("system_and_information_integrity", "System and Information Integrity (SII)"),
    ("awareness_and_training", "Awareness and Training (AT)"),
    ("audit_and_accountability", "Audit and Accountability (AA)"),
    ("secureity_assessment", "Security Assessment (SAS)"),
    ("configuration_management", "Configuration Management (CM)"),
    ("incident_response", "Incident Response (IA)"),
    ("maintenance", "Maintenance (MA)"),
    ("personnel_security", "Personnel Security (PS)"),
    ("recovery", "Recovery (RE)"),
    ("risk_management", "Risk Management (RM)"),
    ("asset_management", "Asset Management (AM)"),
)

STATUS_CHOICES = (
    ("non-compliant", "Non-Compliant"),
    ("compliant", "Compliant"),
    ("non-applicable", "Non-Applicable"),
)

class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    cui_description = models.CharField(max_length=500)
    level = models.CharField(
        max_length=3,
        choices = LEVEL_CHOICES,
        default = '2'
    )



class Controls(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    control_id = models.CharField(max_length=15)
    level = models.CharField(
        max_length=3,
        choices = LEVEL_CHOICES,
        default = '2'
    )
    family = models.CharField(
        max_length=100,
        choices = FAMILY_CHOICES,
        default = 'asset_management'
    )
    description = models.CharField(max_length=500)
    status = models.CharField(
        max_length=25,
        choices = STATUS_CHOICES,
        default = 'Non-Compliant'
    )
    notes = models.CharField(max_length=500)

    def __str__(self):
        return self.control_id

class Users(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

