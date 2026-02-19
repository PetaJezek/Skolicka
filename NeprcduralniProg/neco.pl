male(adam).
male(jan).
male(martin).
male(petr).
male(vojtech).
male(kuba).

female(alena).
female(martina).
female(petra).


parent(adam, martin).
parent(adam, jan).

parent(jan, martina).
parent(alena, martina).

parent(petra, adam).
parent(petra, vojtech).
parent(vojtech, kuba).

parent(petr, alena).

father(Father, Child) :-
    parent(Father, Child),
    male(Father).

son(Son, Parent) :-
    parent(Parent, Son),
    male(Son).
    
sibling(X, Y) :-
    parent(Parent, X),
    parent(Parent, Y),
    dif(X, Y).

ancestor(A, S) :-
    parent(A, S).

ancestor(A, S) :-
    parent(A, Intermediate),
    ancestor(Intermediate, S).


mother(Mother, Child) :- parent(Mother, Child), female(Mother).

daughter(Daughter, Parent) :- parent(Parent, Daughter), female(Daughter).


grandparent(Grandparent, Child) :- parent(Grandparent, X), parent(X, Child).

grandfather(Grandfather, Child) :- grandparent(Grandfather, Child), male(Grandfather).

grandmother(Grandmother, Child) :- grandparent(Grandmother, Child), female(Grandmother).


brother(Person, Brother) :- sibling(Person, Brother), male(Brother).

uncle(Person, Uncle) :- sibling(Parent, Uncle), parent(Parent, Person), male(Uncle).

cousin(Person, Cousin) :- male(Cousin), son(Cousin, Uncle), uncle(Person, Uncle).

relative(X,Y) :- parent(Parent, X), parent(Parent,Y), dif(X,Y).

relative(X,Y) :- parent(Parent, X), parent(Paarent, Y), dif(X,Y), relative(Parent, Paarent).
  
