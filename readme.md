# Name 

Jordi Muñoz Florensa: jordi.munoz.florensa@estudiantat.upc.edu

# Pratica d'LP: Analitzador de tipus HinNer

En aquest zip s'inclouen els arxius necessaris per la realització de la 
pràctica:
- hm.g4: conté la gramàtica accepatada del llenguatge.
- hmLexer.py: llegeix l'entrada de text i la converteix en una seqüència de tokens.
- hmParser.py: que rep una seqüència de tokens i els organitza en un AST seguint les regles gramaticals definides.
- hmVisitor.py: que s'encarrega de definir els mètodes corresponents per les regles definides
- hm.py: codi principal encarregat de tota la gestió

# Descripció del hm.py

Per realitzar la pràctica he utilitzat diferents tipus algebraics per
simplificar estructurar de millor manera els diferents components que 
s'utilitzen, per fer l'arbre he utilitzat una classe Node que entre altres,
conté un atribut que guarda el tipus amb un tipus Type que pot ser tant de
tipus Variable, Constant o Aplicatiu.

Per conservar els valors de la taula de simbols he utilitzat una variable 
global que s'anomena taula_de_simbols que carrega símbols d'execucions 
anteriors utilitzant Pickle, que utilitza un arxiu .pkl on es guarden els 
símbols previs.

A l'hora de recórrer el visitador de l'arbre he pres la decisió de disseny
de fer la gestió de l'streamlit al visitRoot, on només en el cas de que rebi
una expresió escriure la taula de símbols, l'arbre, l'arbre amb les inferencies
i la taula amb les inferencies.

# Execució

Primer cop: antlr4 -Dlanguage=Python3 -no-listener -visitor hm.g4
streamlit run hm.py

Per realitzar l'execuió, he utilizat la funcionalitat de que en la primera 
execució ja hi hagi un exemple a evaluar, es pot canviar en la linia 288
modificant l'atribut value de la funcio text_area seguint el format adient.

Es recomana sempre fer les declaracions dels tipus abans d'una expressió, ja
que si no s'haurà de prèmer dos cops el botó fer degut a que l'expressió es
posterior a l'última definició de tipus i per tant l'arbre guardarà aquesta
definició despres d'avaluar l'expressió.

Per probar un exemple s'ha de premer el boto fer.

Per esborrar els símbols d'execucions prèvies s'ha de premer el botó resetejar.