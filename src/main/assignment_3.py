def euler_method(f, t0, y0, h, n):
    t = t0
    y_current = y0
    for _ in range(n):
        y_current += h * f(t, y_current)
        t += h
    return y_current

def runge_kutta_method(f, t0, y0, h, n):
    t = t0
    y_current = y0
    for _ in range(n):
        k1 = h * f(t, y_current)
        k2 = h * f(t + h/2, y_current + k1/2)
        k3 = h * f(t + h/2, y_current + k2/2)
        k4 = h * f(t + h, y_current + k3)
        y_current += (k1 + 2*k2 + 2*k3 + k4)/6
        t += h
    return y_current
