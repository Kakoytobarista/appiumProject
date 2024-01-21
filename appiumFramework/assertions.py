class Assertions(object):

    @staticmethod
    def assert_are_equal(expected_result,
                         actual_result):
        assert expected_result == actual_result, ('Unexpected result value! '
                                                  'Expected: {}. '
                                                  'Actual: {}'.format(expected_result,
                                                                      actual_result))

    @staticmethod
    def assert_is_not_none(expected_result):
        assert expected_result is not None, ('Unexpected value in data, expected not None,'
                                             'data: {data}'.format(data=expected_result))

    @staticmethod
    def assert_are_not_equal(expected_result,
                             actual_result):
        assert expected_result != actual_result, ('Unexpected result value! '
                                                  'Expected: {}. '
                                                  'Actual: {}'.format(expected_result,
                                                                      actual_result))

    @staticmethod
    def assert_value_is_not_empty(dictionary, key):
        if key not in dictionary:
            raise KeyError("Key: {} not found in dictionary".format(key))
        if not dictionary[key]:
            raise ValueError("Value for key: {} is empty".format(key))

    @staticmethod
    def assert_key_is_present(dictionary, key):
        if key not in dictionary:
            raise KeyError("Key: {} not found in dictionary".format(key))

    @staticmethod
    def assert_dict_is_not_empty(dictionary):
        assert dictionary, "Dictionary: {} is empty".format(dictionary)

    @staticmethod
    def assert_is_instance(first_obj, second_obj):
        assert isinstance(first_obj, second_obj), "Object {first_obj} is not an instance of {second_obj}".format(
            first_obj=first_obj, second_obj=second_obj
        )

    @staticmethod
    def assert_is_include_value(data, include_value):
        assert include_value in data, ("Data does not contain include value. data: {data}, include_value: "
                                       "{include_value}".format(data=data, include_value=include_value))
