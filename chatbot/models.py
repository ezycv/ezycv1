from django.db import models

# Create your models here.
class eresume(models.Model):
    name = models.CharField(max_length = 250)
    mobile = models.CharField(max_length = 100 , default = 'NULL')
    elaborate = models.CharField(max_length = 1000, default = 'NULL')
    fblink= models.CharField(max_length = 1000, default = 'NULL')
    description= models.CharField(max_length = 1000, default = 'NULL')
    emailid= models.CharField(max_length = 1000, default = 'NULL')
    state= models.CharField(max_length = 1000, default = 'NULL')
    location = models.CharField(max_length = 250, default = 'NULL')
    twitterlink = models.CharField(max_length = 250, default = 'NULL')
    dob = models.CharField(max_length = 1250, default = 'NULL')
    githublink = models.CharField(max_length = 250, default = 'NULL')
    instagramlink = models.CharField(max_length = 250, default = 'NULL')
    displaypicture = models.CharField(max_length = 250, default = 'NULL')
    work1 = models.CharField(max_length = 1250, default = 'NULL')
    work2 = models.CharField(max_length = 250, default = 'NULL')
    work3 = models.CharField(max_length = 250, default = 'NULL')
    work4 = models.CharField(max_length = 250, default = 'NULL')
    name1 = models.CharField(max_length = 1250, default = 'NULL')
    name2 = models.CharField(max_length = 250, default = 'NULL')
    name3 = models.CharField(max_length = 250, default = 'NULL')
    name4 = models.CharField(max_length = 250, default = 'NULL')
    workdescribe1 = models.CharField(max_length = 1250, default = 'NULL')
    workdescribe2 = models.CharField(max_length = 250, default = 'NULL')
    workdescribe3 = models.CharField(max_length = 250, default = 'NULL')
    workdescribe4 = models.CharField(max_length = 250, default = 'NULL')
    cvlink = models.CharField(max_length = 250, default = 'NULL')
    fbid = models.CharField(max_length = 250 , default = 'NULL')
    i = models.CharField(max_length = 250, default = '0')
    j = models.CharField(max_length = 250, default = '1')
    field = models.CharField(max_length = 250, default = ' ')
    

    def __str__(self):
        return self.fbid

class resume_input(models.Model):
    greetings = models.CharField(max_length = 250)
    state = models.CharField(max_length = 1000)
    city = models.CharField(max_length = 1000)
    dob = models.CharField(max_length = 1000)
    LinkedIn = models.CharField(max_length = 1000)
    fbid= models.CharField(max_length = 1000 )
    name = models.CharField(max_length = 250)
    emailid = models.CharField(max_length = 1000)
    contact = models.CharField(max_length = 100)
    objective_line1 = models.CharField(max_length = 100)
    objective_achievements = models.CharField(max_length = 100)
    educational_qualifications_1 = models.CharField(max_length = 100)
    educational_qualifications_2 = models.CharField(max_length = 100)
    educational_qualifications_3 = models.CharField(max_length = 100)
    educational_qualifications_4 = models.CharField(max_length = 100)
    skills_1 = models.CharField(max_length = 100)
    skills_2 = models.CharField(max_length = 100)
    skills_3 = models.CharField(max_length = 100)
    skills_4 = models.CharField(max_length = 100)
    experience_1 = models.CharField(max_length = 100)
    experience_2 = models.CharField(max_length = 100)
    experience_3 = models.CharField(max_length = 100)
    experience_4 = models.CharField(max_length = 100)
    hobbies_1 = models.CharField(max_length = 100)
    hobbies_2 = models.CharField(max_length = 100)
    hobbies_3 = models.CharField(max_length = 100)
    hobbies_4 = models.CharField(max_length = 100)
    

    def __str__(self):
        return self.fbid