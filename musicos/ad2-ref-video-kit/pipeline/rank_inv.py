"""ponytail: rank inventory_<SLOT>.txt lines against reference hits. usage: rank_inv.py SLOT t1,t2,... [fmin fmax]"""
import sys, re, numpy as np, rank
slot=sys.argv[1]; times=[float(x) for x in sys.argv[2].split(',')]
fmin,fmax=(int(sys.argv[3]),int(sys.argv[4])) if len(sys.argv)>4 else (40,600)
import librosa, measure
y,sr=librosa.load('ref2.wav',sr=44100,mono=True); rows=[measure.feats(y,sr,t,fmin,fmax) for t in times]
ref={k:float(np.median([r[k] for r in rows])) for k in rows[0]}
def parse(line):
    d={}; cid=line.split()[0]
    for k,v in re.findall(r'([\w\-]+)=([\d\.]+)',line):
        d[k]=float(v)/1000 if k.startswith('dec') else float(v)
    return cid,d
out=[]
for line in open(f'inventory_{slot}.txt'):
    cid,c=parse(line); out.append((rank.dist(ref,c),cid,c))
fmt=lambda c:' '.join(f"{k}={v:.2f}" if '-' in k else f"{k}={v:.0f}" if k in('f0','cent') else f"{k}={v*1000:.0f}ms" for k,v in c.items() if k in ('f0','cent','dec20','dec30') or '-' in k)
print('REF  ',fmt(ref))
for d,cid,c in sorted(out)[:int(sys.argv[5]) if len(sys.argv)>5 else 15]: print(f'{d:5.2f} {cid} ',fmt(c))
