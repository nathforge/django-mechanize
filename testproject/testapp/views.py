from django.shortcuts import render_to_response
from testapp.forms import TestForm


def test_view(request):
    success = None
    if request.method == 'POST':
        form = TestForm(request.POST, request.FILES)
        if form.is_valid():
            success = True
    else:
        form = TestForm()
    
    return render_to_response('testapp/test_view.html', {
        'form': form,
        'success': success,
    })
