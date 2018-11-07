from django_filters import filters
from django_filters import FilterSet
from .models import Unyou



class MyOrderingFilter(filters.OrderingFilter):
 descending_fmt = '%s （降順）'



class UnyouFilter(FilterSet):

    lbc = filters.CharFilter(label='LBC', lookup_expr='contains')
    main_lbc = filters.CharFilter(label='MAIN_LBC', lookup_expr='contains')
    group_top_lbc1 = filters.CharFilter(label='グループトップLBC', lookup_expr='contains')
    Industry_id1 = filters.NumberFilter(label='業種',lookup_expr='contains')
    municipality_name = filters.CharFilter(label='都道府県', lookup_expr='contains')
    company_name = filters.CharFilter(label='会社名（全角)', lookup_expr='contains')

    #def get_top(self, queryset, name, value):
       #return queryset.all()[25]


    order_by = MyOrderingFilter(
        # tuple-mapping retains order
        fields=(
            ('lbc', 'lbc'),
            ('main_lbc', 'main_lbc'),
            ('group_top_lbc1', 'group_top_lbc1'),
            ('Industry_id1', 'Industry_id1'),
            ('municipality_name', 'municipality_name'),
            ('company_name', 'company_name'),
        ),
        field_labels={
            'lbc': 'LBC',
            'main_lbc': 'main_LBC',
            'group_top_lbc1': 'グループトップLBC',
            'Industry_id1': '業種',
            'municipality_name': '都道府県',
            'company_name': '会社名',
        },
        label='並び順'
    )


    #top = filters.NumberFilter(method='get_top')

    class Meta:
        model = Unyou
        fields = ('lbc', 'main_lbc', 'Industry_id1','group_top_lbc1','municipality_name','company_name')


    def handle(self, *args, **options):
        def get(self, request, **kwargs):
            if request.GET:
                    request.session['query'] = request.GET
            else:
                    request.GET = request.GET.copy()
                    if 'query' in request.session.keys():
                        for key in request.session['query'].keys():
                            request.GET[key] = request.session['query'][key]

            return super().get(request, **kwargs)

