#
# Copyright (C) 2014-2018 GEM Foundation
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
# along with OpenQuake. If not, see <http://www.gnu.org/licenses/>.


"""
:module:`openquake.hazardlib.gsim.can15.western` implements
:class:`OceanicCan15Mid`, :class:`OceanicCan15Low`, :class:`OceanicCan15Upp`
"""

import numpy as np

from openquake.hazardlib.gsim.can15.western import WesternCan15Mid
from openquake.hazardlib.gsim.can15.western import get_sigma


class OceanicCan15Mid(WesternCan15Mid):
    """
    Implements the GMPE for oceanic sources
    """

    def get_mean_and_stddevs(self, sites, rup, dists, imt, stddev_types):
        """ """
        # get original values
        rup.mag -= 0.5
        mean, stddevs = super().get_mean_and_stddevs(sites, rup, dists, imt,
                                                     stddev_types)
        stddevs = [np.ones(len(dists.rjb))*get_sigma(imt)]
        return mean, stddevs


class OceanicCan15Low(WesternCan15Mid):

    def get_mean_and_stddevs(self, sites, rup, dists, imt, stddev_types):
        """ """
        # get original values
        mean, stddevs = super().get_mean_and_stddevs(sites, rup, dists, imt,
                                                     stddev_types)
        # adjust mean values using the reccomended delta (see Atkinson and
        # Adams, 2013)
        tmp = 0.1+0.0007*dists.rjb
        tmp = np.vstack((tmp, np.ones_like(tmp)*0.3))
        rup.mag -= 0.5
        delta = np.log(10.**(np.amin(tmp, axis=0)))
        mean_adj = mean - delta
        stddevs = [np.ones(len(dists.rjb))*get_sigma(imt)]
        return mean_adj, stddevs


class OceanicCan15Upp(WesternCan15Mid):

    def get_mean_and_stddevs(self, sites, rup, dists, imt, stddev_types):
        """ """
        # get original values
        mean, stddevs = super().get_mean_and_stddevs(sites, rup, dists, imt,
                                                     stddev_types)
        # Adjust mean values using the reccomended delta (see Atkinson and
        # Adams, 2013)
        tmp = 0.1+0.0007*dists.rjb
        tmp = np.vstack((tmp, np.ones_like(tmp)*0.3))
        delta = np.log(10.**(np.amin(tmp, axis=0)))
        rup.mag -= 0.5
        mean_adj = mean + delta
        stddevs = [np.ones(len(dists.rjb))*get_sigma(imt)]
        return mean_adj, stddevs
