import datetime
from django.http import HttpResponse
from django_tables2.views import SingleTableView
from django.shortcuts import render
from table import helpers
from django.urls import reverse
from django.views import generic
# from decimal import Decimal

from time import gmtime, strftime


from .models import Main
from .models import Assortment
from .tables import MainTable, CellarTable
from .forms import AddForm


def TableListView(request):
    table = MainTable(Main.objects.all())

    return render(request, 'table/table.html', {
        "table": table,
    })

    # model = Main
    # table_class = MainTable
    # template_name = 'table/table.html'


def addtotable(request):
    if request.method == 'POST':
        category = request.POST['category']
        assortment = request.POST['assortment_name']
        assortment_year = request.POST['year']
        stage = request.POST['stage']
        note = request.POST['note']
        num_protocol = request.POST['numProtocol']
        batch = request.POST['batch']
        alcohol = request.POST['alcohol']
        sugar = float(request.POST['sugar'])
        titr_acids = float(request.POST['titr_acids'])
        ph = float(request.POST['pH'])
        vol_acids = float(request.POST['vol_acids'])
        rel_weight = float(request.POST['rel_weight'])
        mal_acids = float(request.POST['mal_acids'])
        lactic_acids = float(request.POST['lactic_acids'])
        total_ext = float(request.POST['total_ext'])
        so2 = float(request.POST['SO2'])
        o2 = float(request.POST['O2'])
        co2 = float(request.POST['CO2'])
        ntu = float(request.POST['NTU'])
        assim_nitrgen = float(request.POST['assim_nitrgen'])
        pecto_test = request.POST['pecto_test']
        index_of_filt = int(request.POST['index_of_filt'])
        fe = float(request.POST['Fe'])
        cu = float(request.POST['Cu'])
        sowing = request.POST['sowing']
        sorb_acid = float(request.POST['sorb_acid'])
        prot_stab = request.POST['prot_stab']
        delta = request.POST['delta']
        cold_stab = request.POST['cold_stab']
        h2o2 = float(request.POST['H2O2'])
        scheme = request.POST['scheme']
        other_proc = request.POST['other_proc']

        def f(x):
            if x == 'Изба':
                return 1
            elif x == 'Мостри':
                return 2
            elif x == 'Стабилизация':
                return 3
            elif x == 'Високоалкохолни напитки':
                return 4


        if not Assortment.objects.filter(name=assortment, year=assortment_year).exists():
            Assortment(name=assortment, year=assortment_year).save()

        id_assortment = Assortment.objects.filter(name=assortment, year=assortment_year)

        post = Main(id_category=f(category), date=helpers.getNow(), id_assortment=id_assortment[0].id, id_vessel=1, stage=stage, note=note,
                    num_protocol=num_protocol, batch=batch, alcohol=alcohol, sugar=sugar, titr_acids=titr_acids,
                    ph=ph, vol_acids=vol_acids, rel_weight=rel_weight, mal_acids=mal_acids, lactic_acids=lactic_acids,
                    total_ext=total_ext, so2=so2, o2=o2, co2=co2, ntu=ntu, assim_nitrgen=assim_nitrgen,
                    pecto_test=pecto_test, index_of_filt=index_of_filt, fe=fe, cu=cu, sowing=sowing, sorb_acid=sorb_acid,
                    prot_stab=prot_stab, delta=delta, cold_stab=cold_stab, h2o2=h2o2, scheme=scheme, other_proc=other_proc)

        post.save()

        table = MainTable(Main.objects.all())

        return render(request, 'table/table.html', {
            "table": table,
        })
    else:
        context = {
            'years': range(1900, 2025),
        }
        return render(request, 'table/addtotable.html', context)



def CellarView(request):
    if request.method == 'POST' and 'cellar_operation' in request.POST:
        assortment = request.POST['assortment_name']
        assortment_year = helpers.checkInt(request.POST['year'])
        stage = request.POST['stage']
        note = request.POST['note']
        alcohol = helpers.checkFloats(request.POST['alcohol'])
        sugar = helpers.checkFloats(request.POST['sugar'])
        titr_acids = helpers.checkFloats(request.POST['titr_acids'])
        ph = helpers.checkFloats(request.POST['pH'])
        vol_acids = helpers.checkFloats(request.POST['vol_acids'])
        rel_weight = helpers.checkFloats(request.POST['rel_weight'])
        mal_acids = helpers.checkFloats(request.POST['mal_acids'])
        lactic_acids = helpers.checkFloats(request.POST['lactic_acids'])
        so2 = helpers.checkFloats(request.POST['SO2'])
        o2 = helpers.checkFloats(request.POST['O2'])
        co2 = helpers.checkFloats(request.POST['CO2'])
        ntu = helpers.checkFloats(request.POST['NTU'])
        assim_nitrgen = helpers.checkFloats(request.POST['assim_nitrgen'])
        pecto_test = request.POST['pecto_test']

        if not Assortment.objects.filter(name=assortment, year=assortment_year).exists():
            Assortment(name=assortment, year=assortment_year).save()

        id_assortment = Assortment.objects.filter(name=assortment, year=assortment_year)[0].id
       #TODO: id_vessel needs to be discused
        post = Main(date=helpers.getNow(),id_category=1, id_assortment=id_assortment, id_vessel=1,
                    stage=stage, note=note, alcohol=alcohol, sugar=sugar, titr_acids=titr_acids,
                    ph=ph, vol_acids=vol_acids, rel_weight=rel_weight, mal_acids=mal_acids, lactic_acids=lactic_acids,
                    so2=so2, o2=o2, co2=co2, ntu=ntu, assim_nitrgen=assim_nitrgen,
                    pecto_test=pecto_test)

        post.save()

    table = CellarTable(Main.objects.raw('''SELECT a.id, a.`date`, a.`id_vessel`, CONCAT(b.`name`,' ', b.`year`) AS 'assort', a.`stage`, a.`note`, a.`alcohol`,
    a.`sugar`, a.`titr_acids`, a.`pH`, a.`vol_acids`, a.`rel_weight`, a.`mal_acids`, a.`lactic_acids`, a.`SO2`, a.`O2`,
    a.`CO2`, a.`NTU`, a.`assim_nitrgen`, a.`pecto_test`
    FROM main a
    LEFT JOIN assortment b ON a.id_assortment = b.id'''))
    return render(request, 'table/cellar.html', {
        "table": table,
        "years": range(1900, 2025),
    })
