class multi_set:

    # def add_element(self, elem):

    def Add_element(setA, element):
        sA = list(setA)
        sA.append(element)
        sA.sort()
        # Making the format
        result = '{' + str(setA)[1:-1] + '} + ' + str(element) + ' = {' + str(sA)[1:-1] + '}'
        return result

    print(Add_element({1, 2, 3}, 1))
