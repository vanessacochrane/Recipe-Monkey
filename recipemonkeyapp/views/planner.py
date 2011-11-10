from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.http import Http404
from recipemonkeyapp.models import Planner,PlannerCalendar
from django.utils.safestring import mark_safe

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
	
	

