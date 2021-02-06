from lib.action import CiscoSparkAction

__all__ = [
    'GenericAction'
]


class GenericAction(CiscoSparkAction):

    def run(self, accessor, method_name, **kwargs):
        a = getattr(self.connection, accessor)
        result = getattr(a, method_name)(**kwargs)
        if method_name == 'list':
            result = list(result)  # iterate generator
        if isinstance(result, list):
            return [x.json_data for x in result]  # pylint: disable=no-member
        else:
            return result.json_data  # pylint: disable=no-member
