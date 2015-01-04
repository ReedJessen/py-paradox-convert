__author__ = 'peter'


def deserialize(tokens):
    def __evaluate_atom(phrase):
        return {phrase[0] : phrase[2] }
    result = []
    i = 0
    while i < len(tokens):
        if tokens[i] == '=' and tokens[i+1] != '{':
            result.append(__evaluate_atom([result.pop(),tokens[i],tokens[i+1]]))
            i = i + 1
        elif tokens[i] == '}':
            phrase = []
            while (result[-1] != '{'):
                phrase.insert(0,result.pop())
            result.pop()
            if result[-1] == '=':
                result.pop()
                result.append(__evaluate_atom([result.pop(),'=',phrase]))
            else:
                result.append(phrase)
        else:
            result.append(tokens[i])
        i = i + 1
    return result


