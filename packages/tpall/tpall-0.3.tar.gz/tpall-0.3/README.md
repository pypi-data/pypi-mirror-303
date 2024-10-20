# tpall 


Quelques classes pour le TP de l'UE Automates, Langages et Logique :
 - `tpall.af.AFD` : Automate Fini Déterministe ;
 - `tpall.af.AFN` : Automate Fini Non-déterministe ;
 - `tpall.re.{EnsembleVide, Epsilon, Lettre, Somme, Concat, Etoile}` : Expressions Rationnelles.

Visualisation des automates à l'aide de `graphviz` par la méthode `dessine()`.

Visualisation des expressions rationnelles à l'aide de `svgling.arbre(e)`.

Génération d'expressions rationnelles à partir de chaînes de caractères à l'aide de `tpall.re.analyse`.

Décomposition d'expressions rationnelles par pattern matching.
