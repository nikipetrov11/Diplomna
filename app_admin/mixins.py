from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy


class AdminRequired(UserPassesTestMixin):
    """
    Used for class based views.
    """

    def test_func(self):
        return self.request.user.is_superuser

    def get_login_url(self):
        return reverse_lazy('admin_login')
