# Task: encode logic-grid puzzles as solver constraints

Translate each puzzle below into constraints in a small Python DSL. A program will check your
constraints with a SAT/SMT solver, so they must say exactly what each clue says - no more, no less.

The DSL:
- pos('value') is the house number (an integer from 1 to N) of the given value. Use the value names
  exactly as they appear in the puzzle header (case does not matter).
- The basic rules (every value is in exactly one house; values of the same category are in different
  houses) are added automatically. Do not encode them.
- Encode each numbered clue as ONE Python boolean expression using pos(...), integer constants,
  == != < <= > >= + -, and the functions Abs(x), And(a, b, ...), Or(a, b, ...), Not(a), Implies(a, b).
- Do not use Python's and/or/not/in, chained comparisons such as 1 < x < 3, or abs().

Examples (from other puzzles):
- "The baker keeps the parrot."            ->  pos('baker') == pos('parrot')
- "The violinist lives in the fourth house." ->  pos('violinist') == 4
- "The person who reads poetry lives next to the person who drinks lemonade."
                                            ->  Abs(pos('poetry') - pos('lemonade')) == 1

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e2_enc_encA\e2_enc_encA_002.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra/1/g8

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, green, blue, yellow, ivory
- nationality: Spanish, English, Ukrainian, Norwegian, Japanese
- pet: dog, snails, fox, horse, zebra
- drink: coffee, tea, milk, juice, water

Clues:
1. The Spaniard lives in the red house.
2. The Englishman drinks milk.
3. The milk drinker lives in the ivory house.
4. The ivory house is directly right of the red house.
5. The Norwegian lives in the yellow house, which is at one end of the row.
6. The Ukrainian drinks coffee.
7. The coffee drinker lives in the blue house.
8. The blue house is directly right of the ivory house.
9. The Japanese lives next to the Norwegian.
10. The green house is somewhere to the right of the red house.
11. The tea drinker lives next to the milk drinker.
12. The Japanese does not drink water.
13. The Englishman keeps the dog.
14. The fox is kept by the water drinker.
15. The horse owner lives directly left of the zebra owner.

## Puzzle zebra/0/g1

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, green, white, blue, yellow
- pet: cat, dog, bird, fish, horse
- drink: tea, juice, milk, coffee, water
- job: doctor, pilot, chef, artist, teacher

Clues:
1. The chef lives in house 3.
2. The chef lives in the white house.
3. The milk drinker lives in the white house.
4. The fish owner lives directly right of the white house.
5. The fish owner drinks coffee.
6. The artist drinks coffee.
7. The doctor lives directly left of the pilot.
8. The pilot drinks juice.
9. The teacher lives in the yellow house.
10. The blue house is next to the yellow house.
11. The horse owner drinks water.
12. The cat owner drinks tea.
13. The dog owner lives in the green house.
14. The cat owner lives in the red house.

## Puzzle zebra/0/g4

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Drew, Cleo, Finn, Ava, Ben
- pet: parrot, rabbit, hamster, turtle, goldfish
- dish: curry, pizza, sushi, tacos, pasta
- sport: hockey, tennis, soccer, rugby, cricket

Clues:
1. Ben lives at one of the two ends of the street.
2. Drew lives at one of the two ends of the street.
3. Drew lives somewhere left of Ben.
4. Finn lives directly left of Ava.
5. Cleo lives next to Drew.
6. Drew owns the parrot.
7. The rabbit owner lives next to the parrot owner.
8. The turtle owner lives directly right of the hamster owner.
9. The goldfish owner does not live next to the rabbit owner.
10. The pizza eater owns the rabbit.
11. The sushi eater owns the hamster.
12. The tacos eater lives directly left of the pasta eater.
13. The tennis player eats pizza.
14. The curry eater plays hockey.
15. The cricket player owns the goldfish.
16. Finn does not play rugby.

## Puzzle zebra/0/g10

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Vera, Tess, Sam, Rhea, Uri
- hat: visor, beret, beanie, fedora, cap
- snack: bagel, olives, popcorn, grapes, fries
- city: Quito, Paris, Perth, Tunis, Delhi

Clues:
1. Sam lives in the middle house.
2. Vera lives in house 1.
3. Tess lives directly right of Vera.
4. Rhea lives next to Sam.
5. Sam wears the beanie.
6. The beret wearer lives directly left of the beanie wearer.
7. Uri wears the cap.
8. The fedora wearer lives next to the cap wearer.
9. The beret wearer eats olives.
10. The bagel eater wears the visor.
11. The fries eater wears the cap.
12. The grapes eater lives directly left of the fries eater.
13. The Parisian eats olives.
14. The Quito resident lives at one end of the street and does not wear the cap.
15. The Tunis resident lives next to Sam.
16. The Delhi resident eats fries.

## Puzzle zebra/3/g1

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: yellow, blue, red, white, green
- pet: cat, dog, bird, horse, fish
- drink: water, tea, milk, coffee, juice
- job: pilot, artist, doctor, chef, teacher

Clues:
1. The milk drinker lives in the middle house.
2. The doctor lives in the red house.
3. The dog owner drinks tea.
4. The green house is house 5.
5. The white house is directly left of the green house.
6. The coffee drinker lives in the white house.
7. The bird owner drinks milk.
8. The chef owns the horse.
9. The fish owner lives in the green house.
10. The yellow house is not next to the red house.
11. The pilot lives somewhere to the left of the doctor.
12. The pilot lives in the yellow house.
13. The teacher drinks juice.
14. The artist lives next to the pilot.
15. The cat owner lives in house 1.

## Puzzle zebra/3/g8

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Kara, Jack, Liam, Hugo, Iris
- sport: rugby, judo, archery, swimming, tennis
- meal: salad, pizza, soup, curry, pasta
- scarf: teal, orange, pink, gray, brown

Clues:
1. Hugo lives directly right of Liam.
2. Jack lives directly left of Liam.
3. Kara lives somewhere to the left of Jack.
4. Iris lives somewhere to the right of Hugo.
5. Iris plays tennis.
6. Hugo is the swimmer.
7. The rugby player lives in an end house.
8. The judo player lives directly left of the archer.
9. The soup eater lives in the middle house.
10. The curry eater is the swimmer.
11. The pizza eater lives next to the rugby player.
12. The salad eater lives somewhere to the left of the pasta eater.
13. The orange scarf belongs to the judo player.
14. The gray scarf is directly right of the pink scarf.
15. The curry eater wears the gray scarf.
16. The pasta eater wears the brown scarf.

## Puzzle zebra/2/g7

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: ivory, maroon, teal, orange, black
- pet: goat, duck, mouse, snake, pony
- drink: cola, tea, juice, milk, beer
- job: vet, cook, poet, clerk, mason

Clues:
1. The poet lives in the ivory house.
2. The beer drinker is the poet.
3. The ivory house is in the middle of the row.
4. The orange house is directly right of the ivory house.
5. The teal house is next to the ivory house.
6. The mason lives in the maroon house.
7. The vet lives in the black house.
8. The vet lives somewhere to the right of the mason.
9. The clerk lives in the teal house.
10. The cook drinks milk.
11. The cola drinker lives next to the beer drinker.
12. The juice drinker lives directly right of the milk drinker.
13. The goat owner drinks cola.
14. The mouse owner is the vet.
15. The pony owner lives in the orange house.
16. The mason does not own the duck.

## Puzzle zebra/2/g2

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- name: Alice, Bob, Carol, Dave, Eve
- drink: water, tea, milk, juice, coffee
- pet: rabbit, parrot, dog, turtle, cat
- hobby: chess, cycling, painting, reading, gardening

Clues:
1. The painter lives in the middle house.
2. Eve is the painter.
3. Dave plays chess.
4. The chess player owns the rabbit.
5. The rabbit owner lives directly left of Alice.
6. Dave does not live next to Eve.
7. Carol does not live next to Eve.
8. The cyclist lives directly right of the chess player.
9. Carol is the gardener.
10. The tea drinker is the cyclist.
11. Bob drinks juice.
12. The milk drinker lives directly left of Bob.
13. The coffee drinker lives next to the juice drinker.
14. The parrot owner is the cyclist.
15. Eve owns the dog.
16. Bob does not own the cat.

## Puzzle zebra/1/g7

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Irish, Greek, Thai, Peruvian, Swiss
- drink: beer, cocoa, juice, tea, water
- pet: hamster, horse, lizard, mouse, snail
- hobby: knitting, sailing, baking, diving, yoga

Clues:
1. The Swiss lives in the middle house.
2. The Swiss drinks water.
3. The Thai lives next to the Swiss.
4. The beer drinker lives directly right of the water drinker.
5. The Irish drinks beer.
6. The Greek lives next to the Thai.
7. The Thai drinks juice.
8. The Peruvian does not drink tea.
9. The snail owner drinks water.
10. The mouse owner drinks tea.
11. The hamster owner is Irish.
12. The horse owner lives next to the Swiss.
13. The knitter keeps the snail.
14. The sailor keeps the horse.
15. The diver lives directly left of the baker.

## Puzzle zebra/1/g1

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- colour: red, green, blue, yellow, white
- nationality: Brit, Dane, German, Norwegian, Swede
- pet: dog, cat, bird, fish, horse
- drink: tea, coffee, milk, beer, water

Clues:
1. The green house is directly left of the yellow house.
2. The red house and the white house are at opposite ends of the row.
3. The blue house is next to the red house.
4. The green house is somewhere to the right of the red house.
5. The Brit lives in the red house.
6. The Dane lives in the blue house.
7. The German lives in the green house.
8. The Swede lives directly right of the German.
9. The cat owner lives next to the Brit.
10. The Swede keeps the fish.
11. The dog owner lives in the red house.
12. The horse is kept in one of the end houses.
13. The milk drinker lives in the middle house.
14. The Dane drinks coffee.
15. The beer drinker lives directly right of the milk drinker.
16. The water drinker lives next to the beer drinker.
