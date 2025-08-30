class BaseAssertions:

    def assert_data_in_data(self, act, exp):
        assert act in exp, (f'Объект {exp} не содержит в себе:\n'
                            f'{act}')

    def assert_data_equal_data(self, act, exp):
        assert act == exp, (f'Данные не идентичны!\n'
                            f'ОР: {exp}\n'
                            f'ФР: {act}')
