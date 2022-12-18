# razz music engine
# -> 2022 ConfusedParrotFish

import numpy as np
import clutil as cl
import wav as wgen
import audio_obj as auoj
import sys

# start (subchorous (chorus) drift/drop)* <- (mid:drift) end
tofali = {
    "start": {
        "drift":1/4,
        "subchorous":3/4,
    },
    "subchorous": {
        "chorus":4/7,
        "drop":3/7
    },
    "chorus":{
        "drop":0.5,
        "drift":0.5,
    },
    "drop":{
        "subchorous":1/3,
        "drift":2/3
    },
    "drift":{
        "drop":1/4,
        "subchorous":3/4
    },
}

length = 7

def delivai(value,depth):
    # get ljois, then call on result
    result = []
    cval = ljois(tofali[value])[0]
    result.append(cval)
    # print("\u001b[F"+cl.fg.yellow+(round(depth/length*100).__str__())+"%"+cl.reset)
    # time.sleep(0.000000000025)
    if depth < length:
        result = mix(result,delivai(cval,depth+1))
    return result
def ljois(prth):
    lo = []  # names
    lw = []  # weights
    for i in prth:
        lo.append(i)
        lw.append(prth[i])
    return(np.random.choice(lo,size=1,replace=False, p=lw))

def mix(mol, kal):
    for x in kal:
        mol.append(x)
    return mol
def join(mol):
    res = ""
    for x in mol:
        res += x+" "
    return res.strip()

def create(wav,razz):
    sav =  auoj.razz_audio_object()
    cde = delivai("start",0)
    cde.append("end")
    cde.reverse()
    cde.append("start")
    cde.reverse()
    sav.stage1 = cde

    cdg = wgen.mocml(cde,"10")
    sav.stage2 = cdg
    
    sav.save(razz)
    sav.truetone(wav)

def generate(path):
    sav =  auoj.razz_audio_object()
    cde = delivai("start",0)
    cde.append("end")
    cde.reverse()
    cde.append("start")
    cde.reverse()
    sav.stage1 = cde

    cdg = wgen.mocml(cde,"10")
    sav.stage2 = cdg

    sav.save(path)

#razz compile ./path/to/dot.razz ./filename.wav
#razz create <timestamp, def: 4/4> <sect, def:7> ./output/file.razz
#razz generate 4:4 7 ./song.wav -intermediate

if (sys.argv[1] == "generate"):
    if (len(sys.argv)>3):
        create(sys.argv[2],sys.argv[3])
    else:
        print(cl.fg.red+"razz.generate requires 2 arguments, try:\n  "+cl.fg.yellow+"python "+cl.fg.rgb(255,0,128)+"razz.py"+cl.fg.blue+" ./output.wav "+cl.fg.rgb(255,0,128)+"./output.razz"+cl.reset)

# calculate duel strip, starting with backwards interpolation
# wgen.drjalis(sav.stage2)#255,0,182
# print(join(cde))
# print(cl.fg.blue+"     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ patterngen"+cl.reset)
# print("\u001b[F"+cl.fg.green+"    ━━━━━━━━━"+cl.fg.blue+"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  generate equalization"+cl.reset)
# print("\u001b[F"+cl.fg.green+"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ done!"+cl.reset)