from django.contrib.auth.backends import BaseBackend

from .models import Employee



class EmployeeBackend(BaseBackend):

    def authenticate(self, request, username=None,password = None):

        try:

             emp = Employee.objects.get(username = username, password = password)

             return emp

        except Employee.DoesnotExist:

                return None

