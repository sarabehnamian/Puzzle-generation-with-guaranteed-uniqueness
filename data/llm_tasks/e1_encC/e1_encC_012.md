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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_012.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00010

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, Brit, German, Swede, Spaniard
- hobby: golf, painting, cooking, tennis, chess
- drink: juice, water, coffee, tea, cocoa
- job: doctor, baker, farmer, teacher, lawyer

Clues:
1. The baker lives somewhere between the doctor and the German.
2. At least one house separates the farmer from the teacher.
3. The person who enjoys painting and the teacher are one and the same person.
4. The baker and the person who enjoys tennis are one and the same person.
5. The left-hand neighbour of the Swede is the Spaniard.
6. The person who enjoys cooking lives further to the right than the farmer.
7. One of the neighbours of the water drinker drinks coffee.
8. The person who enjoys cooking and the lawyer are one and the same person.
9. The coffee drinker and the golf enthusiast are one and the same person.
10. The teacher lives somewhere between the Brit and the person who enjoys chess.
11. The person who drinks cocoa and the Swede are one and the same person.
12. The water drinker lives somewhere between the farmer and the lawyer.
13. The baker and the juice drinker are one and the same person.

## Puzzle paraphrase:zebra-00198

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, tea, milk, coffee, cocoa
- color: red, green, yellow, blue, purple
- hobby: painting, tennis, chess, cooking, hiking
- job: baker, lawyer, teacher, pilot, farmer

Clues:
1. The blue house sits immediately to the right of the tea drinker's house.
2. The coffee drinker lives immediately to the right of the baker.
3. The juice drinker is the farmer.
4. The milk drinker lives somewhere to the left of the hiking enthusiast.
5. The farmer and the tennis enthusiast are two houses apart.
6. The pilot lives directly to the right of the milk drinker.
7. The hiking enthusiast and the purple house's occupant live in adjacent houses.
8. The chess enthusiast lives in house 5.
9. The lawyer and the yellow house's occupant are next-door neighbours.
10. The purple house is immediately to the right of the juice drinker's house.
11. The pilot does not have painting as a hobby.
12. The green house is directly to the right of the cooking enthusiast's house.

## Puzzle hard:zebra_hard-00045

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, red, blue, purple, green
- pet: rabbit, dog, horse, bird, fish
- hobby: painting, cooking, golf, chess, hiking
- job: baker, doctor, farmer, pilot, teacher

Clues:
1. The right-hand neighbour of the farmer lives in the blue house.
2. The farmer lives two doors away from the person who enjoys golf.
3. Exactly 3 houses lie to the left of the home of the person who enjoys cooking.
4. The person who keeps the bird and the person who enjoys hiking are one and the same person.
5. The occupant of the green house lives two doors away from the owner of the horse.
6. One of the neighbours of the baker enjoys chess.
7. One of the neighbours of the hiking enthusiast works as the doctor.
8. The farmer does not live in the third house from the right.
9. Exactly 2 houses lie to the left of the home of the person in the purple house.
10. The owner of the dog does not live in the rightmost house.
11. The left-hand neighbour of the person who enjoys painting works as the pilot.
12. The occupant of the yellow house does not live to the right of the occupant of the green house.
13. If the owner of the dog does not live in the green house, then that person lives in the red house.
14. The right-hand neighbour of the person who keeps the fish lives in the purple house.

## Puzzle plain:zebra-00090

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Spaniard, Dane, Swede, Brit
- job: farmer, doctor, pilot, baker, teacher
- color: purple, red, white, yellow, green
- pet: bird, rabbit, horse, cat, fish

Clues:
1. There is exactly one house between the bird owner and the Swede.
2. The fish owner lives immediately to the right of the Brit.
3. The pilot lives in house 2.
4. The farmer lives in the house just left of the one where the Spaniard lives.
5. The doctor either is the Dane or is the Norwegian.
6. The Norwegian lives next to the occupant of the purple house.
7. The occupant of the purple house lives immediately to the right of the baker.
8. The person who keeps the fish and the owner of the horse live in adjacent houses.
9. The owner of the fish lives immediately to the right of the person in the yellow house.
10. The owner of the cat and the doctor live in adjacent houses.
11. The Spaniard lives directly to the left of the doctor.
12. The person in the green house either is the Dane or is the Spaniard.
13. Whoever lives in the green house and the occupant of the red house live two houses apart.

## Puzzle plain:zebra-00078

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, coffee, cocoa, juice, water
- hobby: golf, tennis, chess, painting, cooking
- color: white, yellow, red, green, blue
- nationality: Norwegian, Swede, Spaniard, German, Dane

Clues:
1. The person in the blue house and the juice drinker live in adjacent houses.
2. The occupant of the green house lives directly to the left of the golf enthusiast.
3. The occupant of the green house and whoever lives in the yellow house live two houses apart.
4. The German lives next to the person who enjoys golf.
5. The person in the yellow house is the Swede.
6. The person who drinks coffee lives immediately to the right of the person who drinks milk.
7. The painting enthusiast lives directly to the left of the occupant of the white house.
8. Whoever lives in the green house either enjoys chess or enjoys painting.
9. The Dane enjoys painting.
10. The German drinks milk.
11. The water drinker lives in house 2.
12. The person who drinks juice enjoys tennis.
13. The occupant of the yellow house lives immediately to the right of the Norwegian.

## Puzzle plain:zebra-00057

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Swede, Spaniard, Norwegian, Dane
- drink: juice, coffee, cocoa, water, tea
- hobby: tennis, hiking, painting, cooking, chess
- job: farmer, teacher, doctor, baker, lawyer

Clues:
1. The person who enjoys hiking and the tennis enthusiast live two houses apart.
2. The person who drinks cocoa is the Norwegian.
3. The chess enthusiast either is the Norwegian or is the Spaniard.
4. The water drinker is the Dane.
5. The farmer drinks juice.
6. The tennis enthusiast works as the teacher.
7. The baker and the painting enthusiast live in adjacent houses.
8. There is exactly one house between the hiking enthusiast and the juice drinker.
9. The chess enthusiast lives directly to the left of the coffee drinker.
10. The juice drinker lives immediately to the right of the Brit.
11. The Spaniard lives at one end of the row.
12. The baker does not live next to the lawyer.

## Puzzle paraphrase:zebra-00172

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, dog, fish, cat, bird
- job: lawyer, pilot, doctor, baker, teacher
- nationality: Swede, Norwegian, German, Brit, Dane
- color: blue, yellow, white, red, purple

Clues:
1. The occupant of the yellow house is the doctor.
2. The German is not a neighbour of the pilot.
3. The cat owner lives in either the blue house or the white house.
4. Two houses separate the red house from the yellow house.
5. The dog owner lives immediately to the left of the yellow house's occupant.
6. The bird owner lives somewhere to the left of the Dane.
7. The lawyer and the occupant of the white house have exactly one house between them.
8. The fish owner lives immediately to the right of the teacher.
9. One house lies between the Brit and the pilot.
10. The lawyer and the Norwegian have exactly one house between them.
11. The Brit and the Dane do not live next to each other.
12. The rabbit owner lives in house 2.
13. Immediately to the right of the Norwegian is the purple house.

## Puzzle hard:zebra_hard-00062

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, German, Brit, Norwegian, Dane
- color: white, blue, purple, red, yellow
- drink: juice, water, coffee, cocoa, tea
- hobby: cooking, golf, painting, hiking, tennis

Clues:
1. The coffee drinker lives somewhere between the cooking enthusiast and the person who enjoys tennis.
2. Whoever lives in the blue house lives somewhere between the German and the Spaniard.
3. Neither the Dane nor the person who enjoys golf lives in the red house.
4. Exactly one house separates the person who enjoys painting from the occupant of the yellow house.
5. If the person who drinks juice does not enjoy painting, then that person enjoys tennis.
6. The left-hand neighbour of the Norwegian enjoys cooking.
7. The person who enjoys cooking lives further to the right than the German.
8. The occupant of the red house and the tea drinker are one and the same person.
9. The juice drinker lives somewhere between the cocoa drinker and whoever lives in the white house.
10. The occupant of the white house lives somewhere between the person in the blue house and the German.
11. The occupant of the blue house does not live to the right of the person in the red house.
12. The right-hand neighbour of the Dane drinks cocoa.

## Puzzle paraphrase:zebra-00117

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, cocoa, water, juice, coffee
- pet: rabbit, dog, bird, cat, fish
- hobby: hiking, painting, chess, cooking, tennis
- job: lawyer, pilot, teacher, baker, farmer

Clues:
1. The chess enthusiast lives in house 5.
2. The baker is the tea drinker.
3. The cooking enthusiast lives immediately to the right of the cocoa drinker.
4. The bird owner drinks either coffee or water.
5. The cat keeper and the pilot are two houses apart.
6. The bird owner lives directly to the right of the fish owner.
7. The farmer drinks either coffee or juice.
8. The fish owner lives immediately to the right of the dog keeper.
9. The coffee drinker and the hiking enthusiast have exactly one house between them.
10. The lawyer lives directly to the left of the pilot.
11. The baker is the tennis enthusiast.
12. The teacher does not live in the third house.
13. The bird owner is a hiking enthusiast.

## Puzzle paraphrase:zebra-00104

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, coffee, tea, water, milk
- nationality: Swede, Spaniard, Dane, Norwegian, German
- hobby: chess, painting, golf, tennis, cooking
- color: blue, red, yellow, white, purple

Clues:
1. The red house's occupant and the Spaniard live in neighbouring houses.
2. The milk drinker and the occupant of the white house live two houses apart.
3. The Norwegian lives right next to the Spaniard, on the right.
4. The cooking enthusiast lives next door to the German.
5. The coffee drinker lives immediately to the right of the German.
6. The coffee drinker is not a neighbour of the water drinker.
7. The coffee drinker and the golf enthusiast do not live next door to each other.
8. The Norwegian lives in house 5.
9. The milk drinker's hobby is either chess or cooking.
10. The Dane lives immediately to the left of the blue house's occupant.
11. The cocoa drinker lives in the leftmost house.
12. The yellow house's occupant enjoys painting.
13. The painting enthusiast lives immediately to the left of the water drinker.
14. The occupant of the red house drinks water.
