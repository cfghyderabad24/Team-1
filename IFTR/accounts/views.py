from django.shortcuts import render
from django.contrib.auth.models import User,auth
from accounts.models import *
# Create your views here.
def farmerForm(request):
    user = User.objects.filter(username="admin")[0]
    print(user.pk)
    if request.method == "POST":
        farm = Farmer.objects.create(f_id= user,f_name = "John Doe",
        f_pincode = 123456,
        f_contact_number = 1234567890)
        farm.save()
        area_ploughed = request.POST.get('areaPloughed')
        season = request.POST.get('season')
        crop_grown = request.POST.get('cropGrown')
        seeds_used = request.POST.get('variety-quantityUsed')
        date_seed_sown = request.POST.get('dateSeedSown')
        transplanting = request.POST.get('transplanting')
        irrigation_method = request.POST.get('irrigationMethod')
        fertilizers_used = request.POST.get('fertilizersUsed')
        date_harvesting = request.POST.get('dateHarvesting')
        yield_kg = request.POST.get('yieldKg')
        farmer_info = FarmerQuery( fq_id= farm,
            fq_area_ploughed=area_ploughed,
            fq_season=season,
            fq_crop_grown=crop_grown,
            fq_date_of_seed_sown=date_seed_sown,
            fq_transplanting=transplanting,
            fq_irrigation=irrigation_method,
            fq_fertilizers_used=fertilizers_used,
            fq_date_of_harvest=date_harvesting,
            fq_yield=yield_kg,
            fq_seeds_used=seeds_used
        )
        print(farmer_info)
        farmer_info.save()
        return render(request,'form.html')
    return render(request,'form.html')
