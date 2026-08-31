:- use_module(library(clpfd)).
gen(0, Xs) :-
    Xs = [].
gen(N, Xs) :-
    N > 0, 
    Nsq is N *N,    
    genHelper(Nsq, Nsq, Xs).
genHelper(0, _, Xs) :-
    Xs = [].
genHelper(N1, N, Xs) :-
    N1 > 0,
    N2 is N1 - 1,              % is/2 : evaluate the right side arithmetically, unify with left
    X is N - N2,
    genHelper(N2, N, Xs1),
    append([X], Xs1, Xs).      % append/3 : Xs is Xs1 with [X] glued on the end

radek(0, M, Xs, Zbytek) :-
    Xs = [],
    Zbytek = M.


radek(N, M,Xs,Zbytek):-
    radekHelper(N, M, Xs),
    subtract(M, Xs, Zbytek).

radekHelper(0, _, Xs) :-
    Xs = [].
radekHelper(N, M, Xs) :-
    N > 0,
    Xs = [X|Xs1],
    member(X, M),
    subtract(M, [X], M1),
    N1 is N - 1,
    radekHelper(N1, M1, Xs1).


diag([[]], []).

diag(Rows, Diag) :-
    length(Rows, L),
    Pos is 1,
    diagHelper(Rows, Pos, L, Diag).

diagHelper([], _, _, []).
diagHelper([Row|Rows], Pos, L, [X|Diag]) :-
    Pos =< L,
    nth1(Pos, Row, X),
    Pos1 is Pos + 1,
    diagHelper(Rows, Pos1, L, Diag).

konstanta(N,M) :-
    N > 0,
    M is (N * (N^2 + 1)) // 2.


checkSumForAll([],_).
checkSumForAll([List|Rest], Konstanta) :-
    checkSum(List, Konstanta),
    checkSumForAll(Rest, Konstanta).


magicky([]).
magicky(Rows) :-
    length(Rows, Lenght),
    gen(Lenght, M),
    konstanta(Lenght, Konstanta),
    transpose(Rows, Cols),
    diag(Rows, Diag),
    maplist(reverse, Rows, OteceneRows),
    diag(OteceneRows, Diag2),
    append(Rows, Cols, Temp),
    append(Temp, [Diag], Temp2),
    append(Temp2, [Diag2], All),
    magickyHelper(Rows, M, Lenght, Konstanta),
    checkSumForAll(All, Konstanta).
    
checkSum(List, Konstanta) :-
    sum_list(List, Sum),
    Sum =:= Konstanta.

odstranCisla([], _, _, N,NewN) :-
    NewN is N.
odstranCisla([X|Xs], M, Volne, N, NewN) :-
    nonvar(X),
    member(X, M),
    N1 is N - 1,
    subtract(M, [X], NewM),
    Volne = NewM,
    odstranCisla(Xs, NewM, Volne, N1, NewN).

odstranCisla([X|Xs], M, Volne, N, NewN) :-
    var(X),
    Volne = M,
    odstranCisla(Xs, M, Volne, N, NewN).

odstraneNeCisla([],[]).
odstraneNeCisla([X|Xs], Rest) :-
    var(X),
    odstraneNeCisla(Xs, Rest).

odstraneNeCisla([X|Xs], [X|Rest]) :-
    nonvar(X),
    odstraneNeCisla(Xs, Rest).


vypln(_, []).
vypln([X|Xs], Vals) :-
    nonvar(X),
    vypln(Xs,Vals).

vypln([X|Xs], [V|Vals]) :-
    var(X),
    X = V,
    vypln(Xs, Vals).

checkVolne(Volne, M) :-
    var(Volne),
    Volne = M.
checkVolne(Volne, M) :-
    nonvar(Volne).


magickyHelper([],_,_,_).
magickyHelper([List|Rest], M, Lenght, Konstanta) :-
    odstranCisla(List, M, Volne, Lenght, N),
    radek(N, Volne, Xs, Zbytek),
    vypln(List, Xs),
    checkSum(List, Konstanta),
    magickyHelper(Rest, Zbytek, Lenght, Konstanta).





% problem ctyr hobitu

% stavy budou definovany mnozinou hobitu na leve strane a zda tam je pochoden


stav([frodo, pippin,smisek,sam], true).
final_stav([],false).

rychlost(frodo,3).
rychlost(pippin,4).
rychlost(smisek, 5).
rychlost(sam,6).


vyber(_, []).
vyber([X,Y], ZKoho) :-
    member(X, ZKoho),
    member(Y, ZKoho),
    X \= Y.

vyber([X], Zkoho) :-
    member(X, Zkoho).

prechod([Leva, true], [Leva2, false]) :-
    vyber(Kdo, Leva),
    subtract(Leva, Kdo, Leva2).


prechod([Leva, false], [Leva2, true]) :-
    findall(H, rychlost(H,_), Vsichni),
    subtract(Vsichni,Leva, Moznosti),
    vyber(Kdo,Moznosti),
    append(Leva, Kdo, Leva2).
    


najdiMaxCas([],MaxTime,Time) :-
    Time = MaxTime.

najdiMaxCas([X|Rest], MaxTime, Time) :-
    rychlost(X,H),
    MaxTime > H,
    najdiMaxCas(Rest, MaxTime,Time).

najdiMaxCas([X|Rest], MaxTime, Time) :-
    rychlost(X,H),
    MaxTime < H,
    najdiMaxCas(Rest, H,Time).

najdiMaxCas([X|Rest], MaxTime, Time) :-
    rychlost(X,H),
    MaxTime is H,
    najdiMaxCas(Rest, H,Time).

spocitejCas([M,_], [N,_], Time) :-
    length(M, K),
    length(N, L),
    K > L,
    subtract(M, N, MovingHobits),
    najdiMaxCas(MovingHobits, 0, Time).


spocitejCas([M,_], [N,_], Time) :-
    length(M, K),
    length(N, L),
    K < L,
    subtract(N,M, MovingHobits),
    najdiMaxCas(MovingHobits, 0, Time).

hadanka(Reseni) :-
    stav(H, T),
    final_stav(N, M),
    once(najdi_reseni([[H,T]], 25, [H,T], [N,M], 0, Reseni)).
 


najdi_reseni(Acc, MaxTime, [[],false], _, CurTime, Acc) :-
    CurTime < MaxTime + 1.


najdi_reseni(Acc, MaxTime, Stav1, Stav2, CurTime, Reseni) :-
    prechod(Stav1, Stav),
    spocitejCas(Stav1, Stav, Time),
    NewCurTime is CurTime + Time,
    NewCurTime < MaxTime+1,
    \+ member(Stav, Acc),
    append(Acc, [Stav], NovyAcc),
    najdi_reseni(NovyAcc, MaxTime, Stav, Stav2, NewCurTime, Reseni).
    




