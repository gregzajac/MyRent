from datetime import datetime, timedelta

from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from MyRent.forms import OperationAgreementForm, ImageFlatForm
from MyRent.models import Flat, Agreement, Operation, Tenant, OperationDict, Image


class FlatListView(ListView):
    model = Flat

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            flats = Flat.objects.all().order_by("-is_for_rent")
        else:
            flats = Flat.objects.filter(is_for_rent=True)
        return flats


class FlatDetailView(DetailView):
    model = Flat

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=None, **kwargs)
        images = self.object.image_set.all()
        ctx.update({'images': images})
        return ctx


class AgreementListView(ListView):
    model = Agreement

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            agreements = Agreement.objects.all().order_by("-agreement_date")
        else:
            tenant = Tenant.objects.get(user=user)
            agreements = Agreement.objects.filter(tenant=tenant).order_by("-agreement_date")
        return agreements


class AgreementDetailView(DetailView):
    model = Agreement

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=None, **kwargs)
        operations = Operation.objects.filter(agreement=self.object).order_by("date")
        ctx.update({'operations': operations})

        balance = 0
        for operation in operations:
            balance += operation.value
        ctx.update({'balance': balance})
        return ctx


class AddObligationsView(View):

    def get(self, request, id_agreement):
        user = self.request.user
        if user.is_superuser:
            obligation_type = OperationDict.objects.get(pk=1)  # operacja naliczenia
            agreement = Agreement.objects.get(pk=id_agreement)
            actual_obligations = agreement.operation_set.filter(type=obligation_type)

            actual_obligation_dates_list = []
            for actual_obligation in actual_obligations:
                obligation_tmp = datetime(actual_obligation.date.year, actual_obligation.date.month, 1).date()
                if obligation_tmp not in actual_obligation_dates_list:
                    actual_obligation_dates_list.append(obligation_tmp)

            start_date = datetime(agreement.date_from.year, agreement.date_from.month, 1).date()
            if agreement.date_from.day > 1:
                start_date = start_date + timedelta(days=35)
                start_date = datetime(start_date.year, start_date.month, 1).date()

            if datetime.now().date() <= agreement.date_to:
                end_date = datetime.now().date()
            else:
                end_date = agreement.date_to

            while start_date <= end_date:
                if start_date not in actual_obligation_dates_list:  # dodawanie nowych naliczeń
                    Operation.objects.create(agreement=agreement,
                                             type=obligation_type,
                                             date=start_date,
                                             value=-agreement.mth_payment_value,
                                             info=f"Naliczenie za okres {start_date.year}/{start_date.month}")
                start_date = start_date + timedelta(days=35)
                start_date = datetime(start_date.year, start_date.month, 1).date()
        return redirect(f"/myrent/agreement/{id_agreement}")


class CreateFlatView(UserPassesTestMixin, CreateView):
    model = Flat
    fields = "__all__"
    success_url = reverse_lazy('flat-list')

    def test_func(self):
        return self.request.user.is_superuser


class FlatDeleteView(DeleteView):
    model = Flat
    success_url = reverse_lazy('flat-list')


class FlatUpdateView(UpdateView):
    model = Flat
    fields = "__all__"
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('flat-list')


class AgreementCreateView(CreateView):
    model = Agreement
    fields = "__all__"
    success_url = reverse_lazy('agreement-list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['flat'].queryset = Flat.objects.filter(is_for_rent=True)
        return form


class AgreementDeleteView(DeleteView):
    model = Agreement
    success_url = reverse_lazy('agreement-list')


class AgreementUpdateView(UpdateView):
    model = Agreement
    fields = "__all__"
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('agreement-list')


class OperationCreateView(View):
    def get(self, request, agreement_id):
        agreement = Agreement.objects.get(pk=agreement_id)
        form = OperationAgreementForm()
        ctx = {
            "form": form,
            "agreement": agreement
        }
        return render(request, "MyRent/operation_form.html", ctx)

    def post(self, request, agreement_id):
        form = OperationAgreementForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.agreement = Agreement.objects.get(pk=agreement_id)
            obj.save()
        return redirect(reverse_lazy('agreement-detail', kwargs={"pk": agreement_id}))


class OperationDeleteView(DeleteView):
    model = Operation

    def get_success_url(self):
        agreement_id = self.object.agreement.id
        return reverse_lazy('agreement-detail', kwargs={"pk": agreement_id})


class OperationUpdateView(UpdateView):
    model = Operation
    fields = ["type", "date", "value", "info"]
    template_name_suffix = '_update_form'

    def get_success_url(self):
        agreement_id = self.object.agreement.id
        return reverse_lazy('agreement-detail', kwargs={"pk": agreement_id})


class ImageCreateView(View):
    def get(self, request, flat_id):
        flat = Flat.objects.get(pk=flat_id)
        form = ImageFlatForm()
        ctx = {
            "form": form,
            "flat": flat
        }
        return render(request, "MyRent/image_form.html", ctx)

    def post(self, request, flat_id):
        form = ImageFlatForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.flat = Flat.objects.get(pk=flat_id)
            obj.save()
        return redirect(reverse_lazy('flat-detail', kwargs={"pk": flat_id}))


class ImageDeleteView(DeleteView):
    model = Image

    def get_success_url(self):
        flat_id = self.object.flat.id
        return reverse_lazy('flat-detail', kwargs={"pk": flat_id})


class TenantListView(ListView):
    model = Tenant


class TenantCreateView(CreateView):
    model = Tenant
    fields = "__all__"
    success_url = reverse_lazy('tenant-list')


class TenantUpdateView(UpdateView):
    model = Tenant
    fields = "__all__"
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('tenant-list')


class TenantDeleteView(DeleteView):
    model = Tenant
    success_url = reverse_lazy('tenant-list')
