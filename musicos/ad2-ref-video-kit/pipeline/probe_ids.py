"""ponytail: try candidate KitPieceSelection ids for one slot, render one hit, report peak + f0. usage: probe_ids.py SLOT NOTE id1 id2 ..."""
import sys, subprocess, time, numpy as np, adstate, measure, librosa
import os; S=os.path.dirname(os.path.abspath(__file__)).replace(os.sep,'/')+'/'  # ponytail: scripts, chunks y wavs viven juntos
def rcmd(*a,timeout=120):
    r=subprocess.run(['bash',S+'rcmd.sh',*map(str,a)],capture_output=True,text=True,timeout=timeout+10); return r.stdout.strip()
slot,note=sys.argv[1],int(sys.argv[2])
base=adstate.load(S+'chunk_252e.txt')
open(S+'midi_spec.txt','w').write(f'1.5\n0.3 {note} 120 0.2\n')
for cid in sys.argv[3:]:
    d=adstate.load(S+'chunk_252e.txt'); adstate.setv(d,f'Sampler_{slot}_KitPieceSelection',cid)
    for k,v in d['pairs']:  # neutral: all channel FX off, no pitch/env tweaks on the probed slot
        if k.endswith('/EnableFX'): adstate.setv(d,k,'0')
    for k in ('Pitch_Enable','AmpEnv_Enable','FilterHiLo_Enable'):
        try: adstate.setv(d,f'Sampler_{slot}_{k}','0')
        except KeyError: pass
    adstate.setv(d,f'Sampler_{slot}_Pitch_Course','0.5'); adstate.save(d,S+'chunk_probe.txt')
    r1=rcmd('setchunk',S+'chunk_probe.txt'); time.sleep(5)
    import os
    try: os.remove(S+f'probe_{slot}_{cid}.wav')
    except FileNotFoundError: pass
    rcmd('eval',S+'midi.lua'); r3=rcmd('render',S+f'probe_{slot}_{cid}')
    time.sleep(1); y,sr=librosa.load(S+f'probe_{slot}_{cid}.wav',sr=44100,mono=True); pk=float(np.abs(y).max())
    line=f'{slot} {cid}: peak={pk:.3f}'
    if pk>0.01: f=measure.feats(y,sr,0.3); line+=f" f0={f['f0']:.0f} cent={f['cent']:.0f} dec30={f['dec30']*1000:.0f}ms"
    print(line,flush=True)
