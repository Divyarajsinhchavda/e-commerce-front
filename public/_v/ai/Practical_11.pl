% Recursion and backtracking: routes between cities, Tower of Hanoi
:- initialization(main).

road(ahmedabad, vadodara, 110).  road(vadodara, surat, 150).
road(ahmedabad, rajkot, 215).    road(rajkot, bhavnagar, 175).
road(ahmedabad, bhavnagar, 200). road(bhavnagar, surat, 290).
link(X, Y, D) :- road(X, Y, D) ; road(Y, X, D).

% route/4 explores paths by recursion, backtracking on dead ends
route(X, X, _, [X], 0).
route(X, Y, Visited, [X|P], D) :-
    X \= Y, link(X, Z, D1), \+ member(Z, Visited),
    route(Z, Y, [Z|Visited], P, D2), D is D1 + D2.

hanoi(0, _, _, _) :- !.
hanoi(N, From, To, Via) :-
    N1 is N - 1,
    hanoi(N1, From, Via, To),
    format("   Move disk ~w: ~w -> ~w~n", [N, From, To]),
    hanoi(N1, Via, To, From).

main :-
    writeln('Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____'),
    nl,
    writeln('All routes ahmedabad -> surat:'),
    forall(route(ahmedabad, surat, [ahmedabad], P, D),
           format("   ~w  (~w km)~n", [P, D])),
    findall(D-P, route(ahmedabad, surat, [ahmedabad], P, D), L),
    keysort(L, [Best-BP|_]),
    format("Shortest: ~w (~w km)~n~n", [BP, Best]),
    writeln('Tower of Hanoi (3 disks):'),
    hanoi(3, left, right, middle).
