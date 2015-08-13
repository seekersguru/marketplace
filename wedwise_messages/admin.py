from django.contrib import admin
from models import Messages
# Register your models here.


class MessagesAdmin(admin.ModelAdmin):
    fields = ('vendor', 'customer', 'from_to', 'message', 'msg_type',
              'book_json', 'event_date', 'time_slot','bid_json',
              'bid_price','bid_quantity','status','self_booking',
              )
    model = Messages
    list_display = ('vendor', 'customer', 'from_to', 'message', 'msg_type')
    readonly_fields=('vendor', 'customer', 'from_to', 'message', 'msg_type',
              'book_json', 'event_date', 'time_slot','bid_json',
              'bid_price','bid_quantity','status','self_booking',
              )
    list_filter = ('msg_type','status')
    
admin.site.register(Messages,MessagesAdmin)
