
dup([], []).

dup([H | T], [H, H | R]) :-
    dup(T, R).




%------------------------------------

dedup([], []).

dedup([X], [X]).


dedup([X,X|T],M) :-
    dedup([X|T],M).


dedup([X,Y|T],[X|M]) :-
    dif(X,Y),
    dedup([Y|T],M).


%------------------------------------

group([],[]).

group([H|T], [Group|Rest]) :-
    group_helper(H, T, Group, Remainder),
    group(Remainder, Rest).

% Hodnota kterou hledame, seznam ve kterem hledame, akumulator, zbytek pro rekurzi
group_helper(X, [], [X], []).
group_helper(X, [X|T], [X|Group], Remainder) :-
    group_helper(X, T, Group, Remainder).
group_helper(X, [Y|T], [X], [Y|T]) :-
    dif(X, Y).
