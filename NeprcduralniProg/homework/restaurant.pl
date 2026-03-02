male(david).
male(thomas).
female(emma).
female(stella).


person(X) :- male(X).
person(X) :- female(X).

sits_accross(X,Y) :- male(X), male(Y),
    dif(X,Y).

sits_accross(X,Y) :- female(X), female(Y),
    dif(X,Y).


solve(Dumplings, Pasta, Soup, Trout) :- 
    dif(Dumplings, Pasta),
    dif(Dumplings, Soup),
    dif(Dumplings, Trout),
    dif(Pasta, Soup),
    dif(Pasta, Trout),
    dif(Soup, Trout),
    
    dif(Cider, Beer),
    dif(Cider, Tea),
    dif(Cider, Wine),
    dif(Beer, Tea),
    dif(Beer, Wine),
    dif(Tea, Wine),

  

    person(Dumplings), person(Pasta), person(Soup), person(Trout),
    person(Cider), person(Beer), person(Tea), person(Wine),

    /* podminky */
    sits_accross(Cider, Trout),
    Dumplings = Beer,
    Soup = Cider,
    sits_accross(Pasta, Beer),
    Tea \= david,
    Wine = emma,
    Dumplings \= stella.
