from django.urls import path
from reminders import views

urlpatterns = [
    path('reminder_lists', views.ReminderLists.as_view(), name='reminder_lists'),
    path('add_reminder', views.AddReminder.as_view(), name='add_reminder'),
    path('reminder/<int:id>', views.ReminderItem.as_view(), name='reminder_item'),
]


