:- use_module(library(clpfd)).


stutter_head([], []).

stutter_head([H|T], [H, H | Rest]) :-
    stutter_head(T, Rest).


stutter_acc([],[]).

stutter_acc(List, Result) :-
    stutter_acc_helper(List, [], Result).



stutter_acc_helper([], Acc, Result) :-
    reverse(Acc, Result).
    
    

stutter_acc_helper([H|T], Acc, Result) :-
    stutter_acc_helper(T, [H, H | Acc], Result).





