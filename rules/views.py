from django.shortcuts import render, redirect, get_object_or_404
from .models import Rule
from .forms import RuleForm
from .utils import create_rule, evaluate_rule

def rule_list(request):
    rules = Rule.objects.all()
    return render(request, 'rule_list.html', {'rules': rules})

def rule_create(request):
    if request.method == 'POST':
        form = RuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rule_list')
    else:
        form = RuleForm()
    return render(request, 'rule_form.html', {'form': form})

def rule_evaluate(request, pk):
    rule = get_object_or_404(Rule, pk=pk)
    ast_node = create_rule(rule.rule_string)

    if request.method == 'POST':
        data = {
            'age': int(request.POST['age']),
            'department': request.POST['department'],
            'salary': int(request.POST['salary']),
            'experience': int(request.POST['experience']),
        }
        result = evaluate_rule(ast_node, data)
        return render(request, 'rule_evaluate.html', {'rule': rule, 'result': result})

    return render(request, 'rule_evaluate.html', {'rule': rule})
