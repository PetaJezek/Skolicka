filter_positives([], []).
filter_positives([H|T], [H|Positives]) :-
    H > 0,
    filter_positives(T, Positives).
filter_positives([H|T], Positives) :-
    H =< 0,
    filter_positives(T, Positives).




























% % Helper predicate that defines the condition
% is_positive(X) :- X > 0.

% % Higher-order filter predicate
% filter(_, [], []).
% filter(Predicate, [H|T], Result) :-
%     ( call(Predicate, H) ->
%         Result = [H|Rest]
%     ;
%         Result = Rest
%     ),
%     filter(Predicate, T, Rest).
