from django.views.generic import TemplateView
from django.shortcuts import render
from .models import SomeData
from .forms import InputForm


class IndexView(TemplateView):
    template_name = 'input_output/index.html'

class InputView(TemplateView):
    template_name = 'input_output/input.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = InputForm()
        return context

    def post(self, *args, **kwargs):
        names    = self.request.POST.getlist('name')
        messages = self.request.POST.getlist('msg')

        for name, msg in zip(names, messages):
            SomeData.objects.create(data={
                'name': name,
                'msg': msg,
            })

        context =  self.get_context_data()
        context['success'] = True

        return render(self.request, self.template_name, context)

class OutputView(TemplateView):
    template_name = 'input_output/output.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.method == 'GET':
            context['data'] = SomeData.objects.all()

        return context