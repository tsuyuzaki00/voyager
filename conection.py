import maya.cmds as cmds

a = cmds.ls(sl=True, dag=True)
print a

for mae in a[0:3]:
    for ushiro in a[4:8]:
        cmds.pointConstraint(mae , ushiro)
