extrakce(Zaznamy, Atributy) :-
    all_atributy(Zaznamy, AllAtributes),
    sort(AllAtributes, SortedAtributes),
    length(Zaznamy, Count),
    assign_values(SortedAtributes, Zaznamy, Atributy, Count).
    
%Najdi vsechny atributy 
all_atributy([], []).
all_atributy([[]|Zaznamy], Atributes) :-
    all_atributy(Zaznamy, Atributes).
all_atributy([[A-_|Rest]|Zaznamy], [A|RestAtributes]) :-
    all_atributy([Rest|Zaznamy], RestAtributes).

assign_values([], _, [], _).
% Najdi vsechny hodnoty pro dany atribut
assign_values([A|RestAtributes], Zaznamy, [A-Values1|Rest], Count) :-
    %format('Matching attribute: ~w~n', [A]),
    findall(Value,(member(Row, Zaznamy), member(A-Value, Row)), Values),
    length(Values, Int),
    (Int < Count 
        -> 
        append(Values, [nedef], NoveHodnoty),
        sort(NoveHodnoty, Values1)
        ;
        sort(Values, Values1)
    ),
    assign_values(RestAtributes, Zaznamy, Rest, Count).
