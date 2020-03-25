def uwu(a):
    b = ""
    prev = "\0"
    for c in a:
        if c in "LR":
            b += "W"
        elif c in "lr":
            b += "w"
        elif c in "oO":
            if prev in "nNmM":
                b += "yo"
            else:
                b += c
        else:
            b += c
        prev = c
    return b + " uwu"
