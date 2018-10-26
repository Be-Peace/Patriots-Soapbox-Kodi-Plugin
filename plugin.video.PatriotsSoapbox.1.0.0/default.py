# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Youtube Channel
# (c) 2015 - Simple TechNerd
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.PatriotsSoapbox'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

livelist=[
        ("Patriots' Soapbox 24/7 Livestream", "search/?q=Patriots+Soapbox+Live&sp=EgQIAkAB", 'https://yt3.ggpht.com/a-/AN66SAzSekjM9Yy0bKIzXkZ3B2or0lS91LmGM6B7cQ=s288-mo-c-c0xffffffff-rj-k-no'),
]

channellist=[
        ("Patriots' Soapbox Backup Channel 1", "channel/UC5ot7kRfXVOe4DcX3RC6lcQ", 'https://yt3.ggpht.com/a-/AN66SAwWpT6_MosWiPM4YhVxjXNPE1prImRv8A-6uw=s288-mo-c-c0xffffffff-rj-k-no'),
        ("Patriots' Soapbox Backup Channel 2", "channel/UCRpVyLulpV6PJM6RsRhGaRA", 'https://yt3.ggpht.com/a-/AN66SAz0fC4lq2VV0Lfrzv30u2n_ut6Tg74_0VX00A=s288-mo-c-c0xffffffff-rj-k-no'),
        ("BLACK MIRROR (Patriots' Soapbox Archive)", "channel/UC-sh4x6CuaYnTVZYoO-3NIQ", 'https://yt3.ggpht.com/a-/AN66SAx2tcYwy4sA3v8bAvX4db-CPRrNGASm3Brl8w=s288-mo-c-c0xffffffff-rj-k-no'),
]



# Entry point
def run():
    plugintools.log("PatriotsSoapbox.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("PatriotsSoapbox.main_list "+repr(params))

for name, id, icon in livelist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )

for name, id, icon in channellist:
	plugintools.add_item(title=name,url="plugin://plugin.video.youtube/"+id+"/",thumbnail=icon,folder=True )



run()