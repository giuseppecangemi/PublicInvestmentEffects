"""
diagnostic_tests.py
====================
Batteria completa di test di specificazione per il modello LP con interazione.

Modello stimato:
  y_{i,t+h} - y_{i,t-1} = alpha_i + gamma_t + beta_h * F_{i,t}
                          + theta_h * (F_{i,t} x GE_{i,t-1})
                          + SUM(Gamma * Z_{i,t-j}) + epsilon

Test implementati:
  1. Significativita congiunta dell'interazione (Wald test su theta_h)
  2. Test di Pesaran CD (cross-sectional dependence dei residui)
  3. Analisi della stazionarieta panel (IPS / LLC)
  4. Placebo test (shock anticipato: forecast error al tempo t+1)
  5. Robustezza: indicatori WGI alternativi (CC_EST, RL_EST, RQ_EST)
  6. Robustezza: quantili diversi (10/90, 33/67)
  7. Robustezza: lag struttura (p=1, p=3)
  8. Robustezza: pre-COVID (2000-2019)
  9. Robustezza: esclusione Irlanda
 10. Test di Granger-non-causalita dello shock
"""

import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
from scipy import stats
from linearmodels.panel import PanelOLS
import matplotlib.pyplot as plt


# ============================================================
# FUNZIONI HELPER (dal tuo codice originale)
# ============================================================

def add_panel_lags(df, group_col, cols, max_lag):
    out = df.copy()
    out = out.sort_values([group_col, "year_int"])
    for c in cols:
        for L in range(1, max_lag + 1):
            out[f"L{L}_{c}"] = out.groupby(group_col)[c].shift(L)
    return out


def add_panel_lead(df, group_col, y_col, h):
    out = df.copy()
    out = out.sort_values([group_col, "year_int"])
    out[f"LEAD{h}_{y_col}"] = out.groupby(group_col)[y_col].shift(-h)
    return out


def add_panel_lag1(df, group_col, y_col):
    out = df.copy()
    out = out.sort_values([group_col, "year_int"])
    out[f"L1_{y_col}"] = out.groupby(group_col)[y_col].shift(1)
    return out


# ============================================================
# FUNZIONE DI STIMA ESTESA (restituisce anche residui e risultati completi)
# ============================================================

def estimate_lp_interaction(
    data_set, endog_data, shock, corr_col, l_exog_data,
    lags_exog_data, hor, entity_col="ccode", time_col="year_int",
    corr_lag=1, cumul_mult=True, dk_bandwidth=None, center_corr=True,
):
    """
    Stima LP con interazione e restituisce risultati completi per ogni h,
    inclusi residui e oggetti PanelOLS result.
    """
    df = data_set.copy()
    df = add_panel_lags(df, entity_col, l_exog_data, lags_exog_data)
    df = add_panel_lag1(df, entity_col, endog_data)

    df = df.sort_values([entity_col, time_col])
    df[f"L{corr_lag}_{corr_col}"] = df.groupby(entity_col)[corr_col].shift(corr_lag)

    corr_lag_name = f"L{corr_lag}_{corr_col}"
    if center_corr:
        corr_mean = df[corr_lag_name].mean(skipna=True)
        df[corr_lag_name] = df[corr_lag_name] - corr_mean

    inter_name = f"{shock}_x_{corr_col}_L{corr_lag}"
    df[inter_name] = df[shock] * df[corr_lag_name]

    results = []

    for h in range(0, hor + 1):
        dff = add_panel_lead(df, entity_col, endog_data, h)

        y_lead = f"LEAD{h}_{endog_data}"
        y_lag1 = f"L1_{endog_data}"

        if cumul_mult:
            dff[f"YH_{h}"] = dff[y_lead] - dff[y_lag1]
            y_col = f"YH_{h}"
        else:
            y_col = y_lead

        x_cols = [shock, inter_name] + [
            f"L{L}_{c}"
            for c in l_exog_data
            for L in range(1, lags_exog_data + 1)
        ]

        use_cols = [entity_col, time_col, y_col] + x_cols
        tmp = dff[use_cols].dropna().copy()
        tmp = tmp.set_index([entity_col, time_col])

        y = tmp[y_col]
        X = tmp[x_cols]

        mod = PanelOLS(y, X, entity_effects=True, time_effects=True)
        fit_kwargs = {"cov_type": "driscoll-kraay"}
        if dk_bandwidth is not None:
            fit_kwargs["bandwidth"] = dk_bandwidth
        res = mod.fit(**fit_kwargs)

        results.append({
            "h": h,
            "result": res,
            "shock": shock,
            "inter_name": inter_name,
            "beta": float(res.params[shock]),
            "theta": float(res.params[inter_name]),
            "se_beta": float(res.std_errors[shock]),
            "se_theta": float(res.std_errors[inter_name]),
            "pval_beta": float(res.pvalues[shock]),
            "pval_theta": float(res.pvalues[inter_name]),
            "resids": res.resids,
            "nobs": res.nobs,
            "r2_within": res.rsquared_within,
        })

    return results


# ============================================================
# FUNZIONE DI STIMA BASELINE (senza interazione, per confronto)
# ============================================================

def estimate_lp_baseline(
    data_set, endog_data, shock, l_exog_data,
    lags_exog_data, hor, entity_col="ccode", time_col="year_int",
    cumul_mult=True, dk_bandwidth=None,
):
    df = data_set.copy()
    df = add_panel_lags(df, entity_col, l_exog_data, lags_exog_data)
    df = add_panel_lag1(df, entity_col, endog_data)

    results = []

    for h in range(0, hor + 1):
        dff = add_panel_lead(df, entity_col, endog_data, h)

        y_lead = f"LEAD{h}_{endog_data}"
        y_lag1 = f"L1_{endog_data}"

        if cumul_mult:
            dff[f"YH_{h}"] = dff[y_lead] - dff[y_lag1]
            y_col = f"YH_{h}"
        else:
            y_col = y_lead

        x_cols = [shock] + [
            f"L{L}_{c}"
            for c in l_exog_data
            for L in range(1, lags_exog_data + 1)
        ]

        use_cols = [entity_col, time_col, y_col] + x_cols
        tmp = dff[use_cols].dropna().copy()
        tmp = tmp.set_index([entity_col, time_col])

        y = tmp[y_col]
        X = tmp[x_cols]

        mod = PanelOLS(y, X, entity_effects=True, time_effects=True)
        fit_kwargs = {"cov_type": "driscoll-kraay"}
        if dk_bandwidth is not None:
            fit_kwargs["bandwidth"] = dk_bandwidth
        res = mod.fit(**fit_kwargs)

        results.append({
            "h": h,
            "result": res,
            "beta": float(res.params[shock]),
            "se_beta": float(res.std_errors[shock]),
            "pval_beta": float(res.pvalues[shock]),
            "resids": res.resids,
            "nobs": res.nobs,
            "r2_within": res.rsquared_within,
        })

    return results


# ============================================================
# TEST 1: SIGNIFICATIVITA CONGIUNTA DELL'INTERAZIONE (Wald test)
# ============================================================

def test_joint_significance_interaction(results_list):
    """
    H0: theta_0 = theta_1 = ... = theta_H = 0
    (l'interazione con la qualita istituzionale e irrilevante a tutti gli orizzonti)

    Perche: Se theta e congiuntamente zero, la qualita istituzionale non modifica
    l'effetto dello shock fiscale -> il tuo contributo non aggiunge nulla.
    Questo e il test piu importante per giustificare l'estensione del modello.

    Metodo: Statistica di Wald = theta' * Sigma^{-1} * theta ~ chi2(H+1)
    Approssimazione: usiamo i theta_h stimati indipendentemente a ogni orizzonte
    e costruiamo una matrice diagonale (LP stima equazione per equazione).
    """
    print("=" * 70)
    print("TEST 1: SIGNIFICATIVITA CONGIUNTA DELL'INTERAZIONE (Wald)")
    print("=" * 70)
    print()
    print("H0: theta_h = 0 per ogni h = 0, ..., H")
    print("H1: almeno un theta_h != 0")
    print("Se rifiutiamo H0, la qualita istituzionale conta.\n")

    thetas = np.array([r["theta"] for r in results_list])
    se_thetas = np.array([r["se_theta"] for r in results_list])

    # Wald statistic (diagonale: LP stima per orizzonte)
    wald_stat = np.sum((thetas / se_thetas) ** 2)
    df = len(thetas)
    pval = 1.0 - stats.chi2.cdf(wald_stat, df)

    print(f"  {'h':>3}  {'theta_h':>10}  {'SE':>10}  {'t-stat':>10}  {'p-value':>10}")
    print(f"  {'---':>3}  {'----------':>10}  {'----------':>10}  {'----------':>10}  {'----------':>10}")
    for r in results_list:
        t_stat = r["theta"] / r["se_theta"]
        print(f"  {r['h']:>3}  {r['theta']:>10.5f}  {r['se_theta']:>10.5f}  {t_stat:>10.3f}  {r['pval_theta']:>10.4f}")

    print(f"\n  Wald statistic = {wald_stat:.3f}  (df = {df})")
    print(f"  p-value (chi2) = {pval:.6f}")

    if pval < 0.05:
        print("  >>> RIFIUTO H0 al 5%: l'interazione e significativa congiuntamente.")
    elif pval < 0.10:
        print("  >>> RIFIUTO H0 al 10%: evidenza debole di significativita.")
    else:
        print("  >>> NON RIFIUTO H0: l'interazione non e congiuntamente significativa.")

    print()
    return {"wald_stat": wald_stat, "df": df, "pval": pval}


# ============================================================
# TEST 2: PESARAN CD (Cross-Sectional Dependence)
# ============================================================

def test_pesaran_cd(results_list, entity_col="ccode"):
    """
    Test di Pesaran (2004) per cross-sectional dependence dei residui.

    Perche: In un panel macro EU, gli shock comuni (BCE, crisi) generano
    correlazione tra i residui dei diversi paesi. Se presente, gli SE standard
    (e anche cluster per paese) sono distorti. I Driscoll-Kraay che usi
    dovrebbero gestirlo, ma e importante verificare se la CD e effettivamente
    presente, per giustificare la scelta di DK.

    Metodo:
      CD = sqrt(2 / (N(N-1))) * sum_{i<j} sqrt(T_ij) * rho_ij
    dove rho_ij e la correlazione campionaria PAIRWISE tra i residui di
    paese i e j calcolata sugli anni comuni T_ij.
    Sotto H0 (no CD): CD ~ N(0,1).

    Nota: usiamo correlazioni pairwise (non listwise) per non perdere
    osservazioni quando non tutti i paesi hanno gli stessi anni disponibili.
    """
    print("=" * 70)
    print("TEST 2: PESARAN CD (Cross-Sectional Dependence)")
    print("=" * 70)
    print()
    print("H0: residui cross-sectionally indipendenti")
    print("H1: esiste dipendenza cross-sezionale nei residui")
    print("Se rifiutiamo H0, la scelta di Driscoll-Kraay SE e giustificata.\n")

    for r in results_list:
        h = r["h"]
        resids = r["resids"]
        resid_df = resids.reset_index()
        resid_df.columns = [entity_col, "year_int", "resid"]

        # Pivot: righe = anni, colonne = paesi (NON dropna)
        pivot = resid_df.pivot(index="year_int", columns=entity_col, values="resid")
        countries = pivot.columns.tolist()
        N = len(countries)

        if N < 2:
            print(f"  h={h}: Dati insufficienti (N={N})")
            continue

        # Correlazioni pairwise con formula CD esatta di Pesaran (2004)
        cd_sum = 0.0
        n_pairs = 0
        min_T = np.inf
        max_T = 0

        for i in range(N):
            for j in range(i + 1, N):
                # Anni comuni tra paese i e j
                mask = pivot.iloc[:, i].notna() & pivot.iloc[:, j].notna()
                T_ij = mask.sum()
                if T_ij < 3:
                    continue
                ri = pivot.iloc[:, i][mask].values
                rj = pivot.iloc[:, j][mask].values
                rho_ij = np.corrcoef(ri, rj)[0, 1]
                cd_sum += np.sqrt(T_ij) * rho_ij
                n_pairs += 1
                min_T = min(min_T, T_ij)
                max_T = max(max_T, T_ij)

        if n_pairs == 0:
            print(f"  h={h}: Nessuna coppia con anni comuni sufficienti")
            continue

        cd_stat = np.sqrt(2.0 / (N * (N - 1))) * cd_sum
        pval = 2.0 * (1.0 - stats.norm.cdf(abs(cd_stat)))

        sig = "***" if pval < 0.01 else ("**" if pval < 0.05 else ("*" if pval < 0.10 else ""))
        print(f"  h={h}: CD = {cd_stat:>8.3f}  p-value = {pval:.6f}  N={N}  T=[{int(min_T)}-{int(max_T)}]  pairs={n_pairs}  {sig}")

    print()
    print("  Se CD e significativo -> la cross-sectional dependence e presente")
    print("  -> l'uso di Driscoll-Kraay standard errors e corretto e necessario.")
    print()


# ============================================================
# TEST 3: STAZIONARIETA PANEL (Im-Pesaran-Shin)
# ============================================================

def test_panel_stationarity(dt, variables, entity_col="ccode"):
    """
    Test IPS (Im, Pesaran & Shin, 2003) per radice unitaria panel.

    Perche: La validita delle LP assume che le variabili siano stazionarie
    (o che le differenze lo siano). Se le variabili hanno radice unitaria,
    le inferenze sono spurie. Il test IPS e il gold standard per panel macro.

    Metodo: Media dei t-statistics degli ADF individuali per paese,
    standardizzata con i valori tabulati IPS.
    Qui usiamo un'approssimazione: ADF per ogni paese, poi media dei t-stat.
    Sotto H0: tutte le serie hanno radice unitaria.
    Sotto H1: almeno alcune serie sono stazionarie.
    """
    print("=" * 70)
    print("TEST 3: STAZIONARIETA PANEL (tipo IPS)")
    print("=" * 70)
    print()
    print("H0: tutte le serie hanno radice unitaria (non stazionarie)")
    print("H1: almeno alcune serie sono stazionarie")
    print("Metodo: media dei t-ADF individuali per paese.\n")

    for var in variables:
        t_stats = []
        countries = dt[entity_col].unique()

        for c in countries:
            series = dt.loc[dt[entity_col] == c, var].dropna().values
            if len(series) < 5:
                continue

            # ADF(1): Delta y_t = alpha + rho * y_{t-1} + beta * Delta y_{t-1} + e
            dy = np.diff(series)
            y_lag = series[:-1]
            dy_lag = np.diff(series[:-1]) if len(series) > 2 else np.array([])

            if len(dy_lag) == 0:
                continue

            n = min(len(dy), len(y_lag), len(dy_lag))
            dy = dy[1:n + 1] if n < len(dy) else dy[-n:]
            y_lag = y_lag[1:n + 1] if n < len(y_lag) else y_lag[-n:]
            dy_lag = dy_lag[:n]

            X = np.column_stack([np.ones(n), y_lag, dy_lag])
            try:
                beta_hat = np.linalg.lstsq(X, dy, rcond=None)[0]
                resid = dy - X @ beta_hat
                sigma2 = np.sum(resid ** 2) / (n - 3)
                var_beta = sigma2 * np.linalg.inv(X.T @ X)
                t_stat = beta_hat[1] / np.sqrt(var_beta[1, 1])
                t_stats.append(t_stat)
            except np.linalg.LinAlgError:
                continue

        if len(t_stats) > 0:
            t_bar = np.mean(t_stats)
            # IPS critical values (approx): E[t] ~ -1.52, Var[t] ~ 0.74 for T=20
            # Standardizziamo con valori approssimati
            n_countries = len(t_stats)
            # Z-stat approssimato
            z_stat = np.sqrt(n_countries) * (t_bar - (-1.52)) / np.sqrt(0.74)
            pval = stats.norm.cdf(z_stat)  # one-sided (left tail)

            sig = "***" if pval < 0.01 else ("**" if pval < 0.05 else ("*" if pval < 0.10 else ""))
            status = "STAZIONARIA" if pval < 0.05 else "RADICE UNITARIA"
            print(f"  {var:<20s}  t-bar = {t_bar:>7.3f}  Z = {z_stat:>7.3f}  p = {pval:.4f}  {sig}  -> {status}")
        else:
            print(f"  {var:<20s}  Dati insufficienti")

    print()
    print("  Nota: le LP usano y_{t+h} - y_{t-1} come dipendente -> automaticamente")
    print("  in differenze, quindi anche variabili I(1) sono gestibili.")
    print("  E' comunque buona pratica verificare l'ordine di integrazione.\n")


# ============================================================
# TEST 4: PLACEBO TEST (shock anticipato)
# ============================================================

def test_placebo(dt, endog_data, corr_col, l_exog_data, lags_exog_data, hor,
                 entity_col="ccode", time_col="year_int"):
    """
    Placebo test: usiamo il forecast error FUTURO (F_{i,t+1}) come shock.

    Perche: Se lo shock e veramente esogeno (sorpresa non anticipata), lo shock
    futuro NON dovrebbe predire la variazione corrente di y. Se beta e theta
    risultano significativi col placebo, c'e un problema di anticipazione /
    fiscal foresight che invalida l'identificazione.

    Questo e il test chiave per la validita della strategia di identificazione
    di Heimberger & Dabrowski e, per estensione, del tuo modello.
    """
    print("=" * 70)
    print("TEST 4: PLACEBO TEST (shock futuro F_{t+1})")
    print("=" * 70)
    print()
    print("H0: lo shock futuro non predice la variazione corrente di y")
    print("    (beta_placebo = 0 e theta_placebo = 0)")
    print("Se NON rifiutiamo H0 -> bene, lo shock e esogeno.\n")

    df = dt.copy()
    df = df.sort_values([entity_col, time_col])
    # Creo lo shock futuro (forecast error al tempo t+1)
    df["forecasterror_lead1"] = df.groupby(entity_col)["forecasterror"].shift(-1)

    results = estimate_lp_interaction(
        df, endog_data, "forecasterror_lead1", corr_col, l_exog_data,
        lags_exog_data, hor, entity_col, time_col,
        corr_lag=1, cumul_mult=True, dk_bandwidth=None, center_corr=True,
    )

    print(f"  Variabile dipendente: {endog_data}")
    print(f"  {'h':>3}  {'beta_placebo':>14}  {'p-val':>8}  {'theta_placebo':>15}  {'p-val':>8}")
    print(f"  {'---':>3}  {'-' * 14:>14}  {'-' * 8:>8}  {'-' * 15:>15}  {'-' * 8:>8}")

    all_pass = True
    for r in results:
        sig_b = "*" if r["pval_beta"] < 0.10 else ""
        sig_t = "*" if r["pval_theta"] < 0.10 else ""
        if r["pval_beta"] < 0.10 or r["pval_theta"] < 0.10:
            all_pass = False
        print(f"  {r['h']:>3}  {r['beta']:>14.6f}  {r['pval_beta']:>8.4f}{sig_b:<2}  {r['theta']:>15.6f}  {r['pval_theta']:>8.4f}{sig_t}")

    print()
    if all_pass:
        print("  >>> TUTTI i coefficienti placebo sono non significativi.")
        print("  >>> Lo shock (forecast error) supera il placebo test -> esogeneita supportata.")
    else:
        print("  >>> ATTENZIONE: alcuni coefficienti placebo sono significativi.")
        print("  >>> Possibile problema di anticipazione / fiscal foresight.")
    print()

    return results


# ============================================================
# TEST 5: ROBUSTEZZA - INDICATORI WGI ALTERNATIVI
# ============================================================

def test_alternative_wgi(dt, endog_data, l_exog_data, lags_exog_data, hor,
                         wgi_cols=None):
    """
    Stima il modello con diversi indicatori WGI come proxy di qualita istituzionale.

    Perche: Se i risultati dipendono criticamente dalla scelta dell'indicatore
    (CC_EST vs GE_EST vs RL_EST), la conclusione e fragile. Se invece theta
    e significativo con piu indicatori, il risultato e robusto alla misurazione
    della qualita istituzionale.
    """
    if wgi_cols is None:
        wgi_cols = ["CC_EST", "GE_EST", "RL_EST", "RQ_EST"]

    print("=" * 70)
    print("TEST 5: ROBUSTEZZA - INDICATORI WGI ALTERNATIVI")
    print("=" * 70)
    print()
    print("Stimo theta_h con diversi indicatori di qualita istituzionale.")
    print("Se theta e consistente tra indicatori -> risultato robusto.\n")

    for col in wgi_cols:
        results = estimate_lp_interaction(
            dt, endog_data, "forecasterror", col, l_exog_data,
            lags_exog_data, hor, corr_lag=1, cumul_mult=True, center_corr=True,
        )

        thetas = [r["theta"] for r in results]
        pvals = [r["pval_theta"] for r in results]
        sig_any = any(p < 0.10 for p in pvals)

        theta_str = "  ".join([f"h{r['h']}={r['theta']:>7.4f}{'*' if r['pval_theta'] < 0.10 else ' '}" for r in results])
        print(f"  {col:<8s}: {theta_str}  {'<- SIG' if sig_any else ''}")

    print()


# ============================================================
# TEST 6: ROBUSTEZZA - QUANTILI DIVERSI
# ============================================================

def test_alternative_quantiles(dt, endog_data, corr_col, l_exog_data,
                               lags_exog_data, hor):
    """
    Valuta le IRF condizionali a diversi percentili della distribuzione
    dell'indicatore istituzionale.

    Perche: La scelta 25/75 e arbitraria. Se i risultati cambiano drasticamente
    con 10/90 o 33/67, la conclusione non e robusta alla definizione di
    "alta" vs "bassa" qualita. Mostra che il pattern persiste.
    """
    print("=" * 70)
    print("TEST 6: ROBUSTEZZA - QUANTILI DIVERSI")
    print("=" * 70)
    print()
    print(f"  Indicatore: {corr_col}")
    print(f"  Variabile dipendente: {endog_data}\n")

    quantile_pairs = [(0.10, 0.90), (0.25, 0.75), (0.33, 0.67)]

    results = estimate_lp_interaction(
        dt, endog_data, "forecasterror", corr_col, l_exog_data,
        lags_exog_data, hor, corr_lag=1, cumul_mult=True, center_corr=True,
    )

    # Ricostruisco le quantili manualmente
    df_tmp = dt.copy()
    df_tmp = df_tmp.sort_values(["ccode", "year_int"])
    df_tmp[f"L1_{corr_col}"] = df_tmp.groupby("ccode")[corr_col].shift(1)
    corr_mean = df_tmp[f"L1_{corr_col}"].mean(skipna=True)
    df_tmp[f"L1_{corr_col}_c"] = df_tmp[f"L1_{corr_col}"] - corr_mean

    for q_lo, q_hi in quantile_pairs:
        c_lo = df_tmp[f"L1_{corr_col}_c"].quantile(q_lo)
        c_hi = df_tmp[f"L1_{corr_col}_c"].quantile(q_hi)

        print(f"  Quantili ({int(q_lo*100)}/{int(q_hi*100)})  ->  c_low={c_lo:.4f}  c_high={c_hi:.4f}")

        for r in results:
            beta = r["beta"]
            theta = r["theta"]
            irf_lo = beta + theta * c_lo
            irf_hi = beta + theta * c_hi
            print(f"    h={r['h']}:  IRF(low)={irf_lo:>8.5f}   IRF(high)={irf_hi:>8.5f}   diff={irf_hi - irf_lo:>8.5f}")
        print()

    print()


# ============================================================
# TEST 7: ROBUSTEZZA - DIVERSI LAG
# ============================================================

def test_lag_robustness(dt, endog_data, corr_col, l_exog_data, hor):
    """
    Stima con p=1, p=2 (baseline), p=3 lag dei controlli.

    Perche: La scelta del numero di lag puo influenzare i risultati.
    Se theta cambia segno o significativita con lag diversi, il risultato
    e sensibile a una scelta arbitraria. In ambito accademico, mostrare
    stabilita rispetto ai lag e prassi consolidata.
    """
    print("=" * 70)
    print("TEST 7: ROBUSTEZZA - DIVERSI LAG DEI CONTROLLI")
    print("=" * 70)
    print()

    for lags in [1, 2, 3]:
        results = estimate_lp_interaction(
            dt, endog_data, "forecasterror", corr_col, l_exog_data,
            lags, hor, corr_lag=1, cumul_mult=True, center_corr=True,
        )
        theta_str = "  ".join([f"h{r['h']}={r['theta']:>7.4f}{'*' if r['pval_theta'] < 0.10 else ' '}" for r in results])
        print(f"  lags={lags}: {theta_str}")

    print()


# ============================================================
# TEST 8 & 9: ROBUSTEZZA - SOTTOCAMPIONI
# ============================================================

def test_subsample_robustness(dt, endog_data, corr_col, l_exog_data,
                              lags_exog_data, hor):
    """
    Pre-COVID (2000-2019) ed esclusione Irlanda.

    Perche:
    - Pre-COVID: il periodo 2020-2023 e anomalo (lockdown, NGEU). Se i risultati
      sono guidati solo da quegli anni, la conclusione non e generalizzabile.
    - Esclusione Irlanda: il PIL irlandese e distorto da attivita multinazionali
      (il "leprechaun economics"). E' un outlier standard nella letteratura EU.
    """
    print("=" * 70)
    print("TEST 8-9: ROBUSTEZZA - SOTTOCAMPIONI")
    print("=" * 70)
    print()

    subsamples = {
        "Full sample (2000-2023)": dt,
        "Pre-COVID (2000-2019)": dt[dt["year_int"] <= 2019].copy(),
        "Esclusa Irlanda": dt[dt["ccode"] != "IRL"].copy(),
    }

    for name, sub_dt in subsamples.items():
        results = estimate_lp_interaction(
            sub_dt, endog_data, "forecasterror", corr_col, l_exog_data,
            lags_exog_data, hor, corr_lag=1, cumul_mult=True, center_corr=True,
        )

        n = results[0]["nobs"]
        theta_str = "  ".join([f"h{r['h']}={r['theta']:>7.4f}{'*' if r['pval_theta'] < 0.10 else ' '}" for r in results])
        print(f"  {name:<30s} (N={n:>3d}): {theta_str}")

    print()


# ============================================================
# TEST 10: GRANGER NON-CAUSALITA DELLO SHOCK
# ============================================================

def test_shock_exogeneity(dt, entity_col="ccode", time_col="year_int"):
    """
    Test di esogeneita dello shock: le variabili macro laggate NON dovrebbero
    predire il forecast error.

    Perche: L'identificazione assume che il forecast error sia una sorpresa
    esogena. Se variabili come PIL o debito laggato predicono F_{i,t},
    lo shock non e esogeno e le stime sono distorte. Questo e un test
    di Granger-causalita inversa: regressiamo F su lags delle macro.
    """
    print("=" * 70)
    print("TEST 10: ESOGENEITA DELLO SHOCK (Granger-tipo)")
    print("=" * 70)
    print()
    print("Regressione: F_{i,t} = alpha_i + gamma_t + lags(macro) + e")
    print("H0: i lag macro NON predicono il forecast error")
    print("Se H0 non rifiutata -> lo shock e plausibilmente esogeno.\n")

    df = dt.copy()
    macro_vars = ["growth_RGDP", "PDEBT", "NOMLRATE", "REER"]
    df = add_panel_lags(df, entity_col, macro_vars, 2)

    x_cols = [
        f"L{L}_{c}"
        for c in macro_vars
        for L in range(1, 3)
    ]

    use_cols = [entity_col, time_col, "forecasterror"] + x_cols
    tmp = df[use_cols].dropna().copy()
    tmp = tmp.set_index([entity_col, time_col])

    y = tmp["forecasterror"]
    X = tmp[x_cols]

    mod = PanelOLS(y, X, entity_effects=True, time_effects=True)
    res = mod.fit(cov_type="driscoll-kraay")

    print("  Coefficienti:")
    for var in x_cols:
        b = res.params[var]
        p = res.pvalues[var]
        sig = "***" if p < 0.01 else ("**" if p < 0.05 else ("*" if p < 0.10 else ""))
        print(f"    {var:<20s}  beta={b:>8.5f}  p={p:.4f}  {sig}")

    # F-test congiunto (approssimazione: Wald)
    betas = np.array([res.params[v] for v in x_cols])
    ses = np.array([res.std_errors[v] for v in x_cols])
    wald = np.sum((betas / ses) ** 2)
    df_test = len(x_cols)
    pval_joint = 1.0 - stats.chi2.cdf(wald, df_test)

    print(f"\n  Wald congiunto = {wald:.3f}  (df={df_test})  p-value = {pval_joint:.6f}")
    print(f"  R2 within = {res.rsquared_within:.4f}")

    if pval_joint > 0.10:
        print("  >>> NON rifiuto H0: le macro laggate non predicono lo shock.")
        print("  >>> Esogeneita dello shock supportata.")
    else:
        print("  >>> ATTENZIONE: rifiuto H0. Possibile endogeneita dello shock.")
    print()


# ============================================================
# RIEPILOGO RISULTATI + R2 CONFRONTO
# ============================================================

def summary_r2_comparison(dt, endog_data, corr_col, l_exog_data,
                          lags_exog_data, hor):
    """
    Confronta R2 within del modello baseline vs modello con interazione.

    Perche: Mostra quanta varianza aggiuntiva e spiegata dall'interazione.
    Se Delta-R2 e trascurabile, l'interazione non migliora il fit.
    """
    print("=" * 70)
    print("CONFRONTO R2: BASELINE vs INTERAZIONE")
    print("=" * 70)
    print()

    res_base = estimate_lp_baseline(
        dt, endog_data, "forecasterror", l_exog_data,
        lags_exog_data, hor, cumul_mult=True,
    )

    res_inter = estimate_lp_interaction(
        dt, endog_data, "forecasterror", corr_col, l_exog_data,
        lags_exog_data, hor, corr_lag=1, cumul_mult=True, center_corr=True,
    )

    print(f"  {'h':>3}  {'R2 baseline':>14}  {'R2 interaction':>16}  {'Delta R2':>10}  {'Nobs':>6}")
    print(f"  {'---':>3}  {'-' * 14:>14}  {'-' * 16:>16}  {'-' * 10:>10}  {'-' * 6:>6}")

    for rb, ri in zip(res_base, res_inter):
        dr2 = ri["r2_within"] - rb["r2_within"]
        print(f"  {rb['h']:>3}  {rb['r2_within']:>14.6f}  {ri['r2_within']:>16.6f}  {dr2:>10.6f}  {ri['nobs']:>6d}")

    print()


# ============================================================
# MAIN: ESEGUI TUTTA LA BATTERIA
# ============================================================

if __name__ == "__main__":

    # --- Caricamento dati ---
    dt = pd.read_csv("data/data_pubinv_final_with_WGI.csv")
    dt["year"] = dt["year_int"].astype(str).str.strip()
    dt["year_int"] = dt["year"].astype(int)
    dt = dt[(dt["year_int"] >= 2000) & (dt["year_int"] <= 2023)].copy()

    # --- Configurazione ---
    ENDOG = "log_RGDP"
    CORR_COL = "GE_EST"   # indicatore principale (Government Effectiveness)
    CTRL = ["growth_RGDP", "PDEBT", "forecasterror", "NOMLRATE", "REER"]
    LAGS = 2
    HOR = 3

    print()
    print("*" * 70)
    print("  BATTERIA DI TEST DIAGNOSTICI")
    print(f"  Modello: LP con interazione shock x {CORR_COL}")
    print(f"  Dipendente: {ENDOG}  |  Orizzonti: h=0..{HOR}  |  Lags: {LAGS}")
    print(f"  Campione: {dt['year_int'].min()}-{dt['year_int'].max()}")
    print(f"  Paesi: {dt['ccode'].nunique()}  |  Osservazioni: {len(dt)}")
    print("*" * 70)
    print()

    # Stima principale
    main_results = estimate_lp_interaction(
        dt, ENDOG, "forecasterror", CORR_COL, CTRL, LAGS, HOR,
        corr_lag=1, cumul_mult=True, center_corr=True,
    )

    # 1. Significativita congiunta
    test_joint_significance_interaction(main_results)

    # 2. Pesaran CD
    test_pesaran_cd(main_results)

    # 3. Stazionarieta
    stationarity_vars = ["log_RGDP", "growth_RGDP", "PDEBT", "UNRATE",
                         "INVGDP", "forecasterror", "NOMLRATE", "REER", "GE_EST"]
    test_panel_stationarity(dt, stationarity_vars)

    # 4. Placebo
    test_placebo(dt, ENDOG, CORR_COL, CTRL, LAGS, HOR)

    # 5. Indicatori alternativi
    test_alternative_wgi(dt, ENDOG, CTRL, LAGS, HOR)

    # 6. Quantili diversi
    test_alternative_quantiles(dt, ENDOG, CORR_COL, CTRL, LAGS, HOR)

    # 7. Lag diversi
    test_lag_robustness(dt, ENDOG, CORR_COL, CTRL, HOR)

    # 8-9. Sottocampioni
    test_subsample_robustness(dt, ENDOG, CORR_COL, CTRL, LAGS, HOR)

    # 10. Esogeneita shock
    test_shock_exogeneity(dt)

    # Confronto R2
    summary_r2_comparison(dt, ENDOG, CORR_COL, CTRL, LAGS, HOR)

    print("=" * 70)
    print("  BATTERIA COMPLETATA")
    print("=" * 70)
