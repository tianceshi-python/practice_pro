# encoding:utf-8

class MyAPP():
    def __init__(self):
        self.func_map = {}


    def register(self,name):
        def func_wrapper(func):
            self.func_map[name] = func
            return func

        return func_wrapper

    def call_method(self,name = None):
        func = self.func_map.get(name,None)
        if func is None:
            raise Exception ('No function registered against - ' + str(name))
        return func


app = MyAPP()

@app.register('/')
def main_page_func():
    return 'this is the main page.'

@app.register('/next_page')
def next_page_func():
    return 'this is the next page'


print(app.call_method('/'))
print(app.call_method('/next_page'))
