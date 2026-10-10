"""ponytail: coarse grid over snare EQ (hi shelf gain, mid cut) on chosen piece; prints distance to reference."""
import itertools, variant, rank
REF=rank.refmed('ref2.wav',[7.40,7.98,10.37,12.72,13.53,13.91,15.69,17.26,18.91,20.99])
PIECE,PITCH='180201','0.526'
base={'Sampler_SNAR_KitPieceSelection':PIECE,'Sampler_SNAR_Pitch_Enable':'1','Sampler_SNAR_Pitch_Course':PITCH,
      'FX_SNAR/EnableFX':'1','FX_SNAR/EQ_Enable':'1','FX_SNAR/MultiFX1/Enable':'0','FX_SNAR/MultiFX2/Enable':'0','FX_SNAR/Sends_Enable':'0'}
res=[]
for hi,mid in itertools.product(('0.5','0.7','0.9'),('0.5','0.3','0.15')):
    sets=dict(base,**{'FX_SNAR/EQ_HiGain':hi,'FX_SNAR/EQ_HiFreq':'0.6','FX_SNAR/EQ_MidGain':mid,'FX_SNAR/EQ_MidFreq':'0.4','FX_SNAR/EQ_MidQ':'0.5'})
    c=variant.run(f'eq_h{hi}_m{mid}',38,sets,neutral_slot='SNAR')
    if c: d=rank.dist(REF,c); res.append((d,hi,mid)); print(f'   dist={d:.2f}',flush=True)
print('BEST:',sorted(res)[:3])
