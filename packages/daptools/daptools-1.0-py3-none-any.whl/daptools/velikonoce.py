#!/usr/bin/python
# -*- coding: utf-8 -*-
u""" vypocita datum velikonoc v obdobi 1900 - 2099.

Pouziti:
    vel = velikonoce();
    datum = vel.getVelikonoce(rok)
    format datumu: (rrrr, mm, dd)

Výpočet:
K výpočtu je nutné znát konstanty m a n. Pro roky 1900 až 2099 jsou m = 24 a n = 5.
Pro léta 1800 - 1899 je m = 23 a n = 4. Funkcí mod se rozumí zbytek po dělení.

a = rok mod 19
b = rok mod 4
c = rok mod 7
d = (19a + m) mod 30
e = (n + 2b + 4c + 6d) mod 7

Pro březen platí:

22 + d + e = velikonoční neděle

Pro duben platí:

d + e - 9 = velikonoční neděle

Výpočet zbytku a bere v potaz fakt, že měsíční cyklus se opakuje s devatenáctiletou periodou;
zbytek b zahrnuje přestupné dny a zbytek c dorovnává dny v týdnu.

Je potřeba dosadit hodnoty do výpočtu pro březen i duben. Platí vždy pouze jeden výsledek a to ten,
pro který se vejde Velikonoční neděle do požadovaného období 22. března do 25. dubna.

Poznámka: Může se pochopitelně stát, že jeden nebo více zbytků jsou nuly. Tím se výpočet zjednoduší,
neboť násobíme-li nulou je výsledek nula. Poznamenejme ještě, že dělíme-li například 24 číslem 30,
považuje se za zbytek 24!

Příklad – výpočet pro rok 2008

Konstanty m = 24 a n = 5

Přesný postup pro hodnotu a: 2008 / 19 = 105,6842105. Takže 105 . 19 = 1995, to znamená 2008 – 1995 = 13 = zbytek.

2008 / 19 = 105 + zbytek 13; a = 13
2008 / 4 = 502; zbytek b = 0
2008 / 7 = 286 + zbytek 6; c = 6
(19.a + m) / 30 = (19.13 + 24) / 30 = 9 + zbytek 1; d = 1
(n + 2b + 4c + 6d) / 7 = (5 + 2.0 + 4.6 + 6.1) / 7 = 5; zbytek e = 0

Pro březen platí:

22 + d + e = 22 + 1 + 0 = 23 => 23. března – Velikonoční neděle

Pro duben platí:

d + e - 9 = 1 + 0 – 9 = - 8 (záporné číslo je nesmysl)

Doporučené a použité odkazy:

    * http://www.sbor-strahov.cz/miscellaneous/Velikonoce.htm
    * http://www.ian.cz/detart_fr.php?id=1739
"""
import sys


class velikonoce:
    def validateBrezen(self, brezen):
        """ ovÄÅÃ­, ze breznove datum je v mezich mesice """
        if (brezen > 0) & (brezen <= 31):
            return True
        else:
            return False

    def getDayMonth(self, t):  # (d, e, rok)
        """ vrati datum velikonocni nedele, t je tuple """
        brezen = 22 + t[0] + t[1]
        duben = t[0] + t[1] - 9
        if self.validateBrezen(brezen):
            return (t[2], 3, brezen)
        else:
            return (t[2], 4, duben)

    def coefficients(self, rok):
        a = rok % 19
        b = rok % 4
        c = rok % 7
        m = 0
        n = 0
        if ((rok >= 1800) & (rok <= 1899)):
            m = 23
            n = 4
        elif ((rok >= 1900) & (rok <= 2099)):
            m = 24
            n = 5
        else:
            print("Pracuji pouze v rozpětí 1800 až 2099.")
            sys.exit()

        d = (19 * a + m) % 30
        e = (n + 2 * b + 4 * c + 6 * d) % 7
        return (d, e, rok)

    def getVelikonoce(self, rok):
        return self.getDayMonth(self.coefficients(rok))


if __name__ == "__main__":
    rok = int(input(u"Výpočet velikonoc, zadej rok: "))
    vel = velikonoce()
    datum = vel.getVelikonoce(rok)
    print('velka noc je: {}'.format(datum))
    print("(format rrrr, mm, dd)")


