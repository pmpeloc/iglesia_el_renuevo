"""ponytail: JUCE MemoryBlock base64 <-> bytes, and inject a plugin state into the standalone devicestate."""
import re,sys
LOOKUP=".ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def decode(v):
    size,data=v.split('.',1); size=int(size); out=bytearray(size)
    for i,ch in enumerate(data):
        val=LOOKUP.index(ch); bit=i*6
        for b in range(6):
            if val>>b&1:
                idx=(bit+b)>>3
                if idx<size: out[idx]|=1<<((bit+b)&7)
    return bytes(out)
def encode(raw):
    n=len(raw); nchars=((n<<3)+5)//6; s=[]
    for i in range(nchars):
        bit=i*6; val=0
        for b in range(6):
            idx=(bit+b)>>3
            if idx<n and raw[idx]>>((bit+b)&7)&1: val|=1<<b
        s.append(LOOKUP[val])
    return f'{n}.'+''.join(s)
def state_from_chunk(chunk_path):
    import adstate
    lines,i,j,raw=adstate.read_chunk(chunk_path); head,state,tail=adstate.split_state(raw); return state
def inject(devicestate_path,state_bytes):
    s=open(devicestate_path,encoding='utf-8').read()
    enc=encode(state_bytes)
    if 'name="filterState"' in s: s=re.sub(r'<VALUE name="filterState" val="[^"]*"/>',f'<VALUE name="filterState" val="{enc}"/>',s)
    else: s=s.replace('</PROPERTIES>',f'  <VALUE name="filterState" val="{enc}"/>\n</PROPERTIES>')
    open(devicestate_path,'w',encoding='utf-8',newline='').write(s)
if __name__=='__main__':
    # self-check: roundtrip
    import os
    b=os.urandom(1000); assert decode(encode(b))==b; print('roundtrip ok')
