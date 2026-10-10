"""Adapta un preset de SD3 (librería Core) a EZdrummer 2 Modern.
Base = un preset válido de la librería destino (kit, pads, micmap intactos).
Del origen se copian: canales del mixer mapeados, todos los buses/salidas (FX, sends, PLATE) y la afinación del ride.
uso: port_preset.py ORIGEN BASE_DESTINO SALIDA "Nombre nuevo"
"""
import re, sys

# canal de la librería destino (EZ2 Modern) <- canal del preset origen (SD3 Core)
MAP = {'Kick': 'Kick-In', 'KickExt': 'Kick-Out', 'SnareTop': 'SnareTop', 'SnareBottom': 'SnareBottom',
       'Hats': 'Hats', 'Toms': 'Tom2', 'TomsR': 'Tom2', 'Oh': 'Oh-Beyer', 'OhR': 'Oh-BeyerR',
       'Amb': 'Ambience-R88', 'AmbR': 'Ambience-R88R'}

def blocks(lines, start):
    """bloques de primer nivel dentro del bloque que abre en lines[start]: [(header, [lineas])]"""
    out, i, depth = [], start + 1, 0
    while True:
        l = lines[i]
        if depth == 0 and l == '}': return out, i
        if depth == 0:
            if l.endswith('{'): cur = [l]; out.append((l[:-1].strip(), cur))
            else: out.append((l, [l]))
        else: cur.append(l)
        depth += l.count('{') - l.count('}')
        i += 1

def mixer(lines):
    s = lines.index('mixer {'); b, e = blocks(lines, s); return s, e, b

def port(src, base, name):
    S = open(src, encoding='utf-8').read().replace('\r', '').split('\n')
    B = open(base, encoding='utf-8').read().replace('\r', '').split('\n')
    B[0] = f'"{name}" {{'
    _, _, sb = mixer(S); src_ch = {h: body for h, body in sb}
    s, e, bb = mixer(B); new = []
    for h, body in bb:
        if h in MAP:
            body = [f'{h} {{'] + src_ch[MAP[h]][1:]
            pan = next(l for l in dict(bb)[h] if l.startswith('pan '))       # conservar paneo estéreo del destino
            body = [pan if l.startswith('pan ') else l for l in body]
        elif h == 'AmbMono':
            route = next(l for l in src_ch['Ambience-R88'] if l.startswith('route '))
            body = [route if l.startswith('route ') else l for l in body]
        elif re.match(r'(buss|output) \d+$', h):
            body = src_ch[h]
        new += body
    B = B[:s + 1] + new + B[e:]
    # afinación del ride: el pitch de los pads del ride origen, en cada pad del ride destino
    pitch = next(l for l in S if l.startswith('pitch '))
    i = B.index(next(l for l in B if l.startswith('instbox') and '"Ride"' in l)); depth = 0
    while True:
        l = B[i]; depth += l.count('{') - l.count('}')
        if depth == 0: break
        if l.startswith('pad ') and l.endswith('{'): B.insert(i + 1, pitch); i += 1
        i += 1
    return '\r\n'.join(B)

if __name__ == '__main__':
    src, base, out, name = sys.argv[1:5]
    txt = port(src, base, name)
    assert txt.count('{') == txt.count('}'), 'llaves desbalanceadas'
    open(out, 'w', encoding='utf-8', newline='').write(txt); print('ok', out)
