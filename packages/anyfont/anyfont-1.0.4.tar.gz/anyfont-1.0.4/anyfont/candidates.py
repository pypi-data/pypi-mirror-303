from fontTools.ttLib import TTFont
import subprocess
import brotli

def ttf_woff2(file, f):
    f = TTFont(file)
    f.flavor='woff2'
    f.save(change_ext(file,"woff2"))
    return 'TTF TO WOFF2 SUCCESSFUL'
def otf_woff2(file, f):
    subprocess.call(['powershell', 'otf2ttf '+ f])
    ttf_woff2(change_ext(file,"ttf"), None)
    return 'OTF TO WOFF2 SUCCESSFUL'
def change_ext(f,ext):
    cext = [x for x in ext]
    i = -1
    start = False
    def replace(replacement, n):
        return f[0:n] + replacement + f[n+1: ]
    while len(cext) > 0:
        i += 1
        try:
            if (f[i-1] == "."):
                start = True
        except:
            start = False
            f += cext[0]
            cext.pop(0)
            continue
        if start:
            f = replace(cext[0],i)
            cext.pop(0)
    return f
