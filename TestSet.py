
class TestCase(object):

    def __init__(self, parameters):
        """
        :param parameters: A list containing TestFactor objects
        :return: this
        """
        self.components = parameters
        self.tc_len = len(parameters)
        self.tc_array = [None] * self.tc_len
        self.val_to_index_map = dict()


        for val_list, count in zip([component.get_values_list() for component in self.components], range(self.tc_len)):
            for value in val_list:
                self.val_to_index_map[value] = count

    def __contains__(self, item):
        return item in self.tc_array

    def get_uncovered_parameters_set(self):
        """
        :return: a set with TestFactor objects that are uncovered in this test case
        """
        return frozenset(self.components[i] for i in range(self.tc_len) if self.tc_array[i] is None)

    def add_slot(self, slot):
        """
        Adds the slot contents (values) to this test case
        :param slot:
        :return: void
        """
        for val in slot:
            # TODO - Check that the value is not yet assigned
            self.tc_array[self.val_to_index_map[val]] = val

    def get_values_list(self):
        return [val for val in self.tc_array if val is not None]

    def __repr__(self):
        pass #TODO
