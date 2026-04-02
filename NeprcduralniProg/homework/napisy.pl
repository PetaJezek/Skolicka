<<<<<<< HEAD
delka_seznam([],0).

delka_seznam ([_|Tail], L):-
    delka_seznamu(Tail, L1),
    L is L1 + 1.


% delka_seznamu(+Xss, -PocetFragmentu, -CelkovaDelka)
% delka_seznamu(+ListOfLists, -NumberOfLists, -TotalElements)
delka_seznamu([], 0, 0).
delka_seznamu([Head|Tail], Count, Total) :-
    delka_seznam(Head, L),
    delka_seznamu(Tail, CountTail, TotalTail),
    Count is CountTail + 1,
    Total is TotalTail+1

% Seznam, 
spoj_vse([], Zprava).
spoj_vse


solve(+Xss, ?Zs) :-
    delka_seznamu(Xss, Count, Total),
    N is Count / 2,
    ZLen is Total / N, 
    delka_seznam(Zs, K),
    K =:= ZLen,



    % Predikat ktery zaruci ze vsechny Zs maji delku ZLen

    % Predikat ktery zaruci ze vsechny Zs se pomoci otoceni daji seskladat na dana slova. 



=======
delka_seznamu([], 0, 0).
delka_seznamu([H|T], Count, Total) :-
    delka_seznamu(T, CountTail, TotalTail),
    Count is CountTail + 1,
    delka_seznam(H, Len),
    Total is TotalTail + Len.

% delka_seznam(+List, -Length)
% Note: This is equivalent to the built-in length/2
delka_seznam([], 0).
delka_seznam([_|T], Len) :-
    delka_seznam(T, LenTail),
    Len is LenTail + 1.

vytvor_kostru(0, []).
vytvor_kostru(Zlen, [_|T]) :-
    Zlen > 0,
    Zlen1 is Zlen - 1,
    vytvor_kostru(Zlen1, T).

% moznost_otoceni(Fragment, Možnost)
% Succeeds if Možnost is the fragment or its reverse.
% Avoids duplicate success for palindromes.
moznost_otoceni(F, F).
moznost_otoceni(F, O) :-
    reverse(F, O),
    F \= O.

% pasuji(Fragment1, Fragment2, CílovéSlovo)
% Succeeds if F1 and F2 (or their reverses) can be appended to form Zs.
pasuji(F1, F2, Zs) :-
    moznost_otoceni(F1, A),
    moznost_otoceni(F2, B),
    (append(A, B, Zs); append(B,A,Zs)).
    

% zaradit(+ZbývajícíFragmenty, +CílovéSlovo)
% Recursively pairs up all fragments to form copies of Zs.
zaradit([], _).
zaradit([F1|Rest], Zs) :-
    select(F2, Rest, NewRest),
    pasuji(F1, F2, Zs),
    zaradit(NewRest, Zs).

solve(Xss, Zs) :-
    % Xss is a list of fragments.
    % Zs is one of the original words we are trying to reconstruct.
    delka_seznamu(Xss, Count, Total),
    N is Count // 2,
    ZLen is Total // N,
    vytvor_kostru(ZLen, Zs),
    Count > 0,
    0 is Count mod 2, % Must be an even number of fragments.
    N is Count // 2, % N is the number of original words.
    0 is Total mod N, % Total length must be divisible by the number of words.
    ZLen is Total // N, % ZLen is the length of each original word.
    length(Zs, ZLen), % Zs is a template for a word of the correct length.
    zaradit(Xss, Zs).

solve_unique(Xss, Solutions) :-
    findall(Zs, solve(Xss, Zs), All),
    sort(All, Solutions).
>>>>>>> 3b471557cf0582e8fec2a0c24d437119d46d7266
