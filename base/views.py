# Create your views here.
from django.views.generic import TemplateView, DetailView
from base.models import RegroupementSalle


class SallesView(DetailView):
    template_name = 'base/liste_salle.html'
    model = RegroupementSalle
    pk_url_kwarg = 'regroupement'

