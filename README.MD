# Corso di Laboratorio di Fisica I
### dati raccolti e analisi anno 2022/23
gruppo di lavoro numero 3
Arnoldi Marta, matricola: 898938, m.arnoldi9@campus.unimib.it
Carminati Giovanni, matricola: 897462, g.carminati17@campus.unimib.it

### installazione
includere interpolazione3.py in sys.path oppure copiare il file e includerlo nella cartella contenete il file .py che si vuole eseguire

## GUIDA ALL'USO DELLA LIBRERIA:

la libreria prevede la definizione di classi e funzioni per eseguire interpolazioni di dati

### FUNZIONI:
- **decimal_val(x,decimals = 2, exp=0, udm: str = '') -> str** \
    inserendo un valore questo viene formattato come stringa arrotondata a _decimals_ ciffre dopo la virgola e rappresentata come multiplo della decima potenza _exp_.
    E' possibile aggiungere una stringa in coda come unità di misura (_udm_)

- **final_val(x,sigma,decimals = 2,exp = 0, udm: str = '') -> str** \
    come il metodo precedente ma con aggiunta di un incertezza

- **b_std(x: ndarray)** \
    ritorna la deviazione standard con la correzione di bessel applicata

- **probability_under_norm(mean,sigma,val)** \
    dato un valore medio, un sigma e un valore generico, calcola l'area sottesa a una distribuzione normale centrata in _mean_ larga _sigma_ tra (mean-t,mean+t) dove _t_ = |_mean_ - val| / _sigma_ 

## CLASSI

### **Interpolazione**
la classe Interpolazione si serve della funzione _scipy.optimize.curve_fit_ 

sudo cp interpolazione3.py /usr/lib/python3.10

