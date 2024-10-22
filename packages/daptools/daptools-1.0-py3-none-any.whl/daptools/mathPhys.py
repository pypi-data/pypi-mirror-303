#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Sep 21, 2015

@author: David Potucek
'''
# konstanty
GRAV_CONST = 6.674 * (10 ** -11)    # [m^3/kg s^2]
GZERO = 9.80665                 #  sea level accel. of gravity [m/s^2]
AU = 1.495979 * (10 ** 11)      # [km]
M_Earth = 5.972 * (10 ** 24)    # [kg]
M_Sun = 1.989 * (10 ** 30)      # [kg]
EARTH_RADIUS_KM = 6378  # [km]
REARTH  = 6356.7523     # polar radius of the earth [km]
FT2METERS = 0.3048      # mult. ft. to get meters (exact)
KELVIN2RANKINE = 1.8    # mult deg K to get deg R
KELVIN2C = 273.15       # odecist od K
BETAVISC = 1.458E-6     # viscosity constant
SUTH    = 110.4         # Sutherland's constant, kelvins
AVOGADRO =  6.022169E26   # 1/kmol, Avogadro constant
BOLTZMANN = 1.380622E-23  # Nm/K, Boltzmann constant
BTU2JOULE = 1055.0      # mult BTU to get joules
RSTAR = 8314.32          # perfect gas constant, N-m/(kmol-K)


def fibonacci(pocet):
    """ Generator returning iterable sequence of Fibonacci. Accepts count of numbers to return.
    use:
    if type(fibonacci(1)) == types.GeneratorType:        # check for generator type, not mandatory ;)
        if __DEBUG__: print "fibonacci je generator!"
        for number in fibonacci(10):
            print number

    NOTE: first 3 numbers are always {0,1,1}
    """
    yield 0
    predchozi = 1
    yield predchozi
    dalsi = 1
    yield dalsi
    for i in range(2, pocet):
        predchozi, dalsi = dalsi, predchozi + dalsi
        yield dalsi


def __testFibonacci():
    for number in fibonacci(10):
        print(number)


def gravityBetweenBodies(m1, m2, distance):
    """returns gravity force between body1 and body2 at given distance.
    m1 = mass of body 1, m2 = mass of body 2, distance is distence between bodies."""
    return (GRAV_CONST * (m1 * m2) / (distance ** 2))


def __test_gravityBetweenBodies():
    power = gravityBetweenBodies(M_Earth, M_Sun, AU)
    print("gravity between sun and earth in 1 AU is {0} N".format(power))


def C2F(celsius):
    """converts celsius to fahrenheit temperature"""
    return (celsius * 9 / 5) + 32


def F2C(fahrenheit):
    """converts fahrenheit to celsius temperature """
    return (fahrenheit - 32) * 5 / 9

def K2C(temp):
    """Prepocte Kelvina na Celsia."""
    return temp - KELVIN2C

def C2K(temp):
    """Prepocte Celsia na Kelvina."""
    return temp + KELVIN2C

def degree2decimal(deg, min, sec, direction):
    """Bere koordinaty ve stupnich, minutach, sekundach a smeru a vraci cislo.
    Negativni koordinaty jsou zapad a jih."""
    decDeg = float(deg) + float(min)/60 + float(sec)/(60**2)
    if direction:
        if direction == 'W' or direction == 'S':
            decDeg *= -1
    return decDeg

def decimal2degree(decimal):
    """bere stupne jako cislo a prevadi z 50.319348 do notace 50°19'9.652".
      Smery (E/W/N/S) si pro zemepisne vypocty musi volajici udrzet sam."""
    d = int(decimal)
    md = abs(decimal - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return d, m, sd

def rad2deg(uhel):
    """ accepts radians, returns degree"""
    import math
    return uhel * 180 / math.pi


def deg2rad(uhel):
    """accepts degrees, returns radians"""
    import math
    return uhel * math.pi / 180

if __name__ == '__main__':
    #     __testFibonacci()
    #     __testTemperatureConversion()
    __test_gravityBetweenBodies()
