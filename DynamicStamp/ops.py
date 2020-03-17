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
from bpy.app.handlers import persistent

@persistent
def juds_frame_change_handler(scene):
    if not bpy.context.scene.juds_use_dynstamp:
        return

    frame = bpy.context.scene.frame_current
    if str(frame) not in [framedata.name for framedata in bpy.context.scene.juds_data]:
        if not bpy.context.scene.juds_use_placeholder:
            bpy.context.scene.render.use_stamp_note = False
            return
        bpy.context.scene.render.use_stamp_note = True
        bpy.context.scene.render.stamp_note_text = bpy.context.scene.juds_placeholder
        return

    bpy.context.scene.render.use_stamp_note = True
    framedata_index = bpy.context.scene.juds_data.find(str(frame))
    bpy.context.scene.render.stamp_note_text = bpy.context.scene.juds_data[framedata_index].note


class POSE_OT_juds_update_text(bpy.types.Operator):
    bl_idname = "text.juds_update_text"
    bl_label = "Update Data"
    bl_options = {'REGISTER'}

    @classmethod
    def poll(self, context):
        return True

    def execute(self, context):
        while len(context.scene.juds_data) != 0:
            context.scene.juds_data.remove(0)

        for line in bpy.data.texts[context.scene.juds_text].lines:
            tab = line.body.split(";",1)
            if len(tab) != 2:
                continue
            try:
                frame = int(tab[0])
                framedata = context.scene.juds_data.add()
                framedata.name = str(frame)
                framedata.note  = tab[1]
            except: pass

        return {'FINISHED'}

def register():
    bpy.utils.register_class(POSE_OT_juds_update_text)
    bpy.app.handlers.frame_change_post.append(juds_frame_change_handler)
    bpy.app.handlers.render_pre.append(juds_frame_change_handler)

def unregister():
    bpy.utils.unregister_class(POSE_OT_juds_update_text)
    bpy.app.handlers.frame_change_post.remove(juds_frame_change_handler)
    bpy.app.handlers.render_pre.remove(juds_frame_change_handler)
