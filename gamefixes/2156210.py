""" Game fix for Warhammer 40,000 Darktide Playtest
"""

#pylint: disable=C0103

from protonfixes import util

def main():
    """ Launcher fix; requires MS WebView2
    """

    util.protontricks('msewv2-64_ge')
