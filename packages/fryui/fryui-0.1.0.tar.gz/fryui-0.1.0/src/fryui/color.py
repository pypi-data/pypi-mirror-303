from coloraide import Color

def is_dark(c):
    color = Color(c)
    return color.contrast('white') > color.contrast('black')

def content_color(c):
    return Color(c).mix('white' if is_dark(c) else 'black', 0.8)

def focus_color(c):
    return Color(c).mix('black', 0.07)

def dump(c):
    return Color(c).convert('srgb').to_string()[4:-1]
