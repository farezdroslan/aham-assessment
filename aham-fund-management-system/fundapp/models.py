from django.db import models
from django.utils import timezone

# Create your models here.
class Manager(models.Model):
    """
    Represents a fund manager.
    """
    manager_id = models.AutoField(primary_key=True)  # Unique identifier for the manager
    manager_name = models.CharField(max_length=255, null=False, blank=False)  # Name of the manager
    manager_bio = models.TextField(null=True, blank=True)  # Biography or description of the manager


class Fund(models.Model):
    """
    Represents an investment fund in the database.
    """
    fund_id = models.AutoField(primary_key=True)  # Unique identifier for the fund
    fund_name = models.CharField(max_length=255, null=False, blank=False)  # Name of the fund
    # fund_manager_name = models.CharField(max_length=255, null=False, blank=False)  # Name of the fund manager
    fund_manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='funds', null=True, blank=True)  # Foreign key to Manager
    fund_description = models.TextField(null=False, blank=False)  # Description of the fund
    nav = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)  # Net Asset Value (NAV)
    date_of_creation = models.DateField(default=timezone.now)  # Date when the fund was created
    performance = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)  # Performance as a percentage

# Investor Model
class Investor(models.Model):
    """
    Represents an investor who invests in funds.
    """
    investor_id = models.AutoField(primary_key=True)  # Unique identifier for the investor
    investor_name = models.CharField(max_length=255, null=False, blank=False)  # Name of the investor
    investor_email = models.EmailField(unique=True, null=False, blank=False)  # Email address of the investor

# Investment Model
class Investment(models.Model):
    """
    Tracks which investors have invested in which funds and the amount invested.
    """
    investment_id = models.AutoField(primary_key=True)  # Unique identifier for the investment
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE, related_name='investments')  # Foreign key to Investor
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE, related_name='investments')  # Foreign key to Fund
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)  # Amount invested
    investment_date = models.DateField(default=timezone.now)  # Date when the investment was made