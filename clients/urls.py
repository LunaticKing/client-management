from django.urls import path
from .views import people_list, people_new, people_update, people_delete

urlpatterns = [
    path("list/", people_list, name = "people_list"), #c.R.u.d
    path("new/", people_new, name = "people_new"), #C.r.u.d
    path("update/<int:id>", people_update, name = "people_update"), #c.r.U.d
    path("delete/<int:id>", people_delete, name = "people_delete"), #c.r.u.D
]