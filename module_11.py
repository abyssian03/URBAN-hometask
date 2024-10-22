def introspection_info(obj):
    methods = []
    method_wrappers = []
    builtin_functions_or_methods = []
    undef = []
    dictionary = {}
    others = {}
    for attribute in dir(obj):
        if attribute == '__class__':
            print("class:", getattr(obj, attribute))
        elif attribute == '__init__':
            continue
        elif attribute == '__dict__':
            dictionary.update(getattr(obj, attribute))
            print('dict items (attribute, key):', *dictionary.items())
            continue
        s = str(type(getattr(obj, attribute)))
        if s == "<class 'method'>":
            methods.append(attribute)
        elif s == "<class 'method-wrapper'>":
            method_wrappers.append(attribute)
        elif s == "<class 'builtin_function_or_method'>":
            builtin_functions_or_methods.append(attribute)
        elif s == "<class 'NoneType'>":
            undef.append(attribute)
        else:
            others.update({attribute: getattr(obj, attribute)})
    print("special methods:", *methods)
    print("method wrappers:", *method_wrappers)
    print("builtin functions or methods:", *builtin_functions_or_methods)
    print("undefined:", *undef)
    for key in dictionary:
        del others[key]
    other_attributes = others.items()
    print("other attributes:", *other_attributes)

class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def destroy(self):
        print(self.name, "разрушен")
        del self

lenin_house = House('Дом Ленина', 4)
introspection_info(lenin_house)
