#!/usr/bin/env python3

# lab01-1 KmToMiles....  testing

import os
import sys

if( __name__ == '__main__' ):
    path = os.path.dirname(os.path.realpath(__file__))
    sys.stdin = open( path + '/KmToMiles_testdata.txt', 'r' )

    # m.main()

    exec(open( path + '/KmToMiles.py' ).read()) # 26.2 --> 42.16
    exec(open( path + '/KmToMiles.py' ).read()) # 100 --> 160.93
    exec(open( path + '/KmToMiles.py' ).read()) # 6.21 --> 10
    exec(open( path + '/KmToMiles.py' ).read()) # 1 --> 1.61
    print( 'done' )
