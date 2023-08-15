# views.py

from django.shortcuts import render, redirect
from .models import PolicyModel

def createData(request):
    if request.method == 'POST':
        # Retrieve form data from the request.POST dictionary
        # policy_making_process = request.POST.get('policy_making_process')
        user_name = request.POST.get('user_name')
        policy_choice = request.POST.get('policy_choice')

        justified_yes = request.POST.get('justified_yes')
        justified_no = request.POST.get('justified_no')
        justified_comment = request.POST.get('justified_comment')
        justified_file = request.FILES.get('justified_file')

        redistributive_yes = request.POST.get('redistributive_yes')
        redistributive_no = request.POST.get('redistributive_no')
        redistributive_comment = request.POST.get('redistributive_comment')
        redistributive_file = request.FILES.get('redistributive_file')

        practical_yes = request.POST.get('practical_yes')
        practical_no = request.POST.get('practical_no')
        practical_comment = request.POST.get('practical_comment')
        practical_file = request.FILES.get('practical_file')

        interventional_yes = request.POST.get('interventional_yes')
        interventional_no = request.POST.get('interventional_no')
        interventional_comment = request.POST.get('interventional_comment')
        interventional_file = request.FILES.get('interventional_file')

        cost_yes = request.POST.get('cost_yes')
        cost_no = request.POST.get('cost_no')
        cost_comment = request.POST.get('cost_comment')
        cost_file = request.FILES.get('cost_file')

        finance_yes = request.POST.get('finance_yes')
        finance_no = request.POST.get('finance_no')
        finance_comment = request.POST.get('finance_comment')
        finance_file = request.FILES.get('finance_file')

        # Create or save your model instance with the form data
        instance = PolicyModel.objects.create(
            # policy_making_process=policy_making_process,
            user_name=user_name,
            policy_choice = policy_choice,

            justified_yes=bool(justified_yes),
            justified_no=bool(justified_no),
            justified_comment=justified_comment,
            justified_file=justified_file,

            redistributive_yes=bool(redistributive_yes),
            redistributive_no=bool(redistributive_no),
            redistributive_comment=redistributive_comment,
            redistributive_file=redistributive_file,

            practical_yes=bool(practical_yes),
            practical_no=bool(practical_no),
            practical_comment=practical_comment,
            practical_file=practical_file,

            interventional_yes=bool(interventional_yes),
            interventional_no=bool(interventional_no),
            interventional_comment=interventional_comment,
            interventional_file=interventional_file,

            cost_yes=bool(cost_yes),
            cost_no=bool(cost_no),
            cost_comment=cost_comment,
            cost_file=cost_file,

            finance_yes=bool(finance_yes),
            finance_no=bool(finance_no),
            finance_comment=finance_comment,
            finance_file=finance_file,
        )
        instance.save()

        # Redirect to a success page or to the admin change view of the created instance
        # For example, redirect to the admin change view of the created instance:
        return redirect('success')

    return render(request, 'index.html')

def successpage(request):
    return render(request,'success.html')

