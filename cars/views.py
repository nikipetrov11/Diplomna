from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView

from cars.forms import UserRegistrateForm, ServiceRequestForm, InvitedUserCarRequestForm, ContactForm
from cars.models import ServiceRequest, UserProfile, InvitedUserCarRequest, ContactFormModel, Car


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler403(request, exception):
    return render(request, '403.html', status=403)


class IndexView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class PriceAndDiscountView(TemplateView):
    template_name = 'prices_and_discounts.html'


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or self.success_url


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegistrateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('reg_success')

    def form_valid(self, form):
        user = form.save()
        profile = UserProfile(user=user, phone=form.cleaned_data['phone'])
        profile.save()
        return super().form_valid(form)


class RegisterSuccess(TemplateView):
    template_name = 'registration/reg-success.html'


def logout_view(request):
    logout(request)
    return redirect('index')


class ServiceRequestCreateView(CreateView):
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'add-service-request.html'
    success_url = reverse_lazy('success_service_request')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if self.request.user.is_authenticated:
            del form.fields['first_name']
            del form.fields['last_name']
            del form.fields['email']
            del form.fields['phone']
        return form

    def form_valid(self, form):
        # Set the user field to the currently logged-in user, if there is one
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            form.instance.first_name = self.request.user.first_name
            form.instance.last_name = self.request.user.last_name
            form.instance.email = self.request.user.email
            form.instance.phone = self.request.user.userprofile.phone
        return super().form_valid(form)


class SuccessServiceRequestView(TemplateView):
    template_name = 'success-service-request.html'


class InvitedUserCarRequestView(LoginRequiredMixin, CreateView):
    model = InvitedUserCarRequest
    form_class = InvitedUserCarRequestForm
    template_name = 'invited-user-request-form.html'
    success_url = reverse_lazy('index')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ContactView(CreateView):
    model = ContactFormModel
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('contact_success')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if self.request.user.is_authenticated:
            del form.fields['first_name']
            del form.fields['last_name']
            del form.fields['email']
            del form.fields['phone']
        return form

    def form_valid(self, form):
        # Set the user field to the currently logged-in user, if there is one
        if self.request.user.is_authenticated:
            form.instance.first_name = self.request.user.first_name
            form.instance.last_name = self.request.user.last_name
            form.instance.email = self.request.user.email
            form.instance.phone = self.request.user.userprofile.phone
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = 'contact-success.html'


class ShopView(TemplateView):
    template_name = 'shop.html'


class UserCarListView(LoginRequiredMixin, ListView):
    model = Car
    context_object_name = 'car_list'
    template_name = 'user-car-list.html'
    login_url = 'login'

    def get_queryset(self):
        return Car.objects.filter(user_id=self.request.user.id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_cars'] = bool(Car.objects.filter(user_id=self.request.user.id))
        return context


class LiveCarView(LoginRequiredMixin, DetailView):
    model = Car
    template_name = 'live-car.html'

    # TODO: Logic for live steaming
    # TODO: Does not work. It's just generated from ChatGPT
    # def get(self, request, *args, **kwargs):
    #     # Get the object you want to display details for
    #     self.object = self.get_object()
    #
    #     # Initialize the camera
    #     cap = cv2.VideoCapture(0)
    #
    #     def generate_frames():
    #         while True:
    #             # Capture frame-by-frame
    #             ret, frame = cap.read()
    #
    #             # If the frame was not captured successfully, break the loop
    #             if not ret:
    #                 break
    #
    #             # Convert the frame to JPEG format
    #             ret, buffer = cv2.imencode('.jpg', frame)
    #
    #             # Yield the resulting image as a byte stream
    #             yield (b'--frame\r\n'
    #                    b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')
    #
    #     # Return the response as a streaming response
    #     response = StreamingHttpResponse(generate_frames(),
    #                                      content_type='multipart/x-mixed-replace; boundary=frame')
    #
    #     # Set the appropriate headers
    #     response['Content-Length'] = '0'  # You can set the appropriate length or remove this line
    #     response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    #     response['Pragma'] = 'no-cache'
    #     response['Expires'] = '0'
    #
    #     return response
