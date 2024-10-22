#!/usr/bin/python 3
# -*- coding: utf-8 -*-
'''
METAR and TAF data extraction.
Created on 12/03/2018, 08:49

adresy, priklady:
NOAA: https://www.aviationweather.gov/adds/tafs?station_ids=LKKB&submit_both=Get+TAFs+and+METARs

@author: David Potucek
'''

import simplejson as json
from requests_html import HTMLSession

ceskyURL = 'http://meteo.rlp.cz/LK_opmet.htm'   # vraci v html vsechny letiste v cechach
aviationData = 'https://www.aviationweather.gov/adds/tafs?station_ids=LKKB&submit_both=Get+TAFs+and+METARs'

METARtext = """
{
  "Altimeter": "1008", 
  "Cloud-List": [
    [
      "FEW", 
      "015"
    ]
  ], 
  "Dewpoint": "02", 
  "Flight-Rules": "VFR", 
  "Meta": {
    "Cache-Timestamp": "Thu, 15 Mar 2018 09:10:51 GMT", 
    "Timestamp": "Thu, 15 Mar 2018 09:11:57 GMT"
  }, 
  "Other-List": [], 
  "Raw-Report": "LKKB 150900Z 09011KT 9000 FEW015 06/02 Q1008 NOSIG", 
  "Remarks": "NOSIG", 
  "Remarks-Info": {}, 
  "Runway-Vis-List": [], 
  "Station": "LKKB", 
  "Temperature": "06", 
  "Time": "150900Z", 
  "Units": {
    "Altimeter": "hPa", 
    "Altitude": "ft", 
    "Temperature": "C", 
    "Visibility": "m", 
    "Wind-Speed": "kt"
  }, 
  "Visibility": "9000", 
  "Wind-Direction": "090", 
  "Wind-Gust": "", 
  "Wind-Speed": "11", 
  "Wind-Variable-Dir": []
}"""

TAFtext = '''
{
  "Forecast": [
    {
      "Altimeter": "", 
      "Cloud-List": [
        [
          "SCT", 
          "040"
        ]
      ], 
      "End-Time": "2700", 
      "Flight-Rules": "VFR", 
      "Icing-List": [], 
      "Other-List": [], 
      "Probability": "", 
      "Raw-Line": "2600/2700 VRB02KT 9999 SCT040", 
      "Start-Time": "2600", 
      "Summary": "Winds Variable at 02kt, Vis 10km, Scattered clouds at 4000ft", 
      "Turb-List": [], 
      "Type": "BASE", 
      "Visibility": "9999", 
      "Wind-Direction": "VRB", 
      "Wind-Gust": "", 
      "Wind-Shear": "", 
      "Wind-Speed": "02"
    }, 
    {
      "Altimeter": "", 
      "Cloud-List": [
        [
          "BKN", 
          "030"
        ]
      ], 
      "End-Time": "2606", 
      "Flight-Rules": "MVFR", 
      "Icing-List": [], 
      "Other-List": [], 
      "Probability": "", 
      "Raw-Line": "TEMPO 2602/2606 6000 BKN030", 
      "Start-Time": "2602", 
      "Summary": "Vis 6km, Broken layer at 3000ft", 
      "Turb-List": [], 
      "Type": "TEMPO", 
      "Visibility": "6000", 
      "Wind-Direction": "", 
      "Wind-Gust": "", 
      "Wind-Shear": "", 
      "Wind-Speed": ""
    }, 
    {
      "Altimeter": "", 
      "Cloud-List": [
        [
          "BKN", 
          "035"
        ]
      ], 
      "End-Time": "2608", 
      "Flight-Rules": "VFR", 
      "Icing-List": [], 
      "Other-List": [], 
      "Probability": "", 
      "Raw-Line": "BECMG 2606/2608 34008KT BKN035", 
      "Start-Time": "2606", 
      "Summary": "Winds NNW-340 at 08kt, Broken layer at 3500ft", 
      "Turb-List": [], 
      "Type": "BECMG", 
      "Visibility": "", 
      "Wind-Direction": "340", 
      "Wind-Gust": "", 
      "Wind-Shear": "", 
      "Wind-Speed": "08"
    }, 
    {
      "Altimeter": "", 
      "Cloud-List": [
        [
          "BKN", 
          "015"
        ]
      ], 
      "End-Time": "2700", 
      "Flight-Rules": "MVFR", 
      "Icing-List": [], 
      "Other-List": [
        "RA"
      ], 
      "Probability": "", 
      "Raw-Line": "TEMPO 2616/2700 6000 RA BKN015", 
      "Start-Time": "2616", 
      "Summary": "Vis 6km, Rain, Broken layer at 1500ft", 
      "Turb-List": [], 
      "Type": "TEMPO", 
      "Visibility": "6000", 
      "Wind-Direction": "", 
      "Wind-Gust": "", 
      "Wind-Shear": "", 
      "Wind-Speed": ""
    }
  ], 
  "Max-Temp": "", 
  "Meta": {
    "Cache-Timestamp": "Mon, 26 Mar 2018 05:58:39 GMT", 
    "Timestamp": "Mon, 26 Mar 2018 06:00:37 GMT"
  }, 
  "Min-Temp": "", 
  "Raw-Report": "TAF LKKB 252300Z 2600/2700 VRB02KT 9999 SCT040 TEMPO 2602/2606 6000 BKN030 BECMG 2606/2608 34008KT BKN035 TEMPO 2616/2700 6000 RA BKN015", 
  "Remarks": "", 
  "Station": "LKKB", 
  "Time": "252300Z", 
  "Units": {
    "Altimeter": "hPa", 
    "Altitude": "ft", 
    "Temperature": "C", 
    "Visibility": "m", 
    "Wind-Speed": "kt"
  }
}'''


def getDataResponse(airport = 'LKKB'):
    """Gets actual data from the servers.
    """             # TODO: dodelat moznost parametricky definovat letiste
    debug = False
    session = HTMLSession()
    respMet = session.get('http://avwx.rest/api/metar/' + airport)
    respTaf = session.get('http://avwx.rest/api/taf/' + airport + '?options=summary')
    if debug: print("session status: {}\ndata{}".format(respMet, respMet.text))
    return respMet, respTaf

class metarClass():
    """Wraper class pro METAR data. Zparsuje dodana data a vytvori instanci soucasneho METAR reportu
    dane stanice.
    Poskytuje jednotky ve kterych je uvaden report pomoci getUnit(nazev)
    """

    def __init__(self, data):
        self.metarData = json.loads(data)
        self.altimeter = self.metarData['Altimeter']
        self.cloudList = self.metarData['Cloud-List']
        self.dewPoint = self.metarData['Dewpoint']
        self.rule = self.metarData['Flight-Rules']
        self.other = self.metarData['Other-List']
        self.raw = self.metarData['Raw-Report']
        self.remarks = self.metarData['Remarks']
        self.remInfo = self.metarData['Remarks-Info']
        self.rwyVisibility = self.metarData['Runway-Vis-List']
        self.rawReport = self.metarData['Raw-Report']
        self.station = self.metarData['Station']
        self.temp = self.metarData['Temperature']
        self.time = self.metarData['Time']
        self.units = self.metarData['Units']
        self.visibility = self.metarData['Visibility']
        self.windDir = self.metarData['Wind-Direction']
        self.windGust = self.metarData['Wind-Gust']
        self.windSpeed = self.metarData['Wind-Speed']
        self.windVarDir = self.metarData['Wind-Variable-Dir']

    def getUnit(self, nazev):
        if nazev not in self.units:
            raise ValueError('requested unit name is not used in this METAR!')
        return self.units[nazev]

    def __str__(self):
        return(self.raw)

if __name__ == "__main__":

    metarRaw, tafRaw = getDataResponse()

    # print('METAR: {}'.format(metarRaw.text))
    # print('TAF: {}'.format(tafRaw.text))

    # metarRaw = METARtext
    # tafRaw = TAFtext
    metar = metarClass(metarRaw.content.decode("utf-8"))
    print(metar)
    print(metar.cloudList)


