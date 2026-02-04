title: "Public Investment Multipliers and Corruption: Does Institutional Quality Matter?"
subtitle: "Replication and Extension of Heimberger & Dabrowski (2025)"
author: "Nome Cognome"
date: "2026-XX-XX"


> *This article combines replication and methodological extension.  
> First, I replicate recent evidence on public investment multipliers in the EU.  
> Second, I ask whether the effectiveness of public investment depends on institutional quality, proxied by corruption.*


### 1. Motivation

In recent years, public investment has returned to the centre of the European policy debate. The need to close infrastructure gaps, support the green transition, and strengthen long-run growth has renewed interest in the macroeconomic effects of public investment, both among policymakers and in the academic literature.

A recent contribution by Heimberger and Dabrowski (2025) provides compelling evidence that public investment shocks boost output, reduce unemployment, and do not endanger public debt sustainability in the European Union. Their results are based on a transparent identification strategy and a modern local projection framework, and they contribute to a growing consensus that public investment may play a central role in stabilisation and growth policies.

At the same time, an important question remains largely unexplored. While average effects are informative, they may conceal substantial heterogeneity across countries. In particular, it is not obvious that public investment should be equally effective in all institutional environments.

This article therefore asks whether the macroeconomic impact of public investment differs systematically between countries with low and high levels of corruption.


### 2. The Original Paper: Idea and Identification Strategy

#### 2.1 Public Investment Shocks via Forecast Errors

The key idea in Heimberger and Dabrowski (2025) is to identify public investment shocks using forecast errors, defined as the difference between realised public investment and the corresponding ex-ante forecast.

```math
F_{i,t} = I^{\text{actual}}_{i,t} - I^{\text{forecast}}_{i,t}
```

Public investment is measured as general government gross fixed capital formation as a share of GDP. This identification strategy addresses two well-known challenges in the empirical analysis of fiscal policy. First, it mitigates the fiscal foresight problem, as economic agents may adjust their behaviour in anticipation of announced investment plans. Second, it alleviates concerns about endogeneity, since forecast errors are plausibly orthogonal to contemporaneous macroeconomic shocks.

By exploiting archive data from European Commission forecasts, the authors align the econometric information set with that of households and firms, strengthening the causal interpretation of the estimated impulse responses.


#### 2.2 Econometric Framework

The dynamic effects of public investment shocks are estimated using local projections following Jordà (2005). At each horizon \(k\), the baseline specification takes the form:

```math
y_{i,t+k} - y_{i,t-1}
=
\beta_k F_{i,t}
+ \sum_j \gamma_{k,j} Z_{i,t-j}
+ \delta_i^k
+ \theta_t^k
+ \varepsilon_{i,t}^k
```

The dependent variable captures the cumulative response of the outcome of interest, which includes real GDP, unemployment, private investment, and the public-debt-to-GDP ratio. The vector of controls accounts for standard macroeconomic dynamics, while country and time fixed effects absorb unobserved heterogeneity. Inference is conducted using Driscoll–Kraay standard errors to account for serial and cross-sectional dependence.

The original paper finds cumulative output multipliers above one, no evidence of crowding-out of private investment, and no deterioration in public debt dynamics.


### 3. Replication: Why It Matters

Before extending the analysis, I replicate the original results using the same empirical framework. Replication serves a dual purpose. First, it provides a validation of the original findings. Second, it establishes a clean benchmark against which the extended specification can be evaluated.

The replicated impulse-response functions closely match those reported in the original study, both in terms of magnitude and dynamic patterns, lending confidence to the subsequent analysis.


### 4. Baseline Results: Interpretation and Economic Context

This section briefly discusses the baseline results obtained from the replication, which form the empirical reference point for the analysis of institutional heterogeneity.


#### 4.1 Real GDP: Cumulative Investment Multiplier

![Real GDP: cumulative investment multiplier](gdp.png)

The response of real GDP to a public investment shock exhibits a clear and economically meaningful pattern. On impact, the output multiplier is approximately 0.6, indicating that public investment generates a sizable increase in economic activity, though not a one-to-one effect in the very short run. Over time, the multiplier rises steadily, exceeding unity after one year and stabilising around 1.2 to 1.3 after two to three years.

This gradual build-up is consistent with the idea that public investment operates through both demand-side channels in the short run and supply-side channels in the medium run, as improved infrastructure and public capital enhance productive capacity. The magnitude and persistence of the estimated multipliers are fully in line with the existing empirical literature on public investment.


#### 4.2 Private Investment: Complementarity Rather Than Crowding-Out

![Private investment ratio](private_investment.png)

Private investment responds positively to public investment shocks. The response peaks after one year and remains positive over the entire horizon, although uncertainty increases at longer horizons.

These dynamics suggest that public investment does not crowd out private capital formation. On the contrary, they are consistent with a crowding-in mechanism, whereby public investment raises the expected profitability of private projects, improves infrastructure, or reduces adjustment costs faced by firms.


#### 4.3 Public Debt: Debt Dynamics Remain Benign

![Public debt ratio](public_debt.png)

The response of the public-debt-to-GDP ratio is mildly negative in the first two years following the shock and returns close to zero thereafter. While the confidence bands are wide, there is no indication of a systematic increase in public debt.

This pattern suggests that the growth effects of public investment are sufficiently strong to offset its fiscal cost, at least over the medium run. In this sense, public investment appears broadly consistent with debt sustainability.


#### 4.4 Unemployment: Short-Run Labour Market Effects

![Unemployment rate](unemployment.png)

Unemployment declines following the public investment shock, reaching its maximum reduction after one to two years before gradually returning towards its pre-shock level. This response mirrors the dynamics of output and reflects higher labour demand as economic activity expands.

Although uncertainty increases at longer horizons, the short-run decline in unemployment is economically meaningful and reinforces the stabilising role of public investment.


#### 4.5 Summary of Baseline Findings

Taken together, the baseline results depict a coherent macroeconomic adjustment. Public investment raises output by more than one-for-one in the medium run, stimulates private investment, reduces unemployment, and does not lead to an increase in public debt. These findings confirm the effectiveness of public investment on average and provide a solid benchmark for the analysis of heterogeneity across institutional environments.


### 5. Research Question: Does Corruption Matter?

While the average effects of public investment are clearly positive, they may conceal substantial variation across countries. A natural candidate driving such heterogeneity is institutional quality, and in particular corruption.

Higher corruption may reduce the efficiency of public investment, increase leakages and rent-seeking, and weaken the transmission from public spending to real economic activity. This consideration motivates the central question of the article: whether the macroeconomic impact of public investment is systematically lower in more corrupt countries.


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

The corruption indicator is lagged and mean-centered, so that \(\beta_k\) captures the effect of public investment at average corruption levels, while \(\theta_k\) measures how this effect varies with institutional quality.


#### 6.2 Interpretation

This specification allows the investment multiplier to vary continuously with corruption. Conditional impulse responses can therefore be computed for countries with different levels of institutional quality, making it possible to assess whether corruption systematically attenuates the effectiveness of public investment.


### 7. Conclusion

This article shows that public investment is highly effective on average, but its macroeconomic impact may depend crucially on institutional quality. Understanding this heterogeneity is essential for the design of public investment strategies that maximise growth and employment gains, particularly in the context of large-scale investment programmes in the European Union.


### References

Heimberger, P., & Dabrowski, C. (2025). *Boosting the economy without raising the public debt ratio? The effects of public investment shocks in the European Union*. Applied Economics Letters.

Jordà, Ò. (2005). Estimation and inference of impulse responses by local projections. *American Economic Review*.
