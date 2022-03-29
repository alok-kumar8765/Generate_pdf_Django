from ast import arg
from urllib import request
from django.shortcuts import get_object_or_404, render
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from .models import Customer
# Create your views here.
class CustomerListView(ListView):
    model = Customer
    template_name = 'app/main.html'

def customer_render_pdf(request,*args,**kwargs):
    pk=kwargs.get('pk')
    customer=get_object_or_404(Customer,pk=pk)
    template_path = 'app/pdf2.html'
    context = {'custm':customer}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="repost.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html,dest=response
    )
    if pisa_status.err:
        return HttpResponse('We had some error')
    return response
    return HttpResponse('working')

def render_pdf_view(request):
    template_path = 'app/pdf.html'
    context = {'myvar':'this is ypur temp context'}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="repost.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(
        html,dest=response
    )
    if pisa_status.err:
        return HttpResponse('We had some error')
    return response