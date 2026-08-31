fronta(Predni, Zadni).



prazdna(fronta([],[])).



pridej(fronta(Predni, Zadni), X, fronta(Predni, [X|Zadni])).


odeber(fronta([], Zadni), X, NovaFronta) :-
    reverse(Zadni, Predni),
    odeber(fronta(Predni, []), X, NovaFronta).


odeber(fronta([X|Rest], Zadni), X, fronta(Rest, Zadni)).


prevod(fronta(Predni, Zadni), Xs) :-
    reverse(Zadni, ZadniOtoc),
    append(Predni,ZadniOtoc, Xs).



okno_helper(_, N, Usek, Fronta, N) :-
    prevod(Fronta, Usek).
okno_helper([X|Rest], N, Usek, Fronta, CurSoucet) :-
    CurSoucet < N,
    pridej(Fronta, X, NewFronta),
    NewSoucet is CurSoucet + X,
    okno_helper(Rest, N, Usek, NewFronta,NewSoucet).

okno_helper(Xs, N, Usek , Fronta, CurSoucet) :-
    CurSoucet > N,
    odeber(Fronta, X, NewFronta),
    NewSoucet is CurSoucet - X,
    okno_helper(Xs, N, Usek, NewFronta, NewSoucet).



okno(Xs, N, Usek) :-
    prazdna(Fronta),
    okno_helper(Xs, N, Usek, Fronta, 0).




genh([],1).

genh([Head|Body], N) :-
    N > 1,
    N1 is N-1,
    between(1, N1, J),
    K is N- J,
    genh(Body, J),
    genh(Head, K).

gen(Xs, N) :-
    genh(Xs, N).



gen_hehlper(Xs, N):-
    gen(Xs, N),
    N1 is N +1,
    gen_hehlper(Xs, N1).


gen(Xs) :-
    gen_hehlper(Xs, 1).