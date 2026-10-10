"""ponytail: crude hit classifier for the reference videos. prints time, class guess, features."""
import sys, numpy as np, librosa
path=sys.argv[1]; t0=float(sys.argv[2]) if len(sys.argv)>2 else 0
y,sr=librosa.load(path,sr=44100,mono=True); y=y[int(t0*sr):]
on=librosa.onset.onset_detect(y=y,sr=sr,units='samples',backtrack=True,delta=0.05,wait=6)
n=4096; f=np.fft.rfftfreq(n,1/sr)
def band(X,lo,hi): m=(f>=lo)&(f<hi); return (X[m]**2).sum()
rows=[]
for s in on:
    seg=y[s:s+n]
    if len(seg)<n: continue
    X=np.abs(np.fft.rfft(seg*np.hanning(n))); tot=band(X,20,16000)+1e-12
    lo,lm,mid,hi,vh=[band(X,a,b)/tot for a,b in ((40,110),(110,150),(150,350),(2000,8000),(8000,16000))]
    m=(f>=40)&(f<=500); f0=f[m][X[m].argmax()]
    pk=20*np.log10(np.abs(y[s:s+2048]).max()+1e-9)
    L=int(1.0*sr); env=np.abs(librosa.util.frame(y[s:s+L],frame_length=512,hop_length=128)).max(0) if s+L<len(y) else None
    dec=-1
    if env is not None:
        e=20*np.log10(env/env.max()+1e-6); idx=np.where(e<-20)[0]; dec=int(idx[0]*128/sr*1000) if len(idx) else 1000
    if hi+vh>0.5: cls='CYM/HH'
    elif lo>0.5 and hi<0.1: cls='KICK'
    elif mid>0.5 and 150<=f0<=260: cls='SNARE'
    elif (lo+lm+mid)>0.6 and 70<=f0<=150 and dec>120: cls='TOM?'
    else: cls='?'
    rows.append((t0+s/sr,cls,pk,f0,lo,lm,mid,hi,vh,dec))
for r in rows: print(f'{r[0]:6.2f} {r[1]:7s} pk={r[2]:6.1f} f0={r[3]:4.0f} lo={r[4]:.2f} lm={r[5]:.2f} mid={r[6]:.2f} hi={r[7]:.2f} vh={r[8]:.2f} dec20={r[9]}')
