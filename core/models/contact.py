from django.db import models

# contact information related models 
# it contain company data 
# 
class Contact(models.Model):
   
    company_name = models.CharField(max_length=255, default="", blank=True) 
    webiste = models.CharField(max_length=255, default="", blank=True)
    ger_email = models.EmailField(max_length=255, default="", blank=True)
    billing_email = models.EmailField(max_length=255, default="", blank=True)
    street = models.CharField(max_length=255, default="", blank=True)
    suite = models.CharField(max_length=255, default="", blank=True)
    city = models.CharField(max_length=255, default="", blank=True)
    state = models.CharField(max_length=255, default="", blank=True)
    zip = models.IntegerField(default=0, blank=True, null=True)
    plus_4 = models.IntegerField(default=0, blank=True, null=True)
    client_no = models.IntegerField(default=0, blank=True, null=True)
    f_name = models.CharField(max_length=255, default="", blank=True)
    l_name = models.CharField(max_length=255, default="", blank=True)
    dob = models.CharField(max_length=255, default="", blank=True)
    ssn = models.IntegerField(default=0, blank=True, null=True)
    mobile_no = models.IntegerField(default=0, blank=True, null=True)
    home_no = models.IntegerField(default=0, blank=True, null=True)
    office_no = models.IntegerField(default=0, blank=True, null=True)
    fax_no = models.IntegerField(default=0, blank=True, null=True)
    other_no = models.IntegerField(default=0, blank=True, null=True)
    email_1 = models.EmailField(max_length=255, default="", blank=True)
    email_2= models.EmailField(max_length=255, default="", blank=True)
    email_3= models.EmailField(max_length=255, default="", blank=True)
    street2 = models.CharField(max_length=255, default="", blank=True)
    suite2= models.CharField(max_length=255, default="", blank=True)
    city2= models.CharField(max_length=255, default="", blank=True)
    state2= models.CharField(max_length=255, default="", blank=True)
    zip2 = models.IntegerField(default=0, blank=True, null=True)
    plus_42 = models.IntegerField(default=0, blank=True, null=True)
    office= models.CharField(max_length=255, default="", blank=True)
    team= models.CharField(max_length=255, default="", blank=True)
    member= models.CharField(max_length=255, default="", blank=True)
    assign_to= models.CharField(max_length=255, default="", blank=True)
    contact= models.CharField(max_length=255, default="", blank=True)
    relation= models.CharField(max_length=255, default="", blank=True)

