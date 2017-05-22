from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from webapp.models import ScannerDetails, DateDetails, VersionDetails, GradsysDetails, CoilDetails, PhantomDetails, Results, SeriesDetails
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect 
from django.template.context_processors import csrf
from .forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from webapp.tokens import account_activation_token
#def signup(request):
	#if request.method == 'POST': 
#		form = UserCreationForm(request.POST)
#		if form.is_valid():
#			form.save()
#			username = form.cleaned_data.get('username')
#			raw_password = form.cleaned_data.get('password1')
#			user = authenticate(username=username, password=raw_password)
#			login(request, user)
#			return redirect('home')
#		else:
#			form = UserCreationForm()
#		return render(request, 'webapp/signup.html', {'form': form})
#
		#form = UserCreationForm(request.POST)
		#if form.is_valid():
			#form.save()
			#username = form.cleaned_data.get('username')
			#raw_password = form.cleaned_data.get('passwo#rd1')
			#user = authenticate(username=username, password=raw_password)
			#login(request, user)
			#return redirect('/')
	#	else:
	#		form = UserCreationForm()
	#		return render(request, 'accounts/signup.html', {'form': form})


def register(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			subject = 'Activate your MrqqaDB Account'
			message = render_to_string('registration/account_activation_email.html', {
				'user':user,
				'domain': current_site.domain,
				'uid' : urlsafe_base64_encode(force_bytes(user.pk)),	
				'token': account_activation_token.make_token(user),})
			user.email_user(subject, message)
			return redirect('registration/account_activation_sent')

	else:
		form = SignUpForm()

	return render(request, 'registration/signup.html', {'form': form})

def registration_complete(request):
	return render_to_response('registration/registration_complete.html')

def account_activation_sent(request):
	return render_to_response('registration/account_activation_sent.html') 

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.profile.email_confirmed = True
		user.save()
		login(request, user)
		return redirect('/')
	else:
		return render(request, 'account_activation_invalid.html')

def account_activation_invalid(request):
	return render_to_response('registration/account_activation_invalid.html') 

@login_required
def home_page(request):
	scanner_list = ScannerDetails.objects.values()
	context = {"scanner_list": scanner_list}
	return render(request,'webapp/home_page.html', context)

@login_required
def get_dates(request):
	query = request.GET.get('scanner_id')
	try:
		query = int(query)
	except ValueError:
		query = None
		results = None 

	if query:
		scanner_dates = DateDetails.objects.select_related().filter(scanner__scanner_id=query).values()
	
		scanner_notes = ScannerDetails.objects.filter(scanner_id=query).values()
		context = {"scanner_dates":scanner_dates, "scanner_notes":scanner_notes }
	return render(request, 'webapp/scanner_dates.html', context) 

@login_required
def date_to_results(request):
	query = request.GET.get('date_id')
	try:
		query = int(query)
	except ValueError:
		query = None
		results = None
	if query: 
		results = Results.objects.select_related().filter(date__date_id=query).values('series__series', 'series__series_notes','result')
		scanner_name =  DateDetails.objects.select_related().filter(date_id=query).values('scanner__scanner_name')
		phantom = DateDetails.objects.select_related().filter(date_id=query).values('phantom__phantom_name', 'phantom__phantom_id')
		gradsys = DateDetails.objects.select_related().filter(date_id=query).values('gradsys__gradsys_name', 'gradsys__gradsys_id')
		coil = DateDetails.objects.select_related().filter(date_id=query).values('coil__coil_name', 'coil__coil_id')
		version = DateDetails.objects.select_related().filter(date_id=query).values('version__version_name', 'version__version_id')
		date = DateDetails.objects.filter(date_id=query).values('full_date')

		context = {"results": results, "scanner_name":scanner_name, "phantom":phantom, "gradsys":gradsys, "coil":coil, "version":version, "date":date}
        
	return render(request, 'webapp/results.html', context)
	
############################################## note requests #########################################################
@login_required
def phantom_notes(request):
	query = request.GET.get('phantom_id')
#	try:
	query = int(query)
	#except ValueError:
#		query = None
#		results = None
#	if query:
	notes = PhantomDetails.objects.filter(phantom_id=query).values('phantom_name', 'phantom_notes')
	context = {"notes": notes}
	return render(request, 'webapp/phantom_notes.html', context)

## 

@login_required
def version_notes(request):
	query = request.GET.get('version_id')
#	try:
	query = int(query)
	#except ValueError:
#		query = None
#		results = None
#	if query:
	notes = VersionDetails.objects.filter(version_id=query).values('version_name', 'version_notes')
	context = {"notes": notes}
	return render(request, 'webapp/version_notes.html', context)



##

@login_required
def gradsys_notes(request):
	query = request.GET.get('gradsys_id')
#	try:
	query = int(query)
	#except ValueError:
#		query = None
#		results = None
#	if query:
	notes = GradsysDetails.objects.filter(gradsys_id=query).values('gradsys_name', 'gradsys_notes')
	context = {"notes": notes}
	return render(request, 'webapp/gradsys_notes.html', context)

@login_required
def coil_notes(request):
	query = request.GET.get('coil_id')
#	try:
	query = int(query)
	#except ValueError:
#		query = None
#		results = None
#	if query:
	notes = CoilDetails.objects.filter(coil_id=query).values('coil_name', 'coil_notes')
	context = {"notes": notes}
	return render(request, 'webapp/coil_notes.html', context)







