import views
from django.shortcuts import render
from django.views import View


class Homepage(View):
    def get(self, request):
        return render(request=request, template_name='core/mainpage.html')

class info(View):
    def get(self, request):
        context = {'title': 'Информация о моем проекте'}
        return render(request=request, template_name='core/info.html')