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



