import maya.cmds as mc
import maya.mel as mel

class ProjectSetter:
    def exe(self):
        filetype = "Maya Scenes(*.ma,*.mb);; OBJ(*.obj);; FBX(*.fbx)"
        filedialog = mc.fileDialog2(ff=filetype, fm=1)

        set = filedialog[0]
        spl = set.split("/scenes")
        mel.eval('setProject "{}" ;'.format(spl[0)]))
        mc.file(set[0], o=True, f=True)

a = ProjectSetter
a.exe()