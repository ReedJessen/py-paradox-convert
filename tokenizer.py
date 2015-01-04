__author__ = 'peter'


def tokenize(inputstring):
        result = []
        if inputstring is None or inputstring == "":
            return result
        buffer = ""
        comment = False
        quotedstring = False
        for i in range(0, len(inputstring)):
            if inputstring[i] == '"':
                quotedstring = not quotedstring
            if inputstring[i] == '#':
                comment = True
            if inputstring[i] == '\n' and comment:
                comment = False
            if comment:
                continue
            if inputstring[i] in ['=', '{', '}', '\n', '\t'] or (inputstring[i] == ' ' and not quotedstring):
                addition = buffer.strip()
                if addition not in ["", '"', "\n", "\r", " ", "\t", "#"]:
                    result.append(addition.replace('"','',2))
                addition = "" + inputstring[i]
                if addition not in ["", '"', "\n", "\r", " ", "\t", "#"]:
                    result.append(addition.replace('"','',2))
                buffer = ""
            else:
                buffer += inputstring[i]
        if len(buffer) > 0:
            result.append(buffer.strip().replace('"','',2)) #flush the buffer
        return result