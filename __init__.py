# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QgsSymbologySharing
                                 A QGIS plugin
 Download colllections shared by other users
                             -------------------
        begin                : 2016-05-29
        copyright            : (C) 2016 by Akbar Gumbira
        email                : akbargumbira@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))

THIRD_PARTY_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'third_party'))
if THIRD_PARTY_DIR not in sys.path:
    sys.path.append(THIRD_PARTY_DIR)


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load QgsSymbologySharing class from file QgsSymbologySharing.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from symbology_sharing.plugin import Plugin
    return Plugin(iface)
