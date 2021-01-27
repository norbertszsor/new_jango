from django_filters.filterset import FilterSet
from .models import *

class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = ['id_user', 'user_name', 'password', 'email', 'age']