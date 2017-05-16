from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from webapp.models import ScannerDetails, DateDetails, VersionDetails, GradsysDetails, CoilDetails, PhantomDetails, Results, SeriesDetails
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def signup(request):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/')
		else:
			form = UserCreationForm()
			return render(request, 'webapp/signup.html', {'form': form})

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







