"""ponytail: per-hit features of a drum recording. usage: measure.py file.wav t1 t2 ... (hit onset times in sec)
Prints f0, band energy ratios, centroid, decay-to-30dB. Same code runs on reference and render so numbers are comparable."""
import sys, numpy as np, librosa
BANDS=((40,110),(110,150),(150,350),(350,1000),(1000,2000),(2000,8000))
def feats(y,sr,t,fmin=40,fmax=600):
    s=int(t*sr); w=y[s:s+int(0.04*sr)]; s=s+int(np.argmax(np.abs(w))) if len(w) else s; n=8192; seg=y[s:s+n]*np.hanning(n); X=np.abs(np.fft.rfft(seg)); f=np.fft.rfftfreq(n,1/sr)
    tot=(X[(f>=20)&(f<16000)]**2).sum()
    br={f'{lo}-{hi}':(X[(f>=lo)&(f<hi)]**2).sum()/tot for lo,hi in BANDS}
    m=(f>=fmin)&(f<=fmax); f0=f[m][X[m].argmax()]
    cm=(f>=20)&(f<16000); cent=(f[cm]*X[cm]**2).sum()/(X[cm]**2).sum()
    env=np.abs(librosa.util.frame(y[s:s+int(1.0*sr)],frame_length=512,hop_length=128)).max(0)
    e=20*np.log10(env/env.max()+1e-6); idx=np.where(e<-30)[0]; dec=idx[0]*128/sr if len(idx) else 1.0
    idx20=np.where(e<-20)[0]; dec20=idx20[0]*128/sr if len(idx20) else 1.0
    return dict(f0=f0,cent=cent,dec30=dec,dec20=dec20,**br)
def report(path,times,label=None):
    y,sr=librosa.load(path,sr=44100,mono=True)
    rows=[feats(y,sr,t) for t in times]
    med={k:float(np.median([r[k] for r in rows])) for k in rows[0]}
    print(f"{label or path}: n={len(rows)} f0={med['f0']:.0f}Hz cent={med['cent']:.0f}Hz dec20={med['dec20']*1000:.0f}ms dec30={med['dec30']*1000:.0f}ms | "+' '.join(f"{k}:{med[k]:.2f}" for k in med if '-' in k))
    return med
if __name__=='__main__':
    report(sys.argv[1],[float(x) for x in sys.argv[2:]])
