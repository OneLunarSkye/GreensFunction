# Brandon Leydon          2/20/2025
# Green's Function and ODE with IVP

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Part 1

# 1) Homogeneous for y'' + 2y' + y = 0
t = sp.Symbol('t', real=True)
y = sp.Function('y')(t)

odeA_hom = sp.Eq(y.diff(t,2) + 2*y.diff(t) + y, 0)
solA_hom = sp.dsolve(odeA_hom)  # general solution
print("Homogeneous solution for ODE (A):")
print(solA_hom)

# Extract the expression on the right-hand side
exprA = solA_hom.rhs
symsA = exprA.free_symbols
symsA.discard(t)
C1_sym, C2_sym = list(symsA)

yA_hom_expr = exprA.subs({C1_sym: 1, C2_sym: 2})
# Convert to numeric function for plotting
yA_hom_func = sp.lambdify(t, yA_hom_expr, 'numpy')


# 2) Homogeneous for y'' + y = 0
x = sp.Symbol('x', real=True)
z = sp.Function('z')(x)

odeB_hom = sp.Eq(z.diff(x,2) + z, 0)
solB_hom = sp.dsolve(odeB_hom)  # general solution
print("\nHomogeneous solution for ODE (B):")
print(solB_hom)


exprB = solB_hom.rhs
symsB = exprB.free_symbols
symsB.discard(x)
A_sym, B_sym = list(symsB)

zB_hom_expr = exprB.subs({A_sym: 1, B_sym: -0.5})
# Convert to numeric function
zB_hom_func = sp.lambdify(x, zB_hom_expr, 'numpy')

# Plotting Solutions

t_vals = np.linspace(0, 5, 200)

yA_vals = yA_hom_func(t_vals)  # eqn (A) homogeneous
zB_vals = zB_hom_func(t_vals)  # eqn (B) homogeneous (reusing t_vals as x-values)

plt.figure(figsize=(10,4))

# Plot for eqn (A)
plt.subplot(1,2,1)
plt.plot(t_vals, yA_vals, label="Hom. eqn (A) with C1=1, C2=2", color='blue')
plt.title("Homogeneous solution: y''+2y'+y=0")
plt.xlabel("t")
plt.ylabel("y_h(t)")
plt.legend()
plt.grid(True)

# Plot for eqn (B)
plt.subplot(1,2,2)
plt.plot(t_vals, zB_vals, label="Hom. eqn (B) with A=1, B=-0.5", color='red')
plt.title("Homogeneous solution: y''+y=0")
plt.xlabel("x")
plt.ylabel("y_h(x)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# Part 2

def G(t_val, tau):

    return np.sin(t_val - tau) * np.heaviside(t_val - tau, 0)

def f(t_val):
    return t_val**2


t_vals = np.linspace(0, 5, 300)
y_vals = []

for T in t_vals:
    tau_points = np.linspace(0, T, 300)
    integrand = G(T, tau_points)*f(tau_points)
    y_T = np.trapz(integrand, tau_points)
    y_vals.append(y_T)

plt.figure()
plt.plot(t_vals, y_vals, label="Green's Function Solution", color='magenta')
plt.title("Solution via Green's Function: y'' + y = t^2")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.grid(True)
plt.legend()
plt.show()
