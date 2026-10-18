% Recursion in Prolog: factorial, fibonacci, list sum, length, member, reverse
:- initialization(main).

fact(0, 1) :- !.
fact(N, F) :- N > 0, N1 is N - 1, fact(N1, F1), F is N * F1.

fib(0, 0) :- !.
fib(1, 1) :- !.
fib(N, F) :- N > 1, A is N - 1, B is N - 2, fib(A, FA), fib(B, FB), F is FA + FB.

sum_list_([], 0).
sum_list_([H|T], S) :- sum_list_(T, S1), S is H + S1.

len([], 0).
len([_|T], N) :- len(T, N1), N is N1 + 1.

mem(X, [X|_]).
mem(X, [_|T]) :- mem(X, T).

rev([], []).
rev([H|T], R) :- rev(T, RT), append(RT, [H], R).

main :-
    writeln('Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____'),
    nl,
    fact(5, F), format("factorial(5)      = ~w~n", [F]),
    fib(10, B), format("fibonacci(10)     = ~w~n", [B]),
    sum_list_([4, 8, 15, 16], S), format("sum([4,8,15,16])  = ~w~n", [S]),
    len([a, b, c, d, e], L), format("length([a..e])    = ~w~n", [L]),
    ( mem(c, [a, b, c]) -> writeln('member(c,[a,b,c]) = true') ; writeln('member(c,[a,b,c]) = false') ),
    ( mem(z, [a, b, c]) -> writeln('member(z,[a,b,c]) = true') ; writeln('member(z,[a,b,c]) = false') ),
    rev([1, 2, 3, 4], R), format("reverse([1,2,3,4]) = ~w~n", [R]).
