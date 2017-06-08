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

def register(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			return HttpResponseRedirect('/accounts/register/complete')

	else:
		form = SignUpForm()

	return render(request, 'registration/signup.html', {'form': form})

def registration_complete(request):
	return render_to_response('registration/registration_complete.html')


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
		phantom = DateDetails.objects.select_related().filter(date_id=query).values('phantom__phantom_name', 'phantom__phantom_id','phantom__phantom_notes')
		gradsys = DateDetails.objects.select_related().filter(date_id=query).values('gradsys__gradsys_name', 'gradsys__gradsys_id', 'gradsys__gradsys_notes')
		coil = DateDetails.objects.select_related().filter(date_id=query).values('coil__coil_name', 'coil__coil_id', 'coil__coil_notes')
		version = DateDetails.objects.select_related().filter(date_id=query).values('version__version_name', 'version__version_id', 'version__version_notes')
		date = DateDetails.objects.filter(date_id=query).values('full_date')

		context = {"results": results, "scanner_name":scanner_name, "phantom":phantom, "gradsys":gradsys, "coil":coil, "version":version, "date":date}
        
	return render(request, 'webapp/results.html', context)
	
############################################## note requests #########################################################






