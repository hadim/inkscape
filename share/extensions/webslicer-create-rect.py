#!/usr/bin/env python
'''
Copyright (C) 2010 Aurelio A. Heckert, aurium (a) gmail dot com

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''

import inkex
import gettext

_ = gettext.gettext

def is_empty(val):
    if val is None:
        return True
    else:
        return len(str(val)) == 0

class WebSlicer_CreateRect(inkex.Effect):

    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option("--name",
                                     action="store", type="string",
                                     dest="name",
                                     help="")
        self.OptionParser.add_option("--format",
                                     action="store", type="string",
                                     dest="format",
                                     help="")
        self.OptionParser.add_option("--dpi",
                                     action="store", type="int",
                                     dest="dpi",
                                     help="")
        self.OptionParser.add_option("--dimension",
                                     action="store", type="string",
                                     dest="dimension",
                                     help="")
        self.OptionParser.add_option("--bg-color",
                                     action="store", type="string",
                                     dest="bg_color",
                                     help="")
        self.OptionParser.add_option("--quality",
                                     action="store", type="int",
                                     dest="quality",
                                     help="")
        self.OptionParser.add_option("--gif-type",
                                     action="store", type="string",
                                     dest="gif_type",
                                     help="")
        self.OptionParser.add_option("--palette-size",
                                     action="store", type="int",
                                     dest="palette_size",
                                     help="")
        self.OptionParser.add_option("--html-id",
                                     action="store", type="string",
                                     dest="html_id",
                                     help="")
        self.OptionParser.add_option("--html-class",
                                     action="store", type="string",
                                     dest="html_class",
                                     help="")
        self.OptionParser.add_option("--layout-disposition",
                                     action="store", type="string",
                                     dest="layout_disposition",
                                     help="")
        self.OptionParser.add_option("--layout-position-anchor",
                                     action="store", type="string",
                                     dest="layout_position_anchor",
                                     help="")
        # inkscape param workarround
        self.OptionParser.add_option("--tab")


    def unique_slice_name(self):
        name = self.options.name
        el = self.document.xpath( '//*[@id="'+name+'"]', namespaces=inkex.NSS )
        if len(el) > 0:
            if name[-3:] == '-00': name = name[:-3]
            num = 0
            num_s = '00'
            while len(el) > 0:
                num += 1
                num_s = str(num)
                if len(num_s)==1 : num_s = '0'+num_s
                el = self.document.xpath( '//*[@id="'+name+'-'+num_s+'"]',
                                          namespaces=inkex.NSS )
            self.options.name = name+'-'+num_s


    def effect(self):
        layer = self.get_slicer_layer()
        #TODO: get selected elements to define location and size
        rect = inkex.etree.SubElement(layer, 'rect')
        if is_empty(self.options.name):
            self.options.name = 'slice-00'
        self.unique_slice_name()
        rect.set('id', self.options.name)
        rect.set('fill', 'red')
        rect.set('opacity', '0.5')
        rect.set('x', '-100')
        rect.set('y', '-100')
        rect.set('width', '200')
        rect.set('height', '200')
        desc = inkex.etree.SubElement(rect, 'desc')
        conf_txt = "format:"+ self.options.format +"\n"
        if not is_empty(self.options.dpi):
            conf_txt += "dpi:"     + str(self.options.dpi) +"\n"
        if not is_empty(self.options.html_id):
            conf_txt += "html-id:" + self.options.html_id
        desc.text = conf_txt

    def get_slicer_layer(self):
        # Test if webslicer-layer layer existis
        layer = self.document.xpath(
                     '//*[@id="webslicer-layer" and @inkscape:groupmode="layer"]',
                     namespaces=inkex.NSS)
        if len(layer) is 0:
            # Create a new layer
            layer = inkex.etree.SubElement(self.document.getroot(), 'g')
            layer.set('id', 'webslicer-layer')
            layer.set(inkex.addNS('label', 'inkscape'), 'Web Slicer')
            layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')
        else:
            layer = layer[0]
        return layer

if __name__ == '__main__':
    e = WebSlicer_CreateRect()
    e.affect()
