from django.http import HttpResponse


# def home(request):
#     print(dir(request))
    
#     return HttpResponse('<h1>hello world</h1>') 


def home(request):
    response = HttpResponse()
    # response.write('<h2>this is the body of the web page</h2>')
    response.content = '<!Doctype html><head><style>h1{color:red}</style></head><body><h1>Hello world</h1></body></html>'
    response.status_code=200
    print(response.status_code)
    
    return response 