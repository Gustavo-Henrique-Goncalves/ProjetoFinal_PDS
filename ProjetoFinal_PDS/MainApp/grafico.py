import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as mt
import matplotlib.ticker as ticker
import soundfile as sf
import numpy as np

def get_info_grafic(signal):
    x, fs = sf.read(signal, )

    x = x[:, 0]
    n = len(x)

    t = np.arange(n) / fs

    return x , t

def make_grafic(signal):
    x, t = get_info_grafic(signal)

    mt.figure(figsize=(20, 4))
    mt.plot(t, x, color="#43b8dc")

    ax = mt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_color("#FFFFFF")
    ax.spines['left'].set_color("#FFFFFF")  
    ax.tick_params(colors="#FFFFFF")

    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))

    mt.savefig("grafico.png", transparent=True, bbox_inches='tight')
    mt.close()