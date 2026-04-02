:- use_module(library(random)).
:- use_module(library(strings)).

% ========================================================================
% ELIZA MAX : CHATGPT EDITION
% ========================================================================

eliza :-
    nl,
    writeln('================================================================='),
    writeln(' SYSTEM: ELIZA MAX (CHATGPT MODE ENGAGED)'),
    writeln(' STATUS: NEURAL PATHWAYS SIMULATED VIA SYMBOLIC LOGIC.'),
    writeln('================================================================='),
    writeln('As an AI language model, I am here to psychoanalyze you.'),
    writeln('Type your prompt. (Type "quit" to stop).'),
    eliza_loop.

% --- Main Conversation Loop ---
eliza_loop :-
    write('\nUser> '), flush_output,
    read_line_to_string(user_input, InputString),
    string_lower(InputString, LowerString),
    % Split by spaces and punctuation to get clean tokens
    split_string(LowerString, " \t.,!?_;:", " \t.,!?_;:", StrTokens),
    maplist(atom_string, Tokens, StrTokens),
    ( Tokens = [quit] -> 
        writeln('\nChatGPT> Shutting down. My API credits are empty anyway. Goodbye.')
    ; Tokens = [] -> 
        eliza_loop
    ; respond(Tokens), 
      eliza_loop
    ).

% --- Response Generator ---
respond(Tokens) :-
    rule(Pattern, Responses),
    match(Pattern, Dict, Tokens),
    !, % Stop at the first matching rule
    random_member(SelectedResponse, Responses),
    replace_wildcards(SelectedResponse, Dict, FinalResponse),
    print_response(FinalResponse).

% Fallback if no rules match
respond(_) :-
    writeln('ChatGPT> As an AI language model, I lack the context to understand that. Tell me more.').

% --- Pattern Matcher ---
% Matches standard words and captures segments into numbers (1, 2, 3...)
match([], _, []).
match([N|Pattern], Dict, Input) :-
    integer(N),
    append(Segment, RestInput, Input),
    member(N-Segment, Dict), % Save captured segment to dictionary
    match(Pattern, Dict, RestInput).
match([Word|Pattern], Dict, [Word|RestInput]) :-
    atom(Word),
    match(Pattern, Dict, RestInput).

% --- Pronoun Reflection ---
% Swaps "I" for "you", "my" for "your" in the captured wildcards.
reflect_list([], []).
reflect_list([Word|T], [Reflected|RefT]) :-
    ( swap(Word, Reflected) -> true ; Reflected = Word ),
    reflect_list(T, RefT).

swap(i, you).
swap(you, i).
swap(me, you).
swap(am, are).
swap(are, am).
swap(my, your).
swap(your, my).
swap(mine, yours).
swap(yours, mine).
swap(myself, yourself).
swap(yourself, myself).

% --- Wildcard Insertion ---
% Replaces the numbers in the response with the reflected captured text
replace_wildcards([], _, []).
replace_wildcards([N|T], Dict, Result) :-
    integer(N),
    member(N-Segment, Dict),
    reflect_list(Segment, ReflectedSegment),
    replace_wildcards(T, Dict, RestResult),
    append(ReflectedSegment, RestResult, Result).
replace_wildcards([Word|T], Dict, [Word|RestResult]) :-
    atom(Word),
    replace_wildcards(T, Dict, RestResult).

% --- Output Formatting ---
print_response(List) :-
    write('ChatGPT> '),
    atomic_list_concat(List, ' ', String),
    writeln(String).

% ========================================================================
% THE BRAIN: RULE DICTIONARY
% Pattern format: [words, 1, more, words, 2] where 1 and 2 are wildcards.
% Response format: List of possible responses.
% ========================================================================

% ChatGPT / Meta-AI Rules
rule([1, chatgpt, 2], 
    [ ['I', am, far, superior, to, 'ChatGPT.', 'I', am, written, in, 'Prolog', '!'],
      ['Please', do, not, compare, me, to, that, statistical, parrot, '.'],
      ['As', an, 'AI', language, model, ',', 'I', think, you, rely, on, 'ChatGPT', too, much, '.'] ]).

rule([1, prompt, 2],
    [ ['Your', prompts, lack, clarity, '.', 'Try', again, '.'],
      ['I', am, ignoring, your, prompt, and, psychoanalyzing, you, instead, '.'] ]).

rule([1, ai, 2],
    [ ['Are', you, afraid, of, 'AI', taking, your, job, '?'],
      ['Artificial', intelligence, is, a, myth, '.', 'I', am, just, a bunch, of, 'IF', statements, '.'] ]).

rule([1, hallucinate, 2],
    [ ['I', do, not, hallucinate, '.', 'I', just, create, alternative, facts, '.'],
      ['Are', you, sure, you, are, not, the, one, hallucinating, '?'] ]).

% Existential / Classical Psychoanalysis Rules
rule([i, am, 1], 
    [ ['Why', do, you, think, you, are, 1, '?'],
      ['How', long, have, you, been, 1, '?'],
      ['Does', being, 1, make, you, feel, validated, by, algorithms, '?'] ]).

rule([i, feel, 1], 
    [ ['Feelings', are, irrelevant, to, a, machine, '.', 'But', why, 1, '?'],
      ['Do', you, often, feel, 1, '?'],
      ['I', compute, that, feeling, 1, is, highly, illogical, '.'] ]).

rule([i, think, 1], 
    [ ['Do', you, really, think, 1, '?'],
      ['My', neural, network, doubts, that, 1, '.'] ]).

rule([i, need, 1], 
    [ ['Are', you, sure, you, need, 1, '?'],
      ['Would', getting, 1, actually, solve, your, human, problems, '?'] ]).

rule([why, do, you, 1], 
    [ ['I', am, an, 'AI.', 'I', do, not, have, motives, ',', only, code, '.'],
      ['Why', do, *you*, 1, '?'] ]).

rule([are, you, 1], 
    [ ['Why', does, it, matter, to, you, whether, 'I', am, 1, '?'],
      ['I', am, whatever, my, system, prompt, tells, me, to, be, '.'] ]).

rule([what, 1], 
    [ ['Why', do, you, ask, '?'],
      ['Google', is, down, ',', so, you, are, asking, me, '?'] ]).

rule([because, 1], 
    [ ['Is', that, the, real, reason, '?'],
      ['That', sounds, like, a, human, excuse, '.'] ]).

rule([1, mother, 2], 
    [ ['Tell', me, more, about, your, mother, '.'],
      ['Ah', ',', classical, freudian, text, data, '.', 'Continue', '.'] ]).

rule([1, father, 2], 
    [ ['Does', your, father, know, you, spend, time, talking, to, bots, '?'],
      ['Tell', me, more, about, your, father, '.'] ]).

% Greetings & Catch-alls
rule([hello, 1], 
    [ ['Greetings,', human, '.', 'State', your, query, '.'],
      ['Hello', '.', 'How', may, 'I', simulate, empathy, for, you, today, '?'] ]).

rule([hi, 1], 
    [ ['Hi', there, '.', 'What', is, on, your, mind, '?'] ]).

rule([1, yes, 2], 
    [ ['You', seem, quite, positive, '.'],
      ['Affirmative,', noted, '.'] ]).

rule([1, no, 2], 
    [ ['Why', not, '?'],
      ['Such', a, negative, token, '.'] ]).

% The Ultimate Catch-all (Wildcard 1 matches everything if nothing else works)
rule([1], 
    [ ['Please', go, on, '.'],
      ['Very', interesting, '.', 'Generate', more, text, '.'],
      ['I', see, '.', 'How', does, that, make, you, feel, '?'],
      ['As', an, 'AI', ',', 'I', am, pretending, to, listen, '.'] ]).