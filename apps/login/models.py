from django.db import models
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First Name too short'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last Name too short'

        try:
            validate_email( postData['email'] )
        except ValidationError:
            errors['email'] = 'Please enter a valid email address'

        all_users = User.objects.all()
        for u in all_users:
            if(postData['email'] == u.email):
                errors['email'] = 'Email address already in use'

        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long'
        if postData['password'] != postData['retype_password']:
            errors['retype_password'] = 'Passwords must match'

        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return f'User Object: ID:({self.id}) first_name:{self.first_name} last_name:{self.last_name} email:{self.email} password:{self.password} Created At:{self.created_at} Updated At:{self.updated_at}'

