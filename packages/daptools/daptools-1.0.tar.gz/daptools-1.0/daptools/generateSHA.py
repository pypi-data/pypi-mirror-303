#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Poskytuje ruzne sha hashes na zaklade knihovny hashlib, porovnavani file a signatury.
Created on 24/02/2021, 07:26

@author: David Potucek
"""

import sys, hashlib
from collections import OrderedDict as od

SHA_TYPES = ['md5sum', 'sha1sum', 'sha224sum', 'sha256sum', 'sha384sum', 'sha512sum']

def get_hashsums(file_path):
    '''Vypocte hash vsech typu pro dany file.'''
    hash_sums = od()
    hash_sums['md5sum'] = hashlib.md5()
    hash_sums['sha1sum'] = hashlib.sha1()
    hash_sums['sha224sum'] = hashlib.sha224()
    hash_sums['sha256sum'] = hashlib.sha256()
    hash_sums['sha384sum'] = hashlib.sha384()
    hash_sums['sha512sum'] = hashlib.sha512()
    with open(file_path, 'rb') as fd:
        data_chunk = fd.read(1024)
        while data_chunk:
              for hashsum in hash_sums.keys():
                  hash_sums[hashsum].update(data_chunk)
              data_chunk = fd.read(1024)

    results = od()
    for key,value in hash_sums.items():
         results[key] = value.hexdigest()
    return results

def createHash(file, type="sha256sum"):
    """Vytvori podle typu hash objekt a napocita hash. Default type je sha256."""
    if (type == 'md5sum'): hashSum = hashlib.md5()          # nastaveni typu hashe
    elif (type == 'sha1sum'): hashSum = hashlib.sha1()
    elif (type == 'sha224sum'): hashSum = hashlib.sha224()
    elif (type == 'sha256sum'): hashSum = hashlib.sha256()
    elif (type == 'sha384sum'): hashSum = hashlib.sha384()
    elif (type == 'sha512sum'): hashSum = hashlib.sha512()
    else:
        raise ValueError('neplatny typ hashe')

    with open(file, 'rb') as fh:            # projedeme file a vyrobime spravny hash
        data_chunk = fh.read(1024)
        while data_chunk:
            hashSum.update(data_chunk)
            data_chunk = fh.read(1024)
    return hashSum, type


def validateFile (file, signature, type="sha256sum"):
    """Zvaliduje dany file oproti dodane signature daneho typu. Vrati True/False, dodany hash, vypocteny hash a jeho typ.
    Default type je sha256."""
    hash, type  = createHash(file, type)  # spocita hash file
    dig = hash.hexdigest()
    if (dig == signature): return True, hash, type
    else:
        return False, hash, type

def testHash():
    print('test default (sha256sum) hashe')
    for path in sys.argv[1:]:
        print(">>> ", path)
        for key, value in get_hashsums(path).items():
            print(key, value)
    fname = sys.argv[0]
    h, t = createHash(fname)
    print('------------------------------------------------------')
    print('file = {}'.format(fname))
    print('hash typu {} je: {}'.format(t, h.hexdigest()))
    nesmysl = 'c94c8b81ef67bc6ff2028e160d707937af9047b084173e76246e01913da65105'
    spravny, typ = createHash(fname)
    vysl, h_vyp, typ = validateFile(fname, nesmysl)

    print('------ chybovy stav, vysledek musi byt False ------')
    print('vypocteny hash = {}'.format(h_vyp.hexdigest()))
    print('dodany spatny hash = {}'.format(nesmysl))
    print('vyledek = {}'.format(vysl))

    vysl, h_vyp, typ = validateFile(fname, spravny.hexdigest())
    print('------ spravny stav, vysledek musi byt True ------')
    print('vypocteny hash = {}'.format(h_vyp.hexdigest()))
    print('dodany auto hash = {}'.format(spravny.hexdigest()))
    print('vyledek = {}'.format(vysl))


def prepareArguments():
    '''Nacte arguemnty a bud vrati jeden,dva, nebo tri. Pokud jich je jine mnozstvi, hodi exception.
    Ocekavane poradi je file, typ, hash k validci.'''
    import argparse
    # vytvoreni parseru, nastaveni message a nastaveni formatovani textu
    parser = argparse.ArgumentParser(description='Pouziti pro generovani hashe k file a  k validaci hashe na file.',
                                     formatter_class=argparse.RawTextHelpFormatter,
                                     epilog='')
    parser.add_argument('parametry',                        # pridani argumentu
                        help='argumenty: soubor, typ, hash.\nPouziti: \ngenerateSHA(file) \t\t- vygeneruje sha256 hash pro dany file\n'
                             'generateSHA(file, typHashe)  \t- vygeneruje pro file hash dodaneho typu\n'
                             'generateSHA(file, typHashe, hash) - zkontroluje jestli file ma hash daneho typu '
                             'rovny zadanemu hashi.',
                        nargs='*')
    argumenty = parser.parse_args()
    lst = []
    for element in argumenty.parametry:     # prepocet z namespace na list. Udelat elegantneji? Ted neni cas...
        lst.append(element)
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 2:
        return lst[0], lst[1]
    elif len(lst) == 3:
        return lst[0], lst[1], lst[2]
    else:
        raise ValueError("parametru musi byt bud 1, 2 nebo 3, dostal jsem {}"
                         .format(len(lst)))

if __name__ == "__main__":
    # testHash()    # testovaci rutina, pocita hash na svem file
    args = prepareArguments()
    if len(args) == 1:              # chci vygenerovat sha256sum hash pro zadany file
        aaa, typ = createHash(args[0])
        print('file {}; type of hash {}\nhash {}'.format(args[0], 'sha256sum', aaa))
    elif len(args) == 2:            # chci vygenerovat jinou hash nez standardni pro file
        aaa, typ = createHash(args[0], args[1])
        print('file {}; type of hash {}\nhash {}'.format(args[0], typ, aaa))
    elif len(args) == 3:            # chci zvalidovat file podle dodaneho hashe
        vysl, hsh, typ = validateFile(args[0], args[2], args[1])
        print('dodavy hash je {}'.format(args[2]))
        print('file {} ma hash = {} typu {}'.format(args[0], hsh.hexdigest(), typ))
        if vysl:
            print('File validated.')
        else:
            print('!!!! Vysledek nesouhlasi !!!!')

