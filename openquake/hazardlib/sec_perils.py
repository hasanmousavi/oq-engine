# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2020, GEM Foundation
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake.  If not, see <http://www.gnu.org/licenses/>.


# to be extended
class SecondaryPeril(object):
    def __init__(self, name):
        self.name = name

    def compute(self, mag, sid, gmv):
        # gmv is an array with M elements, one per IMT
        return gmv[0] * .1  # fake formula

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.name)


supported = 'fake'.split()
