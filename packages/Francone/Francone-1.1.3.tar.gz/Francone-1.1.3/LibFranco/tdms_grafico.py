from nptdms import TdmsFile
import matplotlib.pyplot as plt
import pandas as pd

def esempio():
    stringaesempio="_______\033[1;102mAvvio dell' ESEMPIO\033[0m___________\n\
import LibFranco as fd\n\
data = fd.TDMS(r\"stall load sn0001.tdms\")\n\
forza=data.col(\"/'Forza [N]'/'D1.BW01 [N]'\")\n\
timef=data.colonna(\"Forza*Time\")\n\
spos=data.col(\"*Spostamento [mm]*D1.BG01*\")\n\
velox=data.colonna(\"/'Velocità [mm/s]'/'D1.BV01 [mm/s]'\")\n\
correGS1=data.colonna(\"/'Corrente [mA]'/'T1.GS1.FBK.I [A]'\")\n\
correGS2=data.colonna(\"/'Corrente [mA]'/'T1.GS2.FBK.I [A]'\")\n\
a=fd.GRAFICO('bello')\n\
a.xylabels('assexx','asseyY')\n\
a.curvecolor('blue')\n\
a.label('bello')\n\
a.plot([timef,forza],'label','red')\n\
b=fd.GRAFICO('titolo',(20,10))\n\
b.xlabel('assexxAAA')\n\
b.plot2assi(([timef,forza],'Forza (N)','red'),([timef,spos],'disp (mm)','magenta'))\n\
"
    print(stringaesempio)
def help():
    print("_______\033[1;102mAvvio dell' HELP V.1.1.3\033[0m___________\n\
          Questa Lib contiene la classe TDMS:\n\
          1. prima di tutto: \033[1mdata = fd.TDMS(r\"xxx.tdms\")\033[0m \n\
          2. leggi il contentuto: \033[1mdata.leggi()\033[0m \n\
          3. per la descrizione: \033[1mdata.descrizione()\033[0m \n\
          4. per accedere alla colonna in vettore numpy: \033[1mdata.colonna(\"/'Forza [N]'/'D1.BW01 [N]'\")\033[0m \n\
          5. puoi accedere anche con: \033[1m timef=data.colonna(\"Forza*Time\") \033[0m\n\
          6. puoi accedere anche con: \033[1m timef=data.col(\"*Forza*Time*\") \033[0m\n\
          Questa Lib contiene la classe GRAFICO:\n\
          1. a = fd.GRAFICO()\n\
          2. a.xylabels('assex','asseY')\n\
          3. a.label('label')\n\
          4. a.curvecolor('black')\n\
          5. a.plot([timef,forza],'label1','red') <- label e color facoltativi\n\
          \tDOPPIO ASSE Y \n\
          1. b=fd.GRAFICO('Titolo2Assi')\n\
          2. b.xlabel('assexxAAA')\n\
          3. b.plot2assi(([timef,forza],'Forza (N)','red'),([timef,spos],'disp (mm)','magenta'))")
class TDMS:
    def __init__(self, file):
        if not isinstance(file, str):
            raise ValueError("l'ingresso è la path del file e deve essere una stringa")
        self.file = file
        self.leggi()
    def columns(self):
        return self.lettura.columns
    def leggi(self):
        tdms_file = TdmsFile.read(self.file)
        self.lettura=tdms_file.as_dataframe()
        return self.lettura
    def descrizione(self):
        print("_______\033[1;43mDESCRIZIONE:\033[0m___________\n\
              Restituisce i nomi delle colonne del DataFrame")
        if hasattr(self, 'lettura'):
            print()
        else:
            self.leggi()
            print("\033[1;31mPer accedere alle colonne devi prima leggere il file eseguendo la funzione leggi()\033[0m")
        print(str(self.lettura.columns))
    def colonna(self, colname):
        colonna_trovata = self.trova_colonna(colname, self.lettura.columns)
        if colonna_trovata is None:
            raise ValueError(f"Errore: la colonna '{colname}' non è stata trovata.")
        return self.lettura[str(colonna_trovata)].dropna().to_numpy()
    def col(self,colname):
        return self.colonna(colname)
    def trova_colonna(self, cartelladato, colonne):
        # Split della stringa cartelladato con '*'
        parti = cartelladato.split('*')
        if len(parti) == 1:
            colonna = parti[0]
            if colonna in colonne:
                return colonna
            else:
                raise ValueError(f"Errore: la colonna '{colonna}' non esiste in self.lettura.columns.")
        # Caso con due parti: verifica se entrambe le parti sono presenti in una colonna
        elif len(parti) == 2:
            for colonna in colonne:
                if parti[0] in colonna and parti[1] in colonna:
                    return colonna
            raise ValueError(f"Nessuna colonna trovata contenente '{parti[0]}' e '{parti[1]}'")
        elif len(parti) == 4:
            for colonna in colonne:
                if parti[1] in colonna and parti[2] in colonna:
                    return colonna
        else:
            raise ValueError(f"Errore: la stringa '{cartelladato}' contiene un formato string non supportato.")

        return None
class GRAFICO:
    def __init__(self,title=None,figsize1=None):
        self.figsize1=figsize1
        self.title=title
        self.graf(self.figsize1)
    def graf(self,figsize1=(10,6)):
        self.figsize1=figsize1
        self.fig, self.ax1 = plt.subplots(figsize=self.figsize1)
        self.ax1.title.set_text(self.title)
        return self.fig, self.ax1
    def xylabels(self,xlabel1,ylabel1):
        self.xlabel1=xlabel1
        self.ylabel1=ylabel1
        if hasattr(self, 'x1') and not plt.fignum_exists(self.fig.number):
            self.plot(self.x1,self.y1)
            self.ax1.set_xlabel(str(self.xlabel1))
            self.ax1.set_ylabel(str(self.ylabel1))
        return self.xlabel1,self.ylabel1
    def xlabel(self,xlabel1):
        self.xlabel1=xlabel1        
        if hasattr(self, 'x1') and not plt.fignum_exists(self.fig.number):
            self.plot(self.x1,self.y1)
            self.ax1.set_xlabel(str(self.xlabel1))
        return self.xlabel1
    
    def label(self,label1):
        self.label1=label1
        if hasattr(self, 'x1') and not plt.fignum_exists(self.fig.number):
            self.plot(self.x1,self.y1)
        return self.label1
    def curvecolor(self,color1):
        self.color1=color1
        return self.color1
    def plot(self,data1=([[], []]), label1='label1', color='colore'):
        self.x1, self.y1 = data1
        
        if not hasattr(self, 'label1') or label1!='label1':
            self.label1 = label1
        if hasattr(self, 'color1'):
            self.color = self.color1
            
        if color!='colore' or not hasattr(self, 'color1'):
            self.color =color
            
        if color=='colore' and not hasattr(self, 'color1'):
            self.color ='black'
            
        if color!='colore' and not hasattr(self, 'color1'):
            self.color =color

        if not plt.fignum_exists(self.fig.number):
            self.graf(self.figsize1)
        line1,=self.ax1.plot(self.x1, self.y1,color=self.color,label=str(self.label1))
        self.ax1.grid(True)
        if hasattr(self, 'xlabel1'):
            self.ax1.set_xlabel(str(self.xlabel1))
        if hasattr(self, 'ylabel1'):
            self.ax1.set_ylabel(str(self.ylabel1))
        self.fig.legend()
        plt.tight_layout()
        plt.show()
        return self.x1,self.y1
    def plot2assi(self,data1=([[], []], 'label1', 'blue'), data2=([[], []], 'label2', 'red')):
        self.x1, self.y1 = data1[0]
        self.label1, self.color1 = data1[1], data1[2]
        self.x2, self.y2 = data2[0]
        self.label2, self.color2 = data2[1], data2[2]
        #
        if not plt.fignum_exists(self.fig.number):
            self.graf(self.figsize1)
        self.ax1.plot(self.x1, self.y1,color=self.color1,label=str(self.label1))
        self.ax1.set_ylabel(str(self.label1),color=str(self.color1))
        self.ax1.tick_params(axis='y', labelcolor=str(self.color1))
        self.ax1.grid(True)

        self.ax2 = self.ax1.twinx() # Aggiunge un asse secondario che condivide l'asse X
        
        self.ax2.plot(self.x2, self.y2,color=self.color2,label=str(self.label2))
        self.ax2.set_ylabel(str(self.label2),color=str(self.color2))
        self.ax2.tick_params(axis='y', labelcolor=str(self.color2))
        if hasattr(self, 'xlabel1'):
            self.ax1.set_xlabel(str(self.xlabel1))
        self.fig.legend()
        plt.tight_layout()
        plt.show()
        return self.x1,self.y1,self.x2,self.y2
