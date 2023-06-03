from django.shortcuts import render
from django.views.generic.base import TemplateView


#TODO: Refatorar para usar threads assim que possivel
def home(request):
    #import pdb; pdb.set_trace()
    value1 = 10
    value2 = 20
    result = value1 * value2

    return render(request, 'home.html', {'result': result})

class HomePageView(TemplateView):
    template_name = 'home3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'Ola, seja bem vindo ao curso'
        return context

#FIXME: Corrigir bug ....
def x ():
    pass


