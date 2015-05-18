class CharField:

    def __init__(self, name, max_length, value):
        self.data_dict = {'name':name, 'max_length':max_length, 'value':value}
        

class TextField:

    def __init__(self, name, max_length, value):
        self.data_dict = {'name':name, 'max_length':max_length, 'value':value}
        

class IntergerField:

    def __init__(self, name, max_length, value):
        self.data_dict = {'name':name, 'max_length':max_length, 'value':value}
        

class ChoiceField:

    def __init__(self, name, max_length, value):
        self.data_dict = {'name':name, 'max_length':max_length, 'value':value}
        

class MultipleChoiceField:

    def __init__(self, name, max_length, value):
        self.data_dict = {'name':name, 'max_length':max_length, 'value':value}
        

class BooleanField:

    def __init__(self, name, value):
        self.data_dict = {'name':name, 'value':value}
        

            
    