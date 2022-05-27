from django.core.management.base import BaseCommand, CommandError
import os
import sys
from django.template import TemplateDoesNotExist
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.template import loader
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ValidationError


PW_RESET_TEMPLATE = ('users/password_reset/signup_email.html')
PW_RESET_SUBJECT = 'users/password_reset/subject.txt'
PW_RESET_EMAIL = 'users/password_reset/email.html'


class PasswordResetForm(forms.Form):

    error_messages = {
        'unknown': _("That email address doesn't have an associated user account. Are you sure you've registered?"),
        'unusable': _("The user account associated with this email address cannot reset the password."),
    }
    email = forms.EmailField(label=_("Email"), max_length=254)
 
    def clean_email(self):
        """
        Validates that an active user exists with the given email address.
        """
        UserModel = get_user_model()
        email = self.cleaned_data["email"]
        self.users_cache = UserModel._default_manager.filter(email__iexact=email)
        if not len(self.users_cache):
          raise forms.ValidationError(self.error_messages['unknown'])
        if not any(user.is_active for user in self.users_cache):
          raise forms.ValidationError(self.error_messages['unknown'])
        return email
 
    def save(self,  name=None, subject_template_name=PW_RESET_SUBJECT, email_template_name=PW_RESET_EMAIL, token_generator=default_token_generator, from_email=None):
        """
        Generates a one-use only link for resetting password and sends to the user.
        """
        for user in self.users_cache:
            
            domain = 'lacomer.finkok.com'
            site_name = 'La Comer'
            protocol = 'https'
            name = 'FRIENDS'

            c = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': urlsafe_base64_encode(str(user.id)),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': protocol,
                'name': name,
            }
            subject = loader.render_to_string(subject_template_name, c)
            subject = ''.join(subject.splitlines())
            email = loader.render_to_string(email_template_name, c)
            send_mail(subject, email, from_email, [user.email])


class Command(BaseCommand):

	help = 'Creates Users based on a input csv'

	def add_arguments(self, parser):
		parser.add_argument('csv_file', type=str)

	def handle(self, *args, **options):

		user_lst = []
		csv_file = options['csv_file']
		try:
			#import pdb; pdb.set_trace()
			csv = open(options['csv_file'], 'r')
			count = 0
			for line in csv.readlines():
				line = line.strip()
				user_lst.append([col.strip() for col in line.split(',')])
				count += 1
				print '\r%s: %s lines read.' % (csv_file, count)
			csv.close()
		except Exception, e:
			print str(e)
			raise e

		#import pdb; pdb.set_trace()
		for u in user_lst:
			try:
				validate_email(u[2])
			except:
				print "Skipping User1: %s %s, %s Invalid Email Address" % (u[0], u[1], u[2])
				continue
			user, created = User.objects.get_or_create(email=u[2])
			u.append(str(created))
			success = False
			if True or created:
				print "Adding User: %s %s, %s" % (u[0], u[1], u[2])
				user.first_name = u[0]
				user.last_name = u[1]
				user.username = u[2]
				user.set_unusable_password()
				user.profile.role = 'S'
				user.profile.save()
				try:
					user.save()
					print 'Success!'
					success = True
					u.append('True')
				except:
					print 'Error!'
					u.append('False')
			else:
				print "Skipping User2: %s %s, %s Alredy Registered" % (u[0], u[1], u[2])

			if success:
				try:
					reset_password(email=u[2], from_email=settings.SMTP_FROM_EMAIL, name=u[0])
					email = True
					print 'Email success.'
				except Exception, e:
					email = False
					print 'Email failure. %s' % str(e)
				u.append(str(email))



def reset_password(email, from_email, name=None):
  """
  Reset the password for all (active) users with given E-Mail address
  """
  form = PasswordResetForm({'email': email})
  form.is_valid()

  return form.save(
  	from_email=from_email,
    name=name,
   )