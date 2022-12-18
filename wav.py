# a document of all type waves

import numpy as np


def jeten(s, c):
    tamp = [s, s, s, s, s, s, s, s, s, s]
    for x in range(1, 9):
        tamp[x] += (np.random.random()-0.5)/c
    return tamp


jairiva = {  # wave patterns
    "start": {
        "10": [
            0, 0, 0, 0.1, 0.1, 0.1, 0.2, 0.2, 0.3, 0.3
        ]
    },  # up by 0.3, smooth lerp
    "subchorous": {
        "10": [
            0.3, 0.2, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.4, 0.5
        ]
    },  # sin at 0.3, angle to 0.5
    "chorus": {
        "10": jeten(0.5, 4)
    },  # stay at current (repetative auto patern) (has random prot)
    "drop": {
        "10": [
            0.7, 0.7, 0.8, 0.8, 0.7, 0.5, 0.4, 0.4, 0.5, 0.5
        ]
    },  # 0.6, raise to 0.8, drop to 0.4 end at 0.5
    "drift": {
        "10": jeten(0.3, 7)
    },  # drift at current value
    "end": {
        "10": [0.3, 0.3,0.3,0.3, 0.2,0.2,0.2, 0.1,0.1,0.1, 0,0,0]
    }
}


def mocml(patrn, attr):
    res = []
    for x in patrn:
        cdn = jairiva[x][attr]
        for n in cdn:
            res.append(n)
    return res


def drjalis(ddf):
    lcal = []
    for x in ddf:
        tamp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        tamp[round(x["current"]*10)] = 1
        tamp.reverse()
        lcal.append(tamp)
    enp = ""
    for i in range(10):
        enp += "|"
        for x in lcal:
            if (x[i] == 1):
                enp += "o"
            else:
                enp += " "
        enp += "\n"
    print(enp)
