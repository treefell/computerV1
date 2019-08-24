#!/usr/bin/python

import sys
import re
from fractions import Fraction

""" 1 * X^0 - 9.3 * X^1 +4.2 *X^2 = -2*X^0"""
def check_equa(raw_eq):
    pattern = "(\s*([+-]?)\s*(\d+[.]?\d*)\s*[*]\s*([Xx][\^]){1}[0123])*\s*=((\s*([+-]?)\s*(\d+[.]?\d*)\s*[*]\s*([Xx][\^]){1}[0123])+|(\s*0))"
    if None == re.match(pattern, raw_eq):
        return 0
    else:
        return 1

"""(\s*([+-]?)\s*(\d+[.,]?\d*)\s*[*]\s*(?:[Xx][\^]){1}(\d+){1}([^=]))=(\s*([+-]?)\s*(\d+[.]?\d*)\s*[*]\s*(?:[Xx][\^]){1}(\d+))*"""
def equa_param(eq):
    pattern = "(.*)=(.*)"
    catch_poly = "\s*([+-]?)\s*(\d+[.]?\d*)\s*[*]\s*(?:[Xx][\^]){1}([0123])"
    equa_split = re.findall(pattern, eq)
    result = ["",""]
    result[0] = re.findall(catch_poly, str(equa_split[0][0]))
    result[1] = re.findall(catch_poly, str(equa_split[0][1]))
    return result

"""1st for can be switch for a switch case
entry[x][0] = sign entry[x][1] = coef entry[x][2] = power
data[][] = """
def reduc_data(entry):
    i = 0
    j = 0
    data = []
    for i in range(4):
        tmp = ["+", 0.0, i]
        for j in range(len(entry[0])):
            if (int(entry[0][j][2]) == i):
                if (entry[0][j][0] == "-"):
                    tmp[1] -= float(entry[0][j][1])
                else :
                    tmp[1] += float(entry[0][j][1])
        j = 0
        for j in range(len(entry[1])):
            if (int(entry[1][j][2]) == i):
                if (entry[1][j][0] == "-"):
                    tmp[1] += float(entry[1][j][1])
                else:
                    tmp[1] -= float(entry[1][j][1])
        data.append(tmp)
    return (data)

def get_degree(data):
    j = 2
    while (data[j][1] == 0 and j > 0) :
        j -= 1
    if data[3][1] != 0:
        print "3rd degree equation"
        exit()
    return j

def print_equa(equa_list):
    equa_prt=""
    nb = 0
    for j in range(len(equa_list)) :
        if equa_list[j][1] != 0:
            if equa_list[j][1] > 0 and nb != 0:
                equa_prt += "+"
            else :
                nb += 1
            equa_prt += str('{0:g}'.format(equa_list[j][1])) + "*X^" +str(equa_list[j][2])
    equa_prt += " = 0"
    return (equa_prt)


def square_root(nb):
    if nb == 0.0:
        return 0.0
    elif nb < 0 :
        print "error"
        exit()
    elif nb < 1 :
        print "this square root function doesn't work on number under 1"
        exit()
    else :
        start = 0.0
        end = nb
        prevMid = 0
        m2 = 0.0
        while m2 != nb and abs(m2 - nb) > 0.000005 :
            mid = (start + end)/2.0
            m2 = mid * mid
            if m2 == nb :
                return mid
            elif m2 < nb:
                start = mid
            else :
                end = mid
        mid = float("{0:.5f}".format(mid))
        return mid

def resolve_equa(table):
    c = float(table[0][1])
    b = float(table[1][1])
    a = float(table[2][1])
    if a == 0 :
        if (b == 0 and c != 0):
            print "Equation don't have solution"
        elif(b == 0 and c == 0):
            print "Any number is solution"
        else:
            print "equation lineary"
            print "The solution is:"
            print str('{0:g}'.format(-c/b))
    else:
        det = (b * b) - (4 * a * c)
        a *= 2
        print "discriminant", '{0:g}'.format(det)
        if det > 0:
            if det < 1:
                print "sorry this program cam't give the answer failling squareroot function for number under 1"
                exit()
            print "The solution are:"
            print "1st root", str('{0:g}'.format((-b + (square_root(det)))/a))
            print "2nd root", str('{0:g}'.format((-b - (square_root(det)))/a))
        elif det < 0:
            det *= -1
            print "No real solution:"
            print "1st complex root",str('{0:g}'.format(-b/a)), "+",  str('{0:g}'.format(square_root(det)/a)), "i"
            print "2nd complex root", str('{0:g}'.format(-b/a)), "-",  str('{0:g}'.format(square_root(det)/a)), "i"
        else:
            print "unique root",str('{0:g}'.format(-b/a))


"""Set the escape on wrong polynom"""
if __name__ =='__main__':
    if len(sys.argv) > 1:
        equa = sys.argv[1]
        equa= ''.join(equa.split())
        """print "equa", equa"""
        if check_equa(equa) == 0:
            print "rejected argument, expected: \"1*X^0 - 9.3*X^1 + 4.2*X^2 = -2*X^0\""
            print "variant format: \"1*X^2 - 9.3*X^1 + 4.2*X^2 = 0\""
            exit()
        else :
            table = reduc_data(equa_param(equa))
            degree = get_degree(table)
            print "Reduced form:", print_equa(table)
            print "Polynomial degree:", degree
            resolve_equa(table)

