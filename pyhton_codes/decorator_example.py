# input = 'India'
def dec_func(func):
    def wraper_func(*args):
        res = func(*args)
        output=''
        for char in res:
            if char.lower() in 'aeiou':
                output=output+'z'
            else:
                output=output+char
        
        return output
    return wraper_func

@dec_func
def printing(var):
    return var


def main():
    print(printing("India"))
main()