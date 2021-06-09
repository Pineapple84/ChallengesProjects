'''
  I'm not sure is this the right method and formula to calculate Fermat's Theorem.
'''

def check_fermat(a,b,c,n):

    a_exp = a**n
    b_exp = b**n
    c_exp = c**n
    formula_fermat = a_exp + b_exp
    
    if n > 2 and c_exp == formula_fermat:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

a = input("Enter number a: ")
b = input("Enter number b: ")
c = input("Enter number c: ")
n = input("Enter exponential n: ")
