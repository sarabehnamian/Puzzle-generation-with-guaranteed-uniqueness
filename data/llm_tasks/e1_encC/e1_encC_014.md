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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_014.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00028

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Brit, Spaniard, German, Dane
- hobby: cooking, golf, painting, chess, hiking
- color: yellow, red, blue, purple, white
- drink: juice, water, milk, coffee, tea

Clues:
1. The person who drinks coffee and the German are not neighbours.
2. The Norwegian either drinks milk or drinks water.
3. The Norwegian lives in a lower-numbered house than the person who drinks milk.
4. There is exactly one house between the German and the juice drinker.
5. The Brit and the cooking enthusiast live two houses apart.
6. The person who enjoys chess and whoever lives in the yellow house live in adjacent houses.
7. The person who enjoys chess lives in the red house.
8. The person who enjoys hiking lives in the house just left of the one where the golf enthusiast lives.
9. The Spaniard enjoys painting.
10. The occupant of the blue house does not live next to the milk drinker.
11. The tea drinker is the German.
12. Whoever lives in the blue house lives directly to the left of the person in the red house.
13. The Brit lives next to the Norwegian.
14. The Norwegian either lives in the white house or lives in the yellow house.

## Puzzle plain:zebra-00074

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Swede, Dane, Brit, Norwegian
- color: purple, green, red, yellow, blue
- job: farmer, teacher, pilot, baker, lawyer
- pet: horse, rabbit, bird, fish, dog

Clues:
1. The pilot lives in the house just left of the one where the person who keeps the horse lives.
2. The owner of the dog and the Swede are not neighbours.
3. The Norwegian lives in one of the two end houses.
4. The farmer keeps the horse.
5. The Swede lives in house 5.
6. The person in the green house works as the baker.
7. Whoever lives in the yellow house keeps the bird.
8. The bird owner and the farmer are neighbours.
9. The Swede keeps the rabbit.
10. The Brit lives in the red house.
11. The pilot lives in the house just left of the one where the German lives.
12. The lawyer does not live next to the person who keeps the rabbit.
13. Whoever lives in the blue house lives in the house just left of the one where the German lives.

## Puzzle hard:zebra_hard-00056

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, milk, juice, cocoa, coffee
- nationality: Norwegian, Dane, Spaniard, Brit, German
- pet: dog, bird, fish, rabbit, cat
- job: baker, pilot, teacher, lawyer, farmer

Clues:
1. One of the neighbours of the dog owner is the Dane.
2. The Dane and the lawyer are one and the same person.
3. The Norwegian does not live to the right of the Dane.
4. The left-hand neighbour of the cat owner keeps the fish.
5. The left-hand neighbour of the person who drinks tea works as the baker.
6. The baker and the person who drinks juice are one and the same person.
7. The lawyer lives somewhere between the person who keeps the bird and the owner of the cat.
8. The person who drinks milk lives somewhere between the cocoa drinker and the owner of the fish.
9. The person who drinks juice and the Spaniard are one and the same person.
10. One of the neighbours of the milk drinker is the German.
11. One of the neighbours of the person who drinks cocoa keeps the rabbit.
12. The farmer lives further to the right than the person who drinks coffee.
13. Exactly 1 house lies to the left of the home of the milk drinker.
14. The person who keeps the cat and the teacher are one and the same person.

## Puzzle plain:zebra-00031

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, tennis, painting, chess, hiking
- job: doctor, pilot, lawyer, teacher, baker
- nationality: Dane, Norwegian, Swede, Spaniard, German
- color: purple, yellow, white, green, blue

Clues:
1. The pilot lives in the house just left of the one where the teacher lives.
2. The baker and the hiking enthusiast live two houses apart.
3. The Swede lives at one end of the row.
4. The Swede works as the lawyer.
5. There is exactly one house between the chess enthusiast and the Norwegian.
6. The person who enjoys painting lives in the second house.
7. The Dane lives next to the occupant of the yellow house.
8. The Spaniard lives immediately to the right of the cooking enthusiast.
9. The chess enthusiast lives at one end of the row.
10. The doctor either lives in the blue house or lives in the yellow house.
11. The doctor lives in the house just left of the one where the cooking enthusiast lives.
12. Whoever lives in the green house either enjoys cooking or enjoys hiking.
13. The painting enthusiast and the person in the purple house live in adjacent houses.
14. The person in the yellow house lives directly to the left of the person in the blue house.

## Puzzle plain:zebra-00088

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, baker, pilot, farmer
- pet: horse, bird, cat, fish, dog
- hobby: hiking, painting, cooking, chess, golf
- color: green, blue, yellow, red, purple

Clues:
1. The baker lives somewhere to the right of the teacher.
2. The person who keeps the cat lives in the red house.
3. The person who keeps the dog lives in house 4.
4. The pilot lives in the middle house.
5. The person who enjoys chess and whoever lives in the red house live two houses apart.
6. There is exactly one house between the hiking enthusiast and the painting enthusiast.
7. Whoever lives in the blue house enjoys hiking.
8. The occupant of the red house works as the farmer.
9. The owner of the cat enjoys golf.
10. The doctor lives in the fourth house.
11. The occupant of the yellow house lives in house 1.
12. The pilot lives in the purple house.
13. The person who enjoys golf lives somewhere to the left of the person who keeps the fish.
14. The occupant of the purple house keeps the horse.

## Puzzle hard:zebra_hard-00064

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, chess, golf, cooking, painting
- pet: bird, rabbit, dog, cat, fish
- color: blue, red, yellow, white, green
- job: lawyer, farmer, pilot, baker, teacher

Clues:
1. The bird owner and the pilot are one and the same person.
2. The right-hand neighbour of the painting enthusiast enjoys cooking.
3. If the person in the green house is not the lawyer, then that person works as the pilot.
4. The person who enjoys chess has only one neighbour.
5. Neither the owner of the bird nor the chess enthusiast lives in the blue house.
6. The right-hand neighbour of the person who enjoys cooking lives in the white house.
7. The occupant of the green house and the person who enjoys tennis are one and the same person.
8. Exactly 1 house lies to the left of the home of whoever lives in the yellow house.
9. The baker lives further to the right than the bird owner.
10. The owner of the fish lives further to the right than the farmer.
11. At least one house separates the cooking enthusiast from the owner of the cat.
12. The person who keeps the cat lives two doors away from the person who keeps the dog.
13. Exactly 1 house lies to the left of the home of the person who keeps the dog.
14. The person who enjoys painting and the teacher are one and the same person.
15. The golf enthusiast lives somewhere between whoever lives in the blue house and whoever lives in the red house.

## Puzzle paraphrase:zebra-00127

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, milk, juice, coffee, tea
- color: blue, red, green, yellow, white
- nationality: Spaniard, Brit, Swede, Dane, German
- pet: fish, bird, horse, cat, rabbit

Clues:
1. The cocoa drinker and the Swede live next door to each other.
2. The cat owner does not live next door to the Swede.
3. The Spaniard is the rabbit keeper.
4. The Dane lives directly to the left of the fish owner.
5. The milk drinker lives immediately to the left of the fish owner.
6. The German and the green house's occupant live two houses apart.
7. The rabbit owner lives somewhere to the right of the fish owner.
8. The coffee drinker lives in either the blue house or the white house.
9. The German lives in house 4.
10. The juice drinker lives in the blue house.
11. The milk drinker lives in the yellow house.
12. The German is not next door to the horse owner.
13. The blue house stands directly to the left of the Spaniard.
14. The cat keeper lives next door to the Spaniard.

## Puzzle hard:zebra_hard-00087

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, yellow, white, purple, green
- hobby: cooking, hiking, tennis, golf, chess
- nationality: Brit, German, Swede, Dane, Norwegian
- drink: coffee, water, cocoa, milk, tea

Clues:
1. If the person who enjoys chess does not live in the purple house, then that person lives in the yellow house.
2. The tea drinker lives somewhere between the cocoa drinker and whoever lives in the purple house.
3. One of the neighbours of the person who drinks coffee lives in the blue house.
4. One of the neighbours of the Norwegian enjoys cooking.
5. Exactly 2 houses lie to the left of the home of the golf enthusiast.
6. The person who drinks cocoa and the Dane are one and the same person.
7. At least one house separates the cooking enthusiast from the occupant of the yellow house.
8. The person who enjoys hiking and the Swede are one and the same person.
9. The Brit lives two doors away from the person who enjoys hiking.
10. The person who drinks milk and the Norwegian are one and the same person.
11. The occupant of the blue house lives somewhere between the person who enjoys golf and the person who drinks water.
12. Exactly 1 house lies to the left of the home of whoever lives in the white house.

## Puzzle hard:zebra_hard-00076

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, cat, rabbit, horse, dog
- job: farmer, baker, teacher, doctor, pilot
- hobby: painting, golf, chess, tennis, cooking
- color: red, white, green, blue, purple

Clues:
1. If the person who enjoys golf is not the baker, then that person works as the doctor.
2. The person who enjoys painting lives two doors away from the pilot.
3. One of the neighbours of the person in the green house enjoys chess.
4. None of the neighbours of the owner of the cat keeps the dog.
5. The owner of the cat and the doctor are one and the same person.
6. The person who enjoys chess lives in the second house from the right.
7. The doctor and the person in the red house are one and the same person.
8. The person in the purple house lives further to the right than the person who enjoys cooking.
9. The owner of the cat lives in the third house from the right.
10. The owner of the fish and whoever lives in the white house are one and the same person.
11. The farmer and the person who keeps the horse are one and the same person.
12. The cooking enthusiast lives somewhere between the owner of the fish and the horse owner.
13. If the baker does not keep the fish, then that person keeps the horse.

## Puzzle hard:zebra_hard-00073

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Swede, Dane, Brit, German
- pet: bird, cat, dog, horse, fish
- job: doctor, baker, pilot, lawyer, teacher
- drink: cocoa, juice, water, tea, coffee

Clues:
1. One of the neighbours of the fish owner works as the teacher.
2. The right-hand neighbour of the water drinker works as the pilot.
3. If the person who drinks water is not the lawyer, then that person works as the teacher.
4. The left-hand neighbour of the Dane keeps the dog.
5. The Dane lives two doors away from the Swede.
6. One of the neighbours of the Brit is the Dane.
7. The juice drinker and the Swede are one and the same person.
8. The owner of the cat is not the same person as the Swede.
9. The person who keeps the horse lives in the fifth house from the right.
10. The lawyer and the Spaniard are one and the same person.
11. The baker and the person who drinks cocoa are one and the same person.
12. The cocoa drinker lives two doors away from the person who drinks coffee.
13. The left-hand neighbour of the owner of the fish works as the pilot.
