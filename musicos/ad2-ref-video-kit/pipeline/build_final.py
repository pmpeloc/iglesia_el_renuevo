"""ponytail: build the final AD2 state from a dict of settings. usage: build_final.py out.txt  (edit KIT below)"""
import sys, adstate
import os; S=os.path.dirname(os.path.abspath(__file__)).replace(os.sep,'/')+'/'  # ponytail: scripts, chunks y wavs viven juntos
def semis(n): return str(round(0.5+n/24,4))   # Pitch_Course: 0..1 = -12..+12 semitones
KIT={  # slot -> settings (Sampler_<slot>_* and FX_<slot>/* keys)
 'SNAR':{'KitPieceSelection':'180201','Pitch_Enable':'1','Pitch_Course':semis(0.63),'Level':'0.8',
         'fx':{'EQ_Enable':'1','EQ_MidGain':'0.3','EQ_MidFreq':'0.4','EQ_MidQ':'0.5','EQ_Hi2Gain':'0.8','EQ_Hi2Freq':'0.8'}},
}
GLOBAL={'OH_Level':'0.5','Room_Level':'0.35'}
def build(kit,out,base='chunk_252e.txt'):
    d=adstate.load(S+base)
    for k,v in d['pairs']:                       # clean slate: every channel FX chain off, master/bus untouched later
        if k.endswith('/EnableFX'): adstate.setv(d,k,'0')
        if k.endswith('/Sends_Enable'): adstate.setv(d,k,'0')
    for slot,cfg in kit.items():
        for k in ('AmpEnv_Enable','FilterHiLo_Enable'): adstate.setv(d,f'Sampler_{slot}_{k}','0')
        adstate.setv(d,f'Sampler_{slot}_EnvFiltersEnable','1'); adstate.setv(d,f'Sampler_{slot}_Pitch_Enable','0')
        adstate.setv(d,f'Sampler_{slot}_Pitch_Course','0.5')
        for k,v in cfg.items():
            if k=='fx':
                adstate.setv(d,f'FX_{slot}/EnableFX','1'); adstate.setv(d,f'FX_{slot}/MultiFX1/Enable','0'); adstate.setv(d,f'FX_{slot}/MultiFX2/Enable','0')
                for fk,fv in v.items(): adstate.setv(d,f'FX_{slot}/{fk}',fv)
            else: adstate.setv(d,f'Sampler_{slot}_{k}',v)
        for g,gv in GLOBAL.items(): adstate.setv(d,f'Sampler_{slot}_{g}',gv)
    # unused slots silent
    for slot in ('CYM4','CYM5','CYM6','RID2','FLX1','FLX2','FLX3','TOM4'):
        if slot not in kit: adstate.setv(d,f'Sampler_{slot}_KitPieceSelection','0')
    adstate.setv(d,'Layer1/PresetSaveName','Ref Video Kit'); adstate.setv(d,'Layer1/CurrentPresetName','Ref Video Kit')
    adstate.save(d,out); return d
if __name__=='__main__': build(KIT,S+sys.argv[1]); print('built',sys.argv[1])
