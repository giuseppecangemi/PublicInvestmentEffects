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


### 4. Baseline Results: Interpretation and Economic Context

Before turning to the role of corruption, it is useful to discuss the baseline results obtained from the replication. These results provide the empirical benchmark against which the extended specification with institutional heterogeneity is evaluated.


#### 4.1 Real GDP: Cumulative Investment Multiplier

![Real GDP: cumulative investment multiplier](gdp.png)

The first panel reports the cumulative response of real GDP to a one percentage point of GDP public investment shock.

On impact, the estimated output multiplier is approximately 0.6, indicating that public investment generates a sizable but initially incomplete increase in aggregate output. Over time, the multiplier rises steadily, exceeding unity after one year and stabilizing around 1.2–1.3 after two to three years.

This dynamic pattern is consistent with the presence of both short-run demand effects and medium-run supply-side effects, such as improved infrastructure and higher productive capacity. The magnitude and persistence of the multiplier are fully in line with the empirical literature on public investment multipliers.


#### 4.2 Private Investment: Absence of Crowding-Out

![Private investment ratio](private_investment.png)

The response of private investment is positive on impact and peaks after one year, before gradually declining while remaining positive over the entire horizon.

These results provide no evidence of crowding-out effects. Instead, they suggest a crowding-in mechanism, whereby public investment stimulates complementary private investment, possibly through improved infrastructure, higher expected demand, or lower adjustment costs for firms.


#### 4.3 Public Debt: No Deterioration in Debt Sustainability

![Public debt ratio](public_debt.png)

The response of the public-debt-to-GDP ratio is mildly negative in the first two years following the shock and returns close to zero thereafter. Although uncertainty bands are wide, there is no indication of a systematic increase in public debt.

This suggests that the output gains generated by public investment are sufficiently strong to offset the initial fiscal cost, mitigating concerns about debt sustainability.


#### 4.4 Unemployment: Short-Run Labor Market Effects

![Unemployment rate](unemployment.png)

Unemployment declines on impact and reaches its maximum reduction after one to two years, before gradually returning towards zero.

This pattern mirrors the dynamics of output and reflects increased labor demand as economic activity expands following the investment shock.


#### 4.5 Summary of Baseline Findings

Taken together, the baseline results indicate that:

- public investment multipliers exceed one in the medium run,
- private investment is crowded in rather than crowded out,
- public debt does not deteriorate,
- unemployment declines in the short to medium run.

These findings provide a solid benchmark and motivate the analysis of heterogeneity across institutional environments.


### 5. Research Question: Does Corruption Matter?

While average effects are informative, fiscal multipliers may vary across countries.

A natural candidate driving heterogeneity is **institutional quality**, and in particular **corruption**.

From an economic perspective, higher corruption may reduce investment efficiency, increase leakages and rent-seeking, and weaken the transmission from public spending to real activity.

This leads to the central question of this article:

> **Is the macroeconomic impact of public investment lower in more corrupt countries?**


### 6. Methodological Extension: Introducing Corruption Interactions

#### 6.1 Extended Specification

To address this question, I extend the baseline local projection framework by allowing the public investment shock to interact with lagged corruption.

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

where \(\text{Corr}_{i,t-1}\) is a lagged corruption indicator. Corruption is mean-centered so that \(\beta_k\) captures the effect at average corruption levels.


#### 6.2 Interpretation

The coefficient \(\beta_k\) measures the effect of a public investment shock at average corruption levels, while \(\theta_k\) captures how this effect varies with institutional quality.

Conditional impulse responses can therefore be computed for low- and high-corruption countries.


### 7. Conclusion

This article shows that while public investment is highly effective on average, its macroeconomic impact may depend crucially on institutional quality.

Understanding this heterogeneity is essential for the design of effective public investment strategies and for maximizing the growth and employment benefits of fiscal policy.


### References

Heimberger, P., & Dabrowski, C. (2025). *Boosting the economy without raising the public debt ratio? The effects of public investment shocks in the European Union*. Applied Economics Letters.

Jordà, Ò. (2005). Estimation and inference of impulse responses by local projections. *American Economic Review*.
