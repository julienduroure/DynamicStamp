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

class POSE_PT_juds_dynstamp(bpy.types.Panel):
    bl_label = 'Dynamic Note Stamp'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "output"

    @classmethod
    def poll(self, context):
        return True

    def draw_header(self, context):
        self.layout.prop(context.scene, "juds_use_dynstamp", text="")
        if context.scene.juds_use_dynstamp:
            if len(context.scene.juds_data) == 0:
                self.layout.label(text="", icon='ERROR')

    def draw(self, context):
        layout = self.layout
        if not context.scene.juds_use_dynstamp:
            return

        row = layout.row()
        col = row.column(align=True)
        col.prop_search(context.scene, "juds_text", bpy.data, "texts", text="Text")
        col = row.column(align=True)
        col.operator("text.juds_update_text", icon='FILE_REFRESH', text='')

        row = layout.row()
        col = row.column(align=True)
        col.prop(context.scene, "juds_use_placeholder", text="Use Placeholder")
        col = row.column(align=True)
        col.prop(context.scene, "juds_placeholder", text="")
        col.active = context.scene.juds_use_placeholder

def register():
    bpy.utils.register_class(POSE_PT_juds_dynstamp)

def unregister():
    bpy.utils.unregister_class(POSE_PT_juds_dynstamp)
