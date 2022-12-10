from django.urls import path

from accounts.views.accounts import AccountCreateView,TutorCreateView, StudyCenterCreateView

from accounts.views.base import IndexView
# from accounts.views.accounts import AccountStudyCenterCreateView, AccountTutorCreateView

urlpatterns = [
    # path('login/', LoginView.as_view(), name='login'),
    path('register/account/<str:type>', AccountCreateView.as_view(), name='account_register'),

    # path('register/tutor', AccountTutorCreateView.as_view(), name='tutor_register'),
    path('register/tutor/<int:pk>', TutorCreateView.as_view(), name='tutor_module_register'),

    # path('register/study_center', AccountStudyCenterCreateView.as_view(), name='study_center_register'),
    path('register/study_center/<int:pk>', StudyCenterCreateView.as_view(), name='study_center_module_register'),

    path('', IndexView.as_view(), name='index'),
    # path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    # path('profile/<int:pk>/change', UserChangeView.as_view(), name='change'),
    # path('logout/', logout_view, name='logout'),
    # path('<int:pk>/password_change', UserPasswordChangeView.as_view(), name='password_change')
]
