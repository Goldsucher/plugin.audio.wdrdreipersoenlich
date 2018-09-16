#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# WDR 3 Persönlich mit Götz Alsmann Kodi Plug-in
# by Goldsucher

import sys
import xbmcgui
import xbmcplugin
import xbmcaddon
import feedparser


#Selbst-Referenzierung fürs Plug-in
addon_handle = int(sys.argv[1])

#Siedle Plug-in in den Bereich Audio
xbmcplugin.setContent(addon_handle, 'audio')


#Parse Feed
d = feedparser.parse('https://www1.wdr.de/radio/wdr3/programm/sendungen/wdr3-persoenlich-alsmann/uebersicht-persoenlich-alsmann-100.feed')

#Liste mit allen Folgen aufbauen
listing = []

for item in d['entries']:
    title = item['title']
    url = item.enclosures[0].href

    #Beschreibung der Folge auslesen, für Audio nicht notwendig, aber für Audio praktisch
    summary = item['description']

    #Einige Folgen haben kein Thumbnailbild, die bekommen ein Standard-Bild verpasst
    try:
        thumb = item['image'].href
    except:
        thumb = "https://www1.wdr.de/mediathek/audio/sendereihen-bilder/wdrdrei-sendereihenbild-102~_v-gseaclassicxl.jpg"

    #Baue fürs GUI ein Listenelement
    list_item = xbmcgui.ListItem(label=title, thumbnailImage=thumb)

    #Fanart des Plug-ins als Hintergrundbild nutzen
    wdrdreipersoenlich_plugin = xbmcaddon.Addon('plugin.audio.wdrdreipersoenlich')
    list_item.setArt({'fanart': wdrdreipersoenlich_plugin.getAddonInfo('fanart')})

    list_item.setProperty('IsPlayable', 'true')
    listing.append((url, list_item, False))


#In diesem Beispiel fügen wir alle Items in einem der Liste hinzu
xbmcplugin.addDirectoryItems(addon_handle, listing, len(listing))

#Schließe die Liste ab
xbmcplugin.endOfDirectory(addon_handle, succeeded=True)
