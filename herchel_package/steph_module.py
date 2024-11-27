import pyjokes

def tell_joke():
    joke = pyjokes.get_joke()
    print('Here is a joke for you:', joke)
    print("\n")
