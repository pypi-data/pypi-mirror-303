import ast


def extractHyperParamstoFile(filename):
    with open(filename, "r") as file:
        tree = ast.parse(file.read(), filename)

    hyperParams_values = []

    class FunctionCallVisitor(ast.NodeVisitor):
        def __init__(self):
            self.variables = {}
            super().__init__()

        def visit_Assign(self, node):
            value = self.get_node_value(node.value)
            for target in node.targets:
                if isinstance(target, ast.Name):
                    self.variables[target.id] = value
            self.generic_visit(node)

        def visit_Call(self, node):
            if isinstance(node.func, ast.Attribute) and node.func.attr == "train":
                for keyword in node.keywords:
                    if keyword.arg == "hyperParams":
                        value = self.get_node_value(keyword.value)
                        if isinstance(keyword.value, ast.Name):
                            var_name = keyword.value.id
                            value = self.variables.get(
                                var_name, f"Unknown variable {var_name}"
                            )
                        hyperParams_values.append(value)
            self.generic_visit(node)

        def get_node_value(self, node):
            if isinstance(node, ast.Dict):
                return {
                    self.get_node_value(k): self.get_node_value(v)
                    for k, v in zip(node.keys, node.values)
                }
            elif isinstance(node, ast.List):
                return [self.get_node_value(e) for e in node.elts]
            elif isinstance(node, ast.Constant):  # for Python 3.6+
                return node.value
            elif isinstance(node, ast.Str):  # for Python 3.5 and earlier
                return node.s
            elif isinstance(node, ast.Num):  # for Python 3.5 and earlier
                return node.n
            elif isinstance(node, ast.Name):
                return self.variables.get(node.id, f"Unknown variable {node.id}")
            # 추가적인 노드 타입 처리 가능
            else:
                return None

    visitor = FunctionCallVisitor()
    visitor.visit(tree)
    return hyperParams_values
