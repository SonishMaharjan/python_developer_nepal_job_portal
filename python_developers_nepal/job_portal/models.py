from django.db import models
from django.conf import settings

# Create your models here.
INTERN_TYPE = [
    ('PAID', 'Paid'),
    ('UNPAID', 'Unpaid')
]

JOB_TYPE = [
    ('PART-TIME', 'Part Time'),
    ('FULL-TIME', 'Full Time'),
    ('FREELANCER', 'Freelancer')
]

JOB_POSITION = [
    ('JUNIOR', 'Junior Level'),
    ('MID', 'Mid Level'),
    ('SENIOR', 'Senior Level')
]


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    profile_description = models.TextField(max_length=2000)
    email = models.CharField(max_length=100)
    company_website = models.CharField(max_length=100, null=True)
    company_logo = models.ImageField(upload_to="company_logo", null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.company_name


class HirePost(models.Model):
    posted_by_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, verbose_name="Company", on_delete=models.CASCADE)
    hire_post_title = models.CharField("Position Title",max_length=255)
    hire_post_description = models.TextField("Position Description",max_length=2000)
    apply_before = models.DateTimeField()
    location = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    salary = models.FloatField(null=True)

    class Meta:
        abstract = True


class InternPost(HirePost):
    intern_type = models.CharField(max_length=50, choices=INTERN_TYPE, default='PAID')

    def __str__(self):
        return self.hire_post_title


class JobPost(HirePost):
    job_type = models.CharField(max_length=50, choices=JOB_TYPE)
    job_position = models.CharField(max_length=50, choices=JOB_POSITION)

    def __str__(self):
        return self.hire_post_title

