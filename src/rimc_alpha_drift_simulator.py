import numpy as np
import matplotlib.pyplot as plt

# --- 1. Parameter Settings (Definition of RIMC) ---
# Time settings
T_MAX = 200        # Simulation horizon
dt = 0.1           # Time resolution (step size)

# Parameters for the RV system (Tech–Capital recursive loop)
L = 1.1            # Social adoption speed
A = 1.1            # Capital concentration rate
beta = 1.01        # Nonlinearity of technology (>=1.0 leads to exponential scaling)
gamma = 0.5        # Feedback rate from capital to technology
delta = 0.8        # Investment sensitivity
kappa_v = 0.5      # Value decay (competition / saturation)
kappa_r = 0.05     # Technology decay (obsolescence)

# ★ Core of RIMC: Observation lag & memory
tau = 20           # Time lag: market only "sees" technology from 20 steps ago
lambda_decay = 0.1 # Forgetting rate: rate at which old information decays
G_sens = 1.0       # Market sensitivity to the information gap

# --- 2. Variable Initialization ---
time_steps = int(T_MAX / dt)
V = np.zeros(time_steps)  # Economic value (V)
r = np.zeros(time_steps)  # Real technological recursion rate (r)
alpha = np.zeros(time_steps)  # Alpha drift (α)

# Initial conditions
V[0] = 10.0
r[0] = 10.0

# --- 3. Main Loop (Discrete form of the differential equations) ---
for t in range(1, time_steps):
    
    # A. Apply time lag (Lookback)
    # Market-perceived technology level = r at (t - tau)
    past_index = max(0, t - int(tau / dt))
    r_market = r[past_index]
    
    # B. Compute observation gap
    # Difference between "real tech" and "market-observed tech"
    epsilon_R = r[t-1] - r_market
    
    # C. RV equations (coupled differential system)
    # dV/dt = L * A * r(delay)^beta - decay
    dV = (L * A * (r_market ** beta) - kappa_v * V[t-1]) * dt
    V[t] = V[t-1] + dV
    
    # dr/dt = gamma * V^delta - decay
    dr = (gamma * (V[t-1] ** delta) - kappa_r * r[t-1]) * dt
    r[t] = r[t-1] + dr
    
    # D. Alpha drift equation (Leaky integrator implementation)
    # Integration is "accumulation" with exponential decay
    # alpha_new = alpha_old * (1 - decay) + (gap * sensitivity)
    d_alpha = (epsilon_R * G_sens - lambda_decay * alpha[t-1]) * dt
    alpha[t] = alpha[t-1] + d_alpha

# --- 4. Visualization (Plotting) ---
plt.figure(figsize=(12, 8))

# Upper plot: Evolution of Technology (r) and Value (V)
plt.subplot(2, 1, 1)
plt.plot(r, label='Real Technology (r)', color='blue', linestyle='--')
plt.plot(V, label='Market Value (V)', color='green')
plt.title('RV Equation: Interaction of Technology & Value')
plt.legend()
plt.grid(True)

# Lower plot: Alpha drift
plt.subplot(2, 1, 2)
plt.plot(alpha, label='Alpha Drift (Accumulated Lag)', color='red')
plt.axhline(0, color='black', linewidth=0.5)
plt.fill_between(range(len(alpha)), alpha, 0, where=(alpha > 0),
                 color='red', alpha=0.1, label='Positive Alpha Zone')
plt.title('Alpha Drift Equation: Visualization of Structural Opportunity')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
