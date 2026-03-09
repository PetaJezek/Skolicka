delka_seznamu([], 0, 0).
delka_seznamu([H|T], Count, Total) :-
    delka_seznamu(T, CountTail, TotalTail),
    Count is CountTail + 1,
    delka_seznam(H, Len),
    Total is TotalTail + Len.

delka_seznam([], 0).
delka_seznam([_|T], Len) :-
    delka_seznam(T, LenTail),
    Len is LenTail + 1.

vytvor_kostru(0, []).
vytvor_kostru(Zlen, [_|T]) :-
    Zlen > 0,
    Zlen1 is Zlen - 1,
    vytvor_kostru(Zlen1, T).

moznost_otoceni(F, F).
moznost_otoceni(F, O) :-
    reverse(F, O),
    F \= O.

pasuji(F1, F2, Zs) :-
    moznost_otoceni(F1, A),
    moznost_otoceni(F2, B),
    (append(A, B, Zs); append(B,A,Zs)).
    

zaradit([], _).
zaradit([F1|Rest], Zs) :-
    select(F2, Rest, NewRest),
    pasuji(F1, F2, Zs),
    zaradit(NewRest, Zs).

solve(Xss, Zs) :-
    delka_seznamu(Xss, Count, Total),
    N is Count // 2,
    ZLen is Total // N,
    vytvor_kostru(ZLen, Zs),
    zaradit(Xss, Zs).

solve_unique(Xss, Solutions) :-
    findall(Zs, solve(Xss, Zs), All),
    sort(All, Solutions).