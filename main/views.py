from django.shortcuts import render
from django.http import HttpResponse
import json  # Import the json module
from .forms import InsuranceForm

# Create your views here.
def index(request):
    return render(request, "main/index.html")

def products_accident(request):
    return render(request, 'main/products_accident.html')

def checkout(request):
    return render(request, 'main/Checkout.html')

def cart(request):
    return render(request, 'main/cart.html')


def products_maid(request):
    return render(request, 'main/products_maid.html')

def products_travel(request):
    return render(request, 'main/products_travel.html')


def load_insurance_data():
    with open("C:\\Users\\shubh\\Desktop\\InsureMe\\insure_me\\main\\static\\main\\data_maidInsurance.json", 'r') as file:
        data = json.load(file)
    return data

def maid_insurance(request):
    policies = load_insurance_data()

    selected_policies = []
    if request.method == 'POST':
        policy1_id = request.POST.get('policy1')
        policy2_id = request.POST.get('policy2')
        if policy1_id and policy2_id:
            selected_policies = [policies[policy1_id], policies[policy2_id]]

    return render(request, 'main/maid_insurance.html', {'policies': policies, 'selected_policies': selected_policies})

def load_accident_insurance_data():
    with open("C:\\Users\\shubh\\Desktop\\InsureMe\\insure_me\\main\\static\\main\\data_accidentInsurance.json", 'r') as file:
        data = json.load(file)
    return data


def accident_insurance(request):
    policies = load_accident_insurance_data()
    selected_policies = []
    if request.method == 'POST':
        policy1_id = request.POST.get('policy1')
        policy2_id = request.POST.get('policy2')
        if policy1_id in policies and policy2_id in policies:
            selected_policies = [policies[policy1_id], policies[policy2_id]]
    return render(request, 'main/accident_insurance.html', {'policies': policies, 'selected_policies': selected_policies})

def load_travel_insurance_data():
    with open("C:\\Users\\shubh\\Desktop\\InsureMe\\insure_me\\main\\static\\main\\data_travelInsurance.json", 'r') as file:
        data = json.load(file)
    return data

def travel_insurance(request):
    all_policies = load_travel_insurance_data()
    selected_policies = []

    if request.method == 'POST':
        country = request.POST.get('country')
        policy1_id = request.POST.get('policy1')
        policy2_id = request.POST.get('policy2')
        if policy1_id and policy2_id and country:
            selected_policies.append(all_policies[country][policy1_id])
            selected_policies.append(all_policies[country][policy2_id])

    return render(request, 'main/travel_insurance.html', {
        'all_policies': all_policies,
        'selected_policies': selected_policies
    })

def load_insurance_rec_data():
    with open(f'C:\\Users\\shubh\\Desktop\\InsureMe\\insure_me\\main\\static\\main\\recommendation.json', 'r') as file:
        data = json.load(file)
    return data

def recommend_policy(request):
    print("Something")
    print(request.method)
    insurance_data = load_insurance_rec_data()  # Ensure this returns a properly formatted dictionary
    if request.method == 'POST':
        form = InsuranceForm(request.POST)
        if form.is_valid():
            print("In")
            category = form.cleaned_data['category']
            max_premium = form.cleaned_data.get('max_premium', float('inf'))  # Handle None case
            age = form.cleaned_data.get('age')  # Directly get age as integer

            filtered_policies = []
            for company, categories in insurance_data.items():
                policies = categories.get(category, [])
                for policy in policies:
                    # Handle premium comparison based on category
                    if category == 'Critical Illness' and age is not None:
                        age_group_premiums = policy.get('age_group_premium', {})
                        matched = False
                        for age_range, premium in age_group_premiums.items():
                            age_low, age_high = map(int, age_range.split('-'))
                            if age_low <= age <= age_high:
                                # Check if the age-specific premium is within the maximum premium
                                if premium <= max_premium:
                                    matched = True
                                    break
                        if matched:
                            filtered_policies.append(policy)
                    elif category != 'Critical Illness':
                        policy_premium = policy.get('monthly_premium', float('inf'))  # Use inf as default
                        if policy_premium <= max_premium:
                            filtered_policies.append(policy)

            # Sort and limit policies based on sum_insured
            filtered_policies.sort(key=lambda x: x.get('sum_insured', 0), reverse=True)
            top_policies = filtered_policies[:3]

            return render(request, 'main/recommendations.html', {'policies': top_policies, 'category': category})
        else:
            print("Form is not valid")
            return render(request, 'main/insurance_form.html', {'form': form})
    else:
        form = InsuranceForm()
        return render(request, 'main/insurance_form.html', {'form': form})
