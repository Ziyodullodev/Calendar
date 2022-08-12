from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
import datetime


def Calendar(request):
    month = list(calendar.month_name).index("March")
    # data = datetime.date.strftime("%I")
    x = datetime.datetime.now()
    cal = HTMLCalendar().formatmonth(
        x.year,
        x.month
    )
    kun = f'<td class="{x.strftime("%a").lower()}">{x.day}</td>'
    print(kun)
    # for i in cal:
    cal = cal.replace(kun, f'<td class="today">{x.day}</td>')
    print(type(cal))
    data = datetime.datetime.strptime('2018-06-21', '%Y-%m-%d')
    context = {
        "time":"time",
        "month":month,
        "calendar":cal,
        "year":x.year
    }
    return render(request, 'calendar.html', context=context)