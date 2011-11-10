from calendar import HTMLCalendar
from datetime import date
from itertools import groupby

from django.utils.html import conditional_escape as esc

class PlannerCalendar(HTMLCalendar):

	def __init__(self, planners):
		super(PlannerCalendar, self).__init__()
		self.planners = self.group_by_day(planners)

	def formatday(self, day, weekday):
		if day != 0:
			cssclass = self.cssclasses[weekday]
			if date.today() == date(self.year, self.month, day):
				cssclass += ' today'
			if day in self.planners:
				cssclass += ' filled'
				body = ['<ul>']
				for planner in self.planners[day]:
					body.append('<li>')
					body.append(esc(planner.breakfast))
					body.append('</li>')
					body.append('<li>')
					body.append(esc(planner.lunch))
					body.append('</li>')
					body.append('<li>')
					body.append(esc(planner.dinner))
					body.append('</li>')
					body.append('</ul>')
				return self.day_cell(cssclass, '%d %s' % (day, ''.join(body)))
			return self.day_cell(cssclass, day)
		return self.day_cell('noday', '&nbsp;')

	def formatmonth(self, year, month):
		self.year, self.month = year, month
		return super(PlannerCalendar, self).formatmonth(year, month)

	def group_by_day(self, planners):
		field = lambda planner: planner.date.day
		return dict(
			[(day, list(items)) for day, items in groupby(planners, field)]
		)

	def day_cell(self, cssclass, body):
		return '<td class="%s">%s</td>' % (cssclass, body)