import csv,io
from django.shortcuts import render
from django.contrib import messages
from .models import Food_index
def csv_upload(request):
    template = "csv_upload.html"

    prompt = {
        'order': 'order of the csv should be u_id, u_name,    batch_id, supplier, event_type, food_category,food_name '
    }

    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    
    for column in csv.reader(io_string, delimiter=',',quotechar='|'):
        _, created = Food_index.objects.update_or_create(
            u_id = column[0],
            u_name = column[1],
            batch_id = column[2],
            supplier = column[3],
            event_type = column[4],
            food_category = column[5],
            food_name = column[6],
        )
        

    context = {}
    return render(request, template, context)

    