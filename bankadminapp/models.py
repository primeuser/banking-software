from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, Permission

USER_ROLES = (
    ('BranchManager', 'BranchManager'),
    ('LoanOfficer', 'LoanOfficer'),
    ('Cashier', 'Cashier')
)

CLIENT_ROLES = (
    ('FirstLeader', 'FirstLeader'),
    ('SecondLeader', 'SecondLeader'),
    ('GroupMember', 'GroupMember')
)

GENDER_TYPES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

ACCOUNT_STATUS = (
    ('Applied', 'Applied'),
    ('Withdrawn', 'Withdrawn'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
    ('Closed', 'Closed'),
)


INTEREST_TYPES = (
    ('Flat', 'Flat'),
    ('Declining', 'Declining'),
)

RECEIPT_TYPES = (
    ('EntranceFee', 'EntranceFee'),
    ('MembershipFee', 'MembershipFee'),
    ('BookFee', 'BookFee'),
    ('LoanProcessingFee', 'LoanProcessingFee'),
    ('SavingsDeposit', 'SavingsDeposit'),
    ('FixedDeposit', 'FixedDeposit'),
    ('RecurringDeposit', 'RecurringDeposit'),
    ('AdditionalSavings', 'AdditionalSavings'),
    ('ShareCapital', 'ShareCapital'),
    ('PeenalInterest', 'PeenalInterest'),
    ('LoanDeposit', 'LoanDeposit'),
    ('Insurance', 'Insurance'),
)

# RD: Recurring Deposit
# FD: Fixed Deposit

FD_RD_STATUS = (
    ('Opened', 'Opened'),
    ('Paid', 'Paid'),
    ('Closed', 'Closed'),
)

PAYMENT_TYPES = (
    ('Loans', 'Loans'),
    ('TravellingAllowance', 'TravellingAllowance'),
    ('Paymentofsalary', 'Paymentofsalary'),
    ('PrintingCharges', 'PrintingCharges'),
    ('StationaryCharges', 'StationaryCharges'),
    ('OtherCharges', 'OtherCharges'),
    ('SavingsWithdrawal', 'SavingsWithdrawal'),
    ('FixedWithdrawal', 'Fixed Deposit Withdrawal'),
    ('RecurringWithdrawal', 'Recurring Deposit Withdrawal'),
)


class Branch(models.Model):
    name = models.CharField(max_length=100, unique=True)
    opening_date = models.DateField()
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=150)
    phone_number = models.BigIntegerField()
    pincode = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name
