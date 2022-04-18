#!/usr/bin/env python3

# lab01-1 multiply....  testing

import os
import sys
#import multiply as m

if( __name__ == '__main__' ):
    path = os.path.dirname(os.path.realpath(__file__))
    sys.stdin = open( path + '/multiply_testdata.txt', 'r' )

    # m.main()

    exec(open( path + '/multiply.py' ).read()) # 2 x 3 = 6
    exec(open( path + '/multiply.py' ).read()) # 7 x 8 = 56
    exec(open( path + '/multiply.py' ).read()) # 12 x 11 = 132

    print( 'done' )
