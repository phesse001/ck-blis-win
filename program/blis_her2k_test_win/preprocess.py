#
# Preprocessing CK template demo
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, 2018, Grigori.Fursin@cTuning.org, http://fursin.net
#

import json
import os
import re

def ck_preprocess(i):
    deps=i['deps']
    blis_lib = deps['lib-blis']['cus']
    path = blis_lib['path_lib']

    #add directly to path, otherwise program cannot find library
    os.environ['PATH'] += os.pathsep + path

    return {'return':0}

# Do not add anything here!
