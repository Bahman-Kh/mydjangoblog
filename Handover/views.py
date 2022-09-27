from django.shortcuts import render
from . import models

# Create your views here.
def handover(request):
    handover = models.Handover.objects.all().order_by('date')
    args = {'handover':handover}
    return render(request, 'handover.html', args)
