from django.shortcuts import render
def home_page(request):
	return render(request=request, template_name='moviesapp/homepage.html')

from moviesapp.forms import MoviedetailsForm
def add_movie(request):
	movie_form=MoviedetailsForm()
	
	#This is to make changes in data entered by enduser in database
	if request.method=='POST':
		form_data=MoviedetailsForm(request.POST)
		if form_data.is_valid():
			form_data.save(commit=True)

	#This is used to display data entered by enduser on development server	
	if request.method=='POST':
		form_data=MoviedetailsForm(request.POST)
		if form_data.is_valid():
			print(form_data.cleaned_data['releasedate'])
			print(form_data.cleaned_data['moviename'])
			print(form_data.cleaned_data['hero'])
			print(form_data.cleaned_data['heroine'])
			print(form_data.cleaned_data['rating'])

	my_dict={'movie_form':movie_form}
	return render(request=request,template_name='moviesapp/addmovie.html',context=my_dict)
	
from moviesapp.models import Moviedetails	
def movie_list(request):			
	movie_data=Moviedetails.objects.all()
	my_dict={'movie_data':movie_data}
	return render(request=request, template_name='moviesapp/movielist.html',context=my_dict)