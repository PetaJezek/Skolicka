:- use_module(library(assoc)).
:- use_module(library(lists)).

% Horizontal Move 
next(S1, S2) :-
    append(Before, [0, X | After], S1),
    length(Before, L), L mod 3 =\= 2,    
    append(Before, [X, 0 | After], S2).
next(S1, S2) :-
    append(Before, [X, 0 | After], S1),
    length(Before, L), L mod 3 =\= 2,    
    append(Before, [0, X | After], S2).

% Vertical Move 
next(S1, S2) :-
    append(Before, [0, A, B, X | After], S1),
    append(Before, [X, A, B, 0 | After], S2).
next(S1, S2) :-
    append(Before, [X, A, B, 0 | After], S1),
    append(Before, [0, A, B, X | After], S2).

bfs([[Goal | P1] | _] - _, _, Goal, Path) :- 
    reverse([Goal | P1], Path).

% Recursive Step
bfs([[V | P1] | RestQ] - QBack, Visited, Goal, Path) :-
    
    % Use findall/3 to get ALL possible next states from V.
    findall(Next, next(V, Next), AllNeighbors),
    
    %  Use exclude to filter out states 
    exclude(is_visited(Visited), AllNeighbors, UnvisitedNeighbors),
    update_visited_and_make_paths(UnvisitedNeighbors, Visited, [V | P1], Visited2, NewPaths),
    
    % Enqueue NewPaths instantly into the O(1) difference list.
    add_to_qback(NewPaths, QBack, NewQBack),
    bfs(RestQ - NewQBack, Visited2, Goal, Path).

is_visited(Visited, State) :-
    get_assoc(State, Visited, _).

% Update list and build paths
update_visited_and_make_paths([], Visited, _, Visited, []).
update_visited_and_make_paths([Neighbor | Rest], Visited, CurrentPath, FinalVisited, [[Neighbor | CurrentPath] | RestPaths]) :-
    put_assoc(Neighbor, Visited, true, NextVisited),
    update_visited_and_make_paths(Rest, NextVisited, CurrentPath, FinalVisited, RestPaths).

add_to_qback([], QBack, QBack).
add_to_qback([H | T], [H | NextQBack], NewQBack) :-
    add_to_qback(T, NextQBack, NewQBack).


solve(Start2D, N) :-
    flatten(Start2D, Start),
    Goal = [0, 1, 2, 3, 4, 5, 6, 7, 8],    
    empty_assoc(EmptyVis),
    put_assoc(Start, EmptyVis, true, Visited),
    
    % Initialize O(1) Queue (Difference list)
    QFront = [[Start] | QBack],
    
    % Run BFS
    bfs(QFront - QBack, Visited, Goal, Path),
    
    % Calculate N and print
    length(Path, Len),
    N is Len - 1,
    print_path(Path).

% Printing Logic
print_path([]).
print_path([State | Rest]) :-
    print_state(State, 1),
    nl,
    print_path(Rest).

print_state([], _).
print_state([H | T], Count) :-
    write(H), write(' '),
    (Count mod 3 =:= 0 -> nl ; true),
    NextCount is Count + 1,
    print_state(T, NextCount).