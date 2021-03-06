# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Cryptomatte_KeyerExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Cryptomatte_KeyerExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Cryptomatte_Keyer"

def getLabel():
    return "Cryptomatte_Keyer"

def getVersion():
    return 1

def getIconPath():
    return "Cryptomatte_Keyer.png"

def getGrouping():
    return "Community/Keyer"

def getPluginDescription():
    return "Extracts Cryptomattes"

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(0.7, 0.7, 0.7)

    # Create the user parameters
    lastNode.userNatron = lastNode.createPageParam("userNatron", "control")
    param = lastNode.createColorParam("CrytoMatte_MaskparamValueVec30", "Matte ID 1:", False)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CrytoMatte_MaskparamValueVec30 = param
    del param

    param = lastNode.createColorParam("CrytoMatte_MaskparamValueVec31", "Matte ID 2:", False)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CrytoMatte_MaskparamValueVec31 = param
    del param

    param = lastNode.createColorParam("CrytoMatte_MaskparamValueVec32", "Matte ID 3:", False)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CrytoMatte_MaskparamValueVec32 = param
    del param

    param = lastNode.createColorParam("CrytoMatte_MaskparamValueVec33", "Matte ID 4:", False)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CrytoMatte_MaskparamValueVec33 = param
    del param

    param = lastNode.createColorParam("CrytoMatte_MaskparamValueVec34", "Matte ID 5:", False)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CrytoMatte_MaskparamValueVec34 = param
    del param

    param = lastNode.createColorParam("CrytoMatte_MaskparamValueVec35", "Matte ID 6:", False)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CrytoMatte_MaskparamValueVec35 = param
    del param

    param = lastNode.createColorParam("CrytoMatte_MaskparamValueVec36", "Matte ID 7:", False)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CrytoMatte_MaskparamValueVec36 = param
    del param

    param = lastNode.createColorParam("CrytoMatte_MaskparamValueVec37", "Matte ID 8:", False)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CrytoMatte_MaskparamValueVec37 = param
    del param

    param = lastNode.createColorParam("CrytoMatte_MaskparamValueVec38", "Matte ID 9:", False)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CrytoMatte_MaskparamValueVec38 = param
    del param

    param = lastNode.createColorParam("CrytoMatte_MaskparamValueVec39", "Matte ID 10:", False)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CrytoMatte_MaskparamValueVec39 = param
    del param

    param = lastNode.createColorParam("CrytoMatte_MaskparamValueVec310", "Matte ID 11:", False)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CrytoMatte_MaskparamValueVec310 = param
    del param

    param = lastNode.createColorParam("CrytoMatte_MaskparamValueVec311", "Matte ID 12:", False)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CrytoMatte_MaskparamValueVec311 = param
    del param

    param = lastNode.createColorParam("CrytoMatte_MaskparamValueVec312", "Matte ID 13:", False)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CrytoMatte_MaskparamValueVec312 = param
    del param

    param = lastNode.createColorParam("CrytoMatte_MaskparamValueVec313", "Matte ID 14:", False)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CrytoMatte_MaskparamValueVec313 = param
    del param

    param = lastNode.createColorParam("CrytoMatte_MaskparamValueVec314", "Matte ID 15:", False)

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.CrytoMatte_MaskparamValueVec314 = param
    del param

    param = lastNode.createSeparatorParam("sep1", "Connect BG_In Node to Extract Mask, Useful for Multiple Crytomatte Nodes")

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sep1 = param
    del param

    param = lastNode.createBooleanParam("maskextract", "Extract Mask")

    # Add the param to the page
    lastNode.userNatron.addParam(param)

    # Set param properties
    param.setHelp("Check if extracting mask is needed. Usefull when multiple Crypto nodes needs to be meged.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.maskextract = param
    del param

    lastNode.Credit = lastNode.createPageParam("Credit", "Credit")
    param = lastNode.createSeparatorParam("sepa", "Original dev: (Fabrice Fernandez - 2018)")

    # Add the param to the page
    lastNode.Credit.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sepa = param
    del param

    param = lastNode.createSeparatorParam("sepb", "Refactoring, Modulation and redesign by")

    # Add the param to the page
    lastNode.Credit.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sepb = param
    del param

    param = lastNode.createSeparatorParam("sepc", "Fahad Hasan Pathik CGVIRUS")

    # Add the param to the page
    lastNode.Credit.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sepc = param
    del param

    param = lastNode.createSeparatorParam("sepd", "")

    # Add the param to the page
    lastNode.Credit.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.sepd = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['userNatron', 'Credit', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Clamp_Alpha"
    lastNode = app.createNode("net.sf.openfx.Clamp", 2, group)
    lastNode.setScriptName("Clamp_Alpha")
    lastNode.setLabel("Clamp_Alpha")
    lastNode.setPosition(833, 223)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.48, 0.66, 1)
    groupClamp_Alpha = lastNode

    del lastNode
    # End of node "Clamp_Alpha"

    # Start of node "CrytoMatte_Mask"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("CrytoMatte_Mask")
    lastNode.setLabel("CrytoMatte_Mask")
    lastNode.setPosition(839, 120)
    lastNode.setSize(104, 55)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupCrytoMatte_Mask = lastNode

    param = lastNode.getParam("paramValueVec30")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("paramValueBool1")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("paramValueVec31")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("paramValueVec32")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("paramValueVec33")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("paramValueVec34")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("paramValueVec35")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("paramValueVec36")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("paramValueVec37")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("paramValueVec38")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("paramValueVec39")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("paramValueVec310")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("paramValueVec311")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("paramValueVec312")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("paramValueVec313")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("paramValueVec314")
    if param is not None:
        param.setValue(0, 0)
        param.setValue(0, 1)
        param.setValue(0, 2)
        del param

    param = lastNode.getParam("imageShaderFileName")
    if param is not None:
        param.setValue("/home/production/Code_PRojects/cryptomatte/Flame/crypto4.glsl")
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("/* Further Development: Fahad Hasan Pathik (CGVIRUS)\nCode is refactored,simplified for multiID with single matte only\nusing modular functionality, GPU Buffer issue is solved. Innode Clamping (done).\n*/\n\n// Adaptation pour Natron par F. Fernandez\n// Code original : Cryptomatte Matchbox pour Autodesk Flame\n\n// Adapted to Natron by F.Fernandez\n// Original code : Cryptomatte Matchbox for Autodesk Flame\n\n/* Cryptomatte\n     Given a set of ID/coverage pairs, extract up to four mattes\n     See https://github.com/Psyop/Cryptomatte\n     This shader by lewis@lewissaunders.com\n     TODO: allow picking using the standard colour pots if the 65504.0\n           limit is ever removed\n*/\n\n// iChannel0: Crypto_ID 1, filter=linear, wrap=clamp\n// BBox: iChannel0\n\n\n// colour pickers\nuniform vec3 pickm1 = vec3( 0.0 , 0.0 , 0.0 );        // Matte ID 1: \nuniform vec3 pickm2 = vec3( 0.0 , 0.0 , 0.0 );        // Matte ID 2: \nuniform vec3 pickm3 = vec3( 0.0 , 0.0 , 0.0 );        // Matte ID 3: \nuniform vec3 pickm4 = vec3( 0.0 , 0.0 , 0.0 );        // Matte ID 4: \nuniform vec3 pickm5 = vec3( 0.0 , 0.0 , 0.0 );        // Matte ID 5: \nuniform vec3 pickm6 = vec3( 0.0 , 0.0 , 0.0 );        // Matte ID 6: \nuniform vec3 pickm7 = vec3( 0.0 , 0.0 , 0.0 );        // Matte ID 7: \nuniform vec3 pickm8 = vec3( 0.0 , 0.0 , 0.0 );        // Matte ID 8: \nuniform vec3 pickm9 = vec3( 0.0 , 0.0 , 0.0 );        // Matte ID 9: \nuniform vec3 pickm10 = vec3( 0.0 , 0.0 , 0.0 );       // Matte ID 10: \nuniform vec3 pickm11 = vec3( 0.0 , 0.0 , 0.0 );       // Matte ID 11: \nuniform vec3 pickm12 = vec3( 0.0 , 0.0 , 0.0 );       // Matte ID 12: \nuniform vec3 pickm13 = vec3( 0.0 , 0.0 , 0.0 );       // Matte ID 13: \nuniform vec3 pickm14 = vec3( 0.0 , 0.0 , 0.0 );       // Matte ID 14: \nuniform vec3 pickm15 = vec3( 0.0 , 0.0 , 0.0 );       // Matte ID 15: \n\n// Accumulate opacity from the ranks for each picked ID\n  vec4 accumulate(vec3 pick_n, vec2 rank0,vec2 rank1,vec2 rank2,\n    vec2 rank3,vec2 rank4,vec2 rank5)\n  {\n  vec4 result = vec4(0.0);\n\n  if(rank0.x == pick_n.r) result.a += rank0.y;\n  if(rank1.x == pick_n.r) result.a += rank1.y;\n  if(rank2.x == pick_n.r) result.a += rank2.y;\n  if(rank3.x == pick_n.r) result.a += rank3.y;\n  if(rank4.x == pick_n.r) result.a += rank4.y;\n  if(rank5.x == pick_n.r) result.a += rank5.y;\n  return result;\n  }\n\n\nvoid mainImage ( out vec4 fragColor, in vec2 fragCoord )\n{\n  // Convert fragment coords in pixels to texel coords in [0..1]\n  vec2 res = vec2(iResolution.x, iResolution.y);\n  vec2 xy = fragCoord.xy / res;\n\n\n\n\n  // In these vectors the first element is the ID, the second the coverage\n  vec2 rank0 = texture2D(iChannel0, xy).rg;\n  vec2 rank1 = vec2(texture2D(iChannel0, xy).b, texture2D(iChannel0, xy).a);\n  vec2 rank2 = texture2D(iChannel1, xy).rg;\n  vec2 rank3 = vec2(texture2D(iChannel1, xy).b, texture2D(iChannel1, xy).a);\n  vec2 rank4 = texture2D(iChannel2, xy).rg;\n  vec2 rank5 = vec2(texture2D(iChannel2, xy).b, texture2D(iChannel2, xy).a);\n\n\n  vec4 c = vec4(0.0);\n  c += accumulate(pickm1,rank0,rank1,rank2,rank3,rank4,rank5);\n  c += accumulate(pickm2,rank0,rank1,rank2,rank3,rank4,rank5);\n  c += accumulate(pickm3,rank0,rank1,rank2,rank3,rank4,rank5);\n  c += accumulate(pickm4,rank0,rank1,rank2,rank3,rank4,rank5);\n  c += accumulate(pickm5,rank0,rank1,rank2,rank3,rank4,rank5);\n  c += accumulate(pickm6,rank0,rank1,rank2,rank3,rank4,rank5);\n  c += accumulate(pickm7,rank0,rank1,rank2,rank3,rank4,rank5);\n  c += accumulate(pickm8,rank0,rank1,rank2,rank3,rank4,rank5);\n  c += accumulate(pickm9,rank0,rank1,rank2,rank3,rank4,rank5);\n  c += accumulate(pickm10,rank0,rank1,rank2,rank3,rank4,rank5);\n  c += accumulate(pickm11,rank0,rank1,rank2,rank3,rank4,rank5);\n  c += accumulate(pickm12,rank0,rank1,rank2,rank3,rank4,rank5);\n  c += accumulate(pickm13,rank0,rank1,rank2,rank3,rank4,rank5);\n  c += accumulate(pickm14,rank0,rank1,rank2,rank3,rank4,rank5);\n  c += accumulate(pickm15,rank0,rank1,rank2,rank3,rank4,rank5);\n\n  vec4 result = vec4(c.r + c.g + c.b + c.a);\n\n  fragColor = result;\n}\n")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("wrap0")
    if param is not None:
        param.set("clamp")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Crypto_ID 1")
        del param

    param = lastNode.getParam("mipmap1")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("wrap1")
    if param is not None:
        param.set("clamp")
        del param

    param = lastNode.getParam("mipmap2")
    if param is not None:
        param.set("linear")
        del param

    param = lastNode.getParam("wrap2")
    if param is not None:
        param.set("clamp")
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(15, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("pickm1")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Matte ID 1:")
        del param

    param = lastNode.getParam("paramType1")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName1")
    if param is not None:
        param.setValue("pickm2")
        del param

    param = lastNode.getParam("paramLabel1")
    if param is not None:
        param.setValue("Matte ID 2:")
        del param

    param = lastNode.getParam("paramType2")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName2")
    if param is not None:
        param.setValue("pickm3")
        del param

    param = lastNode.getParam("paramLabel2")
    if param is not None:
        param.setValue("Matte ID 3:")
        del param

    param = lastNode.getParam("paramType3")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName3")
    if param is not None:
        param.setValue("pickm4")
        del param

    param = lastNode.getParam("paramLabel3")
    if param is not None:
        param.setValue("Matte ID 4:")
        del param

    param = lastNode.getParam("paramType4")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName4")
    if param is not None:
        param.setValue("pickm5")
        del param

    param = lastNode.getParam("paramLabel4")
    if param is not None:
        param.setValue("Matte ID 5:")
        del param

    param = lastNode.getParam("paramType5")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName5")
    if param is not None:
        param.setValue("pickm6")
        del param

    param = lastNode.getParam("paramLabel5")
    if param is not None:
        param.setValue("Matte ID 6:")
        del param

    param = lastNode.getParam("paramType6")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName6")
    if param is not None:
        param.setValue("pickm7")
        del param

    param = lastNode.getParam("paramLabel6")
    if param is not None:
        param.setValue("Matte ID 7:")
        del param

    param = lastNode.getParam("paramType7")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName7")
    if param is not None:
        param.setValue("pickm8")
        del param

    param = lastNode.getParam("paramLabel7")
    if param is not None:
        param.setValue("Matte ID 8:")
        del param

    param = lastNode.getParam("paramType8")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName8")
    if param is not None:
        param.setValue("pickm9")
        del param

    param = lastNode.getParam("paramLabel8")
    if param is not None:
        param.setValue("Matte ID 9:")
        del param

    param = lastNode.getParam("paramType9")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName9")
    if param is not None:
        param.setValue("pickm10")
        del param

    param = lastNode.getParam("paramLabel9")
    if param is not None:
        param.setValue("Matte ID 10:")
        del param

    param = lastNode.getParam("paramType10")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName10")
    if param is not None:
        param.setValue("pickm11")
        del param

    param = lastNode.getParam("paramLabel10")
    if param is not None:
        param.setValue("Matte ID 11:")
        del param

    param = lastNode.getParam("paramType11")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName11")
    if param is not None:
        param.setValue("pickm12")
        del param

    param = lastNode.getParam("paramLabel11")
    if param is not None:
        param.setValue("Matte ID 12:")
        del param

    param = lastNode.getParam("paramType12")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName12")
    if param is not None:
        param.setValue("pickm13")
        del param

    param = lastNode.getParam("paramLabel12")
    if param is not None:
        param.setValue("Matte ID 13:")
        del param

    param = lastNode.getParam("paramType13")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName13")
    if param is not None:
        param.setValue("pickm14")
        del param

    param = lastNode.getParam("paramLabel13")
    if param is not None:
        param.setValue("Matte ID 14:")
        del param

    param = lastNode.getParam("paramType14")
    if param is not None:
        param.set("vec3")
        del param

    param = lastNode.getParam("paramName14")
    if param is not None:
        param.setValue("pickm15")
        del param

    param = lastNode.getParam("paramLabel14")
    if param is not None:
        param.setValue("Matte ID 15:")
        del param

    del lastNode
    # End of node "CrytoMatte_Mask"

    # Start of node "MergeExtract"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("MergeExtract")
    lastNode.setLabel("MergeExtract")
    lastNode.setPosition(832, 313)
    lastNode.setSize(104, 55)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMergeExtract = lastNode

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("mask")
        del param

    param = lastNode.getParam("userTextArea")
    if param is not None:
        param.setValue("<Natron>(over)</Natron>")
        del param

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "MergeExtract"

    # Start of node "Shuffle_In"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Shuffle_In")
    lastNode.setLabel("Shuffle_In")
    lastNode.setPosition(472, 120)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShuffle_In = lastNode

    del lastNode
    # End of node "Shuffle_In"

    # Start of node "Output1"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output1")
    lastNode.setPosition(1156, 326)
    lastNode.setSize(104, 31)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput1 = lastNode

    del lastNode
    # End of node "Output1"

    # Start of node "BG_In_To_Extract_MAsk"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("BG_In_To_Extract_MAsk")
    lastNode.setLabel("BG_In To Extract MAsk")
    lastNode.setPosition(466, 216)
    lastNode.setSize(104, 55)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupBG_In_To_Extract_MAsk = lastNode

    param = lastNode.getParam("optional")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "BG_In_To_Extract_MAsk"

    # Start of node "Switch1"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("Switch1")
    lastNode.setLabel("Switch1")
    lastNode.setPosition(1003, 325)
    lastNode.setSize(104, 32)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupSwitch1 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(0, 0)
        del param

    del lastNode
    # End of node "Switch1"

    # Now that all nodes are created we can connect them together, restore expressions
    groupClamp_Alpha.connectInput(0, groupCrytoMatte_Mask)
    groupCrytoMatte_Mask.connectInput(0, groupShuffle_In)
    groupMergeExtract.connectInput(0, groupBG_In_To_Extract_MAsk)
    groupMergeExtract.connectInput(1, groupClamp_Alpha)
    groupOutput1.connectInput(0, groupSwitch1)
    groupSwitch1.connectInput(0, groupClamp_Alpha)
    groupSwitch1.connectInput(1, groupMergeExtract)

    param = groupCrytoMatte_Mask.getParam("paramValueVec30")
    group.getParam("CrytoMatte_MaskparamValueVec30").setAsAlias(param)
    del param
    param = groupCrytoMatte_Mask.getParam("paramValueVec31")
    group.getParam("CrytoMatte_MaskparamValueVec31").setAsAlias(param)
    del param
    param = groupCrytoMatte_Mask.getParam("paramValueVec32")
    group.getParam("CrytoMatte_MaskparamValueVec32").setAsAlias(param)
    del param
    param = groupCrytoMatte_Mask.getParam("paramValueVec33")
    group.getParam("CrytoMatte_MaskparamValueVec33").setAsAlias(param)
    del param
    param = groupCrytoMatte_Mask.getParam("paramValueVec34")
    group.getParam("CrytoMatte_MaskparamValueVec34").setAsAlias(param)
    del param
    param = groupCrytoMatte_Mask.getParam("paramValueVec35")
    group.getParam("CrytoMatte_MaskparamValueVec35").setAsAlias(param)
    del param
    param = groupCrytoMatte_Mask.getParam("paramValueVec36")
    group.getParam("CrytoMatte_MaskparamValueVec36").setAsAlias(param)
    del param
    param = groupCrytoMatte_Mask.getParam("paramValueVec37")
    group.getParam("CrytoMatte_MaskparamValueVec37").setAsAlias(param)
    del param
    param = groupCrytoMatte_Mask.getParam("paramValueVec38")
    group.getParam("CrytoMatte_MaskparamValueVec38").setAsAlias(param)
    del param
    param = groupCrytoMatte_Mask.getParam("paramValueVec39")
    group.getParam("CrytoMatte_MaskparamValueVec39").setAsAlias(param)
    del param
    param = groupCrytoMatte_Mask.getParam("paramValueVec310")
    group.getParam("CrytoMatte_MaskparamValueVec310").setAsAlias(param)
    del param
    param = groupCrytoMatte_Mask.getParam("paramValueVec311")
    group.getParam("CrytoMatte_MaskparamValueVec311").setAsAlias(param)
    del param
    param = groupCrytoMatte_Mask.getParam("paramValueVec312")
    group.getParam("CrytoMatte_MaskparamValueVec312").setAsAlias(param)
    del param
    param = groupCrytoMatte_Mask.getParam("paramValueVec313")
    group.getParam("CrytoMatte_MaskparamValueVec313").setAsAlias(param)
    del param
    param = groupCrytoMatte_Mask.getParam("paramValueVec314")
    group.getParam("CrytoMatte_MaskparamValueVec314").setAsAlias(param)
    del param
    param = groupMergeExtract.getParam("disableNode")
    param.setExpression("if thisGroup.maskextract.get() == True:\n\tret = False\nelse:\n\tret= True", True, 0)
    del param
    param = groupSwitch1.getParam("which")
    param.setExpression("thisGroup.maskextract.get()", False, 0)
    del param

    try:
        extModule = sys.modules["Cryptomatte_KeyerExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
