# funtions basics

def double_it(number):
    return 2*number

print double_it (2)

print double_it (3.5)

print double_it ('two')

# hypotenuse

def calc_hypo(a,b):
    hypo = ((a*a)+(b*b))**0.5
    return hypo

print calc_hypo(3,4) 

# improve code adding checks
def calc_hypo(a,b):
    if type(a) not in (int,float) or type(b) not in (int,float):
        print "bad argument"
        return False
    if a < 0 or b < 0:
        print "bad argument"
        return False

    hypo = ((a*a)+(b*b))**0.5
    return hypo

print calc_hypo(0, -2)
print calc_hypo("hi", "bye")
print calc_hypo(5,6)

