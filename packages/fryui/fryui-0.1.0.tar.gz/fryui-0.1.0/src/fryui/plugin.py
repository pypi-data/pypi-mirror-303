from .color import dump
from fryhcs.css.color import radix_colors as radix

radix_colored_regular = set(['tomato', 'red', 'ruby', 'crimson', 'pink', 'plum', 'purple', 'violet', 'iris', 'indigo', 'blue', 'cyan', 'teal', 'jade', 'green', 'grass', 'brown', 'orange' ])
radix_colored_bright = set(['sky', 'mint', 'lime', 'yellow', 'amber'])
radix_colored_metal = set(['gold', 'bronze'])

radix_colored_colors = radix_colored_regular.union(radix_colored_bright, radix_colored_metal)

radix_gray_pure = set(['gray'])
radix_gray_desaturated = set(['mauve', 'slate', 'sage', 'olive', 'sand'])

radix_gray_colors = radix_gray_pure.union(radix_gray_desaturated)

radix_colors = radix_colored_colors.union(radix_gray_colors)

def get_gray_color(primary):
    if primary in ('tomato', 'red', 'ruby', 'crimson', 'pink', 'plum', 'purple', 'violet',):
        return 'mauve'
    elif primary in ('iris', 'indigo', 'blue', 'sky', 'cyan',):
        return 'slate'
    elif primary in ('teal', 'jade', 'mint', 'green',):
        return 'sage'
    elif primary in ('grass', 'lime',):
        return 'olive'
    elif primary in ('yellow', 'amber', 'orange', 'brown', 'gold', 'bronze',):
        return 'sand'
    else:
        return 'gray'

def get_contrast_color(color):
    contrast_colors = {
        'sky': radix['slate-12'],
        'mint': radix['sage-12'],
        'lime': radix['olive-12'],
        'yellow': radix['sand-12'],
        'amber': radix['sand-12'],
    }
    if color in contrast_colors:
        return contrast_colors[color]
    if color in radix_colored_colors:
        return 'white'
    raise RuntimeError("Only support contrast color of colored color step 9")


theme = {
    'primary':   'blue',
    'secondary': 'green',
    'accent':    'grass',
    'info':      'sky',
    'success':   'jade',
    'warning':   'yellow',
    'error':     'tomato',
}

#radix-colors:
# 1:  BackGround
# 2:  BackGround eXtra
# 3:  ELement background
# 4:  ELement background eXtra
# 5:  ELement background eXtra eXtra
# 6:  BorDer
# 7:  BorDer eXtra
# 8:  BorDer eXtra eXtra
# 9:  solid
# 10: solid eXtra
# 11: Text
# 12: Text eXtra
#              1       2        3       4        5         6       7        8        9    10     11     12
suffixes  = ['-bg',  '-bgx',  '-el',  '-elx',  '-elxx',  '-bd',  '-bdx',  '-bdxx',  '',  'x',  '-t',  '-tx']
asuffixes = ['-bga', '-bgax', '-ela', '-elax', '-elaxx', '-bda', '-bdax', '-bdaxx', 'a', 'ax', '-ta', '-tax']
def base_css(theme=theme):
    gray, colored = check_theme(theme)
    common_style = {}
    light_style = {
        'color-scheme': 'light',
    }
    dark_style = {
        'color-scheme': 'dark',
    }
    for name, value in colored.items():
        common_style[f'--{name}-contrast'] = dump(get_contrast_color(value))
    allcolors = {'gray':gray, **colored}
    for name, value in allcolors.items():
        for i in range(1, 13):
            light_style[f'--{name}{suffixes[i-1]}'] = dump(radix[f'{value}-{i}'])
            light_style[f'--{name}{asuffixes[i-1]}'] = dump(radix[f'{value}-a{i}'])
            dark_style[f'--{name}{suffixes[i-1]}'] = dump(radix[f'{value}-dark-{i}'])
            dark_style[f'--{name}{asuffixes[i-1]}'] = dump(radix[f'{value}-dark-a{i}'])
    return {
        ':root': common_style,
        ':root, [data-scheme="light"]': light_style,
        '[data-scheme="dark"]': dark_style,
    }


def check_theme(theme):
    curr = dict(theme)
    if not all(n in semantic_names for n in curr.keys()):
        raise RuntimeError("theme should only have one of the 8 semantic names")
    gray = curr.pop('gray', None)
    if 'primary' not in curr:
        raise RuntimeError("'primary' should be in theme")
    if not all(v in radix_colored_colors for v in curr.values()):
        raise RuntimeError("all semantic colors other than 'gray' should be one of radix non-gray colors")
    if not gray:
        gray = get_gray_color(curr['primary'])
    elif gray not in radix_gray_colors:
        raise RuntimeError("'gray' color should be one of radix gray colors")
    return gray, curr

semantic_colored_names = set(['primary', 'secondary', 'accent', 'info', 'success', 'warning', 'error'])
semantic_gray_name = 'gray'
semantic_names = semantic_colored_names.union(set([semantic_gray_name]))

def colors():
    cc = {f'{name}{suffix}': f'rgb(var(--{name}{suffix}))'
          for suffix in (suffixes + asuffixes)
          for name  in semantic_names}
    cc.update({f'{name}-contrast': f'rgb(var(--{name}-contrast))' for name in semantic_colored_names})
    return cc
