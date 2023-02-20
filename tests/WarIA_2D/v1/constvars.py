g_s = 80
g_w = 10
size = (g_s * g_w, g_s * g_w)
movement_factor = 23

def clamp(value, minrange, maxrange):
    if value > maxrange:
        return maxrange

    if value < minrange:
        return minrange

    return value