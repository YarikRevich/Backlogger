

def add_email(request):
    try:
        return {"email":request.user.email,"password":request.user.password}
    except AttributeError:
        return {"email":"None"}