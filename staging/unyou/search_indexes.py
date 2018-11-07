from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from unyou import models
from .models import Unyou
from haystack import indexes



class MemoIndex(indexes.SearchIndex, indexes.Indexable):
    id = models.CharField(db_column='id', primary_key=True, max_length=100, blank=True, null=False)
    lbc = models.CharField(verbose_name='LBC', db_column='LBC', max_length=100, blank=True,
                           null=True)  # Field name made lowercase.
    main_lbc = models.CharField(db_column='Main_LBC', max_length=100, blank=True,
                                null=True)  # Field name made lowercase.
    parent_lbc = models.CharField(db_column='Parent_LBC', max_length=100, blank=True,
                                  null=True)  # Field name made lowercase.
    group_top_lbc1 = models.CharField(db_column='group_top_LBC1', max_length=100, blank=True,
                                      null=True)  # Field name made lowercase.
    group_lbc1 = models.CharField(db_column='group_LBC1', max_length=100, blank=True,
                                  null=True)  # Field name made lowercase.
    group_lbc2 = models.CharField(db_column='group_LBC2', max_length=100, blank=True,
                                  null=True)  # Field name made lowercase.
    group_lbc3 = models.CharField(db_column='group_LBC3', max_length=100, blank=True,
                                  null=True)  # Field name made lowercase.
    group_lbc_id1 = models.CharField(db_column='group_LBC_id1', max_length=100, blank=True,
                                     null=True)  # Field name made lowercase.
    group_lbc_id2 = models.CharField(db_column='group_LBC_id2', max_length=100, blank=True,
                                     null=True)  # Field name made lowercase.
    group_lbc_id3 = models.CharField(db_column='group_LBC_id3', max_length=100, blank=True,
                                     null=True)  # Field name made lsowercase.
    listing_id = models.CharField(db_column='Listing_id', max_length=100, blank=True,
                                  null=True)  # Field name made lowercase.
    listing_name = models.CharField(db_column='Listing_name', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
    ticker_symbol = models.CharField(db_column='Ticker_symbol', max_length=100, blank=True,
                                     null=True)  # Field name made lowercase.
    periodic_report_number = models.CharField(max_length=100, blank=True, null=True)
    company_status_id = models.CharField(max_length=100, blank=True, null=True)
    company_status_name = models.CharField(max_length=100, blank=True, null=True)
    office_status_id = models.CharField(max_length=100, blank=True, null=True)
    office_status_name = models.CharField(max_length=100, blank=True, null=True)
    merged_lbc = models.CharField(db_column='merged_LBC', max_length=100, blank=True,
                                  null=True)  # Field name made lowercase.
    # bankruptcy_date = models.DateField(blank=True, null=True)
    legal_personality = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(verbose_name='会社名', max_length=100, blank=True, null=True)
    legal_personality_place = models.CharField(max_length=100, blank=True, null=True)
    company_name_sub = models.CharField(max_length=100, blank=True, null=True)
    office_name = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)
    prefectures_id = models.CharField(max_length=100, blank=True, null=True)
    municipality_id = models.CharField(max_length=100, blank=True, null=True)
    prefectures_name = models.CharField(max_length=100, blank=True, null=True)
    municipality_name = models.CharField(max_length=100, blank=True, null=True)
    town_name = models.CharField(max_length=100, blank=True, null=True)
    city_block = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    building = models.CharField(max_length=100, blank=True, null=True)
    telephone_number = models.CharField(max_length=100, blank=True, null=True)
    fax_number = models.CharField(max_length=100, blank=True, null=True)
    offices_number = models.CharField(max_length=100, blank=True, null=True)
    # establishment_year = models.DateTimeField()
    capital = models.CharField(max_length=100, blank=True, null=True)
    employee_number = models.CharField(max_length=100, blank=True, null=True)
    current_term_settlement = models.CharField(max_length=100, blank=True, null=True)
    sales_current_term = models.CharField(max_length=100, blank=True, null=True)
    sales_ratio = models.CharField(max_length=100, blank=True, null=True)
    profit_term = models.IntegerField(db_column='Profit_term', blank=True, null=True)  # Field name made lowercase.
    profit_ratio = models.CharField(max_length=100, blank=True, null=True)
    dividend_term = models.CharField(max_length=100, blank=True, null=True)
    representative_position = models.CharField(db_column='Representative_position', max_length=100, blank=True,
                                               null=True)  # Field name made lowercase.
    representatives_name = models.CharField(db_column='Representatives_name', max_length=100, blank=True,
                                            null=True)  # Field name made lowercase.
    representatives_name_sub = models.CharField(db_column='Representatives_name_sub', max_length=100, blank=True,
                                                null=True)  # Field name made lowercase.
    industry_id1 = models.IntegerField(db_column='Industry_id1', blank=True, null=True)  # Field name made lowercase.
    industry_name1 = models.CharField(max_length=100, blank=True, null=True)
    industry_id2 = models.IntegerField(db_column='Industry_id2', blank=True, null=True)  # Field name made lowercase.
    industry_name2 = models.CharField(max_length=100, blank=True, null=True)
    industry_id3 = models.IntegerField(db_column='Industry_id3', blank=True, null=True)  # Field name made lowercase.
    industry_name3 = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telephone_call_check = models.CharField(max_length=100, blank=True, null=True)
    relocation_number = models.CharField(db_column='Relocation_number', max_length=100, blank=True,
                                         null=True)  # Field name made lowercase.
    fax_call_check = models.CharField(max_length=100, blank=True, null=True)
    relocation_fax = models.CharField(max_length=100, blank=True, null=True)
    company_type_id = models.CharField(max_length=100, blank=True, null=True)
    company_type_name = models.CharField(max_length=100, blank=True, null=True)
    foreign_owned_id = models.CharField(db_column='Foreign_owned_id', max_length=100, blank=True,
                                        null=True)  # Field name made lowercase.
    # survey_date = models.DateField(db_column='Survey_date', blank=True, null=True)  # Field name made lowercase.
    number_of_employees = models.IntegerField(blank=True, null=True)
    sales = models.CharField(max_length=100, blank=True, null=True)
    profit = models.CharField(max_length=100, blank=True, null=True)
    overseas_expansion_company = models.CharField(db_column='Overseas_expansion_company', max_length=100, blank=True,
                                                  null=True)  # Field name made lowercase.

    def get_model(self):
        return Unyou

