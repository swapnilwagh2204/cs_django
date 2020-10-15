from django.shortcuts import render

# Create your views here.

from django import views


class DemoView(views.View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        self.context['data'] = 'swapnil'

        return render(request, self.template_name, self.context)

    def post(self, request):
        self.context['data'] = 'welcome swapnil'
        return render(request, 'success.html', self.context)


class DemoView1(DemoView):
    def get(self, request):
        context = super().context
        context['data'] = 'this '
        return render(request, self.template_name, context)
