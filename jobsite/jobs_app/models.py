from django.db.models import(
    Model,
    TextField,
)

# Create your models here.
class JobListing(Model):
    title = TextField(null=True, blank=True)
    description = TextField(null=True, blank=True)

class CandidatesProfile(Model):
    specializationinProfession = TextField(null=True, blank=True)
    description = TextField(null=True, blank=True)
    experience = TextField(null=True, blank=True)

class SkillSetTrainingModules(Model):
    technology = TextField(null=True, blank=True)
    description = TextField(null=True, blank=True)
    courseDuration = TextField(null=True, blank=True)
    price = TextField(null=True, blank=True)

