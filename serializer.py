__author__ = 'peter'


def serialize(tokens):
    def __map_atom(node,indentation=''):
        if isinstance(node,str):
            return node
        new_indentation = indentation + '\t'
        key = node.keys()[0]
        values = node.values()
        if len(values) == 1:
            if isinstance(values[0],dict):
                return key + '={\r\n' + new_indentation + __map_atom(values[0],new_indentation) + '\r\n' + indentation + '}'
            if isinstance(values[0],list):
                return key + '={\r\n' + new_indentation + __map_array(values[0],new_indentation) + '\r\n' + indentation + '}'
            else:
                return key + '=' + str(values[0])
        else:
            return key + '=' + __map_array(values,indentation)

    def __map_array(tokens,indentation=''):
        return ('\r\n' + indentation).join([__map_atom(x,indentation) for x in tokens])

    return __map_array(tokens)