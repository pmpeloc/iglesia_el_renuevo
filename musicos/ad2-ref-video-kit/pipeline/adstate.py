"""ponytail: AD2 VST3 state <-> list of (key,value) string pairs inside REAPER's base64 VST chunk."""
import base64, struct, sys
MARK=b'COTTAD2StateVersion\x00'
SUF=b'\x00'*8+b'JUCEPrivateData'
def read_chunk(path):
    lines=open(path,encoding='utf-8',errors='replace').read().split('\n')
    i=[k for k,l in enumerate(lines) if l.startswith('<VST ')][0]
    b64=[]; j=i+1
    while lines[j].strip()!='>': b64.append(lines[j].strip()); j+=1
    return lines,i,j,b''.join(base64.b64decode(x) for x in b64)
def split_state(raw):
    st=raw.find(MARK); ln=struct.unpack('<I',raw[st-8:st-4])[0]; assert raw[st-4:st]==b'\x01\x00\x00\x00'
    return raw[:st], raw[st:st+ln], raw[st+ln:]
def parse(state):
    cut=state.find(SUF); assert cut>0
    toks=state[:cut].split(b'\x00'); assert toks[-1]==b''; toks=toks[:-1]; assert len(toks)%2==0
    return [(toks[k].decode('latin1'),toks[k+1].decode('latin1')) for k in range(0,len(toks),2)], state[cut:]
def build(pairs): return b''.join(k.encode('latin1')+b'\x00'+v.encode('latin1')+b'\x00' for k,v in pairs)
def load(path):
    lines,i,j,raw=read_chunk(path); head,state,tail=split_state(raw); pairs,suffix=parse(state)
    return dict(lines=lines,i=i,j=j,head=head,tail=tail,pairs=pairs,suffix=suffix)
def save(doc,path):
    state=build(doc['pairs'])+doc['suffix']; head=bytearray(doc['head']); ln=len(state)
    head[-8:-4]=struct.pack('<I',ln); head[-20:-16]=struct.pack('<I',ln+16)
    b64=base64.b64encode(bytes(head)+state+doc['tail']).decode()
    lines=doc['lines'][:doc['i']+1]+[b64[k:k+128] for k in range(0,len(b64),128)]+doc['lines'][doc['j']:]
    open(path,'w',encoding='utf-8',newline='\n').write('\n'.join(lines))
def setv(doc,key,val):
    for n,(k,v) in enumerate(doc['pairs']):
        if k==key: doc['pairs'][n]=(k,str(val)); return
    raise KeyError(key)
def getv(doc,key): return dict(doc['pairs'])[key]
if __name__=='__main__':
    d=load(sys.argv[1]); print(len(d['pairs']),'pairs; suffix',len(d['suffix']))
    if len(sys.argv)>2:
        e=load(sys.argv[2]); a=dict(d['pairs']); b=dict(e['pairs'])
        for k in sorted(set(a)|set(b)):
            if a.get(k)!=b.get(k): print(f'{k}: {a.get(k)!r} -> {b.get(k)!r}'[:300])
        # roundtrip check
        save(e,'rt.txt'); f=load('rt.txt'); assert f['pairs']==e['pairs'] and f['suffix']==e['suffix']; print('roundtrip OK')
