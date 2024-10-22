#!/usr/bin/python 3
# -*- coding: utf-8 -*-
'''
Implements spherical geodetic calculations.
Negative coordinates are west/south.

Created on 31/01/2018, 10:14

@author: David Potucek
'''

def parseCoordinates(coordinate):
    """posles koordinat ve formatu 50°19'9.652"E a vrati to cislo 50.319348
    Negative coordinates are west/south.
    Doesn't check input format."""
    import re
    import mathPhys
    parts = re.split('[°\'"]+', coordinate) # TODO - dodelat vstupni kontroly
    coord = mathPhys.degree2decimal(parts[0], parts[1], parts[2], parts[3])
    return coord

def __testParseCoordinates():
    from mathPhys import decimal2degree
    # print('prevadim {}'.format("""50°19'9.652"E"""))
    print('prevadim {}'.format("""50°19'9.652"E"""))
    c = parseCoordinates("""50°19'9.652"E""")
    print('vysledek je {}'.format(c))
    d = decimal2degree(c)
    print('a nazpet: {}'.format(d))

def formatDegreesTuple(degrees, kategorie = 'NA'):
    """posles tuple stupne, minuty, sekundy a optional kategorie(lat, lon, NA), vrati string
    reprezentaci."""
    if len(degrees) == 1:           # validace na pocet parametru
        stupne = degrees[0]
        minuty = 0
        sec = 0
    elif len(degrees) == 2:
        stupne = degrees[0]
        minuty = degrees[1]
        sec = 0
    elif len(degrees) == 3:
        stupne = degrees[0]
        minuty = degrees[1]
        sec = degrees[2]
    else:
        raise ValueError("incorrect number of arguments")
    return formatDegrees(stupne, minuty, sec, kategorie)

def formatDegrees(stupne, minuty, vteriny, kategorie = 'NA'):
    """Negative coordinates are west/south."""
    if kategorie == 'long':
        if stupne <= 0: direction = 'W'
        else: direction = 'E'
    elif kategorie == 'lat':
        if stupne <= 0: direction = 'S'
        else: direction = 'N'
    elif kategorie == 'NA':
        direction = ''
    else: raise ValueError("unknown parameter of latitude/longitude")
    return """{}°{}\'{:.2f}\"{}""".format(stupne, minuty, vteriny, direction)


class GreatCircleTrackSpherical():
    """Class representing a path from one point on earth to another on spherical Earth.
    Both points are defined as pair of coordinates.
    All these formulae are for calculations on the basis of a spherical earth (ignoring
    ellipsoidal effects) – which is accurate enough for most purposes. In fact, the
    earth is very slightly ellipsoidal; using a spherical model gives errors typically
    up to 0.3%.
    """

    def __init__(self, lat1, lon1, lat2, lon2):
        import mathPhys as tools
        self.lat1 = lat1
        self.lon1 = lon1
        self.lat2 = lat2
        self.lon2 = lon2
        self.lat1R = tools.deg2rad(lat1)
        self.lat2R = tools.deg2rad(lat2)
        self.lon1R = tools.deg2rad(lon1)
        self.lon2R = tools.deg2rad(lon2)
        self.deltaLat = tools.deg2rad(lat2 - lat1)
        self.deltaLon = tools.deg2rad(lon2 - lon1)

    def calculateDistance(self):
        """uses the ‘haversine’ formula to calculate the great-circle distance between two points in km
            a = sin²(Δφ/2) + cos φ1 * cos φ2 * sin²(Δλ/2)
            c = 2*atan2(√a, √(1−a) )
            d = R*c
            where 	φ is latitude, λ is longitude, R is earth’s radius
            @:return distance
            """
        import math
        from mathPhys import EARTH_RADIUS_KM

        a = (math.sin(self.deltaLat/2))**2 + math.cos(self.lat1R) * math.cos(self.lat2R) \
            * (math.sin(self.deltaLon/2))**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = EARTH_RADIUS_KM * 1000 * c
        return d/1000

    def getBearings(self):          # TODO nechodi, opravit!!
        initBearing = self.__initialBearing(self.lat1R, self.lat2R, self.deltaLon)
        print('init  data {}, {}, delta longitude: {}'.format(self.lat1R, self.lat2R, self.deltaLon))
        print('final data {}, {}, delta longitude: {}'.format(self.lat2R, self.lat1R, self.deltaLon))
        finalBearing = self.__initialBearing(self.lat2R, self.lat1R, self.deltaLon)
        # finalBearing = (finalBearing + 180) % 360
        return (initBearing, finalBearing)

    def __initialBearing(self, l1R, l2R, dLon):
        """service method for greatCircleTrack.
        Uses formula: θ = atan2( sin Δλ ⋅ cos φ2 , cos φ1 ⋅ sin φ2 − sin φ1 ⋅ cos φ2 ⋅ cos Δλ )
            where φ1,λ1 is the start point, φ2,λ2 the end point (Δλ is the difference in longitude)
        """
        import mathPhys as tools
        import math

        y = math.sin(dLon) * math.cos(l2R)
        x = (math.cos(l1R) * math.sin(l2R)) - (math.sin(l1R) * math.cos(l2R) * math.cos(dLon))
        result = math.atan2(y, x)
        resultDGR = tools.rad2deg(result)
        resultDGR = (resultDGR + 360) % 360
        return resultDGR

    def midpoint(self):
        """ This is the half-way point along a great circle path between the two points.1
            Formula:
            Bx = cos φ2 ⋅ cos Δλ
            By = cos φ2 ⋅ sin Δλ
            φm = atan2( sin φ1 + sin φ2, √(cos φ1 + Bx)² + By² )
            λm = λ1 + atan2(By, cos(φ1)+Bx)"""
        import math
        Bx = math.cos(self.lat2R) * math.cos(self.deltaLon)
        By = math.cos(self.lat2R) * math.sin(self.deltaLon)
        latM = math.atan2(math.sin(self.lat1R) + math.sin(self.lat2R),
                math.sqrt((math.cos(self.lat1R) + Bx)**2 + By**2))
        lonM = self.lon1R + math.atan2(By, math.cos(self.lat1R) + Bx)
        return latM, lonM

    def __str__(self):
        import mathPhys
        temp = self.getBearings()
        midpoint = self.midpoint()
        stredobod = []
        for m in midpoint:
            temp = mathPhys.decimal2degree(m)
            stredobod.append(formatDegreesTuple(temp))
        return('Great circle track from [{}, {}] to [{}, {}];\n'
               'distance = {:.2f}km, initial bearing = {}, final bearing = {}\n'
               'midpoint = [{}, {}]'.
            format(self.lat1, self.lon1, self.lat2, self.lon2,
            self.calculateDistance(),formatDegreesTuple(mathPhys.decimal2degree(temp[0])),
            formatDegreesTuple(mathPhys.decimal2degree(temp[1])),
            stredobod[0], stredobod[1]))

def __testGreatCircleTrack():

    track = GreatCircleTrackSpherical(parseCoordinates("""50°00'00"N"""),
                                parseCoordinates("""05°00'00"W"""),
                                parseCoordinates("""51°00'00"N"""),
                                parseCoordinates("""10°00'00"E"""))
    print(track)


if __name__ == '__main__':
        __testParseCoordinates()
    # __testGreatCircleTrack()