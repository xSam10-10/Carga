# Vetoriza a arte das silhuetas (canal alfa) em caminhos SVG para o avatar de água. Uso: python3 tools/silhueta.py <imagem>
import cv2, numpy as np, json
from PIL import Image
A=np.array(Image.open(__import__('sys').argv[1]))[:,:,3].astype(np.float32)
U=4; S=0.27; PAD=6
def fmt(v): s=('%.1f'%v).rstrip('0').rstrip('.'); return s if s!='-0' else '0'
def path(cs,ox,oy):
    out=[]
    for c in cs:
        c=cv2.approxPolyDP(c,0.35*U,True).reshape(-1,2).astype(float)
        if len(c)<3: continue
        pts=[((x/U-ox)*S,(y/U-oy)*S) for x,y in c]
        d='M'+fmt(pts[0][0])+' '+fmt(pts[0][1])
        px,py=pts[0]
        for x,y in pts[1:]:
            # relative coords for brevity
            d+='l'+fmt(round(x,1)-round(px,1))+' '+fmt(round(y,1)-round(py,1)); px,py=round(x,1),round(y,1)
        out.append(d+'z')
    return ''.join(out)
res={}
for key,(x0,x1) in {'m':(212,645),'f':(683,1079)}.items():
    ox=x0-PAD; oy=30-PAD; w=x1-x0+2*PAD; h=1165-30+2*PAD
    sub=np.zeros((h,w),np.float32); y0=0
    sub[:, :]=A[oy:oy+h, ox:ox+w]
    big=cv2.resize(sub,(w*U,h*U),interpolation=cv2.INTER_CUBIC)
    ink=(big>110).astype(np.uint8)*255
    cs,_=cv2.findContours(ink,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    cs=[c for c in cs if cv2.contourArea(c)>20*U*U]
    line=path(cs,0,0)
    # body region
    ff=ink.copy(); m=np.zeros((h*U+2,w*U+2),np.uint8)
    cv2.floodFill(ff,m,(0,0),128)
    body=(ff!=128).astype(np.uint8)*255
    body=cv2.erode(body,np.ones((3*U,3*U),np.uint8))
    bc,_=cv2.findContours(body,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    bc=[max(bc,key=cv2.contourArea)]
    ys=bc[0][:,0,1]
    res[key]={'w':round(w*S,1),'h':round(h*S,1),'top':round(ys.min()/U*S,1),'bot':round(ys.max()/U*S,1),'line':line,'body':path(bc,0,0)}
    print(key,res[key]['w'],res[key]['h'],res[key]['top'],res[key]['bot'],len(line),len(res[key]['body']))
json.dump(res,open('sil.json','w'))
for k in res:
    r=res[k]
    open(k+'.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {r["w"]} {r["h"]}" width="{r["w"]*3}"><path d="{r["body"]}" fill="#cfe"/><path d="{r["line"]}" fill="#769F92" fill-rule="evenodd"/></svg>')
