from django.contrib import admin
from models import Messages
# Register your models here.


class MessagesAdmin(admin.ModelAdmin):
    fields = ('vendor', 'customer', 'from_to', 'message', 'msg_type',
               'event_date', 'time_slot','bid_json',
              'status','self_booking',"num_guests","notes","package"
              )
    model = Messages
    list_display = ('vendor', 'customer', 'from_to', 'message', 'msg_type')
    readonly_fields=("msg_time","vendor","customer","from_to","message","msg_type",
                     "event_date","time_slot","package","bid_json","num_guests","notes","status","self_booking",
              )
    list_filter = ('msg_type','status')
    
admin.site.register(Messages,MessagesAdmin)
