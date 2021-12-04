import django_tables2 as tables
from .models import Main, CellarModel


class MainTable(tables.Table):
    class Meta:
        model = Main
        template_name = "django_tables2/bootstrap.html"
        # fields = ('date', 'stage', 'note', 'num_protocol', 'batch', 'alcohol', 'sugar', 'titr_acids', 'pH', 'vol_acids',
        #           'rel_weight', 'mal_acids', 'lactic_acids','total_ext', 'SO2', 'O2', 'CO2', 'NTU', 'assim_nitrgen',
        #           'pecto_test', 'index_of_filt', 'Fe', 'Cu', 'sowing', 'sorb_acid', 'prot_stab', 'delta', 'cold_stab',
        #           'H2O2', 'scheme', 'other_proc')

        #exclude = ('')

class CellarTable(tables.Table):
    class Meta:
        model = CellarModel
        template_name = "django_tables2/bootstrap.html"






