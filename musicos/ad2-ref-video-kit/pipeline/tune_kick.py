import variant, rank, measure, librosa, numpy as np
REF=rank.refmed('ref2.wav',[8.42,8.84,10.01,10.77,15.43,16.23,16.75,20.88])
base={'Sampler_KICK_KitPieceSelection':'180102','FX_KICK/EnableFX':'1','FX_KICK/EQ_Enable':'1','FX_KICK/MultiFX1/Enable':'0','FX_KICK/MultiFX2/Enable':'0','FX_KICK/Sends_Enable':'0'}
res=[]
for g in ('0.5','0.7','0.85'):
    c=variant.run(f'kick_g{g}',36,dict(base,**{'FX_KICK/EQ_Hi2Gain':g,'FX_KICK/EQ_Hi2Freq':'0.8'}),neutral_slot='KICK')
    if c: d=rank.dist(REF,c); res.append((d,g)); print(f'   dist={d:.2f}',flush=True)
print('BEST:',sorted(res)[:2])
