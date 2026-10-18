% Facts, rules and queries: student-course database
:- initialization(main).

student(riya).  student(aman).  student(neha).
enrolled(riya, ai).   enrolled(riya, cn).
enrolled(aman, ai).   enrolled(neha, dbms).
marks(riya, ai, 82).  marks(aman, ai, 35).  marks(neha, dbms, 67).
teaches(prof_shah, ai).  teaches(prof_mehta, dbms).

passed(S, C)    :- marks(S, C, M), M >= 40.
classmate(X, Y) :- enrolled(X, C), enrolled(Y, C), X \= Y.
taught_by(S, T) :- enrolled(S, C), teaches(T, C).
grade(S, C, G)  :- marks(S, C, M),
                   ( M >= 80 -> G = 'A' ; M >= 60 -> G = 'B'
                   ; M >= 40 -> G = 'C' ; G = 'F' ).

q(Label, Goal) :-
    format("?- ~w~n", [Label]),
    ( findall(Goal, Goal, L), L \= [] ->
        forall(member(Goal, L), format("   ~w~n", [Goal]))
    ;   writeln('   false.') ).

main :-
    writeln('Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____'),
    nl,
    q('passed(S, ai)', passed(_, ai)),
    q('classmate(riya, Y)', classmate(riya, _)),
    q('taught_by(neha, T)', taught_by(neha, _)),
    q('grade(S, C, G)', grade(_, _, _)),
    q('passed(aman, ai)', passed(aman, ai)).
