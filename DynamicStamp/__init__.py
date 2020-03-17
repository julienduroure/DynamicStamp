##########################################################################################
#	GPL LICENSE:
#-------------------------
# This file is part of DynamicStamp.
#
#    DynamicStamp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    DynamicStamp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with DynamicStamp.  If not, see <http://www.gnu.org/licenses/>.
##########################################################################################
#
#	Copyright 2018 Julien Duroure (contact@julienduroure.com)
#
##########################################################################################
bl_info = {
    "name": "DynamicStamp",
    "version": (0, 2, 0),
    "author": "Julien Duroure",
    "blender": (2, 82, 0),
    "description": "Dynamic Stamp",
    "location": "Render Properties",
    "wiki_url": "https://github.com/julienduroure/DynamicStamp/",
    "tracker_url": "https://github.com/julienduroure/DynamicStamp/issues/",
    "category": "Render"
}

if "bpy" in locals():
    import imp
    imp.reload(globs)
    imp.reload(ops)
    imp.reload(ui)
else:
    from .globs import *
    from .ops import *
    from .ui import *

import bpy

def register():
    globs.register()

    bpy.types.Scene.juds_use_dynstamp     = bpy.props.BoolProperty()
    bpy.types.Scene.juds_text             = bpy.props.StringProperty()
    bpy.types.Scene.juds_data             = bpy.props.CollectionProperty(type=DynamicStampFrame)
    bpy.types.Scene.juds_use_placeholder  = bpy.props.BoolProperty()
    bpy.types.Scene.juds_placeholder      = bpy.props.StringProperty()

    ops.register()
    ui.register()

def unregister():

    del bpy.types.Scene.juds_use_dynstamp
    del bpy.types.Scene.juds_text
    del bpy.types.Scene.juds_data
    del bpy.types.Scene.juds_use_placeholder
    del bpy.types.Scene.juds_placeholder

    ops.unregister()
    ui.unregister()
    globs.unregister()

if __name__ == "__main__":
    register()
