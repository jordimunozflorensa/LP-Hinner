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

A continuació hi ha tota la part de les funcions que utilitzat, cadascuna
amb un petit comentari previ que explica que fa la funció.

Per conservar els valors de la taula de simbols he utilitzat una variable 
global que s'anomena taula_de_simbols que carrega símbols d'execucions 
anteriors utilitzant Pickle, que utilitza un arxiu .pkl on es guarden els 
símbols previs utilitzant el load i el dump.

A l'hora de recórrer el visitador de l'arbre he pres la decisió de disseny
de fer la gestió de l'streamlit al visitRoot, on només en el cas de que rebi
una expresió escriure la taula de símbols, l'arbre, l'arbre amb les inferencies
i la taula amb les inferencies.

Per fer la inferència de tipus de les aplicacions i les abstraccions he creat
dues funcions basant-me en l'algorisme de Milner el cual és similar a l'algorisme
general d'unificació implementant una funció per inferir el tipus de les
aplicacions (esq = dre -> @) i una altra funció per inferir els tipus de les
abstraccions (λ = esq -> dre), ambdues fan un recorregut Bottom-UP utilitzant
l'arbre obtingut despres del visitador.

# Execució

Primer cop: antlr4 -Dlanguage=Python3 -no-listener -visitor hm.g4
streamlit run hm.py

La gramàtica només accepat na expresió per execució, d'altra banda accepta
declaracions de tipus abans i despres de la expressió.

Es recomana sempre fer les declaracions dels tipus abans d'una expressió, ja
que si no s'haurà de prèmer dos cops el botó fer degut a que l'expressió es
posterior a l'última definició de tipus i per tant l'arbre guardarà aquesta
definició despres d'avaluar l'expressió.

Per realitzar l'execuió, he utilizat la funcionalitat de que en la primera 
execució ja hi hagi un exemple a evaluar, es pot canviar en la linia 290
modificant l'atribut value de la funcio text_area seguint el format adient.

Per probar un exemple s'ha de premer el botó fer.

Per esborrar els símbols d'execucions prèvies s'ha de premer el botó resetejar.

# Alguns jocs de prova

Inferencia incorrecta
'(+) :: P -> P -> P\n1 :: S\n(+) 1 x'

Inferencia correcta
'(+) :: N -> N -> N\n2 :: N\n\\x -> (+) 2 x'

Error en la gramàtica
'(+) :: N -> N -> N\n2 :: N\n x -> '

Inferencia correcta
'(+) :: N -> N -> N\n2 :: N\n\\x -> \\y -> (+) 2 ((+) x y)'

No es pot inferir el tipus N amb M
'(+) :: N -> N -> N\n2 :: M\n\\x -> \\y -> (+) 2 ((+) x y)'
