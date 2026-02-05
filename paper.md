# Moltiplicatori dell'investimento pubblico e corruzione:  
La qualità istituzionale conta?

**Autore:** Giuseppe Cangemi  
**Data:** 2026-XX-XX  

---

> Questo articolo combina un esercizio di replicazione con un’estensione metodologica:  
> da un lato replico le evidenze recenti sui moltiplicatori dell’investimento pubblico nell’Unione Europea,  
> dall’altro valuto se e in che misura la loro efficacia dipenda dalla qualità delle istituzioni, approssimata dal livello di corruzione.

---

## 1. Motivazione

Negli ultimi anni, l’investimento pubblico è tornato al centro del dibattito di politica economica europea. L’esigenza di colmare i divari infrastrutturali, sostenere la transizione verde e rafforzare la crescita di lungo periodo ha rinnovato l’interesse per gli effetti macroeconomici dell’investimento pubblico, sia tra i responsabili delle politiche economiche sia nella letteratura accademica.

Un contributo recente di Heimberger e Dabrowski (2025) analizza gli effetti macroeconomici degli shock di investimento pubblico nell’Unione Europea, mostrando che tali shock sono associati a un aumento del prodotto e a una riduzione della disoccupazione nel breve periodo, senza evidenza di un peggioramento della dinamica del debito pubblico. Dal punto di vista metodologico, il lavoro si distingue per l’adozione di una strategia di identificazione basata sugli errori di previsione dell’investimento pubblico, che consente di attenuare in modo trasparente due problemi centrali nell’analisi empirica della politica fiscale. In primo luogo, il problema di endogeneità, poiché le decisioni di investimento pubblico tendono a reagire allo stato del ciclo economico: in assenza di un’adeguata strategia di identificazione, un aumento dell’investimento potrebbe riflettere condizioni macroeconomiche favorevoli piuttosto che rappresentare uno shock esogeno. In secondo luogo, il problema del *fiscal foresight*, in quanto famiglie e imprese possono anticipare l’attuazione di programmi di investimento pubblico già annunciati, adattando il proprio comportamento prima che la spesa venga effettivamente realizzata.

L’utilizzo degli errori di previsione dell’investimento pubblico come misura dello shock consente di affrontare entrambe le criticità, isolando variazioni inattese rispetto alle informazioni disponibili al momento della previsione ufficiale. In questo modo, lo shock identificato è plausibilmente ortogonale alle condizioni macroeconomiche correnti e alle aspettative degli agenti economici.

L’adozione di un framework di proiezioni locali consente inoltre di stimare direttamente le risposte dinamiche delle variabili macroeconomiche a ciascun orizzonte temporale, senza imporre una struttura dinamica comune su tutto il profilo della risposta. Rispetto agli approcci VAR tradizionali, le proiezioni locali offrono una maggiore flessibilità e risultano particolarmente adatte in contesti caratterizzati da eterogeneità tra paesi e da potenziali non linearità negli effetti della politica fiscale.

Tuttavia, l’evidenza fornita dal lavoro non suggerisce effetti persistenti nel medio-lungo periodo. In particolare, le risposte stimate risultano statisticamente significative principalmente nei primi orizzonti temporali successivi allo shock, mentre tendono a perdere precisione e significatività a partire dai periodi successivi. Questo aspetto invita a interpretare i risultati come indicativi di effetti prevalentemente di breve periodo, piuttosto che come una prova definitiva di moltiplicatori elevati e persistenti.

Allo stesso tempo, una questione rilevante rimane in gran parte inesplorata. Sebbene gli effetti medi forniscano informazioni utili, essi possono mascherare una sostanziale eterogeneità tra paesi. In particolare, non è affatto scontato che l’investimento pubblico produca effetti simili in contesti istituzionali differenti, caratterizzati da diversi livelli di efficienza amministrativa, qualità della governance e controllo della corruzione.

Questo articolo, pertanto, si propone di analizzare se e in che misura l’impatto macroeconomico dell’investimento pubblico differisca sistematicamente tra paesi con livelli elevati e ridotti di corruzione, contribuendo a chiarire il ruolo della qualità istituzionale come fattore condizionante l’efficacia della politica di investimento pubblico.

---

## 2. Il lavoro originale: idea e strategia di identificazione

### 2.1 Shock di investimento pubblico tramite errori di previsione

L’idea chiave in Heimberger e Dabrowski (2025) consiste nell’identificare gli shock di investimento pubblico attraverso gli errori di previsione, definiti come la differenza tra l’investimento pubblico effettivamente realizzato e la corrispondente previsione formulata ex ante:

$$
F_{i,t} = I^{\text{actual}}_{i,t} - I^{\text{forecast}}_{i,t}.
$$

L’investimento pubblico è misurato come formazione lorda di capitale fisso delle amministrazioni pubbliche in rapporto al PIL.

Come discusso nella sezione di motivazione, l’identificazione degli effetti causali della politica fiscale è resa complessa dalla presenza di endogeneità e di *fiscal foresight*. L’utilizzo degli errori di previsione rappresenta una soluzione particolarmente efficace a queste criticità, poiché consente di isolare variazioni inattese dell’investimento pubblico rispetto all’insieme di informazioni disponibile al momento della previsione ufficiale.

In questo contesto, le previsioni della Commissione Europea svolgono un ruolo centrale: esse incorporano le informazioni macroeconomiche, istituzionali e di policy disponibili agli agenti economici al momento della loro formulazione. Di conseguenza, lo scostamento tra investimento realizzato e previsto cattura esclusivamente sorprese non anticipate da famiglie e imprese, rendendo lo shock plausibilmente esogeno rispetto alle condizioni macroeconomiche correnti.

L’impiego dei *forecast errors* consente quindi di allineare l’insieme informativo utilizzato dall’analisi econometrica a quello effettivamente disponibile per gli agenti economici, rafforzando l’interpretazione causale delle risposte macroeconomiche stimate. In altre parole, le funzioni di risposta all’impulso riflettono l’effetto di variazioni impreviste dell’investimento pubblico, piuttosto che l’anticipazione di politiche già note o reazioni endogene al ciclo economico. Sfruttando i dati d’archivio delle previsioni della Commissione Europea, gli autori allineano l’insieme informativo utilizzato dall’econometria a quello effettivamente disponibile per famiglie e imprese al momento delle decisioni economiche. Questo allineamento riduce il rischio che le stime riflettano informazioni non osservabili dagli agenti e contribuisce a una più credibile identificazione delle funzioni di risposta all’impulso.

### 2.2 Framework econometrico

Gli effetti dinamici degli shock di investimento pubblico sono stimati utilizzando proiezioni locali à la Jordà (2005). Per ciascun orizzonte \(k\), la specificazione di base assume la forma:

$$
y_{i,t+k} - y_{i,t-1}
=
\beta_k F_{i,t}
+ \sum_j \gamma_{k,j} Z_{i,t-j}
+ \delta_i^k
+ \theta_t^k
+ \varepsilon_{i,t}^k.
$$

La variabile dipendente misura la risposta cumulata della variabile macroeconomica di interesse all’orizzonte \(k\), costruita come differenza tra il valore futuro e il valore pre-shock. Questa formulazione consente di interpretare direttamente i coefficienti stimati come effetti cumulativi di uno shock di investimento pubblico, facilitando il confronto con la letteratura sui moltiplicatori fiscali. Il coefficiente \(\beta_k\) cattura l’effetto dello shock di investimento pubblico sull’outcome considerato a ciascun orizzonte temporale \(k\). La stima separata dell’equazione per ogni orizzonte permette di tracciare l’intero profilo dinamico della risposta senza imporre restrizioni parametriche sulla forma della funzione di risposta all’impulso. In questo senso, l’approccio delle proiezioni locali si distingue dai modelli VAR tradizionali, nei quali la dinamica delle risposte è vincolata dalla specificazione del sistema e dalla struttura delle dipendenze temporali.

Il vettore dei controlli \(Z_{i,t-j}\) include variabili macroeconomiche standard laggate, con l’obiettivo di assorbire dinamiche persistenti e ridurre il rischio di confondere lo shock di investimento con altre fonti di variazione macroeconomica. Gli effetti fissi del paese \(\delta_i^k\) controllano per caratteristiche strutturali invarianti nel tempo, mentre gli effetti fissi temporali \(\theta_t^k\) catturano shock comuni a tutti i paesi, come eventi macroeconomici globali o cambiamenti istituzionali a livello europeo.

L’inferenza è condotta utilizzando errori standard di Driscoll–Kraay, che risultano appropriati in un contesto di dati panel caratterizzato da dipendenza seriale e correlazione cross-sezionale tra le unità. Questa scelta consente di ottenere stime dell’incertezza robuste alla presenza di shock comuni e di interdipendenze tra economie nazionali.

Nel lavoro originale, questo framework produce moltiplicatori cumulati del prodotto superiori all’unità, un aumento dell’investimento privato coerente con meccanismi di *crowding-in* e nessuna evidenza di un peggioramento sistematico delle dinamiche del debito pubblico. Tuttavia, tali effetti risultano concentrati principalmente nei primi orizzonti temporali e tendono a perdere significatività statistica nel medio periodo, suggerendo che le stime medie potrebbero mascherare importanti fonti di eterogeneità tra paesi.

---

## 3. Replicazione: perché è importante

Prima di estendere l'analisi, replico i risultati originali utilizzando lo stesso framework empirico. La replicazione ha una duplice funzione. In primo luogo, fornisce una validazione dei risultati originari. In secondo luogo, stabilisce un benchmark pulito rispetto al quale valutare la specificazione estesa.

Le funzioni di risposta all'impulso replicate sono identiche a quelle riportate nello studio originale, sia in termini di magnitudine sia per quanto riguarda i profili dinamici, rafforzando la fiducia nell'analisi successiva.

---

## 4. Risultati di base: interpretazione e contesto economico

Questa sezione discute brevemente i risultati di base ottenuti dalla replicazione, che costituiscono il punto di riferimento empirico per l'analisi dell'eterogeneità istituzionale.

### 4.1 L'impatto della spesa sul PIL reale

La risposta del PIL reale a uno shock di investimento pubblico (Figura 1a) mostra un andamento chiaro e economicamente significativo. All'impatto, il moltiplicatore del prodotto è di circa 0,6, a indicare che l'investimento pubblico genera un aumento consistente dell'attività economica, seppur inferiore a uno nel brevissimo periodo. Nel tempo, il moltiplicatore cresce in modo monotono, supera l'unità dopo un anno e si stabilizza intorno a 1,2–1,3 dopo due o tre anni.

Questo accumulo graduale è coerente con l'idea che l'investimento pubblico operi sia attraverso canali dal lato della domanda nel breve periodo, sia attraverso canali dal lato dell'offerta nel medio periodo, in quanto infrastrutture e capitale pubblico migliori accrescono la capacità produttiva. La magnitudine e la persistenza dei moltiplicatori stimati sono pienamente in linea con la letteratura esistente sui moltiplicatori dell'investimento pubblico.

### 4.2 Investimento privato: crowding-in o crowding-out?

Come mostrato nella Figura 1b, l’investimento privato reagisce positivamente agli shock di investimento pubblico. La risposta aumenta progressivamente nel primo anno successivo allo shock, raggiungendo un massimo intorno all’orizzonte annuale, e rimane positiva anche negli anni successivi. Sebbene l’ampiezza degli intervalli di confidenza cresca alle scadenze più lontane, i coefficienti stimati non suggeriscono un’inversione sistematica del segno della risposta.

Questa dinamica indica che l’investimento pubblico non esercita un effetto di spiazzamento sull’accumulazione di capitale privato. Al contrario, l’evidenza è coerente con un meccanismo di *crowding-in*, secondo il quale l’espansione dell’investimento pubblico aumenta la redditività attesa dei progetti privati. Tale effetto può operare attraverso diversi canali: il miglioramento delle infrastrutture pubbliche, la riduzione dei costi di produzione e di trasporto, nonché una diminuzione dell’incertezza macroeconomica nel breve periodo.

L’aumento dell’incertezza stimata agli orizzonti più lontani riflette verosimilmente una maggiore eterogeneità nelle risposte tra paesi e nel tempo, piuttosto che un indebolimento sistematico del legame tra investimento pubblico e privato. In questo senso, i risultati suggeriscono che, sebbene gli effetti medi siano positivi, la forza del meccanismo di complementarità possa dipendere da caratteristiche strutturali e istituzionali dei singoli paesi.

Nel complesso, l’evidenza empirica suggerisce che l’investimento pubblico possa fungere da catalizzatore per l’attività di investimento privata, rafforzando l’impatto complessivo della politica fiscale sull’economia reale. Questo risultato è coerente con la letteratura che documenta come la spesa pubblica in conto capitale possa generare effetti di *crowding-in* sull’investimento privato, in particolare quando l’investimento pubblico accresce la produttività marginale del capitale privato o migliora la dotazione infrastrutturale dell’economia (Aschauer, 1989; Bom e Ligthart, 2014; Leeper, Walker e Yang, 2010). Evidenze compatibili emergono anche da studi basati su strategie di identificazione alternative, inclusi approcci narrativi e proiezioni locali, che trovano una risposta positiva dell’investimento privato agli shock di investimento pubblico nelle economie avanzate (Auerbach e Gorodnichenko, 2012; Ramey, 2011).

### 4.3 Debito pubblico: un'eterna questione

La risposta del rapporto debito pubblico/PIL allo shock di investimento pubblico (Figura 1c) risulta contenuta e statisticamente imprecisa lungo l’orizzonte considerato. Le stime puntuali indicano una lieve riduzione nei primi due anni successivi allo shock, seguita da un ritorno verso valori prossimi allo zero; tuttavia, le bande di confidenza sono ampie e includono lo zero a tutti gli orizzonti, impedendo di trarre conclusioni statisticamente significative sull’effetto dell’investimento pubblico sul debito.

Nonostante questa incertezza, i risultati suggeriscono che non vi sia evidenza di un aumento sistematico del rapporto debito pubblico/PIL in seguito a uno shock di investimento pubblico. In altre parole, sebbene non sia possibile affermare che l’investimento pubblico riduca il debito in modo statisticamente significativo, l’analisi non fornisce indicazioni di un deterioramento delle dinamiche del debito nel medio periodo. Questa evidenza è coerente con l’interpretazione secondo cui gli effetti di crescita associati all’investimento pubblico possano, almeno in parte, compensarne il costo fiscale.

### 4.4 La spesa pubblica favorisce il mercato del lavoro?

Come mostrato in Figura 1d, la disoccupazione diminuisce in seguito allo shock di investimento pubblico, raggiungendo la riduzione massima dopo poco più di un anno, per poi tornare gradualmente verso il livello pre-shock. Questa risposta rispecchia le dinamiche del prodotto e riflette una maggiore domanda di lavoro via via che l'attività economica si espande.

Sebbene l'incertezza aumenti agli orizzonti più lontani, la riduzione di breve periodo della disoccupazione è economicamente rilevante e rafforza il ruolo stabilizzante dell'investimento pubblico.

### 4.5 Sintesi dei risultati di base

Nel complesso, i risultati di base delineano un profilo di risposta macroeconomica coerente con la letteratura sull’investimento pubblico, ma che richiede un’interpretazione prudente. In media, uno shock di investimento pubblico è associato a un aumento del prodotto, a una risposta positiva dell’investimento privato e a una riduzione della disoccupazione, sebbene tali effetti risultino in larga parte concentrati nei primi orizzonti temporali e accompagnati da un’elevata incertezza statistica alle scadenze più lunghe.

Per quanto riguarda il debito pubblico, l’analisi non fornisce evidenza di un aumento sistematico del rapporto debito/PIL, ma non consente nemmeno di trarre conclusioni statisticamente robuste circa un suo miglioramento. Nel complesso, i risultati suggeriscono che, in media, l’investimento pubblico non compromette le dinamiche del debito nel medio periodo.

Questa evidenza media, pur informativa, potrebbe tuttavia mascherare un’eterogeneità rilevante tra paesi. La debole persistenza degli effetti e l’ampiezza dell’incertezza stimata rendono quindi naturale approfondire il ruolo di caratteristiche strutturali e istituzionali nel condizionare l’efficacia dell’investimento pubblico.

#### Figura 1 – Effetti macroeconomici dell'investimento pubblico

<img src="graphs/BASELINE/gdp.png" width="40%" alt="PIL reale: moltiplicatore cumulato dell'investimento pubblico">

<img src="graphs/BASELINE/private_investment.png" width="40%" alt="Investimento privato: risposta cumulata">

<img src="graphs/BASELINE/public_debt.png" width="40%" alt="Rapporto debito/PIL: risposta cumulata">

<img src="graphs/BASELINE/unemployment.png" width="40%" alt="Tasso di disoccupazione: risposta cumulata">

---

## 5. Domanda di ricerca: la corruzione conta?

Sebbene gli effetti medi dell'investimento pubblico siano cautamente positivi, essi possono nascondere una variazione sostanziale tra paesi. Un candidato naturale come fonte di eterogeneità è la qualità istituzionale e, in particolare, la corruzione.  
Una maggiore corruzione può ridurre l'efficienza dell'investimento pubblico, accrescere le perdite e il *rent-seeking* e indebolire la trasmissione della spesa pubblica sull'attività economica reale. Questa considerazione motiva la domanda centrale dell'articolo: l'impatto macroeconomico dell'investimento pubblico è sistematicamente più basso nei paesi più corrotti?

### Evidenza dalla letteratura su corruzione e attività economica

Un ampio filone di ricerca economica ha mostrato che la corruzione non rappresenta soltanto una questione giuridica o etica, ma costituisce anche un fenomeno economicamente rilevante, con implicazioni dirette per l’allocazione delle risorse e l’efficacia delle politiche pubbliche. Dal punto di vista teorico, la corruzione distorce gli incentivi degli agenti economici, favorisce comportamenti di *rent-seeking* e genera inefficienze nell’utilizzo delle risorse pubbliche, in particolare quando i funzionari deviano il potere pubblico verso fini privati. Questi meccanismi sono formalizzati in modelli di tipo principale–agente, nei quali informazione asimmetrica, incentivi distorti e debole *accountability* istituzionale compromettono la performance economica nel tempo (Shleifer e Vishny, 1993; Acemoglu e Verdier, 2000).

Dal punto di vista empirico, numerosi studi hanno documentato una relazione negativa robusta tra corruzione e variabili macroeconomiche fondamentali. Analisi *cross-country* mostrano che livelli più elevati di corruzione sono associati a tassi di crescita di lungo periodo più bassi e a un minore accumulo di capitale privato (Mauro, 1995; Tanzi e Davoodi, 1997). In contesti caratterizzati da elevata corruzione, le imprese tendono a fronteggiare costi più elevati, maggiore incertezza e una protezione più debole dei diritti di proprietà, fattori che scoraggiano l’investimento e riducono l’efficienza allocativa.  
Studi quantitativi successivi hanno confermato questi risultati, mostrando che peggioramenti negli indicatori di controllo della corruzione si associano a livelli inferiori di PIL pro capite e a flussi più contenuti di investimenti diretti esteri (Wei, 2000; Méon e Sekkat, 2005). Nel complesso, l’evidenza suggerisce che la corruzione agisce come un freno sistematico allo sviluppo economico, incidendo sia sulle decisioni di investimento privato sia sulla produttività aggregata.

Questa letteratura fornisce una chiara motivazione per includere la qualità istituzionale – e in particolare il grado di corruzione – come potenziale fonte di eterogeneità nella trasmissione degli shock di investimento pubblico, poiché contesti istituzionali più deboli possono attenuare l’efficacia della spesa in conto capitale e ridurne l’impatto macroeconomico.

### Dati sulla corruzione: Worldwide Governance Indicators

Per misurare la qualità istituzionale, questo studio utilizza i *Worldwide Governance Indicators (WGI)* prodotti dal *World Bank Group*. I WGI sono un dataset globale ampiamente utilizzato, che copre oltre 200 economie su base annua dal 1996, riassumendo diverse fonti di percezioni sulla governance in sei indicatori compositi. Una di queste dimensioni, il *Control of Corruption*, cattura la misura in cui il potere pubblico è esercitato per fini privati, includendo forme di corruzione sia di piccola scala sia di *grand corruption*, nonché fenomeni di *state capture* da parte di élite e interessi privati.

L'indicatore di Controllo della Corruzione è espresso sia come stima su una scala normale standardizzata, sia come rango percentile rispetto a tutti i paesi. Valori e percentili più bassi riflettono esiti di governance peggiori – ossia una corruzione più pervasiva e controlli istituzionali più deboli.

Per l'analisi di eterogeneità proposta in questo articolo, ci concentriamo su un sottoinsieme di 15 paesi con i punteggi più bassi di Controllo della Corruzione tra quelli appartenenti all'Unione Europea e ad alcune economie avanzate selezionate. Questi paesi presentano esiti di governance relativamente deboli, come riflesso dai dati WGI, e costituiscono una base *ex-ante* per valutare se la qualità istituzionale condizioni l'efficacia degli shock di investimento pubblico.  
La scelta di questo sottogruppo è coerente con lavori esistenti che mostrano come la qualità istituzionale possa influenzare le dinamiche macroeconomiche: i paesi con un controllo della corruzione più debole tendono a sperimentare maggior rischi di allocazione inefficiente delle risorse, livelli inferiori di investimento produttivo e un aggiustamento più lento agli shock. Confrontando le funzioni di risposta all'impulso tra questo sottogruppo e il pannello complessivo, l'analisi fornisce indicazioni sul ruolo della corruzione come modificatore dei moltiplicatori fiscali.

---

## 6. Estensione metodologica: introduzione delle interazioni con la corruzione

### 6.1 Specifica estesa

Per affrontare questa domanda, estendo il framework di proiezioni locali di base, consentendo allo shock di investimento pubblico di interagire con la corruzione ritardata:

$$
y_{i,t+k} - y_{i,t-1}
=
\beta_k F_{i,t}
+ \theta_k \left( F_{i,t} \times \text{Corr}_{i,t-1} \right)
+ \sum_j \gamma_{k,j} Z_{i,t-j}
+ \delta_i^k
+ \theta_t^k
+ \varepsilon_{i,t}^k.
$$

L’indicatore di corruzione è ritardato e centrato rispetto alla media del campione, così da ridurre problemi di simultaneità e facilitare l’interpretazione dei coefficienti. In questa specificazione, il parametro \(\beta_k\) cattura la risposta dinamica dell’economia a uno shock di investimento pubblico in corrispondenza di un livello medio di corruzione, mentre \(\theta_k\) misura come tale risposta vari sistematicamente al variare della qualità istituzionale.

Un valore negativo di \(\theta_k\) indica che l’impatto macroeconomico dell’investimento pubblico si attenua in contesti caratterizzati da livelli più elevati di corruzione, mentre un valore nullo suggerisce l’assenza di eterogeneità istituzionale rilevante. Questa formulazione consente quindi di valutare in modo flessibile se e in che misura la qualità delle istituzioni condizioni l’efficacia dell’investimento pubblico lungo l’orizzonte temporale considerato.

Le funzioni di risposta all’impulso condizionate vengono infine ottenute valutando l’equazione stimata a diversi percentili della distribuzione dell’indicatore di corruzione, permettendo un confronto diretto tra paesi caratterizzati da elevata e bassa qualità istituzionale.

### 6.2 Interpretazione

Questa specificazione consente al moltiplicatore dell'investimento di variare in modo continuo con la corruzione. Le funzioni di risposta all'impulso possono quindi essere calcolate condizionatamente a paesi con diversi livelli di qualità istituzionale, rendendo possibile verificare se la corruzione attenui sistematicamente l'efficacia dell'investimento pubblico.

---

## 7. Risultati estesi: paesi ad alta e bassa corruzione

Questa sezione presenta i risultati della specificazione estesa, che consente agli effetti degli shock di investimento pubblico di differire sistematicamente tra paesi con alti e bassi livelli di corruzione. I paesi classificati come ad alta corruzione includono Italy, Spain, Portugal, Greece, Cyprus, Malta, Romania, Bulgaria, Croatia, Hungary, Slovakia, Poland, Czechia, Slovenia e Latvia. I restanti paesi del campione costituiscono il gruppo a bassa corruzione.

Il confronto rivela differenze marcate nella trasmissione degli shock di investimento pubblico tra contesti istituzionali diversi.

### 7.1 Effetti sul PIL

Nei paesi con livelli elevati di corruzione, la risposta cumulata del PIL reale a uno shock di investimento pubblico è debole e statisticamente imprecisa. Le stime puntuali rimangono prossime allo zero lungo tutto l'orizzonte, e le bande di confidenza si allargano in misura rilevante nel tempo. Questo andamento suggerisce che l'investimento pubblico fatichi a generare guadagni sostenuti di prodotto in contesti più corrotti.

Al contrario, nei paesi a bassa corruzione, gli shock di investimento pubblico producono aumenti del prodotto ampi e persistenti. Il moltiplicatore cumulato supera l'unità già dopo il primo anno e continua a crescere, raggiungendo valori ben superiori a quelli osservati nel caso di base. Questi risultati indicano che la qualità istituzionale svolge un ruolo cruciale nel trasformare la spesa in investimento pubblico in attività economica reale.

### 7.2 Effetti sull'investimento privato

Le differenze tra i livelli di corruzione risultano ancora più pronunciate per l'investimento privato. Nei paesi ad alta corruzione, l'investimento privato reagisce inizialmente in modo debole e tende a diventare negativo sugli orizzonti medi. Questo andamento è coerente con meccanismi di *crowding-out*, in cui inefficienze, *rent-seeking* e incertezza scoraggiano la formazione di capitale privato.

Nei paesi a bassa corruzione, al contrario, l'investimento privato risponde in modo positivo e persistente. L'investimento pubblico sembra favorire l'investimento privato, avvalorando l'idea che istituzioni efficaci rafforzino le complementarità tra capitale pubblico e privato.

### 7.3 Il solito debito

Interessantemente, l'investimento pubblico stesso aumenta in misura più marcata nei paesi ad alta corruzione. Questo suggerisce che gli effetti macroeconomici più deboli osservati in tali contesti non dipendono da una minore intensità dell'impulso fiscale, ma piuttosto da inefficienze nell'allocazione e nell'efficacia della spesa in investimenti.

Nei paesi a bassa corruzione, l'investimento pubblico aumenta anch'esso, ma il suo impatto macroeconomico è sensibilmente più forte, rafforzando l'interpretazione secondo cui la qualità istituzionale governa la produttività del capitale pubblico.

### 7.4 Effetti sul mercato del lavoro

Le risposte del mercato del lavoro mettono ulteriormente in evidenza l'importanza della qualità istituzionale. Nei paesi ad alta corruzione, la disoccupazione cala solo brevemente e successivamente aumenta su orizzonti più lunghi, suggerendo che l'investimento pubblico non riesce a generare guadagni occupazionali duraturi e statisticamente significativi.

Nei paesi a bassa corruzione, la disoccupazione diminuisce in modo più marcato e rimane al di sotto del livello pre-shock per un periodo più lungo. Questo profilo, che rispecchia una risposta del prodotto più vigorosa, indica che l'investimento pubblico si traduce più efficacemente in creazione di posti di lavoro quando la governance è più solida.

#### Figura 2 – Risposte cumulate: alta vs bassa corruzione

| PIL – alta corruzione | PIL – bassa corruzione |
| - | - |
| <img src="graphs/CORRUPTION/gdp_high.png" width="60%" alt="PIL - alta corruzione"> | <img src="graphs/CORRUPTION/gdp_low.png" width="55%" alt="PIL - bassa corruzione"> |

| Investimento privato – alta corruzione | Investimento privato – bassa corruzione |
| - | - |
| <img src="graphs/CORRUPTION/private_investment_high.png" width="60%" alt="Investimento privato - alta corruzione"> | <img src="graphs/CORRUPTION/private_investment_low.png" width="55%" alt="Investimento privato - bassa corruzione"> |

| Debito pubblico – alta corruzione | Debito pubblico – bassa corruzione |
| - | - |
| <img src="graphs/CORRUPTION/public_debt_high.png" width="60%" alt="Debito pubblico - alta corruzione"> | <img src="graphs/CORRUPTION/public_debt_low.png" width="55%" alt="Debito pubblico - bassa corruzione"> |

| Disoccupazione – alta corruzione | Disoccupazione – bassa corruzione |
| - | - |
| <img src="graphs/CORRUPTION/unemployment_high.png" width="60%" alt="Disoccupazione - alta corruzione"> | <img src="graphs/CORRUPTION/unemployment_low.png" width="55%" alt="Disoccupazione - bassa corruzione"> |

### 7.5 Interpretazione

Nel complesso, i risultati dell'estensione forniscono una forte evidenza del fatto che la corruzione indebolisce in modo significativo la trasmissione degli shock di investimento pubblico. Mentre i paesi ad alta corruzione sperimentano un aumento della spesa in investimento pubblico, ciò non si traduce in una crescita sostenuta del prodotto, né in un rafforzamento dell'investimento privato o dell'occupazione.

Al contrario, nei paesi a bassa corruzione, l'investimento pubblico risulta altamente efficace, generando moltiplicatori elevati, *crowding-in* dell'investimento privato e una riduzione della disoccupazione. Questi risultati suggeriscono che la qualità istituzionale è un elemento chiave nel determinare i moltiplicatori fiscali e contribuiscono a riconciliare risultati eterogenei presenti nella letteratura empirica sull'investimento pubblico.

---

## 8. Conclusione

Questo articolo mostra che, in media, gli shock di investimento pubblico sono associati a effetti macroeconomici favorevoli, in particolare in termini di aumento del prodotto e riduzione della disoccupazione, senza fornire evidenza di un peggioramento sistematico delle dinamiche del debito pubblico. Tuttavia, tali risultati medi sono accompagnati da un grado non trascurabile di incertezza e appaiono in parte concentrati nei primi orizzonti temporali.

Un contributo centrale dell’analisi è evidenziare che l’efficacia macroeconomica dell’investimento pubblico non è uniforme tra i paesi, ma può dipendere in modo rilevante dalla qualità delle istituzioni. In particolare, i risultati suggeriscono che contesti caratterizzati da una migliore governance e da un minore livello di corruzione tendono a beneficiare in misura maggiore degli shock di investimento pubblico.

Comprendere questa eterogeneità istituzionale è cruciale per la progettazione di politiche di investimento pubblico efficaci. In particolare, nel contesto di programmi di investimento su larga scala nell’Unione Europea, i risultati indicano che il rafforzamento della qualità istituzionale può rappresentare un complemento fondamentale per massimizzare i potenziali benefici macroeconomici dell’investimento pubblico in termini di crescita e occupazione.

---

## Riferimenti

Acemoglu, D., & Verdier, T. (2000).  
The choice between market failures and corruption.  
*American Economic Review*, 90(1), 194–211.

Aschauer, D. A. (1989).  
Is public expenditure productive?  
*Journal of Monetary Economics*, 23(2), 177–200.

Auerbach, A. J., & Gorodnichenko, Y. (2012).  
Measuring the output responses to fiscal policy.  
*American Economic Journal: Economic Policy*, 4(2), 1–27.

Bom, P. R. D., & Ligthart, J. E. (2014).  
What have we learned from three decades of research on the productivity of public capital?  
*Journal of Economic Surveys*, 28(5), 889–916.

Heimberger, P., & Dabrowski, C. (2025).  
Boosting the economy without raising the public debt ratio? The effects of public investment shocks in the European Union.  
*Applied Economics Letters*.

Jordà, Ò. (2005).  
Estimation and inference of impulse responses by local projections.  
*American Economic Review*, 95(1), 161–182.

Leeper, E. M., Walker, T. B., & Yang, S.-C. S. (2010).  
Government investment and fiscal stimulus.  
*Journal of Monetary Economics*, 57(8), 1000–1012.

Mauro, P. (1995).  
Corruption and growth.  
*Quarterly Journal of Economics*, 110(3), 681–712.

Méon, P.-G., & Sekkat, K. (2005).  
Does corruption grease or sand the wheels of growth?  
*Public Choice*, 122(1–2), 69–97.

Ramey, V. A. (2011).  
Identifying government spending shocks: It’s all in the timing.  
*Quarterly Journal of Economics*, 126(1), 1–50.

Shleifer, A., & Vishny, R. W. (1993).  
Corruption.  
*Quarterly Journal of Economics*, 108(3), 599–617.

Tanzi, V., & Davoodi, H. (1997).  
Corruption, public investment, and growth.  
*IMF Working Paper*, WP/97/139.

Wei, S.-J. (2000).  
How taxing is corruption on international investors?  
*Review of Economics and Statistics*, 82(1), 1–11.

World Bank (n.d.).  
Worldwide Governance Indicators: Control of Corruption.  
<https://datacatalog.worldbank.org/search/dataset/0038026/worldwide-governance-indicators>
