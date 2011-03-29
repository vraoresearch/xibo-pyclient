#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Xibo - Digitial Signage - http://www.xibo.org.uk
# Copyright (C) 2011 Alex Harrington
#
# This file is part of Xibo.
#
# Xibo is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version. 
#
# Xibo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Xibo.  If not, see <http://www.gnu.org/licenses/>.
#

from threading import Thread

class ShadowEffect(Thread):

    def run(self):
        ## Options
        
        if self.options == {}:
            self.options['offset'] = (2,2)
            self.options['radius'] = 1
            self.options['opacity'] = 1
            self.options['color'] = "FFFFFF"

        self.p.enqueue('effect',('shadow',
                                 self.media,
                                 self.options['offset'],
                                 self.options['radius'],
                                 self.options['opacity'],
                                 self.options['color']))

        if self.callback != None:
            try:
                self.callback()
            except:
                self.log.log(0,"error","Exception thrown calling the callback " + self.callback)
