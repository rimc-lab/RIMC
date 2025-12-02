# **Chapter 6 — From CAPM to the $\alpha$-Drift Equation**

*Reframing Market Equilibrium through Recursive Learning Dynamics*

---

## **6.1 Continuous-Time CAPM and the Emergence of Asynchrony**

The classical CAPM assumes a **static instantaneous-information equilibrium**, expressed as

$$
E[r_i] = r_f + \beta_i (E[r_m] - r_f)
$$

All information is implicitly incorporated with zero latency ($\tau = 0$).
However, real markets exhibit **non-instantaneous transmission, absorption, and learning**, requiring a continuous-time and asynchronous extension.

A time-dependent expansion yields

$$
\frac{dr_i}{dt}
= \frac{dr_f}{dt}
{}+ \beta_i(t)\frac{d(r_m - r_f)}{dt}
{}+ \alpha_i(t)
$$

Here, $r_i(t)$ is the instantaneous return (e.g., log-price derivative), $\beta_i(t)$ is a time-varying beta, and $\alpha_i(t)$ represents the **structural deviation induced by non-synchronous learning**, not mere noise.

If the market reacted with perfect simultaneity, then $\alpha_i(t)=0$.
But because real markets always operate with a **finite delay $\tau>0$**, $\alpha$ cannot vanish.

---

## **6.2 Delay-Driven Generation of $\alpha$-Drift**

When market responses incorporate delay, the relationship becomes

$$
r_i(t) = r_f(t) + \beta_i(t-\tau)[r_m(t-\tau) - r_f(t-\tau)] + \epsilon_i(t)
$$

The term $\epsilon_i(t)$ is the **delay-induced residual**, treated as noise in static CAPM.
Taking the time derivative:

$$
\frac{dr_i}{dt}
= \frac{dr_f}{dt}
{}+ \dot{\beta}_i(t-\tau)\,[r_m(t-\tau)-r_f(t-\tau)]
{}+ \beta_i(t-\tau)\,\frac{d}{dt}[r_m(t-\tau)-r_f(t-\tau)]
{}+ \dot{\epsilon}_i(t)
$$

and using $\frac{d}{dt}r_x(t-\tau)=\dot r_x(t-\tau)$,

$$
\frac{dr_i}{dt}
= \frac{dr_f}{dt}
{}+ \dot{\beta}_i(t-\tau)\,[r_m(t-\tau)-r_f(t-\tau)]
{}+ \beta_i(t-\tau)\,[\dot r_m(t-\tau)-\dot r_f(t-\tau)]
{}+ \dot{\epsilon}_i(t)
$$

As long as $\dot{\beta}_i$ and $\dot{\epsilon}_i$ are non-zero,
$\alpha$ contains a **persistent structural component**, not a zero-mean error.

Thus, any continuous-time model containing $x(t-\tau)$ necessarily generates residual drift through $\dot x(t-\tau)$ — a **sufficient condition** for RIMC-style $\alpha$-drift.

---

## **6.3 Conversion into a Relaxation Equation**

The delay residual $\epsilon_i(t)$ can be reinterpreted as a **relaxation variable** describing memory and forgetting, rather than a statistical error:

$$
\underbrace{\epsilon_i(t)}_{\text{CAPM residual}}
= \underbrace{\varepsilon_R(t)G(t)}_{\text{delay-induced structural term}}
{}+ \underbrace{\xi(t)}_{\text{exogenous noise}}
$$

Here:

* $\varepsilon_R(t)$: observation gap between real technological recursion and market belief,
* $G(t)$: sensitivity kernel,
* $\xi(t)$: exogenous noise.

Integrating $\epsilon_i(t)$ over a finite memory window $T$ with an exponential kernel yields

$$
\boxed{
\alpha_{\text{drift}}(t)
= \int_{t-T}^{t}\varepsilon_R(\tau)G(\tau)e^{-\lambda(t-\tau)} d\tau
}
$$

with $\lambda$ the learning/forgetting rate.

Differentiating gives the **central $\alpha$-drift equation of RIMC**:

$$
\frac{d\alpha_{\text{drift}}}{dt}
= \varepsilon_R(t)G(t) - \lambda\alpha_{\text{drift}}(t)
$$

* first term: **forward-bias generation** through asynchronous information flow
* second term: **relaxation** by market learning

This corresponds to treating $\epsilon_i(t)$ as a **delay-dependent state variable** in continuous-time CAPM.

---

## **6.4 Interpretation and Consistency with CAPM**

RIMC does **not** reject CAPM.
It operates as a **temporal generalization** that retains the β-risk-premium structure while adding **asynchronous information dynamics**.

Thus, RIMC is a **generalized solution** of CAPM under recursive learning and delayed information.

---

## **6.5 Observational Consequence: The Inevitability of Non-Zero $\alpha$**

If market reactions are never perfectly synchronous,
$\alpha$ must contain a **persistent residual drift**, not a zero-mean noise.

Thus, $\alpha$ should be interpreted as a **structural return** stemming from the gap between:

* the speed at which the market learns the past ($\lambda$), and
* the speed at which technology generates the future (effective $\beta\gamma$).

This differs fundamentally from CAPM’s residual alpha.

---

## **6.6 Traces of $\alpha$-Drift in Observed Price Data**

A key implication of RIMC:
$\alpha$-drift is **not only forward-looking**, but also **embedded in already-observed price series**.

Because $\alpha$ arises from **the process of incorporation**, not from mispricing per se,
the “memory of asynchronous learning” is observable in historical data.

Define the observed drift component:

$$
\boxed{
\alpha_{\text{obs}}(t)
= \int_{t-T}^{t}\left[r_i(\tau) - r_f(\tau) - \beta_i(\tau)(r_m(\tau) - r_f(\tau))\right]
e^{-\lambda(t-\tau)} d\tau
}\tag{6.6}
$$

With $\lambda>0$, the integral is stable and interpretable as **informational lag memory**.

$\alpha_{\text{obs}}(t)$ encodes residual asynchronous structure already embedded in the price series.
Its comparison with theoretical $\alpha_{\text{drift}}(t)$ enables inference of $\lambda$ and $G(t)$.

The persistence of $\alpha$ traces is analogous to **decoherence residues in open quantum systems**:
observation itself modifies the record.

---

### **6.6.1 Implication**

This formalism clarifies that RIMC is a **model of observation**, not prediction.
Past data are not “fully priced-in information”, but a **statistical record of recursive delays**.

---

### **6.6.2 Conclusion: $\alpha$-Drift as the Market’s Memory**

Thus, $\alpha$-drift is not a hypothesis about future delay;
it is the **memory architecture of the market**, continuously written into price history.

> The existence of $\alpha$-drift in observed data indicates that the market
> can never completely forget its past.
> Price formation is inherently recursive: always chasing the future,
> always dragged by its own history.

---

# **6.7 Alpha Drift Capture Ratio: A Bridge Between Theory and Observation**

In RIMC, $\alpha$-drift is

* **theoretically** generated by the recursive structure encoded in the RV-equations, and
* **empirically** measured via the extended continuous-time CAPM.

To evaluate the consistency between these two layers of $\alpha$, we introduce the **Alpha Drift Capture Ratio**.

---

## **6.7.1 Definition**

By comparing the theoretical drift-generation strength with the observed drift series, we quantify how much of the underlying recursive structure the market actually “captures”.

$$
\rho_{\alpha}(t)
= \frac{\displaystyle \int_{t-T}^{t} |\alpha_{\text{obs}}(\tau)|^2 d\tau}
{\displaystyle \int_{t-T}^{t} |\varepsilon_R(\tau)G(\tau)|^2 d\tau}
$$

Where

* $\alpha_{\text{obs}}(t)$: observed $\alpha$-drift (extended-CAPM residual series),
* $\varepsilon_R(t)$: deviation of recursion rate (difference between theoretical $R$ and market-implied $R$),
* $G(t)$: sensitivity kernel (information-transformation efficiency).

For numerical stability, $\epsilon$-regularization (e.g., $\int|\varepsilon_R G|^2 + \epsilon$) may be adopted when the denominator becomes small.

The ratio satisfies $0 \le \rho_{\alpha}(t) \le 1$.
Values close to 1 indicate that the market is **accurately internalizing the recursive structure**.

---

## **6.7.2 Mathematical Interpretation: Finite-Time Efficiency**

This ratio generalizes the EMH into a framework of **finite-time efficiency**.

Instead of assuming instantaneous information incorporation, RIMC treats learning and transmission as processes with **finite velocity**.
Thus efficiency is redefined not as a state, but as a **speed**.

> A market is not “fully efficient”, but possesses a finite-time capacity
> to learn and internalize recursive structure.

Hence $\rho_{\alpha}$ becomes a **kinetic efficiency metric**, quantifying the market’s recursive-learning ability.

---

## **6.7.3 Empirical Implications**

$\rho_{\alpha}$ is computed as the **energy ratio** of observed vs. theoretical drift drivers.
Evaluated on rolling windows, it reveals the dynamic evolution of:

* market learning state,
* sensitivity regime shifts,
* adaptation speed.

Cyclic fluctuations of $\rho_{\alpha}$ imply that the market undergoes **recursive self-adjustment**, confirming that $\alpha$-drift is not noise but **the information-updating process itself**.

---

## **6.7.4 Theoretical Positioning**

| Perspective           | Role within RIMC                                               |
| --------------------- | -------------------------------------------------------------- |
| Theoretical model     | RV-equations: generator of recursive structure (unobservable)  |
| Observational model   | Extended CAPM: projection of asynchronous information flow     |
| Integrating parameter | $\rho_{\alpha}$: bridge linking theoretical and observed drift |
| Conceptual meaning    | Quantifies finite-time efficiency and recursive learning       |

---

## **6.7.5 Summary: Observational Closure of RIMC**

The RV-equations provide the **design blueprint** of recursion, while
$\rho_{\alpha}$ quantifies how much of that structure becomes **observable in the market**.

> RIMC achieves closure through $\rho_{\alpha}$.
> Once the bridge of finite-time efficiency is established,
> RIMC evolves from a hypothesis into an **Observable Recursive Model**.

Thus the capture ratio translates theoretical recursion into an **empirically testable coordinate system**.

---

# **6.8 Finite-Time Lead Estimation and Observational Benchmarks**

**The RV-equations are fundamentally a generative model of $V$.**

Although RIMC appears to estimate the technological recursion rate $R(t)$, its true purpose is to reconstruct the **time evolution of economic value $V(t)$** generated through $R(t)$.
RIMC formalizes the transformation “technology → value”, making $R(t)$ a latent generator and $V(t)$ the observable outcome.

---

## **6.8.1 Generative Layer: Value Formation via the RV-Equation**

The RV-equation defines how recursive technological evolution generates economic value:

$$
\frac{dV}{dt} = L(t)A(t)R(t)^{\beta}
$$

Here $L(t)$ denotes capital efficiency, $A(t)$ institutional/environmental factors, and $R(t)$ the recursion rate.
Since $R(t)$ is unobservable, it is reconstructed **from the dynamics of $V(t)$**, meaning RIMC ultimately estimates **the generative dynamics of value**, not $R$ per se.

---

## **6.8.2 Observational Layer: CAPM as a Projection of Value Dynamics**

Markets observe only the time variation of $V(t)$, represented (approximately) by the continuous-time CAPM:

$$
\frac{dr_i}{dt}
= \frac{dr_f}{dt}

{}+ \beta_i(t)\frac{d(r_m - r_f)}{dt}
{}+ \alpha_i(t)
$$

Here $r_i(t)$ is the individual return, i.e., the observable derivative of $V(t)$.
The market, unable to observe $R(t)$, approximates the evolution of value through a β-structure plus a drift residual.

---

## **6.8.3 Finite-Time Lead Estimation: Connecting Theory and Observation**

RIMC compares the theory-generated $V(t+\tau)$ with the market-observed $r_i(t+\tau)$ to connect:

* **theoretical recursion**, and
* **observed reaction**.

RV-based theoretical forecast:

$$
V_{\text{pred}}(t+\tau)
= V(t) + \int_t^{t+\tau} L(u)A(u)R(u)^{\beta} du
$$

CAPM-based observed evolution:

$$
r_i(t+\tau)
= \int_t^{t+\tau}\frac{1}{V(u)}\frac{dV(u)}{dt} du
+ \int_t^{t+\tau}\alpha_i(u) du
$$

Define the **finite-time lead error**:

$$
\Delta_{\alpha}(t,\tau)
= \frac{1}{\tau}\int_t^{t+\tau}\left[\frac{1}{V(u)}\frac{dV(u)}{du} + \left(r_f(u)+\beta_i(u)(r_m(u)-r_f(u))\right)\right]du
$$

The closer $\Delta_{\alpha}$ is to zero, the more accurately markets learn the recursive structure under finite delay.

> **Finite-Time Lead Estimation**
> refers not to prediction, but to the structural fact that
> the generative model (RV) leads the observational model (CAPM)
> by a finite delay $\tau$ due to bounded information-transmission speeds.

---

## **6.8.4 CAPM as an Observational Benchmark**

Both RV and CAPM describe the evolution of $V(t)$, but at different levels:

| Layer                      | Equation                                                                   | Variable | Function                              |
| -------------------------- | -------------------------------------------------------------------------- | -------- | ------------------------------------- |
| **Generative (theory)**    | $\dfrac{dV}{dt}=LAR^{\beta}$                                               | $V$      | Generates value from recursion        |
| **Observational (market)** | $\dfrac{dr_i}{dt}=\dfrac{dr_f}{dt}+\beta_i\dfrac{d(r_m-r_f)}{dt}+\alpha_i$ | $\dot V$ | Approximates value change via returns |

Thus CAPM becomes the **natural observational benchmark** for evaluating RIMC.
Comparing $V_{\text{pred}}(t+\tau)$ to CAPM-implied returns tests the structural consistency of the underlying recursion.

---

## **6.8.5 Structural Consistency of RIMC**

* RV generates **value** through recursive technology.
* CAPM observes **value changes** through market returns.
* Both describe the same object — from different scales.

Therefore, CAPM fits naturally as the observational counterpart to RV.

> **RIMC’s essence is not estimating $R$,
> but reconstructing the generative evolution of $V$.**
> CAPM then becomes the **recursive observational apparatus**
> that measures how well the market internalizes the generated value.

---

# **6.9 Toward the Final Chapter: From Hypothesis to Verification**

This chapter extended CAPM into continuous time with explicit information delay, redefining $\alpha$ as a **structural deviation arising from learning speed and asynchronous information flow**, rather than a statistical residual.

Through

* continuous-time CAPM derivation,
* formulation of the $\alpha$-drift equation, and
* mapping to observable data,

RIMC progressed from an equilibrium model to a **learning–relaxation model**.

The framework showed both:

* theoretical generation and decay of $\alpha$ via delay-differential structure, and
* empirical extraction of asynchronous traces embedded in historical price series.

Thus RIMC transitions from a conceptual hypothesis into a **testable observational model**.

The remaining task is empirical: apply the $\alpha$-drift equation and the capture ratio to data and quantify **how efficiently the market learns recursive structure**.
