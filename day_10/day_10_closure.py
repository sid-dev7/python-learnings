#closure (referenc of inner function in outer)

def outer(tag):

    #local
    def inner(data):
        print(f"<{tag}>{data}</{tag}>")
    return inner
#function = inner
function = outer('h1')
print(f"function: {function}, type = {type(function)}")
function('header line 1') 

div = outer('div')
div('division 1')
div('division 2')