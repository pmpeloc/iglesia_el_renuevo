"""ponytail: sweep kit-piece ids SLOT NOTE TT PPlist maxNN; per pak stop after first silent NN>=1. Appends to inventory_<SLOT>.txt"""
import sys, os, time, subprocess, numpy as np, adstate, measure, librosa
import os; S=os.path.dirname(os.path.abspath(__file__)).replace(os.sep,'/')+'/'  # ponytail: scripts, chunks y wavs viven juntos
def rcmd(*a):
    r=subprocess.run(['bash',S+'rcmd.sh',*map(str,a)],capture_output=True,text=True,timeout=160); return r.stdout.strip()
slot,note,tt=sys.argv[1],int(sys.argv[2]),sys.argv[3]; pps=[int(x) for x in sys.argv[4].split(',')]; maxn=int(sys.argv[5])
fmin,fmax=(30,200) if slot=='KICK' else (40,600)
open(S+'midi_spec.txt','w').write(f'1.5\n0.3 {note} 120 0.2\n')
out=open(S+f'inventory_{slot}.txt','a')
for pp in pps:
    for nn in range(1,maxn+1):
        cid=f'{pp:02d}{tt}{nn:02d}'
        d=adstate.load(S+'chunk_252e.txt'); adstate.setv(d,f'Sampler_{slot}_KitPieceSelection',cid)
        for k,v in d['pairs']:
            if k.endswith('/EnableFX'): adstate.setv(d,k,'0')
        for k in ('Pitch_Enable','AmpEnv_Enable','FilterHiLo_Enable'): adstate.setv(d,f'Sampler_{slot}_{k}','0')
        adstate.setv(d,f'Sampler_{slot}_Pitch_Course','0.5'); adstate.setv(d,f'Sampler_{slot}_Level','0.6'); adstate.setv(d,f'Sampler_{slot}_EnvFiltersEnable','1')
        adstate.save(d,S+'chunk_probe.txt'); rcmd('setchunk',S+'chunk_probe.txt'); time.sleep(4)
        wav=S+f'probe_{slot}_{cid}.wav'
        try: os.remove(wav)
        except FileNotFoundError: pass
        rcmd('eval',S+'midi.lua'); rcmd('render',S+f'probe_{slot}_{cid}'); time.sleep(1)
        try: y,sr=librosa.load(wav,sr=44100,mono=True); pk=float(np.abs(y).max())
        except Exception as e: pk=0.0
        if pk<0.01:
            print(f'{cid}: silent',flush=True); break
        c=measure.feats(y,sr,0.3,fmin,fmax)
        line=f"{cid} peak={pk:.2f} f0={c['f0']:.0f} cent={c['cent']:.0f} dec20={c['dec20']*1000:.0f}ms dec30={c['dec30']*1000:.0f}ms "+' '.join(f"{k}={v:.3f}" for k,v in c.items() if '-' in k)
        print(line,flush=True); out.write(line+'\n'); out.flush()
