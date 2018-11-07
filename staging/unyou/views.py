import io

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters import FilterSet, filters
from django_filters.views import FilterView
from pure_pagination.mixins import PaginationMixin
from .models import Unyou
from .filters import UnyouFilter, MyOrderingFilter
from .forms import UnyouForm
from django.http import HttpResponse
from django.urls import reverse_lazy
import csv
from django.views.generic import View

class UnyouFilterView(LoginRequiredMixin, PaginationMixin, FilterView):
    model = Unyou
    filterset_class = UnyouFilter
    paginate_by = 25
    object = Unyou


# クエリ未指定の時に全件検索を行うために以下のオプションを指定（django-filter2.0以降）
strict = False


# pure_pagination用設定


# 検索条件をセッションに保存する or 呼び出す
def get(self, request, **kwargs):
    if request.GET:
        request.session['query'] = request.GET
    else:
        request.GET = request.GET.copy()
        if 'query' in request.session.keys():
            for key in request.session['query'].keys():
                request.GET[key] = request.session['query'][key]

    return super().get(request, **kwargs)



class CsvExportViewBase(View):
    output_as_sjis = True

    def get(self, *args, **kwargs):
        if self.output_as_sjis:
            return self._get_response_as_sjis(*args, **kwargs)

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = \
            'attachment; filename={}'.format(self.get_filename())
        writer = csv.writer(response)

        for r in self.get_result_rows():
            writer.writerow(r)
        return response

    def _get_response_as_sjis(self, *args, **kwargs):
        response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
        response['Content-Disposition'] = \
            'attachment; filename={}'.format(self.get_filename())
        sio = io.StringIO()
        writer = csv.writer(sio)

        for r in self.get_result_rows():
            writer.writerow(r)

        response.write(sio.getvalue().encode(encoding='cp932'))
        return response

    def get_connection(self):
        from django.db import connection
        return connection

    def get_cursor(self):
        connection = self.get_connection()
        return connection.cursor()

    def get_sql(self):
        """
        Implement required.
        """
        return "SELECT NOW()"

    def get_sql_args(self):
        return []

    def row_filter(self, row):
        return row

    def get_result_rows(self):

        cursor = self.get_cursor()

        cursor.execute(self.get_sql(), *self.get_sql_args())

        # Header
        yield self.row_filter(f[0] for f in cursor.description)

        # Content
        for r in cursor.fetchall():
            yield self.row_filter(r)

    def get_filename(self):
        return "items.csv"


'''
    writer = csv.writer(response)

    model = queryset.model

    headers = []
    for field in model._meta.fields:
        headers.append(field.name)
    writer.writerow(headers)

    for obj in queryset:
        row = []
        for field in headers:
            val = getattr(obj, field)
            if callable(val):
                val = val()
            row.append(val)
        writer.writerow(row)

    return response
'''


# 詳細画面
class UnyouDetailView(LoginRequiredMixin, DetailView):
    model = Unyou


# 登録画面
class UnyouCreateView(LoginRequiredMixin, CreateView):
    model = Unyou
    form_class = UnyouForm
    success_url = reverse_lazy('index')


# 更新画面
class UnyouUpdateView(LoginRequiredMixin, UpdateView):
    model = Unyou
    form_class = UnyouForm
    success_url = reverse_lazy('index')


# 削除画面
class UnyouDeleteView(LoginRequiredMixin, DeleteView):
    model = Unyou
    success_url = reverse_lazy('index')
