# **Appendix A — A Practitioner’s Interpretation of RIMC**

RIMC is not a tool for forecasting price movements.
It is a **blueprint for exposing the informational delay between technology and markets**.
Its purpose is not trade selection, but the **structural understanding of information transmission, learning, and observation**.

In practice, RIMC serves as a **quantitative language** for examining
*how a model learns from information and when it reacts to it*
within research or portfolio construction workflows.

---

## **A.1 Theoretical Re-Interpretation**

The essence of RIMC can be condensed into the following three statements:

1. There exists an observation delay between technological fundamentals and market pricing.
2. This delay accumulates and generates **$\alpha$-drift**.
3. $\alpha$-drift provides a mathematical representation of this structural delay.

Thus, RIMC is not a predictive model; it is a
**structural theory for analyzing how information is incorporated into markets**.

For quants, researchers, and analysts, RIMC becomes a framework for evaluating
**the phase at which their own models operate relative to the market**.

---

## **A.2 The One-Company-One-Equation Principle**

In RIMC, an “equation” is not a fixed model but a **dynamic mapping**.
All parameters—
$$L(t), A(t), \gamma(t), \delta(t), \kappa_V(t), \kappa_R(t), \beta(t), \mu(t), \nu(t), \tau$$
are defined as **time-varying functions estimated from external data streams** $Z_t$.

Even with the same theoretical scaffolding,
different agents (firms, funds, researchers) observe **different** data streams $Z_t$,
and therefore estimate **different** functional mappings.
As a result, a **distinct equation naturally emerges for each institution**.

The core of RIMC lies in the **choice of observation stream**.
Depending on which layers of information (internal, external, market) are captured and *when*,
the induced recursive market estimate $\hat r_{\text{market}}(t)$ will differ in phase and magnitude.

This is the source of **observation-strategy heterogeneity**
and explains why **each fund develops a unique reaction speed and recursion dynamics**.

Thus, “One Company, One Equation” in RIMC is not an idiosyncratic modeling choice, but
the inevitable result of differing observation sets, delay structures, and parameter estimates—
a **structural necessity**, not a stylistic preference.

---

## **A.3 Re-Defining CAPM $\alpha$**

In RIMC, the $\alpha$ term—treated as statistical residual in CAPM—becomes a
**structural deviation induced by temporal asynchrony**.

Whereas CAPM assumes instantaneous relationships,
RIMC concerns itself with **temporal distortions**.

When such distortions accumulate, observational errors drift in one direction,
manifesting as **$\alpha$-drift**.

Under this interpretation, $\alpha$ is not “unpredictable error”, but a
**dynamic structure arising from the timing gap in information assimilation**.

---

## **A.4 Time Scope — The Meaning of Quarterly Structure**

RIMC can be applied at any timescale, but in practice the
**quarterly horizon (~90 days)** is empirically most observable.

Across firms, technological changes (R&D, AI investment, capital allocation)
typically require **1–2 quarters** before being priced in.

Making this *delay* explicit is essential to RIMC.
It is a hypothesis that treats the **time lag between understanding and valuation**
as a structural variable.

---

## **A.5 Independence of the Observation-Difference Equation**

In RIMC, $\alpha$-drift does **not** depend on a specific system of differential equations describing value creation.
This is because RIMC models not the internal generative mechanism but the
**temporal dynamics of the observation difference** $\varepsilon_R(t)$.

As long as a discrepancy exists between the internal recursion rate $r_{\text{real}}(t)$
and the market’s estimate $r_{\text{market}}(t)$,
a **structural $\alpha$ is inevitable**:

$$
\boxed{
\alpha_{\text{drift}}(t)
= \int_{t-T}^{t}
\varepsilon_R(\tau)G(\tau)e^{-\lambda (t-\tau)} d\tau
}
$$

This integral form is compatible with **any** underlying generative equation—
economic, factor-based, reinforcement-learning-driven, or otherwise.

Thus RIMC is not a “meta-model” sitting above others,
but an **autonomous layer** for analyzing the temporal behavior of observation error.

Through this layer, recursion speeds, reaction delays, and learning pressures
can be compared on a common temporal frame.
Differences in convergence speeds or phase misalignment across models become a
**Recursive Convergence Race**—a measurable object under the RIMC lens.

---

## **A.6 Mapping the Fama–French Five-Factor Model into RIMC**

As a concrete example of RIMC as a “universal mapping layer”,
we show how the **Fama–French Five-Factor (FF5) model** maps naturally to the RIMC RV-equation system.

The conclusion is direct:
**FF5 embeds cleanly and naturally into the RIMC framework of coupled differential equations.**

The two added FF5 factors—RMW and CMA—are particularly compatible with RIMC,
as they behave like **state variables describing recursive growth**.

---

## **A.6.1 FF5 → RV-Equation Mapping**

FF5 can be expressed as a **six-dimensional system of coupled differential equations**,
linking portfolio value $V(t)$ with five state variables $R_k(t)$:

$$
\begin{cases}
\begin{aligned}
\dfrac{dV}{dt} &= \mathcal{L}(Z_t)\left[\sum_{k\in\{M,S,H,R,C\}} w_k(t)R_k(t-\tau_k)\right]^{\beta(t)}
{}- \kappa_V(t)V(t)^{\mu(t)} \\
\dfrac{dR_M}{dt} &= \gamma_M V^{\delta_M} - \kappa_M R_M (\text{Market}) \\
\dfrac{dR_S}{dt} &= \gamma_S V^{\delta_S} - \kappa_S R_S (\text{SMB}) \\
\dfrac{dR_H}{dt} &= \gamma_H V^{\delta_H} - \kappa_H R_H (\text{HML}) \\
\dfrac{dR_R}{dt} &= \gamma_R V^{\delta_R} - \kappa_R R_R (\text{RMW}) \\
\dfrac{dR_C}{dt} &= \gamma_C V^{\delta_C} - \kappa_C R_C (\text{CMA})
\end{aligned}
\end{cases}
$$

Here:

* $V(t)$ denotes value (return, market cap, etc.)
* $R_M, R_S, R_H, R_R, R_C$ correspond to FF5’s
  MKT–RF, SMB, HML, RMW, CMA
  interpreted as **recursive intensities**.

---

## **A.6.2 RIMC Interpretation of the Two Additional FF5 Factors**

### **(1) $R_R(t)$ — Profitability (RMW)**

In FF5: high-profitability firms earn higher expected returns.
In RIMC: $R_R(t)$ represents **recursive efficiency**—how effectively capital self-amplifies.

### **(2) $R_C(t)$ — Investment (CMA)**

In FF5: firms with conservative investment earn higher returns.
In RIMC: $R_C(t)$ represents **internal friction**—excessive investment increases entropy and reduces long-term efficiency.

$R_C$ naturally modulates the damping term $\kappa$,
extending the “lifespan” of the recursive system.

---

## **A.6.3 Three Advancements Enabled by This Mapping**

Mapping FF5 into RIMC yields three structural benefits:

### **1. Factor-Specific Delays $\tau_k$**

Conventional FF5 assumes simultaneity.
RIMC allows factor-specific reaction delays—more realistic:

* Market (MKT–RF): $\tau_M \approx 0$
* Profitability: $\tau_R \approx 1-2$ quarters
* Investment: $\tau_C \approx 1$ year

This captures the true **heterogeneous timing** of factor materialization.

### **2. Explicit Factor Interactions**

Linear FF5 cannot model interference between factors.
RIMC’s differential structure does.

Example chain:

> Higher profitability $R_R$ → inflows to $V$ → overinvestment increases $R_C$ friction → value factor $R_H$ weakens.

This creates a **trajectory-level simulation**, not a static regression.

### **3. Detecting Bubble Modes via $\beta(t)$**

If $\beta(t) \gg 1$, the system enters a regime where:

* capital concentration becomes self-reinforcing,
* nonlinear runaway (bubble) behavior emerges.

RIMC quantifies such overheating in real time as **temporal distortion rather than factor mispricing**.

