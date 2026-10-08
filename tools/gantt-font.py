import sys, base64, io
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
FILLED = "■█=#"          # 作業ありの週
BLANK  = " .・-_□　"   # 作業なしの週
ADV = 1000
def rect(x0,y0,x1,y1):
    p=TTGlyphPen(None); p.moveTo((x0,y0)); p.lineTo((x0,y1)); p.lineTo((x1,y1)); p.lineTo((x1,y0)); p.closePath(); return p.glyph()
def empty():
    return TTGlyphPen(None).glyph()
order=[".notdef","bar","blank"]
fb=FontBuilder(1000,isTTF=True); fb.setupGlyphOrder(order)
cmap={}
for c in FILLED: cmap[ord(c)]="bar"
for c in BLANK: cmap[ord(c)]="blank"
fb.setupCharacterMap(cmap)
# 隣の週と継ぎ目が出ないよう左右に少しはみ出させる
fb.setupGlyf({".notdef":empty(),"bar":rect(-30,60,ADV+30,540),"blank":empty()})
fb.setupHorizontalMetrics({g:(ADV,0) for g in order})
fb.setupHorizontalHeader(ascent=800,descent=-200)
fb.setupNameTable({"familyName":"aoao-gantt","styleName":"Regular"})
fb.setupOS2(sTypoAscender=800,sTypoDescender=-200,usWinAscent=800,usWinDescent=200)
fb.setupPost()
buf=io.BytesIO(); fb.font.flavor="woff2"; fb.save(buf)
print(base64.b64encode(buf.getvalue()).decode())
