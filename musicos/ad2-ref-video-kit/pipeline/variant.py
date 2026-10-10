"""ponytail: render one variant. usage: variant.py NAME NOTE [--base file] [--neutral SLOT] key=val ...  -> writes var_NAME.wav, prints features"""
import sys, os, time, subprocess, numpy as np, librosa, adstate, measure
import os; S=os.path.dirname(os.path.abspath(__file__)).replace(os.sep,'/')+'/'  # ponytail: scripts, chunks y wavs viven juntos
def rcmd(*a):
    r=subprocess.run(['bash',S+'rcmd.sh',*map(str,a)],capture_output=True,text=True,timeout=150); return r.stdout.strip()
def neutral(d,slot):
    for k,v in d['pairs']:
        if k.endswith('/EnableFX'): adstate.setv(d,k,'0')
    for k in ('Pitch_Enable','AmpEnv_Enable','FilterHiLo_Enable'):
        try: adstate.setv(d,f'Sampler_{slot}_{k}','0')
        except KeyError: pass
    adstate.setv(d,f'Sampler_{slot}_Pitch_Course','0.5'); adstate.setv(d,f'Sampler_{slot}_Level','0.6'); adstate.setv(d,f'Sampler_{slot}_EnvFiltersEnable','1')
def run(name,note,sets,base='chunk_252e.txt',neutral_slot=None,vel=120):
    d=adstate.load(S+base)
    if neutral_slot: neutral(d,neutral_slot)
    for k,v in sets.items(): adstate.setv(d,k,v)
    adstate.save(d,S+f'var_{name}.txt'); rcmd('setchunk',S+f'var_{name}.txt'); time.sleep(4)
    open(S+'midi_spec.txt','w').write(f'1.5\n0.3 {note} {vel} 0.2\n'); rcmd('eval',S+'midi.lua')
    try: os.remove(S+f'var_{name}.wav')
    except FileNotFoundError: pass
    rcmd('render',S+f'var_{name}'); time.sleep(1)
    y,sr=librosa.load(S+f'var_{name}.wav',sr=44100,mono=True); pk=float(np.abs(y).max())
    if pk<0.01: print(name,'SILENT'); return None
    c=measure.feats(y,sr,0.3); c['peak']=pk
    print(name,' '.join(f"{k}={v:.3f}" if '-' in k else f"{k}={v:.0f}" if k in('f0','cent') else f"{k}={v*1000:.0f}ms" if k.startswith('dec') else f"{k}={v:.2f}" for k,v in c.items()),flush=True)
    return c
if __name__=='__main__':
    a=sys.argv[1:]; name,note=a[0],int(a[1]); a=a[2:]; base='chunk_252e.txt'; ns=None
    if '--base' in a: i=a.index('--base'); base=a[i+1]; del a[i:i+2]
    if '--neutral' in a: i=a.index('--neutral'); ns=a[i+1]; del a[i:i+2]
    run(name,note,dict(x.split('=',1) for x in a),base,ns)
