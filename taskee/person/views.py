from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person

# Create your views here.

class PersonListView(ListView):
    model = Person
    context_object_name = 'person'

class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'dob', 'country', 'city')
    success_url = reverse_lazy('person_view')

class PersonUpdateView(UpdateView):
    model = Person
    fields = ('name', 'dob', 'country', 'city')
    success_url = reverse_lazy('person_view')

def load_cities(request):
    country_id = request.GET.get('country')
    cities = City.objects.filter(country_id=country_id).order_by('name')
    return render(request, 'person/city_dropdown_list_options.html', {'cities':cities})
