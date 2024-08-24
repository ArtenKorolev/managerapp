from abc import abstractmethod, ABC


class Converter(ABC):
    @abstractmethod
    def convert(self) -> str: ...

    @staticmethod
    def _set_quotes_if_string(arg):
        if type(arg) == str:
            return f'"{arg}"'
        return str(arg)


class ArgsToSqlStrConverter(Converter):
    def convert(self, *args) -> str:
        args_string = ''

        for i in args:
            if i == 'all':
                return '*'
            args_string += f'{self._set_quotes_if_string(i)},'

        return args_string.strip(',')


class KwargsToSqlStrConverter(Converter):
    def convert(self, **kwargs) -> str:
        kwargs_string = ''

        for key, value in kwargs.items():
            kwargs_string += f'{key}={self._set_quotes_if_string(value)},'

        return kwargs_string.strip(',')


class KwargsToInsertSqlStrConverter(Converter):
    def convert(self,**kwargs) -> list[str]:
        params_str = ''
        values_str = ''

        for key, value in kwargs.items():
            params_str += f'{key},'
            values_str += f'{self._set_quotes_if_string(value)},'

        return [params_str.strip(','), values_str.strip(',')]

