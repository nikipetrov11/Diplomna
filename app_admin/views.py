from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView, TemplateView

from app_admin.forms import CarEventForm, CarForm
from app_admin.mixins import AdminRequired
from cars.models import Car, Event, ServiceRequest, InvitedUserCarRequest


class LoginAdminView(LoginView):
    template_name = 'registration/admin-login.html'
    success_url = reverse_lazy('admin_car_list')

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or self.success_url


class AdminPanelView(AdminRequired, TemplateView):
    template_name = 'admin/admin-panel.html'


class AdminCarCreateView(AdminRequired, CreateView):
    model = Car
    form_class = CarForm
    template_name = '../../frontend/templates/admin/add-car.html'
    success_url = reverse_lazy('admin_car_list')


class AdminCarListView(AdminRequired, ListView):
    model = Car
    context_object_name = 'car_list'
    template_name = '../../frontend/templates/admin/car-list.html'

    def get_queryset(self):
        return Car.objects.order_by('-created_at')


class AdminCarDetailView(AdminRequired, DetailView):
    model = Car
    template_name = '../../frontend/templates/admin/car-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.filter(car_id=self.object.id).order_by('-created_at')
        return context


class AdminEventDetailView(AdminRequired, DetailView):
    model = Event
    template_name = '../../frontend/templates/admin/event-detail.html'


class AdminCarDeleteView(AdminRequired, DeleteView):
    model = Car
    template_name = '../../frontend/templates/admin/delete-car.html'
    success_url = reverse_lazy('admin_car_list')


class AdminEventDeleteView(AdminRequired, DeleteView):
    model = Event
    template_name = '../../frontend/templates/admin/event-delete.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('admin_car_detail', args=(self.object.car.id,))


class AdminCarUpdateView(AdminRequired, UpdateView):
    model = Car
    form_class = CarForm
    template_name = '../../frontend/templates/admin/edit-car.html'

    def get_success_url(self):
        return reverse_lazy('admin_car_list')


class AdminEventUpdateView(AdminRequired, UpdateView):
    model = Event
    fields = ['km_of_car', 'event_text', 'periodic_event', 'next_date']
    template_name = '../../frontend/templates/admin/event-update.html'

    def get_success_url(self):
        return reverse_lazy('admin_event_detail', args=(self.object.id,))


class AdminAddEventToCarCreateView(AdminRequired, CreateView):
    model = Event
    template_name = 'admin/add-event.html'
    form_class = CarEventForm

    def get_car(self):
        return get_object_or_404(Car, pk=self.kwargs['pk'])

    def form_valid(self, form):
        form.instance.car = self.get_car()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = self.get_car()
        return context

    def get_success_url(self):
        return reverse_lazy('admin_car_list')


class AdminServiceRequestListView(AdminRequired, ListView):
    model = ServiceRequest
    context_object_name = 'service_requests'
    template_name = 'admin/service-request-list.html'
    success_url = reverse_lazy('admin_car_list')

    def post(self, request, *args, **kwargs):
        if 'toggle_button' in request.POST:
            pk = request.POST.get('pk')
            service_request = self.model.objects.get(pk=pk)

            service_request.toggle_seen()
        return super().get(request, *args, **kwargs)


class AdminServiceRequestNotSeenView(AdminRequired, ListView):
    model = ServiceRequest
    context_object_name = 'not_seen_service_requests'
    template_name = 'admin/not-seen-service-request-list.html'
    success_url = reverse_lazy('not_seen_admin_service_request_list')

    def get_queryset(self):
        return ServiceRequest.objects.filter(is_seen=False)

    def post(self, request, *args, **kwargs):
        if 'toggle_button' in request.POST:
            pk = request.POST.get('pk')
            service_request = self.model.objects.get(pk=pk)

            service_request.toggle_seen()
        return super().get(request, *args, **kwargs)


# TODO: Service request detail view is not used, but if needed this is the view
# class AdminServiceRequestDetailView(AdminRequired, DetailView):
#     model = ServiceRequest
#     template_name = 'admin/service-request-detail.html'
#     context_object_name = 'service_request'
#
#     def post(self, request, *args, **kwargs):
#         service_request = self.get_object()
#         service_request.toggle_seen()
#         return HttpResponseRedirect(reverse_lazy('admin_service_request_detail', kwargs={'pk': service_request.pk}))
#

class AdminInvitedUserRequestsListView(AdminRequired, ListView):
    model = InvitedUserCarRequest
    template_name = 'admin/invited-user-requests.html'


class AdminAccountDetails(AdminRequired, TemplateView):
    template_name = 'admin/account-details.html'
