from django.urls import path
from spending.views import SignUpView,GetMeView,ExpenseListCreateView,ExpenseRetrieveUpdateDeleteView,ObtainAuthToken,ExpenseSummaryView,BudgetPlanView

urlpatterns=[
    path("register/",SignUpView.as_view()),
    path("me/",GetMeView.as_view()),
    path("expenses/",ExpenseListCreateView.as_view()),
    path("expenses/<int:pk>/",ExpenseRetrieveUpdateDeleteView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
    path("expenses/summary/",ExpenseSummaryView.as_view()),
    path("expenses/budgetplan/",BudgetPlanView.as_view())
]