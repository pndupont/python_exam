from django.db import models

class JobManager(models.Manager):
    def validator(self, postData):
        errors = {}
        
        if len(postData['title']) == 0:
            errors['title'] = 'Job title cannot be blank'
        if len(postData['title']) < 3 and len(postData['title']) != 0:
            errors['title'] = 'Job title too short (must be at least 3 characters)'

        if len(postData['description']) == 0:
            errors['description'] = 'Job description cannot be blank'
        if len(postData['description']) < 3 and len(postData['description']) != 0:
            errors['description'] = 'job Description too short (must be at least 3 characters)'

        if len(postData['location']) == 0:
            errors['location'] = 'Job location cannot be blank'
        if len(postData['location']) < 3 and len(postData['location']) != 0:
            errors['location'] = 'location too short (must be at least 3 characters)'

        return errors


class Job(models.Model):
    job_poster = models.ForeignKey('login.User', related_name="posted_jobs")
    title = models.CharField(max_length=255)
    description = models.TextField(null=False)
    location = models.TextField(max_length=255)
    job_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # assuming all jobs are co-operative so many users may take on the same job (like the likes with the quote assignment)
    users = models.ManyToManyField('login.User', related_name='jobs')
    objects = JobManager()
    def __repr__(self):
        return f'Quote Object: ID:({self.id}) Job_poster:{self.job_poster} title:{self.title} description:{self.description} Created At:{self.created_at} Updated At:{self.updated_at} Users: {self.users}'

