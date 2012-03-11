#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pluginmanager import Plugin

class Cat(Plugin):

    def __init__(self, **kwargs):
        self.pluginId = ['cat']

    def process(self, **kwargs):
        print "(ΦωΦ) %s" % kwargs["comment"]
