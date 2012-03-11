#!/usr/bin/env python

import os
import sys
from pluginmanager import PluginManager

def main(id, comment):
    plugin = PluginManager()
    tgt = []
    if id != "all":
       tgt = [id]
    param = {"comment":"%s" % comment}
    plugin.method('process', args=param, target=tgt)

if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    if (argc != 3):
        print 'Usage: You should specify one parameter of cfg file to %s' % argvs[0]
        quit()
    main(argvs[1], argvs[2])
