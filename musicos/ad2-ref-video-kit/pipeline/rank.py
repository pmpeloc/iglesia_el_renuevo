"""ponytail: rank candidate renders against reference hits. Distance = weighted log-ratio of f0, band ratios, decay."""
import sys, glob, numpy as np, librosa, measure
S='./'
def refmed(path,times):
    y,sr=librosa.load(path,sr=44100,mono=True); rows=[measure.feats(y,sr,t) for t in times]
    return {k:float(np.median([r[k] for r in rows])) for k in rows[0]}
def dist(a,b):
    d=0; d+=3*abs(np.log2(a['f0']/b['f0']))          # pitch: octaves, weight 3
    d+=1*abs(np.log2(a['cent']/b['cent']))            # brightness
    d+=1*abs(np.log2((a['dec30']+0.02)/(b['dec30']+0.02)))
    for k in a:
        if '-' in k: d+=0.5*abs(np.log2((a[k]+1e-3)/(b[k]+1e-3)))
    return d
if __name__=='__main__':
    slot=sys.argv[1]; times=[float(x) for x in sys.argv[2].split(',')]
    ref=refmed('ref2.wav',times)
    print('REF ',' '.join(f"{k}={v:.3f}" if '-' in k else f"{k}={v:.0f}" if k in('f0','cent') else f"{k}={v*1000:.0f}ms" for k,v in ref.items()))
    rows=[]
    for f in sorted(glob.glob(f'probe_{slot}_*.wav')):
        y,sr=librosa.load(f,sr=44100,mono=True)
        if np.abs(y).max()<0.01: continue
        c=measure.feats(y,sr,0.3); rows.append((dist(ref,c),f.split('_')[-1][:-4],c))
    for d,cid,c in sorted(rows):
        print(f"{d:5.2f} {cid} ",' '.join(f"{k}={v:.3f}" if '-' in k else f"{k}={v:.0f}" if k in('f0','cent') else f"{k}={v*1000:.0f}ms" for k,v in c.items()))
