% Facts, rules and queries: family tree
:- initialization(main).

parent(raj, amit).   parent(raj, neha).
parent(sita, amit).  parent(sita, neha).
parent(amit, riya).  parent(amit, kabir).
parent(meena, riya). parent(meena, kabir).
male(raj). male(amit). male(kabir).
female(sita). female(neha). female(meena). female(riya).

father(F, C)  :- parent(F, C), male(F).
mother(M, C)  :- parent(M, C), female(M).
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
grandparent(G, C) :- parent(G, P), parent(P, C).
ancestor(A, D) :- parent(A, D).
ancestor(A, D) :- parent(A, X), ancestor(X, D).

q(Label, Goal) :-
    format("?- ~w~n", [Label]),
    ( findall(Goal, Goal, L0), sort(L0, L), L \= [] ->   % sort removes duplicate answers
        forall(member(Goal, L), format("   ~w~n", [Goal]))
    ;   writeln('   false.') ).

main :-
    writeln('Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____'),
    nl,
    q('father(F, riya)', father(_, riya)),
    q('mother(M, neha)', mother(_, neha)),
    q('sibling(riya, X)', sibling(riya, _)),
    q('grandparent(G, riya)', grandparent(_, riya)),
    q('ancestor(raj, X)', ancestor(raj, _)),
    q('sibling(raj, X)', sibling(raj, _)).
