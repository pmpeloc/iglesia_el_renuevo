import itertools, variant, rank
REFS=rank.refmed('ref2.wav',[7.40,7.98,10.37,12.72,13.53,13.91,15.69,17.26,18.91,20.99])
REFK=rank.refmed('ref2.wav',[8.42,8.84,10.01,10.77,15.43,16.23,16.75,20.88])
sn={'Sampler_SNAR_KitPieceSelection':'130201','Sampler_SNAR_Pitch_Enable':'1','Sampler_SNAR_Pitch_Course':'0.433',
    'FX_SNAR/EnableFX':'1','FX_SNAR/EQ_Enable':'1','FX_SNAR/MultiFX1/Enable':'0','FX_SNAR/MultiFX2/Enable':'0','FX_SNAR/Sends_Enable':'0',
    'FX_SNAR/EQ_MidFreq':'0.4','FX_SNAR/EQ_MidQ':'0.5','FX_SNAR/EQ_Hi2Freq':'0.8','FX_SNAR/EQ_HiGain':'0.5','FX_SNAR/EQ_LoGain':'0.5'}
res=[]
for hi2,mid in itertools.product(('0.5','0.65','0.8'),('0.5','0.3')):
    c=variant.run(f'up_sn_h{hi2}_m{mid}',38,dict(sn,**{'FX_SNAR/EQ_Hi2Gain':hi2,'FX_SNAR/EQ_MidGain':mid}),neutral_slot='SNAR')
    if c: d=rank.dist(REFS,c); res.append((d,hi2,mid)); print(f'   dist={d:.2f}',flush=True)
print('SNARE BEST:',sorted(res)[:3])
kk={'Sampler_KICK_KitPieceSelection':'130101','FX_KICK/EnableFX':'1','FX_KICK/EQ_Enable':'1','FX_KICK/MultiFX1/Enable':'0','FX_KICK/MultiFX2/Enable':'0','FX_KICK/Sends_Enable':'0','FX_KICK/EQ_Hi2Freq':'0.8'}
res=[]
for g in ('0.5','0.7','0.85'):
    c=variant.run(f'up_kk_g{g}',36,dict(kk,**{'FX_KICK/EQ_Hi2Gain':g}),neutral_slot='KICK')
    if c: d=rank.dist(REFK,c); res.append((d,g)); print(f'   dist={d:.2f}',flush=True)
print('KICK BEST:',sorted(res)[:2])
for slot,note,cid in (('TOM2',69,'130501'),('TOM3',67,'130601'),('TOM3',67,'130701')):
    variant.run(f'up_{slot}_{cid}',note,{f'Sampler_{slot}_KitPieceSelection':cid},neutral_slot=slot)
