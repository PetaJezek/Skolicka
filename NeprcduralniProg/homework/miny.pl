miny(Pocty,Miny) :-
    same_length(Pocty, Miny),
    check_board(o, Miny, Pocty).
    
mina_hodnota(o, 0).
mina_hodnota(x, 1).

check_board(_, [], []).
check_board(PrevMina, [CurMina, NextMina|MinyRest], [CurPocty|PoctyRest]) :-
    mina_hodnota(CurMina, CurHodnota),
    mina_hodnota(PrevMina, PrevHodnota),
    mina_hodnota(NextMina, NextHodnota),
    CurPocty is PrevHodnota + CurHodnota + NextHodnota,
    check_board(CurMina, [NextMina|MinyRest], PoctyRest).

check_board(PrevMina, [CurMina], [CurPocty]) :-
    mina_hodnota(CurMina, CurHodnota),
    mina_hodnota(PrevMina, PrevHodnota),
    CurPocty is PrevHodnota + CurHodnota.