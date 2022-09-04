# 该作品依赖python运行，若没有安装python，请到
# https://www.python.org/downloads/
# 下载并安装最新python
# linux用户可以直接使用安装命令安装最新python

'''
程序编写时使用的是python 3.10，Windows10
作者 南海蒟蒻 https://codingclip.com/user/110
版本 1.0.1

该程序仅供使用，若有bug请反馈。
若想要避免转换失败造成的损失，请不要删除源文件，除非你确保转换完全是成功的。
不支持使用sb3转换，因为使用了codingclip的扩展导出为sb3容易导致无法再导入到编辑器。
'''
#————————————————————————————————————————————————————
print(__doc__)
#————————————————————————————————————————————————————
#支持库
import json
import zipfile
import re
import tkinter as tk
from tkinter import filedialog
import os,sys,shutil
import ctypes
#解决Windows系统屏幕缩放导致窗口模糊的问题
if __name__ == "__main__":
    if 'win' in sys.platform:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

null,true,false=None,True,False
cvsImage自定义函数支持库= { "raphael.cvsImage.def.loadImage": { "opcode": "procedures_definition", "next": "raphael.cvsImage.shiki.load.loadImage", "parent": null, "inputs": { "custom_block": [ 1, "raphael.cvsImage.fun.loadImage" ] }, "fields": {}, "shadow": false, "topLevel": true, "x": -1484, "y": -1386 }, "raphael.cvsImage.fun.loadImage": { "opcode": "procedures_prototype", "next": null, "parent": "raphael.cvsImage.def.loadImage", "inputs": { "raphael.cvsImage.fun.loadImage.inputs.image": [ 1, "raphael.cvsImage.fun.loadImage.image" ] }, "fields": {}, "shadow": true, "topLevel": false, "mutation": { "tagName": "mutation", "children": [], "proccode": "妙笔. cvsImage. loadImage %s", "argumentids": "[\"raphael.cvsImage.fun.loadImage.inputs.image\"]", "argumentnames": "[\"image\"]", "argumentdefaults": "[\"\",\"\",\"\"]", "warp": "false", "global": "false", "return": "false" } }, "raphael.cvsImage.fun.loadImage.image": { "opcode": "argument_reporter_string_number", "next": null, "parent": "raphael.cvsImage.fun.loadImage", "inputs": {}, "fields": { "VALUE": [ "image", null ] }, "shadow": true, "topLevel": false }, "raphael.cvsImage.def.drawImage": { "opcode": "procedures_definition", "next": "raphael.cvsImage.ifPointNotInimage", "parent": null, "inputs": { "custom_block": [ 1, "raphael.cvsImage.fun.drawImage" ] }, "fields": {}, "shadow": false, "topLevel": true, "x": -1492, "y": -1136 }, "raphael.cvsImage.fun.drawImage": { "opcode": "procedures_prototype", "next": null, "parent": "raphael.cvsImage.def.drawImage", "inputs": { "raphael.cvsImage.fun.drawImage.inputs.image": [ 1, "raphael.cvsImage.fun.drawImage.image" ], "raphael.cvsImage.fun.drawImage.inputs.x": [ 1, "raphael.cvsImage.fun.drawImage.x" ], "raphael.cvsImage.fun.drawImage.inputs.y": [ 1, "raphael.cvsImage.fun.drawImage.y" ] }, "fields": {}, "shadow": true, "topLevel": false, "mutation": { "tagName": "mutation", "children": [], "proccode": "妙笔. cvsImage. drawImage %s %s %s", "argumentids": "[\"raphael.cvsImage.fun.drawImage.inputs.image\",\"raphael.cvsImage.fun.drawImage.inputs.x\",\"raphael.cvsImage.fun.drawImage.inputs.y\"]", "argumentnames": "[\"image\",\"x\",\"y\"]", "argumentdefaults": "[\"\",\"\",\"\"]", "warp": "false", "global": "false", "return": "false" } }, "raphael.cvsImage.fun.drawImage.image": { "opcode": "argument_reporter_string_number", "next": null, "parent": "raphael.cvsImage.fun.drawImage", "inputs": {}, "fields": { "VALUE": [ "image", null ] }, "shadow": true, "topLevel": false }, "raphael.cvsImage.fun.drawImage.x": { "opcode": "argument_reporter_string_number", "next": null, "parent": "raphael.cvsImage.fun.drawImage", "inputs": {}, "fields": { "VALUE": [ "x", null ] }, "shadow": true, "topLevel": false }, "raphael.cvsImage.fun.drawImage.y": { "opcode": "argument_reporter_string_number", "next": null, "parent": "raphael.cvsImage.fun.drawImage", "inputs": {}, "fields": { "VALUE": [ "y", null ] }, "shadow": true, "topLevel": false }, "raphael.cvsImage.shiki.draw.loadImage.Name": { "opcode": "argument_reporter_string_number", "next": null, "parent": "raphael.cvsImage.shiki.drawImage", "inputs": {}, "fields": { "VALUE": [ "image", null ] }, "shadow": false, "topLevel": false }, "raphael.cvsImage.shiki.draw.loadImage.DX": { "opcode": "argument_reporter_string_number", "next": null, "parent": "raphael.cvsImage.shiki.drawImage", "inputs": {}, "fields": { "VALUE": [ "x", null ] }, "shadow": false, "topLevel": false }, "raphael.cvsImage.shiki.draw.loadImage.DY": { "opcode": "argument_reporter_string_number", "next": null, "parent": "raphael.cvsImage.shiki.drawImage", "inputs": {}, "fields": { "VALUE": [ "y", null ] }, "shadow": false, "topLevel": false }, "raphael.cvsImage.ifPointNotInimage": { "opcode": "control_if", "next": "raphael.cvsImage.shiki.drawImage", "parent": "raphael.cvsImage.def.drawImage", "inputs": { "SUBSTACK": [ 2, "raphael.cvsImage.shiki.draw.loadImage" ], "CONDITION": [ 2, "raphael.cvsImage.ifPointNotInimage.not" ] }, "fields": {}, "shadow": false, "topLevel": false }, "raphael.cvsImage.shiki.load.loadImage": { "opcode": "shiki.raphael.loadImage", "next": null, "parent": "raphael.cvsImage.def.loadImage", "inputs": { "TYPE": [ 1, "raphael.cvsImage.shiki.load.loadImage.TYPE" ], "CONTENT": [ 3, "raphael.cvsImage.shiki.load.loadImage.CONTENT", [ 10, "" ] ], "NAME": [ 3, "raphael.cvsImage.shiki.load.loadImage.NAME", [ 10, "" ] ] }, "fields": {}, "shadow": false, "topLevel": false }, "raphael.cvsImage.shiki.load.loadImage.TYPE": { "opcode": "shiki.raphael.loadImage.menu_TYPE", "next": null, "parent": "raphael.cvsImage.shiki.load.loadImage", "inputs": {}, "fields": { "TYPE": [ "md5", null ] }, "shadow": true, "topLevel": false }, "raphael.cvsImage.shiki.load.loadImage.NAME": { "opcode": "argument_reporter_string_number", "next": null, "parent": "raphael.cvsImage.shiki.load.loadImage", "inputs": {}, "fields": { "VALUE": [ "image", null ] }, "shadow": false, "topLevel": false }, "raphael.cvsImage.shiki.load.loadImage.CONTENT": { "opcode": "argument_reporter_string_number", "next": null, "parent": "raphael.cvsImage.shiki.load.loadImage", "inputs": {}, "fields": { "VALUE": [ "image", null ] }, "shadow": false, "topLevel": false }, "raphael.cvsImage.ifPointNotInimage.not.contains.image": { "opcode": "argument_reporter_string_number", "next": null, "parent": "raphael.cvsImage.ifPointNotInimage.not.contains", "inputs": {}, "fields": { "VALUE": [ "image", null ] }, "shadow": false, "topLevel": false }, "raphael.cvsImage.ifPointNotInimage.not.contains": { "opcode": "operator_contains", "next": null, "parent": "raphael.cvsImage.ifPointNotInimage.not", "inputs": { "STRING1": [ 3, "raphael.cvsImage.ifPointNotInimage.not.contains.image", [ 10, "" ] ], "STRING2": [ 1, [ 10, "." ] ] }, "fields": {}, "shadow": false, "topLevel": false }, "raphael.cvsImage.ifPointNotInimage.not": { "opcode": "operator_not", "next": null, "parent": "raphael.cvsImage.ifPointNotInimage", "inputs": { "OPERAND": [ 2, "raphael.cvsImage.ifPointNotInimage.not.contains" ] }, "fields": {}, "shadow": false, "topLevel": false }, "raphael.cvsImage.shiki.drawImage": { "opcode": "shiki.raphael.drawImage", "next": null, "parent": "raphael.cvsImage.ifPointNotInimage", "inputs": { "NAME": [ 3, "raphael.cvsImage.shiki.draw.loadImage.NAME", [ 10, "" ] ], "DX": [ 3, "raphael.cvsImage.shiki.draw.loadImage.DX", [ 4, "" ] ], "DY": [ 3, "raphael.cvsImage.shiki.draw.loadImage.DY", [ 4, "" ] ] }, "fields": {}, "shadow": false, "topLevel": false }, "raphael.cvsImage.shiki.draw.loadImage": { "opcode": "shiki.raphael.loadImage", "next": null, "parent": "raphael.cvsImage.ifPointNotInimage", "inputs": { "TYPE": [ 1, "raphael.cvsImage.shiki.draw.loadImage.TYPE" ], "CONTENT": [ 3, "raphael.cvsImage.shiki.draw.loadImage.CONTENT", [ 10, "" ] ], "NAME": [ 3, "raphael.cvsImage.shiki.draw.loadImage.NAME", [ 10, "" ] ] }, "fields": {}, "shadow": false, "topLevel": false }, "raphael.cvsImage.shiki.draw.loadImage.TYPE": { "opcode": "shiki.raphael.loadImage.menu_TYPE", "next": null, "parent": "raphael.cvsImage.shiki.draw.loadImage", "inputs": {}, "fields": { "TYPE": [ "artboard", null ] }, "shadow": true, "topLevel": false }, "raphael.cvsImage.shiki.draw.loadImage.CONTENT": { "opcode": "argument_reporter_string_number", "next": null, "parent": "raphael.cvsImage.shiki.draw.loadImage", "inputs": {}, "fields": { "VALUE": [ "image", null ] }, "shadow": false, "topLevel": false }, "raphael.cvsImage.shiki.draw.loadImage.NAME": { "opcode": "argument_reporter_string_number", "next": null, "parent": "raphael.cvsImage.shiki.draw.loadImage", "inputs": {}, "fields": { "VALUE": [ "image", null ] }, "shadow": false, "topLevel": false } }
#————————————————————————————————————————————————————
#导入
print('正在导入文件，请留意弹出的窗口')
fileTypes=[('JSON','*.json'),('所有文件','*')]
fileTypes_sprite=[('可用的文件格式','*.sprite3 *.json'),('角色','*.sprite3'),('JSON','*.json'),('所有文件','*')]
fileTypes_project=[('可用的文件格式','*.cc3 *.json'),('codingclip项目','*.cc3'),('JSON','*.json'),('所有文件','*')]
fileTypes_all=[('可用的文件格式','*.sprite3 *.cc3 *.json'),('角色','*.sprite3'),('codingclip项目','*.cc3'),('JSON','*.json'),('所有文件','*')]
root = tk.Tk()
root.withdraw()
importFilepath = filedialog.askopenfilename(title='导入文件 - cvs转画笔',filetypes=fileTypes_all)
if importFilepath == '':
    print("未导入文件")
    exit()
importFilename = initialfile=importFilepath.split('/' if '/' in importFilepath else '\\')[-1]
[importFilename_name,importFilename_suffix]=importFilename.split('.')
if not importFilename_suffix in ['sprite3','cc3','json']:
    print("导入的不是支持的格式，请检查文件或后缀")
    exit()

print('\n选择导出目录，请留意弹出的窗口')
exportfilepath = filedialog.asksaveasfilename(title='导出文件 - cvs转妙笔',initialfile=importFilename_name+' - cvs转妙笔.'+importFilename_suffix,  filetypes= [fileTypes_project,fileTypes_sprite,fileTypes][['cc3','sprite3','json'].index(importFilename_suffix)])
if exportfilepath==None:
    print('未选择导出路径')
    exit()
if not '.' in exportfilepath.split('/' if '/' in exportfilepath else '\\')[-1]:
    exportfilepath=exportfilepath+'.'+importFilename_suffix
[exportfilepath_name,exportfilepath_suffix]=exportfilepath.split('.')
if not exportfilepath_suffix in ['sprite3','cc3','json']:
    print("导出的不是支持的格式，请不要填入不支持的文件后缀")
    exit()
if exportfilepath_suffix!=importFilename_suffix and exportfilepath_suffix!='json':
    print("不支持导出另外的格式，除了导出为独立的JSON格式文件")
    exit()
#————————————————————————————————————————————————————
#定义函数

def addParameterBlock(blockId,jsonOpcode,jsonFields):
    global sprite_jsontxt
    sprite_jsontxt['blocks'].update({blockId:{"opcode": jsonOpcode,"next": null,"parent": i,"inputs": {},"fields": jsonFields,"shadow": true,"topLevel": false}})

需要cvsImage支持库=False
def 更改参数的转换(block):
    global sprite_jsontxt; global name

    if name in ['setFillStyle','setStrokeStyle']:
        #颜色设置模块
        nameInList=['setFillStyle','setStrokeStyle'].index(name)
        addParameterBlock(('setColor'+i), "shiki.raphael.setColor.menu_TYPE", {"TYPE": [['fill','stroke'][nameInList],null]})
        STYLE=['FILL_STYLE','STROKE_STYLE'][nameInList]
        #此处必须判断填入的为颜色码格式，否则填入其它的将导致无法导入
        if re.match('^#[0-9a-fA-F]{6}$',block['inputs'][STYLE][-1][1]):
            block['inputs'][STYLE][-1][0] = 9
        block['inputs'].update({"TYPE":[1,'setColor'+i],"COLOR":block['inputs'][STYLE]})
        block['inputs'].pop(STYLE)
        block['opcode'] = 'shiki.raphael.setColor'

    elif name in ['setLineWidth','setGlobalAlpha']:
        #线条粗细、透明度 设置模块
        nameInList=['setLineWidth','setGlobalAlpha'].index(name)
        SET=['LINE_WIDTH','ALPHA'][nameInList]
        addParameterBlock(('setArttibuteTo'+i), "shiki.raphael.setArttibuteTo.menu_ATTRIBUTE", {"ATTRIBUTE": [['lineWidth','globalAlpha'][nameInList]]})
        block['inputs'].update({"ATTRIBUTE":[1,'setArttibuteTo'+i],"NUMBER":block['inputs'][SET]})
        block['inputs'].pop(SET)
        block['opcode'] = 'shiki.raphael.setArttibuteTo'

    elif name=='setLineCap':
        #笔头形状设置
        addParameterBlock(('setLineCap'+i), "shiki.raphael.setLineCap.menu_VALUE", {"VALUE": [block['inputs']['LINE_CAP'][1][1],null]})
        block['inputs'].update({"VALUE":[block['inputs']['LINE_CAP']]})
        if block['inputs']['VALUE'][0] == 3:
            block['inputs']['VALUE'][2] = [1, 'setLineCap'+i]
        else:
            block['inputs']['VALUE'] = [1, 'setLineCap'+i]
        block['inputs'].pop('LINE_CAP')
        block['opcode'] = 'shiki.raphael.setLineCap'

    elif name in ['measureText','arc','clip','fill']:
        #文字打印横向长度、画圆、裁剪、填充 模块
        nameInList=['measureText','arc','clip','fill'].index(name)
        typelist=["ATTRIBUTE",'ANTICLOCKWISE','FILLRULE','FILLRULE']
        nowtype=typelist[nameInList]
        addParameterBlock((name+i), 'shiki.raphael.'+name+'.menu_'+nowtype, {nowtype: [["width","false",'nonzero','nonzero'][nameInList]]})
        block['inputs'].update({nowtype:[1,name+i]})
        block['opcode'] = 'shiki.raphael.'+name

    elif name =='scale':
        block['inputs'].update({"X": block['inputs']['SCALE_W'], "Y": block['inputs']['SCALE_H']})
        block['inputs'].pop('SCALE_W'); block['inputs'].pop('SCALE_H')
        block['opcode'] = 'shiki.raphael.scale'

    elif name in ['setGlobalCompositeOperation','switchCanvas']:
        #覆盖方式、画板切换 设置模块
        nameInList=['setGlobalCompositeOperation','switchCanvas'].index(name)
        block['inputs'].update({["CO",'ID'][nameInList]:block['inputs'][['CompositeOperation','NUMBER'][nameInList]]})
        block['inputs'].pop(['CompositeOperation','NUMBER'][nameInList])
        block['opcode'] = 'shiki.raphael.'+['setGlobalCompositeOperation','setArtboardIdTo'][nameInList]

    elif name in ['loadImage','drawImage']:
        #加载、打印 图片模块
        global 需要cvsImage支持库
        需要cvsImage支持库=True
        block['opcode'] = 'procedures_call'
        block['inputs'].update({"raphael.cvsImage.fun."+name+".inputs.image": block['inputs']['IMAGE_ID']})
        block['inputs'].pop('IMAGE_ID')
        if name == 'drawImage':
            block['inputs'].update({"raphael.cvsImage.fun."+name+".inputs.x": block['inputs']['X'], "raphael.cvsImage.fun."+name+".inputs.y": block['inputs']['Y']})
            block['inputs'].pop('X'); block['inputs'].pop('Y')
            block.update({"mutation": { "tagName": "mutation", "children": [], "proccode": "妙笔. cvsImage. drawImage %s %s %s", "argumentids": "[\"raphael.cvsImage.fun.drawImage.inputs.image\",\"raphael.cvsImage.fun.drawImage.inputs.x\",\"raphael.cvsImage.fun.drawImage.inputs.y\"]", "warp": "false", "global": "false", "return": "false" }})
        else:
            block.update({"mutation": { "tagName": "mutation", "children": [], "proccode": "妙笔. cvsImage. loadImage %s", "argumentids": "[\"raphael.cvsImage.fun.loadImage.inputs.image\"]", "warp": "false", "global": "false", "return": "false" }})

    sprite_jsontxt['blocks'][i] = block

#————————————————————————————————————————————————————
#加载JSON文件
print('JSON加载中……')
cvs= ['beginPath','closePath','setFillStyle','setStrokeStyle','setLineWidth','setLineCap','setFont','strokeText','fillText','measureText','loadImage','drawImage','clearRect','moveTo','scale','rotate','translate','transform','clearTransform','save','restore','setGlobalAlpha','setGlobalCompositeOperation','switchCanvas','lineTo','arc','rect','clip','fill','stroke','stampOnStage']
只改opc的cvs= ['beginPath','closePath','setFont','strokeText','fillText','clearRect','moveTo','translate','transform','clearTransform','save','restore','lineTo','rect','stroke','stampOnStage','rotate']
直接改opcode的cvs积木结果= ['beginPath','closePath','setFont','strokeText','fillText','clearRect','moveTo','translate','transform','resetTransform','save','restore','lineTo','rect','stroke','apply','rotate']

if exportfilepath_suffix=='json':
    with open(importFilepath, 'r',encoding='utf-8') as f:
        try:
            sprite_jsontxt = json.load(f)
        except Exception as jsonloaderror:
            print('JSON加载失败，程序停止。报错：%s'%jsonloaderror)
            exit()
else:
    z = zipfile.ZipFile(importFilepath, "r")
    z_namelist=z.namelist()
    f = content = z.read('sprite.json' if importFilename_suffix=='sprite3' else 'project.json').decode('utf-8')
    try:
        jsontxt = json.loads(f)
    except Exception as jsonloaderror:
        print('JSON加载失败，程序停止。报错：%s'%jsonloaderror)
        exit()
    #z.close()

if importFilename_suffix=='json':
    try: i= jsontxt["targets"]; isproject=True
    except: isproject=False
else:
    isproject= exportfilepath_suffix=='cc3'
#————————————————————————————————————————————————————
#转换文件（不修改源文件）
print('转换中……')
for spriteid in range(len(jsontxt["targets"]) if isproject else 1):
    sprite_jsontxt= jsontxt["targets"][spriteid] if isproject else jsontxt
    sprite_jsontxtblocks=sprite_jsontxt['blocks']
    for i in list(sprite_jsontxtblocks.keys()):
        try:
            opcode=sprite_jsontxtblocks[i]['opcode']
            if 'alpha.canvas.' in opcode:
                name = sprite_jsontxtblocks[i]['opcode'].split('.')[2]
                if name in 只改opc的cvs:
                    sprite_jsontxt['blocks'][i]['opcode'] = 'shiki.raphael.'+直接改opcode的cvs积木结果[只改opc的cvs.index(name)]
                elif name in cvs:
                    更改参数的转换(sprite_jsontxtblocks[i])
                else:
                    print("\n当前cvs积木不存在，请检查JSON文件里对应积木。\nblockID：%s\nblock内容：%s"%(i,sprite_jsontxtblocks[i]))
        except Exception as transfromError:
            print("\n当前积木转换失败，请检查JSON文件里对应积木。\nblockID：%s\nblock内容：%s\n报错：%s"%(i,sprite_jsontxtblocks[i],transfromError))
    #若有用到Image模块，则添加支持库
    if 需要cvsImage支持库:
        sprite_jsontxt['blocks'].update(cvsImage自定义函数支持库)
    if isproject:
        jsontxt["targets"][spriteid]= sprite_jsontxt
    else:
        jsontxt= sprite_jsontxt

#导出为新文件
def force_rename(beforepath,afterpath):
    #删除重名文件，强行重命名
    if os.path.exists(afterpath):
        os.remove(afterpath)
    os.rename(beforepath,afterpath)

print('导出文件中')
if exportfilepath_suffix=='json':
    with open(exportfilepath+'ouputing', 'w+',encoding='utf-8') as out:
        out.write(json.dumps(jsontxt))
else:
    nowzippath= exportfilepath+'.ouputing'
    nowjsonname= 'project.json' if isproject else 'sprite.json'
    outzip= zipfile.ZipFile(nowzippath, "w", zipfile.ZIP_DEFLATED)
    for i in z.namelist():
        if i== nowjsonname:
            outzip.writestr(('project.json' if isproject else 'sprite.json'), data=json.dumps(jsontxt))
        else:
            outzip.writestr(i,z.read(i))
    outzip.close()
    force_rename(nowzippath,nowzippath+'.finish')
    force_rename(nowzippath+'.finish',exportfilepath)

print('导出完成')