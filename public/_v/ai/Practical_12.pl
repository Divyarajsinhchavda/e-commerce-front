% Small expert system: animal identification (rule-based reasoning)
:- initialization(main).
:- dynamic has/1.

animal(cheetah) :- mammal, carnivore, has(tawny_color), has(dark_spots).
animal(tiger)   :- mammal, carnivore, has(tawny_color), has(black_stripes).
animal(zebra)   :- mammal, has(hooves), has(black_stripes).
animal(penguin) :- bird, \+ has(flies), has(swims).
animal(eagle)   :- bird, has(flies), has(sharp_claws).

mammal    :- has(hair) ; has(gives_milk).
bird      :- has(feathers).
carnivore :- has(eats_meat) ; (has(sharp_teeth), has(sharp_claws)).

identify(Features) :-
    retractall(has(_)),
    forall(member(F, Features), assertz(has(F))),
    format("Features: ~w~n", [Features]),
    (   animal(A)
    ->  format("   Animal is: ~w~n", [A]),
        explain(A)
    ;   writeln('   Animal is: unknown')
    ), nl.

explain(A) :-
    clause(animal(A), Body),
    format("   Because: ~w~n", [Body]).

main :-
    writeln('Name: Chavda Divyaraj S. | Enrollment: 240905040018 | Batch: ____'),
    nl,
    identify([hair, eats_meat, tawny_color, black_stripes]),
    identify([feathers, swims]),
    identify([gives_milk, hooves, black_stripes]),
    identify([feathers, scales]).
