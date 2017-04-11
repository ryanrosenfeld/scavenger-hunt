from django.shortcuts import render
import json
from general.models import SiteUser


def api_call(request):
    response = json.dumps({'None': True})
    if request.method == 'GET':
        task_num = request.GET.get('task_num', None)
        if task_num == 1:
            activate = SiteUser.objects.filter(task_num=1, activate=True)
            if activate is not None:
                response = 1
            else:
                response = 0
    return render(request, 'response.html', {'response': response})