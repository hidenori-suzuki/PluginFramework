#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pluginmanager import Plugin

class Bird(Plugin):

    def __init__(self, **kwargs):
        self.pluginId = ['bird']

    def process(self, **kwargs):
        print "(*ﾟθﾟ) %s" % kwargs["comment"]
