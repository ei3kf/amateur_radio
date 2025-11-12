#!/usr/bin/env python3

'''
So I know which way to point the beam....
'''

import sys
from math import radians, degrees, atan2, sin, cos
import maidenhead

def bearings_between_locators(locator1, locator2):
    """
    Returns short-path and long-path bearings from locator1 to locator2.
    """
    # Convert Maidenhead locators to lat/lon
    lat1, lon1 = maidenhead.to_location(locator1)
    lat2, lon2 = maidenhead.to_location(locator2)

    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Short path bearing calculation
    dlon = lon2 - lon1
    x = sin(dlon) * cos(lat2)
    y = cos(lat1)*sin(lat2) - sin(lat1)*cos(lat2)*cos(dlon)
    initial_bearing = atan2(x, y)

    # Convert to degrees and normalize 0–360°
    bearing_short = (degrees(initial_bearing) + 360) % 360

    # Long path is the opposite direction
    bearing_long = (bearing_short + 180) % 360

    return bearing_short, bearing_long

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <start_locator> <end_locator>")
        sys.exit(1)

    start_locator = sys.argv[1].upper()
    end_locator = sys.argv[2].upper()

    short_bearing, long_bearing = bearings_between_locators(start_locator, end_locator)
    print(f"Short path bearing from {start_locator} to {end_locator}: {short_bearing:.1f}°")
    print(f"Long path bearing  from {start_locator} to {end_locator}: {long_bearing:.1f}°")

if __name__ == "__main__":
    main()
