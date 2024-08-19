from django.http import HttpResponse ,JsonResponse
def home_page(request ):
    print("showing")
    company=[
        'alpha',
        'alpha2',
        'alpha3',
    ]
    return JsonResponse(company,safe=False)