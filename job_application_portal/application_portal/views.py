from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
from django.db import IntegrityError, transaction
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm, ApplicantDetailsForm, AttachmentsForm, EducationForm
from .models import applicant_details, application_attachment, applicant_education

# Account registration view
# Successful account registration will send an email acknowledgement to user
class registerView(View):
    template_name = 'account/register.html'
    form_class = RegistrationForm
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('details')

        # Display the register form
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        # Check if values submitted is valid
        if form.is_valid():
            form.save()
            # Sends an email confirmation to user
            # This will send an email which is visible in both html-capable browsers 
            # and will show plain text for accessibility purposes.

            html_message = render_to_string('account/confirmation_email.html', {
                'recipient': form.cleaned_data['first_name'],
                'login_link': 'http://localhost:8000/login'
            })

            # Generate raw message from html email
            raw_message = strip_tags(html_message)

            # Send email
            send_mail(
                'Welcome! Log-in using your new account',
                raw_message,
                None,
                recipient_list=[form.cleaned_data['email'],],
                html_message=html_message,
                fail_silently=False,
            )

            return redirect('thank_you')

        return render(request, self.template_name, {'form': form})

# Account login view
# Successful login redirects the user to the main details page
class loginView(View):
    template_name = 'account/login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('details')

        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request, data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return redirect('details')
        return render(request, self.template_name, {'form': form})

# Log out user
def logoutView(request):
    template = 'account/logout.html'
    logout(request)
    return render(request, template)

# Shows a message that tells the user that a confirmation email is sent 
# to the specified email address
class messageView(View):
    template_name = 'account/thank_you.html'
    message = 'An email confirmation was sent your email. Yay.'

    def get(self, request):
        return render(request, self.template_name, {'message': self.message})

# This view asks additional datails of the user. 
# It also displays education and attachments formsets
@login_required
def detailsView(request):
    template_name = 'account/details.html'

    # Main details form
    detailsForm = ApplicantDetailsForm

    # Instantiate inline formsets 
    education_inline_formset = inlineformset_factory(User, applicant_education, form=EducationForm, extra=0, min_num=1)
    attachments_inline_formset = inlineformset_factory(User, application_attachment, form=AttachmentsForm, extra=0, min_num=1)

    user = request.user
    user_instance = get_object_or_404(User, pk=user.id)

    try:
        details_instance = applicant_details.objects.get(user=user)
    except ObjectDoesNotExist:
        details_instance = None

    if request.method == 'POST':
        # Validate all fields from main details form and inline formsets
        details_form = detailsForm(request.POST, instance=details_instance)
        education_formset = education_inline_formset(request.POST, instance=user_instance, prefix='fs1')
        attachments_formset = attachments_inline_formset(request.POST, request.FILES, instance=user_instance, prefix='fs2')

        # Check if valid
        if details_form.is_valid() and education_formset.is_valid() and attachments_formset.is_valid():
            if not details_instance:
                # Link logged in user to the saved details object
                details_form.instance.user = user

                # Send acknowledgement email to user
                # Prepare the html message
                html_message = render_to_string('account/acknowledgement_email.html', {
                    'recipient': user_instance.first_name,
                })

                # Generate raw message from html message
                raw_message = strip_tags(html_message)

                # Send email
                send_mail(
                    'Profile acknowledgement reciept',
                    raw_message,
                    None,
                    recipient_list=[user_instance.email,],
                    html_message=html_message,
                    fail_silently=False,
                )
                messages.success(request, 'Profile submitted.', extra_tags='html_safe alert alert-success')
            else:
                messages.success(request, 'You have updated your profile.', extra_tags='html_safe alert alert-success')

            # All is well, save the data
            details_form.save()
            education_formset.save()
            attachments_formset.save()

            return redirect('submit')
        else:
            # If the transaction failed notify user
            messages.error(request, 'There was an error saving your profile.', extra_tags='html_safe alert alert-danger')

    else:
        # Instantiate forms and formsets (for GET requests)
        details_form = detailsForm(instance=details_instance)
        education_formset = education_inline_formset(instance=user_instance, prefix='fs1')
        attachments_formset = attachments_inline_formset(instance=user_instance, prefix='fs2')

    
    context = {
        'form': details_form,
        'education_formset': education_formset,
        'attachments_formset': attachments_formset
    }
    return render(request, template_name, context)

@login_required
def submitView(request):
    template_name = 'account/submit.html'
    return render(request, template_name)
            
            




