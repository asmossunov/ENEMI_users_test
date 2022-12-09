from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from accounts.forms import TutorCreationForm, AccountForm, StudyCenterCreationForm
from accounts.models import Account, Student, Tutor, StudyCenter


class AccountCreateView(CreateView):
    template_name = 'account_register.html'
    model = Account
    form_class = AccountForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            account = form.save()
            account.type = 'student'
            account.save()
            login(request, account)
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self, request):
        return reverse('index')


class AccountTutorCreateView(CreateView):
    template_name = 'account_tutor_register.html'
    model = Account
    form_class = AccountForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            account = form.save()
            account.type = 'tutor'
            account.save()
            login(request, account)
            return redirect('tutor_module_register', pk=account.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self, request):
        return reverse('index')


class TutorCreateView(CreateView):
    template_name = 'tutor_register.html'
    model = Tutor
    form_class = TutorCreationForm

    def get_context_data(self, **kwargs):
        context = super(TutorCreateView, self).get_context_data(**kwargs)
        context['tutor_form'] = TutorCreationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        # form.instance.user_id = self.kwargs['pk']
        user = Account.objects.get(pk=self.kwargs['pk'])
        print(user)
        if form.is_valid():
            print(request.POST)
            print('zashli v sohranenie modulya tutora')
            # tutor = form.save()
            Tutor.objects.create(place_of_study=request.POST['place_of_study'],
                                 working_place=request.POST['working_place'],
                                 user=user)
            login(request, user)
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self, request):
        return reverse('index')


class AccountStudyCenterCreateView(CreateView):
    template_name = 'account_study_center_register.html'
    model = Account
    form_class = AccountForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            account = form.save()
            account.type = 'study_center'
            account.save()
            login(request, account)
            return redirect('study_center_module_register', pk=account.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self, request):
        return reverse('index')


class StudyCenterCreateView(CreateView):
    template_name = 'study_center_register.html'
    model = StudyCenter
    form_class = StudyCenterCreationForm

    def get_context_data(self, **kwargs):
        context = super(StudyCenterCreateView, self).get_context_data(**kwargs)
        context['study_center_form'] = StudyCenterCreationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        # form.instance.user_id = self.kwargs['pk']
        user = Account.objects.get(pk=self.kwargs['pk'])
        print(user)
        if form.is_valid():
            print(request.POST)
            print('zashli v sohranenie modulya study_center')
            # study_center = form.save()
            StudyCenter.objects.create(study_center_name=request.POST['study_center_name'],
                                       contact_person=request.POST['contact_person'],
                                       user=user)
            login(request, user)
            return redirect('index')
        context = {}
        context['form'] = form
        return self.render_to_response(context)

    def get_success_url(self, request):
        return reverse('index')
