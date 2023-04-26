from django.contrib.auth import get_user


def user(request):
    '''
    The `user` function is a Django view function that takes a request object as
    a parameter and returns a dictionary containing the current user object.
    The `get_user` function is imported from the `django.contrib.auth` module in
    order to retrieve the currently authenticated user object from the request
    object.
    This user object is then added to the dictionary as the value associated
    with the key 'user'.
    This dictionary is used as a context processor in order to make the current
    user object available in templates to be used for authentication and
    authorization purposes.
    '''
    return {'user': get_user(request)}
