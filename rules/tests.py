from django.test import TestCase
from .models import Rule
from .utils import create_rule, evaluate_rule, combine_rules

class RuleEngineTest(TestCase):
    def test_create_rule(self):
        rule_string = "((age > 30 AND department = 'Sales'))"
        ast = create_rule(rule_string)
        self.assertIsNotNone(ast)

    def test_evaluate_rule(self):
        rule_string = "((age > 30 AND department = 'Sales'))"
        ast = create_rule(rule_string)
        data = {'age': 35, 'department': 'Sales'}
        self.assertTrue(evaluate_rule(ast, data))

    def test_combine_rules(self):
        rule1 = create_rule("((age > 30 AND department = 'Sales'))")
        rule2 = create_rule("((age < 25 AND department = 'Marketing'))")
        combined_ast = combine_rules([rule1, rule2])
        
        data1 = {'age': 35, 'department': 'Sales'}
        data2 = {'age': 22, 'department': 'Marketing'}
        
        # Both individual rules should still evaluate correctly
        self.assertTrue(evaluate_rule(rule1, data1))
        self.assertTrue(evaluate_rule(rule2, data2))
        
        # The combined rule should handle both conditions
        self.assertTrue(evaluate_rule(combined_ast, data1))
        self.assertTrue(evaluate_rule(combined_ast, data2))
