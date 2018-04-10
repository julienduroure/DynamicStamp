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

import bpy

class DynamicStampFrame(bpy.types.PropertyGroup):
    name  = bpy.props.StringProperty(name="Frame")
    note  = bpy.props.StringProperty(name="Note")

def register():
    bpy.utils.register_class(DynamicStampFrame)

def unregister():
    bpy.utils.unregister_class(DynamicStampFrame)
