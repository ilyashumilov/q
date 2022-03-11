from django.shortcuts import render,redirect
from .forms import *
import pandas as pd
from .filtration import filtration
import requests
from io import BytesIO
from io import StringIO
import openpyxl
import xlsxwriter
from django.http import HttpResponse
# Create your views here.

def MainView(request):
    form = indexform()
    if request.method == 'POST':
        form = indexform(request.POST)
        if form.is_valid:
            file = request.FILES['file']
            data = pd.read_csv(file)
            r = requests.get('http://web:8000/')
            existing = []
            for i in r.json():
                existing.append(i['number'])
            # print(existing)
            fin = filtration(data,existing)
            print(fin)
            for n in fin['DOCUMENT_NUMBER']:
                # print(n)
                if n!='nan' and n!='NaN' and n!='Nan' and len(str(n))!=0 and len(str(n))!=1:
                    payload = {
                        'number':n
                    }
                    r = requests.post('http://web:8000/',payload)

            with BytesIO() as b:
                # Use the StringIO object as the filehandle.
                writer = pd.ExcelWriter(b, engine='xlsxwriter')
                fin.to_excel(writer, sheet_name='Sheet1')
                writer.save()
                # Set up the Http response.
                filename = 'Filtered.xlsx'
                response = HttpResponse(
                    b.getvalue(),
                    content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                response['Content-Disposition'] = 'attachment; filename=%s' % filename
                return response
    context = {
        'form' : form
    }
    return render(request,'main.html',context)