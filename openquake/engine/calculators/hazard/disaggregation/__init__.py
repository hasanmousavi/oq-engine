# -*- coding: utf-8 -*-
# Copyright (c) 2010-2013, GEM Foundation.
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake.  If not, see <http://www.gnu.org/licenses/>.

"""
The Disaggregation approach allows calculating relative contribution to a
seismic hazard level. Contributions are defined in terms of latitude,
longitude, magnitude, distance, epsilon, and tectonic region type.

Sources:

* | Disaggregation of Seismic Hazard
  | by Paolo Bazzurro and C. Allin Cornell
  | Bulletin of the Seismological Society of America, 89, 2, pp. 501-520, April
    1999

*******
Outputs
*******

* :ref:`Hazard Curves <disagg-hazard-curves>`
* :ref:`Disaggregation Matrices <disagg-matrices>`

.. _disagg-hazard-curves:

Hazard Curves
=============

Hazard curve calculation is the first phase in a Disaggregation calculation.
This phase computes the hazard for a given location by aggregation
contributions from all relevant seismic sources in a given model. (The method
for computing these curves is exactly the same as the
`Classical approach <#hazard-curves>`_.)

Mean and quantile post-processing options for hazard curves are not enabled for
the Disaggregation calculator.

Disaggregation Matrices
=======================

Once hazard curves are computed for all sites and logic tree realizations, the
second phase (disaggregation) begins. While the hazard curve calculation phase
is concerned with aggregating the hazard contributions from all sources, the
disaggregation phase seeks to quantify the contributions from a catalogue of
ruptures to the hazard level at a given probability of exceedance (for a given
geographical point) in terms of:

* Longitude
* Latitude
* Magnitude (in Mw, or "Moment Magnitude")
* Distance (in km)
* Epsilon (the difference in terms of standard deviations between IML to be
  disaggregated and the mean value predicted by the GMPE)
* Tectonic Region Type

This analysis, which operates on a single geographical point and all seismic
sources for a given logic tree realization, results in a matrix of 6
dimensions. Each axis is divided into multiple bins, the size and quantity of
which are determined the calculation inputs. Longitude and latitude bins are
determined by the ``coordinate_bin_width`` calculation parameter, in units of
decimal degrees. Magnitude bins are determined given the ``mag_bin_width``.
Distance bins are determined by the ``distance_bin_width``, in units of
kilometers. ``num_epsilon_bins`` defines the quantity of epsilon bins.
``truncation_level`` is taken into account when computing the width of each
epsilon bin, and so this is a required parameter. The number of tectonic region
type bins is simply determined by the variety of tectonic regions specified in
a given seismic source model. (For instance, if a source model defines sources
for "Active Shallow Crust" and "Volcanic", this will result in two bins.)

The final results of a disaggregation calculation are various sub-matrices
extracted from the 6-dimensional matrix. These sub-matrices include common
combinations of terms, which are as follows:

* Magnitude
* Distance
* Tectonic Region Type
* Magnitude, Distance, and Epsilon
* Longitude and Latitude
* Magnitude, Longitude, and Latitude
* Longitude, Latitude, and Tectonic Region Type

Each disaggregation result produced by the calculator includes all of these.

The total number of disaggregation results produce by the calculator is

``T = E * R * I * P``

where

* ``T`` is the total number of disaggregation results
* ``E`` is the total number of probabilities of exceedance (defined by
  ``poes_disagg``)
* ``R`` is the total number of logic tree realizations
* ``I`` is the number of IMT/IML definitions
* ``P`` is the number of points with non-zero hazard (see note below)

Note: In order to not waste computation time and storage, if the hazard curve
used to a compute disaggregation for a given point and IMT contains all zero
probabilities, we do not compute a disagg. matrix for that point.
"""
