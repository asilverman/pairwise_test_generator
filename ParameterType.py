
class Parameter:
    val_count = 0

    def __init__(self, string_declaration):
        tokens = string_declaration.split(':')
        self.name = tokens[0]
        self.value_names = tokens[1].split(',')
        self.value_list = range(Parameter.val_count, Parameter.val_count + len(self.value_names))
        Parameter.val_count += len(self.value_names)

    def get_name(self):
        return self.name

    def get_values_list(self):
        return self.value_list

    def __repr__(self):
        return self.name + ': ' + ', '.join(self.value_names)

    def get_value_dict(self):
        return dict(zip(self.value_list, self.value_names))


class CompoundParameter:
    pass
