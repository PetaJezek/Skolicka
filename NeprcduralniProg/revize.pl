% Seznam intu znacici Muze a zeny, pocet lidi,  a bool ktery oznacuje zda je lodka u brehu. True je,  false neni
% Lide budou seznamy indexu zacinajici od 1. Tedy licha cisla jsou muzi a suda cisla po nich jsou jejich zeny
% A jeste celkovy pocet lidi

stav(Lidi,M, Lodka).
koncovy_stav([], false).



vytvor_seznam(Id, Max, [Id1, Id2|Lidi]) :-
    Id < Max,
    Id1 is Id + 1,
    Id2 is Id + 2,
    NewId is Id2,
    vytvor_seznam(NewId, Max, Lidi).
vytvor_seznam(Id, Max, Lidi):-
    Id >= Max,
    Lidi = [].

pocatecni(M, S) :-
    M2 is M*2,
    vytvor_seznam(0, M2, Lidi),
    S =[Lidi, M2, true].


koncovy([X|_]) :-
    X = [].

vytvor_maxpar2(Lidi, 1, [Clvk], UzNastoupil) :-
    member(Clvk, Lidi),
    Clvk > UzNastoupil.

vytvor_maxpar(Lidi, 0, [Clvk]) :-
    member(Clvk, Lidi).

vytvor_maxpar(Lidi, 0, [Clvk|Rest]) :-
    member(Clvk, Lidi),
    subtract(Lidi, [Clvk], NewLidi),
    vytvor_maxpar2(NewLidi, 1, Rest, Clvk).


prejezd([Lidi, M, false], [NewLidi,M, true]) :-
    vytvor_seznam(0, M, VsechnyLidi),
    subtract(VsechnyLidi, Lidi, LidiCoMuzouPrijet),
    vytvor_maxpar(LidiCoMuzouPrijet, 0, Cestujici),
    append(Lidi, Cestujici, NewLid),
    % NewLidi = NewLid.       % CHYBA: seznam neni kanonicky => stejna konfigurace v jinem poradi
                              %        (napr. [1,2,3,4] vs [1,3,4,2]) se bere jako jiny stav.
                              %        Kontrola "stavy se neopakuji" v hadej pak selhava a lodka jezdi tam a zpet.
    sort(NewLid, NewLidi).    % OPRAVA: drzime seznam serazeny, porovnani stavu pres member tak funguje mnozinove



prejezd([Lidi,M, true], [NewLidi,M, false]) :-
    vytvor_maxpar(Lidi, 0, Cestujici),
    subtract(Lidi, Cestujici, NewLid),
    % NewLidi = NewLid.       % CHYBA: viz vyse - nekanonicky seznam, stejny stav v jinem poradi vypada jinak
    sort(NewLid, NewLidi).    % OPRAVA: serazeny (kanonicky) seznam

% CHYBA: puvodni bezpecny kontroloval jen JEDEN breh (Lidi), druhy breh vubec ne
%        => nebezpecne stavy na druhem brehu prosly. Protipriklad: stav [[1,2,5],6,_] -
%        zena 6 je na druhem brehu s muzem 3 bez sveho manzela 5, presto puvodni verze pustila.
%        Navic vyzadovala manzela u KAZDE zeny, i kdyz u ni zadny cizi muz neni (zbytecne prisne).
% bezpecny_helper([[], _]).
%
% bezpecny_helper([[X|Rest], Lidi]) :-
%     X mod 2 > 0,
%     bezpecny_helper([Rest, Lidi]).
%
% bezpecny_helper([[X|Rest], Lidi]) :-
%     (X mod 2) < 1,
%     Muz is X -1,
%     member(Muz, Lidi),
%     bezpecny_helper([Rest, Lidi]).
%
% bezpecny([[],_,_]).
% bezpecny([Lidi, _, _]) :-
%     bezpecny_helper([Lidi, Lidi]).

% OPRAVA: kontrolujeme OBA brehy a spravnou podminku - zena je v nebezpeci pouze tehdy,
%         kdyz chybi jeji manzel A ZAROVEN je na brehu nejaky (cizi) muz.
bezpecny([Lidi, Total, _]) :-
    numlist(1, Total, Vsichni),
    subtract(Vsichni, Lidi, Druhy),
    bezpecny_breh(Lidi),
    bezpecny_breh(Druhy).

bezpecny_breh(Breh) :-
    \+ ( member(X, Breh), 0 is X mod 2,    % zena X je na brehu
         Manzel is X - 1,
         \+ member(Manzel, Breh),          % jeji manzel na brehu neni
         member(Y, Breh), 1 is Y mod 2 ).  % ale je tu nejaky muz Y
   



hadej(Stav,Acc,  Reseni) :-
    koncovy(Stav),
    Reseni = Acc.

hadej(Stav, Acc, Reseni) :-
    prejezd(Stav, Stav2),
    bezpecny(Stav2),
    \+ member(Stav2, Acc),
    append(Acc, [Stav2], NewAcc),
    hadej(Stav2, NewAcc, Reseni).




hadanka(M, Reseni) :-
    pocatecni(M, S),
    hadej(S, [S], Reseni).
%  f) Moje reseni by neslo lehce rozsirit na lodku se ctyrmi osobami nebot mam natvrdo naprogramovanou funkci prechod ktera bere pouze jednotlivce nebo dvojce.  Ale po prepsani cele funkce ktera by pracovala i s konstantou K jakozto maximalni limitu lodky.





% c
nasobky(X, N) :-
    var(X),
    zkus(1, N, X).


% a
nasobek(X, K):-
    nonvar(X),
    name(X, Seznam),
    M is X * K,
    name(M, Seznam2),
    msort(Seznam, SSeznam),
    msort(Seznam2, SSeznam2),
    SSeznam == SSeznam2.


% b
nasobky(_,0).
nasobky(X, N) :-
    nasobek(X, N),
    N1 is N -1,
    nasobky(X, N1).



zkus(X1, N, Vysledek) :-
    nasobky(X1, N),
    Vysledek = X1.

zkus(X1, N, Vysledek) :-
    X2 is X1 +1,
    zkus(X2, N, Vysledek).
