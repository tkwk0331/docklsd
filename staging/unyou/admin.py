from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Unyou



class UnyouResource(resources.ModelResource):
    class Meta:
        model = Unyou
        fields = ('lbc','main_lbc','parent_lbc','group_top_lbc1','group_lbc1',
                  'group_lbc2','group_lbc3','group_lbc_id1','group_lbc_id2',
                  'group_lbc_id3','listing_id','listing_name','ticker_symbol',
                  'periodic_report_number',
                  'company_status_id','company_status_name','office_status_id',
                  'office_status_name','merged_lbc',
                  'legal_personality','company_name','legal_personality_place','company_name_sub','office_name',
                  'zipcode','prefectures_id','municipality_id','prefectures_name','municipality_name','town_name',
                  'city_block','address','building','telephone_number','fax_number',
                  'offices_number','capital','employee_number',
                  'current_term_settlement','sales_current_term','sales_ratio',
                  'profit_term','profit_ratio','dividend_term',
                  'representative position','representatives_name',
                  'representatives_name_sub','industry_id1','industry_name1',
                  'industry_id2','industry_name2','industry_id3',
                  'industry_name3','url','telephone_call_check','relocation_number',
                  'fax_call_check','relocation_fax','company_type_id',
                  'company_type_name','foreign_owned_id','number_of_employees','sales',
                  'profit',
                  'overseas_expansion_company','a','b','c','d',
                  'e','f','g','h','i','j','k','l',)



class UnyouAdmin(ImportExportModelAdmin, admin.UnyouModelAdmin):
    resource_class = UnyouResource
    to_encoding = "cp932"

    def get_export_data(self, file_format, queryset, *args, **kwargs):
        """
        Returns file_format representation for given queryset.
        """
        request = kwargs.pop("request")
        resource_class = self.get_export_resource_class()
        data = resource_class(**self.get_export_resource_kwargs(request)).export(queryset, *args, **kwargs)
        export_data = file_format.export_data(data)
        return export_data.encode(self.to_encoding)

    list_display = ('id', 'company_name', 'lbc','main_lbc','prefectures_name',)
    list_display_links = ('company_name', 'id')
    search_fields = ['prefectures_name','industry_id1','company_name','lbc']
    list_filter = ['company_status_name','legal_personality','supermain',]


admin.site.register(Unyou, UnyouAdmin)
