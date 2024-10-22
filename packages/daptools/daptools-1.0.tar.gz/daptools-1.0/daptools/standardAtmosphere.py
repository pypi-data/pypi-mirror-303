# /usr/bin/python3
# -*- coding: utf-8 -*-
"""
standardAtmosphere - Implements 1976 NASA standard atmosphere model to height 84 km.
Based on Public Domain Aeronautical Software

Created at 03.08.21 20:17

@author: David Potucek

ICAO Standard atmosphere
MSA (Mezinarodni standardni atmosfera)
Model předpokládá že:
    - atmosféra je homogenní, složení vzduchu 78 % dusík, 21 % kyslík, 1 % ostatní plyny
    - vzduch je ideální plyn, tj. platí stavová rovnice plynů
    - tíhové zrychlení je konstantní g = 9,81 m/s2
    - podmínky ve výšce H = 0 m (při hladině moře)
        - tlak vzduchu 1013,25 hPa
        - hustota vzduchu 1,225 kg/m3
        - teplota vzduchu 15 °C
    - až do výšky 11 km (tj. až do tropopauzy) klesá teplota o 6,5 stupně Celsia na 1 000 m, potom zůstává konstantní -56,5 °C"""

import math, sys

#   S E A   L E V E L   C O N D I T I O N S
STANDARD_PRESSURE = 1013.25     # [N/m^2]
STANDARD_TEMPERATURE = 288.15   # [K]
STANDARD_DENSITY = 1.2257       # [kg/m^3]
ASOUNDZERO = 340.294    # speed of sound at S.L.  m/sec
MUZERO = 1.7894E-5      # viscosity at sea-level,
ETAZERO = 1.4607E-5     # kinetic viscosity at sea-level,
KAPPA_ZERO = 0.025326   # thermal coeff. at sea-level [watts per meter per kelvin]


def simpleAtm(alt):
    '''Prijme vysku v metrech a vrati hustotu[kg/m^3], tlak[hPa] a teplotu[C] do 11km.
    :param alt [m]
    :return hustota, tlak, teplota
        hustota [kg/m^3]
        tlak [hPa]
        teplora [C]
    '''
    if (alt > 11000):
        print('moc velka vyska, nepocitam.')
        sys.exit(0)
    else:
        from mathPhys import KELVIN2C
        tepl = 15 - 0.0065 * alt
        temp = (1 - alt/44308)
        tlk = 1013.25 * pow(temp, 5.2553)
        hust = 1.225 * pow(temp, 4.2553)
        soundSpeed = 20.05 * math.sqrt(tepl + KELVIN2C)
    return hust, tlk, tepl, soundSpeed


def printValues(a, t, tl, h, spd):
    print('vyska nastavena na {} m'.format(a))
    print('v této výšce jsou parametry standardní atmosféry:')
    print('teplota: {} [C]'.format(t))
    print('tlak: {:0.2f} [hPa]'.format(tl))
    print('hustota: {:0.4f} [kg/m^3]'.format(h))
    print('rychlost zvuku: {:0.4f} [m/s]'.format(spd))


if __name__ == "__main__":
    # alt = numUsrIn('zadej vysku [km]', 3)
    alt = 500
    hust, tlk, tplt, spd = simpleAtm(alt)
    printValues(alt, tplt, tlk, hust, spd)