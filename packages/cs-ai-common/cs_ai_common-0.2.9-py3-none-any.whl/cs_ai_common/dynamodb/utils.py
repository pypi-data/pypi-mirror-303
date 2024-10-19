def build_update_expression(kwargs: dict) -> str:
    update_expression = "set "
    for key in kwargs.keys():
        update_expression += f"#{key} = :{key}, "
    return update_expression[:-2]

def build_expression_attribute_names(kwargs: dict) -> dict:
    expression_attribute_names = {}
    for key in kwargs.keys():
        expression_attribute_names[f"#{key}"] = key
    return expression_attribute_names

def build_expression_attribute_values(kwargs: dict) -> dict:
    expression_attribute_values = {}
    for key, value in kwargs.items():
        expression_attribute_values[f":{key}"] = {
            'S': value
        }
    return expression_attribute_values