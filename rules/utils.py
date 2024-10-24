import re

''' Create new data type using Node and use  it to create a tree structure 
re (regular expression) module of python for checking  the pattern of the string and  return a match object if the string matches the pattern, otherwise return None '''


class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left       # Reference to the left child (Node)
        self.right = right     # Reference to the right child (Node)
        self.value = value     # Value for operand nodes

    def __repr__(self):
        if self.type == "operand":
            return f"Operand(value={self.value})"
        return f"Operator(type={self.type}, left={self.left}, right={self.right})"

def parse_condition(condition):
    
    match = re.match(r'(\w+)\s*([<>=!]+)\s*(.+)', condition.strip())
    if match:
        attribute, operator, threshold = match.groups()
        
        threshold = threshold.strip("'\"") if isinstance(threshold, str) else threshold
        return Node("operand", value={"attribute": attribute, "operator": operator, "threshold": threshold})
    raise ValueError(f"Invalid condition: {condition}")

def create_rule(rule_string):
    """Creates an AST from a rule string."""
    try:
       
        rule_string = rule_string.replace(" AND ", " and ").replace(" OR ", " or ")
        rule_string = re.sub(r'\s+', ' ', rule_string).strip()

       
        conditions = []
        operators = []
        tokens = re.split(r'(\band\b|\bor\b|\(|\))', rule_string)

        current_conditions = []
        for token in tokens:
            token = token.strip()
            if not token:
                continue
            if token == '(':
               
                current_conditions.append([])
            elif token == ')':
               
                if current_conditions:
                    conditions.append(current_conditions.pop())
            elif token in ("and", "or"):
                operators.append(token)
            else:
            
                condition_node = parse_condition(token)
                if current_conditions:
                    current_conditions[-1].append(condition_node)
                else:
                    conditions.append([condition_node])

        # Combine conditions and operators into an AST
        root = None
        for i in range(len(conditions)):
            if i > 0:
                # Create an operator node between conditions
                operator_node = Node("operator", left=root, right=conditions[i][0], value=operators[i - 1])
                root = operator_node
            else:
                root = conditions[i][0]

        return root  
    except Exception as e:
        raise ValueError(f"Invalid rule: {e}")

def evaluate_rule(ast_node, data):
   
    if ast_node.type == "operand":
        # Extract the comparison logic
        operand_value = data.get(ast_node.value["attribute"])
        operator = ast_node.value["operator"]
        threshold = ast_node.value["threshold"]

        if operator == '=':
            return operand_value == threshold
        elif operator == '>':
            return operand_value > int(threshold)
        elif operator == '<':
            return operand_value < int(threshold)
        raise ValueError(f"Invalid operator: {operator}")

    elif ast_node.type == "operator":
        left_result = evaluate_rule(ast_node.left, data)
        right_result = evaluate_rule(ast_node.right, data)
        
        if ast_node.value == "and":
            return left_result and right_result
        elif ast_node.value == "or":
            return left_result or right_result
        raise ValueError(f"Invalid operator in AST: {ast_node.value}")


# if __name__ == "__main__":

    # rule_string = "age > 30 AND department = 'Sales'"
    # ast_root = create_rule(rule_string)
    # print(ast_root)  # Display the AST

    # # Evaluate the rule against user data
    # user_data = {"age": 35, "department": "Sales"}
    # result = evaluate_rule(ast_root, user_data)
    # print(f"Evaluation Result: {result}")  # Should print True
