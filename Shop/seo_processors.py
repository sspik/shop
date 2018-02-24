from django.http import HttpResponseRedirect


def get_url(request):
    if request.get_full_path() != request.get_full_path().lower():
        return HttpResponseRedirect(request.get_full_path().lower)