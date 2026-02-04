
title: "Public Investment Multipliers and Corruption: Does Institutional Quality Matter?"
subtitle: "Replication and Extension of Heimberger & Dabrowski (2025)"
author: "Nome Cognome"
date: "2026-XX-XX"


> *This article combines replication and methodological extension.  
> First, I replicate recent evidence on public investment multipliers in the EU.  
> Second, I ask whether the effectiveness of public investment depends on institutional quality, proxied by corruption.*

### 1. Motivation

In recent years, public investment has returned to the centre of the European policy debate.  
The need to close infrastructure gaps, support the green transition, and strengthen long-run growth has led to renewed interest in the **macroeconomic effects of public investment**.

A recent contribution by Heimberger and Dabrowski (2025) provides compelling evidence that **public investment shocks boost output, reduce unemployment, and do not endanger public debt sustainability** in the European Union.  
Their results are based on a transparent identification strategy and modern local projection techniques.

However, an important question remains largely unexplored:

> **Does public investment work equally well in all institutional environments?**

In particular, this article asks whether the impact of public investment differs between countries with **low and high levels of corruption**.


### 2. The Original Paper: Idea and Identification Strategy

#### 2.1 Public Investment Shocks via Forecast Errors

The core idea of Heimberger and Dabrowski (2025) is to identify public investment shocks using **forecast errors**:

```math
F_{i,t} = I^{\text{actual}}_{i,t} - I^{\text{forecast}}_{i,t}
```

where public investment is measured as general government gross fixed capital formation as a share of GDP.

This strategy addresses two classic problems in fiscal policy estimation:

- **Fiscal foresight**: economic agents may anticipate investment plans.
- **Endogeneity**: fiscal policy may respond to the business cycle.

By exploiting forecast errors from European Commission archives, the authors align the econometric information set with that of households and firms.


#### 2.2 Econometric Framework

The paper estimates impulse responses using **local projections** (Jordà, 2005), based on the following baseline equation:

```math
y_{i,t+k} - y_{i,t-1}
=
\beta_k F_{i,t}
+ \sum_j \gamma_{k,j} Z_{i,t-j}
+ \delta_i^k
+ \theta_t^k
+ \varepsilon_{i,t}^k
```

where:

- \(y\) denotes the outcome variable (GDP, unemployment, private investment, public debt),
- \(F_{i,t}\) is the public investment forecast error,
- \(Z\) includes standard macroeconomic controls,
- \(\delta_i^k\) and \(\theta_t^k\) are country and time fixed effects.

The authors find **cumulative output multipliers above one**, with no evidence of crowding-out or rising debt.


### 3. Replication: Why It Matters

Before extending the analysis, I fully **replicate the original results** using the authors’ specification and data structure.

The replication serves three purposes:

1. **Verification** – confirming that the results are reproducible.
2. **Benchmarking** – ensuring comparability with the extension.
3. **Transparency** – allowing readers to visually compare baseline and extended impulse responses.

The replicated impulse-response functions closely match those reported in the original paper, both in magnitude and in statistical uncertainty.

*(Baseline graphs reproduced here in the final version.)*


### 4. Research Question: Does Corruption Matter?

While average effects are informative, fiscal multipliers may vary across countries.

A natural candidate driving heterogeneity is **institutional quality**, and in particular **corruption**.

From an economic perspective, higher corruption may:

- reduce investment efficiency,
- increase leakages and rent-seeking,
- weaken the transmission from public spending to real activity.

This leads to the central question of this article:

> **Is the macroeconomic impact of public investment lower in more corrupt countries?**


### 5. Methodological Extension: Introducing Corruption Interactions

#### 5.1 Extended Specification

To address this question, I extend the baseline local projection framework by allowing the public investment shock to interact with lagged corruption.

The estimated equation at horizon \(k\) is:

```math
y_{i,t+k} - y_{i,t-1}
=
\beta_k F_{i,t}
+ \theta_k \left( F_{i,t} \times \text{Corr}_{i,t-1} \right)
+ \sum_j \gamma_{k,j} Z_{i,t-j}
+ \delta_i^k
+ \theta_t^k
+ \varepsilon_{i,t}^k
```

where \(\text{Corr}_{i,t-1}\) is a lagged corruption indicator.

Corruption is mean-centered so that:

- \(\beta_k\) captures the effect at **average corruption levels**.

This specification allows the **investment multiplier to vary continuously** with institutional quality.


#### 5.2 Interpretation

- \(\beta_k\): effect of a public investment shock at average corruption.
- \(\theta_k\): marginal effect of corruption on the investment multiplier.

Conditional impulse responses can be computed for:

- **low-corruption countries** (e.g. 25th percentile),
- **high-corruption countries** (e.g. 75th percentile).

Inference is conducted using **Driscoll–Kraay standard errors**, robust to serial and cross-sectional correlation.


### 6. Preview of Results (Qualitative)

The extended results suggest that **public investment is not equally effective across institutional environments**.

In particular:

- countries with **lower corruption** experience **larger and more persistent output responses**,
- countries with **higher corruption** exhibit **attenuated multipliers**, especially at medium horizons.

This finding does not contradict the original paper; rather, it qualifies its average result by highlighting meaningful heterogeneity.

*(Quantitative results and figures are presented in the next section.)*


### 7. Why This Matters for Policy

The results have direct policy implications:

- Increasing public investment alone may not be sufficient.
- **Institutional quality conditions the effectiveness of fiscal policy**.
- Complementary reforms targeting governance and transparency may amplify investment multipliers.

In the context of EU-wide investment initiatives, this suggests that **institutional capacity should be treated as a macroeconomic parameter**, not just a political constraint.


### 8. Conclusion

This article builds on recent evidence showing that public investment boosts economic activity in the European Union.

By replicating and extending the original analysis, it shows that:

- average public investment multipliers mask important cross-country heterogeneity,
- corruption weakens the transmission of public investment shocks.

Future research could explore:

- non-linearities,
- alternative institutional indicators,
- sector-specific public investment shocks.



### References

Heimberger, P., & Dabrowski, C. (2025). *Boosting the economy without raising the public debt ratio? The effects of public investment shocks in the European Union*. Applied Economics Letters.

Jordà, Ò. (2005). Estimation and inference of impulse responses by local projections. *American Economic Review*.
