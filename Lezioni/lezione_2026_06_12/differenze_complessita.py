import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

asse_x = np.linspace(1, 1000, 1000)
lineare = asse_x.copy()
quadrato = asse_x ** 2
logaritmico = np.log2(asse_x) * asse_x

# Differenze rispetto al lineare
diff_quadrato = quadrato - lineare
diff_log = logaritmico - lineare
perc_quadrato = diff_quadrato / lineare * 100
perc_log = diff_log / lineare * 100

# Ratio 14:9 per ogni grafico
LARGHEZZA = 1120
ALTEZZA_GRAFICO = LARGHEZZA * 9 / 14  # 720
RIGHE = 3
SPAZIO = 0.06  # frazione verticale tra i grafici

# Altezza totale = somma grafici + spazi tra di loro
altezza_totale = ALTEZZA_GRAFICO * RIGHE / (1 - SPAZIO * (RIGHE - 1))

fig = make_subplots(
    rows=RIGHE,
    cols=1,
    vertical_spacing=SPAZIO,
    subplot_titles=(
        "Complessità",
        "Differenza assoluta rispetto al lineare",
        "Differenza percentuale rispetto al lineare",
    ),
)

# 1 - Complessità
fig.add_trace(go.Scatter(x=asse_x, y=lineare, name="n"), row=1, col=1)
fig.add_trace(go.Scatter(x=asse_x, y=quadrato, name="n²"), row=1, col=1)
fig.add_trace(go.Scatter(x=asse_x, y=logaritmico, name="n·log₂(n)"), row=1, col=1)

# 2 - Differenza assoluta
fig.add_trace(go.Scatter(x=asse_x, y=diff_quadrato, name="n² − n"), row=2, col=1)
fig.add_trace(go.Scatter(x=asse_x, y=diff_log, name="n·log₂(n) − n"), row=2, col=1)

# 3 - Differenza percentuale
fig.add_trace(go.Scatter(x=asse_x, y=perc_quadrato, name="(n² − n) / n"), row=3, col=1)
fig.add_trace(go.Scatter(x=asse_x, y=perc_log, name="(n·log₂(n) − n) / n"), row=3, col=1)

fig.update_yaxes(title_text="%", row=3, col=1)
fig.update_layout(width=LARGHEZZA, height=altezza_totale, title_text="Confronto complessità")
fig.show()
