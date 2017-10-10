from django.template import loader, RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from datetime import datetime
from .models import XfndUser
from .models import XfndProgram
from .models import XfndFunction
from .models import XfndMenu
from .models import XfndMenuItem
from .models import XfndReportGroup
from .models import XfndReportGroupItem
from .models import XfndResp
from .models import XfndUserResp
from .models import XfndFunctionExecLog


def context_proc(request):
    return {
        'user': request.user,
        'company_name': 'ARES Corp.',
        'ip_address': request.META['REMOTE_ADDR']
    }

def program_list(request):
    program_list = XfndProgram.objects.all()

    return render(request,'xfnd/program_list.html', {
        'program_list': program_list,
    })


def index(request):
    """
    return render(request,'index.html', {
            'company_name': 'ARES Corp.',
            'telephone_number': '02-25221351',
        })
    """

    """
    t = loader.get_template('index.html')
    rc = RequestContext(request, {'message': 'index'}, processors=[context_proc]) 
    return t.render(rc)
    """

    return render_to_response(
        'index.html',
        {'message': 'index message'}
    )
