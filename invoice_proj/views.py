from django.http import HttpResponse
from invoices.models import Invoice


def hello_world(request):
    obj = Invoice.objects.get(id=1)
    # print(obj.get_tags())
    # print(obj.get_total_amount())
    qs = Invoice.objects.all()
    print(obj.__dict__)
    print('------')
    print(qs.query)
    return HttpResponse('Hello world')
