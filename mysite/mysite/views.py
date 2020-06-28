from django.http import HttpResponse


def hello(request):
    response = '''
    <span>Hello world! Also, you can go to <a href="/contacts">contacts</a> now.</span>
    '''
    return HttpResponse(response)


def contacts(request):
    response = '''
    <span>Hello, here is contacts!</span>
    <ul>
        <li>Bill Gates gates@microsoft.com</li>
        <li>God sky@earth.com</li>
    </ul>
    <span>Also, you can go to main page <a href="/">here</a>.</span>
    '''
    return HttpResponse(response)
