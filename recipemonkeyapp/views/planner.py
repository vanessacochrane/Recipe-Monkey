from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.http import Http404
from recipemonkeyapp.models import Planner,PlannerCalendar
from django.utils.safestring import mark_safe
from recipemonkeyapp.utils.scheduler import *
from django.contrib import messages

from django.contrib.auth.models import Group
from datetime import *

#management.call_command('flush', verbosity=0, interactive=False)
#management.call_command('loaddata', 'test_data', verbosity=0)



def schedule(request,weeknum,startdate):
    
    startdate=datetime.strptime(startdate,'%Y%m%d')
    weeknum=int(weeknum)
    
    g=Group.objects.get(name='MenuPlanner-Default')
    
    default_p=tuple(x for x in g.user_set.all())
    
    print "Default people [%s]" % ",".join(p.username for p in default_p)
    
    people=[]
    
    for i in range(1,8):
        
        people.append(default_p)
        
    plan=schedule_meals(startdate,weeknum,people)
    messages.add_message(request, messages.SUCCESS, 'Scheduled new meals')
    
    return redirect('/recipemonkeyapp/planner/%d/' % plan.id)
    
    
    

def calendar(request, planner_id):
    
	# try:
	# 		i = GroceryItem.objects.get(pk=id)
	# 	except GroceryItem.DoesNotExist:
	# 		raise Http404
	
	year=2011
	month=11
	
	planners = Planner.objects.order_by('date').filter(
	date__year=year, date__month=month
	)
	cal = PlannerCalendar(planners).formatmonth(year, month)
	
	ct={'calendar': mark_safe(cal),}
	return render_to_response('planner/calendar.html',ct,context_instance=RequestContext(request))
	
	

