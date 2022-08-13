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
    oy = f'<tr><th colspan="7" class="month">{x.strftime("%B")} {x.year}</th></tr>'
    print(kun)
    # for i in cal:
    cal = cal.replace(kun, f'<td class="today">{x.day}</td>')
    cal = cal.replace(oy, f'<tr><th colspan="7" class="month"><a href="/search/{x.year}/{x.month-1}"><<<</a> {x.strftime("%B")} {x.year} <a href="/search/{x.year}/{x.month+1}">>>></a> </th></tr>')
    print(type(cal))
    data = datetime.datetime.strptime('2018-06-21', '%Y-%m-%d')
    context = {
        "time":"time",
        "month":month,
        "calendar":cal,
        "year":oy
    }
    return render(request, 'calendar.html', context=context)


def Search(request, oy, year):
    if oy > 12:
        year = year + 1
        oy = 1
    elif oy <= 0:
        oy = 12
        year = year - 1
    b = datetime.datetime.now()
    month = list(calendar.month_name).index("March")
    x = datetime.datetime(year, oy, 1)
    cal = HTMLCalendar().formatmonth(
        x.year,
        x.month
    )
    oy = f'<tr><th colspan="7" class="month">{x.strftime("%B")} {x.year}</th></tr>'
    kun = f'<td class="{b.strftime("%a").lower()}">{b.day}</td>'
    cal = cal.replace(kun, f'<td class="today">{b.day}</td>')
    cal = cal.replace(oy, f'<tr><th colspan="7" class="month"><a href="/search/{x.year}/{x.month-1}"><<<</a> {x.strftime("%B")} {x.year} <a href="/search/{x.year}/{x.month+1}">>>></a> </th></tr>')
    
    context = {
        "time":"time",
        # "month":month,
        "calendar":cal,
        # "year":oy
    }
    print(x.strftime("%B"))
    print(oy)
    return render(request, 'calendar.html', context=context)