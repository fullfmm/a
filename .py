import maya.cmds as cmds


"オブジェクトから全マテリアルを取得"
def getgeo():

    sel = cmds.ls(sl=True)
    
    mtl_list = []
    shapes = cmds.listRelatives(sel, shapes=True)

    if not shapes:
        return mtl_list
    SGs = cmds.listConnections(shapes[0], source=False, type='shadingEngine')

    if not SGs:
        return mtl_list
    mtl_list = cmds.ls(cmds.listConnections(SGs[0], destination=False), materials=True)
    return mtl_list

"カラー黒"
def col():
    for rend in mt:

        cmds.editRenderLayerAdjustment(rend+".color")
        cmds.setAttr(rend+".color",0,0,0, type = "double3")

"マットの不透明度モード"
def black():
    for rend in mt:

        cmds.editRenderLayerAdjustment(rend+".matteOpacityMode")
        cmds.setAttr(rend+".matteOpacityMode", 0)

"アンビエントカラーのオーバーライド"
def ambi():
    for rend in mt:
        cmds.editRenderLayerAdjustment(rend+".ambientColor")       
        cmds.setAttr(rend+".ambientColor",0,0,0, type = "double3")

"UI"
cmds.window(title="松崎化",widthHeight=(253,137))
cmds.columnLayout( columnAttach=('both', 5), rowSpacing=10, columnWidth=250 ) 
cmds.button(label='取得',command='mt = getgeo()')
cmds.button(label='カラー黒',command='col()')
cmds.button(label='アンビエント黒',command='ambi()')
cmds.button(label='ブラックホール',command='black()')

cmds.showWindow()
