# Chapter 2 — The Foundational Equations of RIMC

**Coupled Dynamics Between Technological Recursiveness and Market Value**

---

## 2.1 Conceptual Framework

RIMC defines the interaction between **technological recursiveness (R)** and **economic value (V)** as a
**Dynamic Coupled System** whose components co-evolve through bidirectional feedback.

The central premise is:

> **“Technology generates capital, and capital accelerates technology.”**

The technological recursiveness vector $\mathbf{R}(t)$ is not a single scalar but a **multidimensional entity** formed by the interaction of R&D activity, data assets, organizational learning, and informational networks.

For analytical tractability, the value-generating components of $\mathbf{R}(t)$ are aggregated into a scalar through an **aggregation operator** $h(\cdot)$:

$$
r(t) = h(\hat{\mathbf{R}}(t)) \quad (\ge 0)
$$

where $r(t)$ is a scalar representation of market-perceived technological recursiveness.

---

## 2.2 The Core Coupled System (RV System)

The minimal coupled system introduced in Chapter 1 captured the essential recursive structure of RIMC.
Here we extend it by incorporating **observation delay, dissipation, and nonlinear amplification**, producing a more operational and realistic representation.

Markets cannot observe true technological activity directly; they infer it through disclosed signals, reporting, and symbolic externalization.
While the formal observation structure is developed in Chapter 3, for now we assume that
$\hat{\mathbf{R}}(t)$ is a **delayed assimilation** of $\mathbf{R}(t)$.

The dual-loop structure of RIMC is defined as:

$$
\boxed{
\begin{cases}
\dfrac{dV}{dt} = L(t)\,A(t)\,[r(t-\tau)]^{\beta(t)} - \kappa_V(t)\, V(t)^{\mu(t)} \\
\dfrac{dr}{dt} = \gamma(t)\, V(t)^{\delta(t)} - \kappa_R(t)\, r(t)^{\nu(t)}
\end{cases}}
$$

Here, $r(t)$ is interpreted as a “representative recursiveness rate,” incorporating both internal dynamics and market estimation.
The distinction between **true technological progression** $r_{\text{real}}$ and **market-perceived progression** $r_{\text{market}}$ will be formalized in Chapter 3.

**Sign and Range Assumptions**
All parameters satisfy:

* $L(t),A(t),\gamma(t) > 0$
* $\beta(t),\delta(t) > 0$
* $\kappa_V(t),\kappa_R(t) \ge 0$
* $\mu(t),\nu(t) \ge 1$
* $\tau \ge 0$

| Symbol                    | Name                         | Interpretation                                       |
| ------------------------- | ---------------------------- | ---------------------------------------------------- |
| $V(t)$                    | Economic value               | Observable market value (market cap, earnings, etc.) |
| $r(t)$                    | Scalarized recursiveness     | Aggregated measure of technological self-improvement |
| $\hat{\mathbf{R}}(t)$     | Observed/assimilated R       | Market‐constructed estimate from signals             |
| $L(t)$                    | Social learning rate         | Institutional/cultural adaptation speed              |
| $A(t)$                    | Capital concentration        | Degree of financial/resource allocation              |
| $\beta(t)$                | Technological nonlinearity   | Strength of **superlinear** amplification            |
| $\gamma(t),\delta(t)$     | Value→technology sensitivity | How economic output stimulates recursion             |
| $\kappa_V(t),\kappa_R(t)$ | Dissipation                  | Saturation, competition, constraints                 |
| $\tau$                    | Observation delay            | Time lag between real R and observable V             |

**Remark**
When $\beta(t),\delta(t)>1$ and dissipation terms approach zero, strong internal positive feedback may generate self-exciting dynamics.
RIMC assumes $\kappa_V(t),\kappa_R(t)>0$ to preserve numerical stability and prevent runaway divergence.

---

### 2.2.1 Model Validity and Positivity Invariance

**Assumption A (Well-posedness of the R–V System)**

Assume:

* $h \in C^1$ and locally Lipschitz, at most polynomial growth
* $L(t),A(t),\gamma(t)$ bounded, piecewise continuous
* $\kappa_V(t),\kappa_R(t)>0$, $\mu(t),\nu(t) \ge 1$
* Initial history $V(\cdot),r(\cdot):[-\tau,0]\to[0,\infty)$

Then the system

$$
\begin{cases}
\dfrac{dV}{dt} = L(t)A(t)[r(t-\tau)]^{\beta(t)} - \kappa_V(t)V^{\mu(t)} \\
\dfrac{dr}{dt} = \gamma(t)V^{\delta(t)} - \kappa_R(t)r^{\nu(t)}
\end{cases}
$$

admits a unique local solution, and
$$V(t)\ge0,\quad r(t)\ge0$$
are preserved for all $t$.

Because the vector field satisfies
$V=0\Rightarrow \dot V\ge0$ and $r=0\Rightarrow \dot r\ge0$,
the **first quadrant is positively invariant**.

---

### 2.2.2 Operational Definition: Time-Varying Estimated Parameters

The parameters
$L(t),A(t),\gamma(t),\delta(t),\kappa_V(t),\kappa_R(t),\beta(t),\mu(t),\nu(t),\tau$
are not constants but **time-varying, data-driven estimates**.

They are generated from exogenous informational series $Z_t$ through mappings:

$$
\begin{aligned}
L(t) &= \mathcal{L}(Z_t;\theta_L), &
A(t) &= \mathcal{A}(Z_t;\theta_A), \\
\gamma(t) &= \Gamma(Z_t;\theta_\gamma), &
\beta(t) &= \mathcal{B}(Z_t;\theta_\beta), \\
\delta(t) &= \Delta(Z_t;\theta_\delta), &
\kappa_V(t) &= \mathcal{K}*V(Z_t;\theta*{K_V}), \\
\kappa_R(t) &= \mathcal{K}*R(Z_t;\theta*{K_R}), &
\mu(t) &= M_V(Z_t;\theta_\mu), \\
\nu(t) &= N_R(Z_t;\theta_\nu)
\end{aligned}
$$

This structure allows RIMC to incorporate macroeconomic, institutional, and informational regimes dynamically.

---

### 2.2.3 Observation Structure and Scalarization

In the observation layer, internal technological activity $\mathbf{R}(t)$ is externalized into symbolic signals $S(t)$ through an operator $\mathcal{O}$, then assimilated by the market through $\mathcal{I}$:

$$
S(t)
= \mathcal{O}(\mathbf{R}(t-\tau_{\mathcal{O}})) + \eta(t),
\qquad
\hat{\mathbf{R}}(t)
= \mathcal{I}(S(t-\tau_{\mathcal{I}}))
$$

with:

* $\tau_{\mathcal{O}},\tau_{\mathcal{I}}$: externalization/assimilation delays
* $\eta(t)$: observational noise
* $S(t)$: symbolic externalization of technological activity

The market-perceived recursiveness is then:

$$
r_{\text{market}}(t) = h(\hat{\mathbf{R}}(t))
$$

while the internal true recursiveness is:

$$
r_{\text{real}}(t) = h(\mathbf{R}(t))
$$

The deviation
$$\varepsilon_R(t)= r_{\text{real}}(t)-r_{\text{market}}(t)$$
defines the **observation gap**, foundational for α-drift.

---

### 2.2.4 The Role of S(t) Within RIMC

The flow of information in RIMC is summarized as:

$$
\mathbf{R}(t)
\xrightarrow[\text{externalization}]{\mathcal{O}}
S(t)
\xrightarrow[\text{interpretation}]{\mathcal{I}}
\hat{\mathbf{R}}(t)
\xrightarrow[\text{scalarization}]{h}
r_{\text{market}}(t)
$$

Thus, $S(t)$ represents the **symbolic layer**:
the external informational footprint of internal technological recursion—earnings reports, disclosures, media, analyst outputs, and social communication.

RIMC operates on a three-layer observational hierarchy:

| Layer                 | Agent             | Variable              | Process                                 |
| --------------------- | ----------------- | --------------------- | --------------------------------------- |
| Internal              | Firms, technology | $\mathbf{R}(t)$       | Generation of knowledge/technology      |
| **Observation layer** | Media, analysts   | **$S(t)$**            | Externalization ($\mathcal{O}$) + noise |
| Market                | Investors         | $\hat{\mathbf{R}}(t)$ | Assimilation ($\mathcal{I}$)            |

---

### 2.2.5 Unified Representation of Time-Varying Estimation

With observation delay, the projected market-recognized recursiveness is:

$$
r_{\text{market}}(t-\tau)
=\mathcal{H}\left(
\Phi(\hat{\mathbf{R}}(t-\tau))\theta_H
\right)
$$

where:

* $\Phi(\cdot)$ extracts domain-specific features
* $\mathcal{H}$, $\mathcal{L}$, $\mathcal{A}$, $\Gamma$... are learned pipelines
* Parameters are re-estimated at each $t$ and injected into the main equations

This formalizes the connection between internal recursion and market observation through data-dependent transformations.

---

### 2.2.6 Proxy Observability of Parameters

Each term in the RIMC equations
($L(t),A(t),\gamma(t),\beta(t),\delta(t),\kappa_V(t),\kappa_R(t)$, etc.)
is not directly observable but a **proxy derived from exogenous series** $Z_t$:

$$
\theta_i(t)
= \mathcal{F}_i(Z_t;\theta_i),
\qquad
\theta_i\in { L,A,\gamma,\beta,\delta,\kappa_V,\kappa_R }
$$

Thus the RIMC framework connects **unobservable internal recursion** (endogenous layer)
and **observable market/environmental data** (exogenous layer) via statistical/ML estimation.

---

## 2.3 Equation (1): Propagation from Technology → Value

$$
\dfrac{dV}{dt}
= L(t)A(t)\,[r(t-\tau)]^{\beta(t)}

- \kappa_V(t)V(t)^{\mu(t)}
  $$

This equation expresses how technological recursiveness translates into economic value.

* $r(t-\tau)$ embeds **delayed market perception**.
* When $\beta(t)>1$, small changes in $r$ can generate **superlinear amplification** in $V$.
* The dissipation term $\kappa_V(t),V^{\mu(t)}$ captures **saturation, competition, and institutional drag**.

---

## 2.4 Equation (2): Feedback from Value → Technological Recursion

$$
\dfrac{dr}{dt}
= \gamma(t)V(t)^{\delta(t)}

- \kappa_R(t) r(t)^{\nu(t)}
  $$

Economic value $V(t)$ promotes technological recursion through R&D expenditure, talent acquisition, infrastructure investment, and data accumulation.

* $\gamma(t)$: how effectively capital accelerates recursive innovation
* $\delta(t)$: sensitivity of technological growth to financial performance
* $\kappa_R(t) r^{\nu(t)}$: constraints from saturation, resource limits, and institutional frictions

This equation captures the **positive feedback loop** whereby economic gains accelerate the next cycle of technological progression—the second half of RIMC’s recursive structure.

---

# 2.5 Non-Dimensionalization and Dimensional Consistency

Let $T_0$, $V_0$, and $R_0$ denote characteristic scales for time, economic value, and technological recursiveness.
Define the non-dimensional variables:

$$
\tilde t = t/T_0,\qquad
\tilde V = V/V_0,\qquad
\tilde r = r/R_0
$$

Then the value equation becomes:

$$
\frac{d\tilde V}{d\tilde t}
= \tilde L(\tilde t)\,\tilde A(\tilde t)\,\tilde r^{\beta}

- \tilde\kappa_V\,\tilde V^{\mu}\,
  $$

where the product $\tilde L(\tilde t)\tilde A(\tilde t)$ is dimensionless.

All subsequent expressions are written in these non-dimensional variables.

---

# 2.6 Interpretation of the R–V Coupled System:

## The Technology–Capital Engine

The RV system expresses, in a minimal nonlinear form, the core recursive loop:

**technology generates value, and value accelerates technology.**

However, the market observes technology with delay $\tau$.
Thus, real technological activity $\mathbf{R}*{\text{real}}(t)$ and the market-assimilated estimate
$\mathbf{R}*{\text{market}}(t)\equiv \hat{\mathbf{R}}(t)$
are **not synchronized**.

Define the **observation gap** as:

$$
\varepsilon_R(t)
= r_{\text{real}}(t) - r_{\text{market}}(t)
$$

When $\varepsilon_R(t) > 0$, the market underestimates technological progression.
Corrections to this delayed perception cause $V(t)$ to adjust upward in a **catch-up dynamic**.
This observation gap is the structural origin of **excess return $\alpha$** in RIMC.

> **In RIMC, α is not a stochastic residual but an
> informational drift arising from the asynchrony between
> “technology generation speed” and “market learning speed.”**

The coupled system thereby operates as a **technology–capital engine**,
a structural driver behind innovation cycles, industrial reorganization,
and capital concentration at the societal and sectoral level.

The time integral of the observation gap $\varepsilon_R(t)$ yields the observed α (developed in Chapter 3).
Thus α is not a static error term but a **history-dependent quantity** accumulated over time.

---

# 2.7 From Observation Misalignment to Generative Structure

The R–V coupled system describes the hypothetical closed recursion in which
**technology ($R$) generates value ($V$)** and **value accelerates technology**.

In real markets, however, the evolution of technology and the evolution of valuation are **not fully synchronized**.
The market observes **past $R$**, always filtered through **information-transmission delays ($\tau$)**
and **assimilation errors ($\varepsilon_R$)**.

In short:

> The market is a *system that observes technological change*,
> not a *system that generates* it.

This **temporal misalignment between observation and generation** constitutes the structural mechanism
through which RIMC produces **systematic return (α)**.

The next chapter formalizes how this misalignment creates a **recursive gap** and
how the time integration of this gap produces observable **α (excess return)**
as a deterministic consequence of asynchronous learning.