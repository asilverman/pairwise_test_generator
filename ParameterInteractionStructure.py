import itertools


class Slot:

    def __init__(self, tup):

        self.data = tup
        self.size = len(tup)
        self.is_covered = False  # can be covered\excluded == True or uncovered == False

    def __repr__(self):
        return "Slot: " + str(self.data)

    def set_covered(self, bool_val=True):
        self.is_covered = bool_val

    def __iter__(self):
        return iter(self.data)


def gen_slots(values_list):
    slot_list = []
    for comb in itertools.product(*values_list):
        slot_list.append(Slot(list(comb)))
    return slot_list


class ParameterInteractionStructure:

    def __init__(self, parameters):
        self.member_parameters = frozenset(parameters)
        self.slots = gen_slots([x.get_values_list() for x in parameters])

    def is_covered(self):
        return all([slot.is_covered for slot in self.slots])

    def __repr__(self):
        return ''.join([x.get_param_name() for x in self.member_parameters])

    def get_uncovered_slots_count(self):
        return sum(not slot.is_covered for slot in self.slots)

    def get_next_slot(self):
        return next(slot for slot in self.slots if not slot.is_covered)

    def get_params_set(self):
        return self.member_parameters

    def get_slots(self):
            return [x for x in self.slots]
