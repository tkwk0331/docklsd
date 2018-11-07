from django.urls import path
from .views import UnyouFilterView, UnyouDetailView, UnyouCreateView, UnyouUpdateView, UnyouDeleteView
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # 一覧画面
    path('',  UnyouFilterView.as_view(), name='index'),
    # 詳細画面
    path('detail/<int:pk>/', UnyouDetailView.as_view(), name='detail'),
    # 登録画面
    path('create/', UnyouCreateView.as_view(), name='create'),
    # 更新画面
    path('update/<int:pk>/', UnyouUpdateView.as_view(), name='update'),
    # 削除画面
    path('delete/<int:pk>/', UnyouDeleteView.as_view(), name='delete'),

    path('export/', views.CsvExportViewBase, name='export'),

]

