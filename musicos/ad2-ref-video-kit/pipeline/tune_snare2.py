import itertools, variant, rank
REF=rank.refmed('ref2.wav',[7.40,7.98,10.37,12.72,13.53,13.91,15.69,17.26,18.91,20.99])
base={'Sampler_SNAR_KitPieceSelection':'180201','Sampler_SNAR_Pitch_Enable':'1','Sampler_SNAR_Pitch_Course':'0.526',
      'FX_SNAR/EnableFX':'1','FX_SNAR/EQ_Enable':'1','FX_SNAR/MultiFX1/Enable':'0','FX_SNAR/MultiFX2/Enable':'0','FX_SNAR/Sends_Enable':'0',
      'FX_SNAR/EQ_HiGain':'0.5','FX_SNAR/EQ_MidGain':'0.3','FX_SNAR/EQ_MidFreq':'0.4','FX_SNAR/EQ_MidQ':'0.5'}
res=[]
for g,f in (('0.65','0.8'),('0.8','0.8'),('0.65','0.95'),('0.8','0.95')):
    c=variant.run(f'eq2_g{g}_f{f}',38,dict(base,**{'FX_SNAR/EQ_Hi2Gain':g,'FX_SNAR/EQ_Hi2Freq':f}),neutral_slot='SNAR')
    if c: d=rank.dist(REF,c); res.append((d,g,f)); print(f'   dist={d:.2f}',flush=True)
print('BEST:',sorted(res)[:2])
