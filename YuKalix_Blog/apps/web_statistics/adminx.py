from  xadmin import views
import xadmin

from .models import DayLookNumber, Userip, VisitNumber, DayNumber

class DayLookNumberAdmin(object):
    list_display = (
        'day',
        'count',
    )

class UseripAdmin(object):
    list_display = (
        'ip',
        'count',
    )

class VisitNumberAdmin(object):
    list_display = (
        'id',
        'count',
    )

class DayNumberAdmin(object):
    list_display = (
        'day',
        'count',
    )


xadmin.site.register(DayLookNumber, DayLookNumberAdmin)
xadmin.site.register(Userip, UseripAdmin)
xadmin.site.register(VisitNumber, VisitNumberAdmin)
xadmin.site.register(DayNumber, DayNumberAdmin)