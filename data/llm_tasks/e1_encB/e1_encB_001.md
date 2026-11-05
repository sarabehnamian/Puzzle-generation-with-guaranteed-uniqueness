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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_001.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00171

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Dane, German, Spaniard, Swede
- color: blue, purple, white, green, yellow
- drink: coffee, cocoa, tea, water, milk
- job: baker, farmer, lawyer, doctor, pilot

Clues:
1. The Dane is the one who drinks tea.
2. The resident of the blue house is either the Dane or the German.
3. The milk drinker lives next door to the pilot.
4. The Dane and the Spaniard live in neighbouring houses.
5. The Norwegian lives next to the purple house.
6. The resident of the yellow house is either the Dane or the Swede.
7. The doctor drinks either coffee or water.
8. The Swede lives in house 1.
9. The pilot is not the person in the green house.
10. The farmer's house has a lower number than the green house.
11. The Norwegian lives right beside the water drinker.
12. The milk drinker lives in one of the two end houses.
13. The farmer lives somewhere to the left of the yellow house.
14. The green house's occupant does not drink cocoa.
15. The baker lives next door to the white house.
16. The doctor and the Spaniard are next-door neighbours.

## Puzzle hard:zebra_hard-00020

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, cat, fish, bird, rabbit
- nationality: Spaniard, Brit, German, Dane, Swede
- drink: water, tea, coffee, cocoa, milk
- color: white, yellow, purple, blue, red

Clues:
1. The person who keeps the bird lives two doors away from the occupant of the purple house.
2. The left-hand neighbour of the cat owner lives in the red house.
3. The person who drinks cocoa and the Dane are one and the same person.
4. The owner of the fish and the person who drinks tea are one and the same person.
5. The person who drinks water has only one neighbour.
6. The Brit lives in the fifth house from the right.
7. Neither the bird owner nor whoever lives in the red house is the Dane.
8. The person who drinks water lives further to the right than the person in the yellow house.
9. The person who drinks coffee and the person in the yellow house are one and the same person.
10. Whoever lives in the blue house lives in the fifth house from the right.
11. The person who drinks milk lives somewhere between the person who drinks water and the occupant of the yellow house.
12. One of the neighbours of the German is the Brit.
13. The Swede lives somewhere between the bird owner and the owner of the horse.

## Puzzle paraphrase:zebra-00120

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, white, yellow, purple, red
- nationality: Brit, Dane, German, Spaniard, Swede
- job: baker, pilot, doctor, farmer, teacher
- drink: juice, tea, water, coffee, cocoa

Clues:
1. The green house and the Spaniard's home are next door to each other.
2. The Dane is a pilot by trade.
3. The white house stands immediately to the left of the Brit's house.
4. The German's drink is tea.
5. The white house is at one of the two ends of the row.
6. The coffee drinker is the farmer.
7. The teacher lives right next door to the German, on his right.
8. The water drinker's house is immediately to the left of the juice drinker's house.
9. The Brit is the one who drinks water.
10. The red house is somewhere to the left of the baker's house.
11. The occupant of the red house is either the baker or the doctor.
12. The purple house is not house 3.

## Puzzle plain:zebra-00043

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, coffee, tea, water, juice
- job: farmer, teacher, pilot, lawyer, doctor
- color: white, green, yellow, red, purple
- pet: dog, cat, horse, rabbit, fish

Clues:
1. The person who drinks cocoa either lives in the green house or lives in the purple house.
2. The tea drinker either lives in the white house or lives in the yellow house.
3. The person who drinks water lives immediately to the right of the farmer.
4. The pilot and the tea drinker live in adjacent houses.
5. The occupant of the green house and the teacher live in adjacent houses.
6. The person who keeps the horse either works as the farmer or works as the teacher.
7. The owner of the fish works as the doctor.
8. The owner of the fish lives in the yellow house.
9. The person who drinks juice and the person in the white house are neighbours.
10. The person who keeps the rabbit and the tea drinker live two houses apart.
11. The person in the purple house lives somewhere to the left of the owner of the dog.
12. Whoever lives in the white house lives directly to the left of the farmer.
13. The person who keeps the horse lives immediately to the right of the doctor.

## Puzzle plain:zebra-00023

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, cat, horse, rabbit, bird
- color: yellow, purple, white, red, blue
- hobby: tennis, chess, cooking, golf, hiking
- nationality: Dane, Norwegian, Brit, Spaniard, Swede

Clues:
1. The Swede enjoys golf.
2. The Dane lives somewhere to the left of the person who keeps the cat.
3. The person in the yellow house lives in the fourth house.
4. The hiking enthusiast does not live in the fourth house.
5. The owner of the rabbit lives somewhere to the right of the person in the purple house.
6. The dog owner lives directly to the left of the owner of the rabbit.
7. The hiking enthusiast lives somewhere to the left of the person in the red house.
8. The Spaniard lives in the house just left of the one where the occupant of the blue house lives.
9. The person who enjoys chess lives in the second house.
10. The Spaniard lives at one end of the row.
11. The hiking enthusiast lives directly to the left of the Brit.
12. The Dane lives next to the occupant of the purple house.
13. The horse owner and the person in the red house live in adjacent houses.
14. The person who enjoys cooking lives directly to the left of the person who keeps the dog.

## Puzzle paraphrase:zebra-00133

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Spaniard, Swede, German, Dane
- drink: tea, water, juice, milk, cocoa
- pet: horse, rabbit, dog, cat, bird
- job: doctor, lawyer, farmer, teacher, baker

Clues:
1. The Swede keeps the dog.
2. The baker lives directly to the left of the horse owner.
3. The Swede is the milk drinker.
4. The bird owner lives right next to the Swede.
5. The bird owner is the lawyer.
6. The doctor is either the Dane or the Swede.
7. The farmer lives immediately to the left of the dog owner.
8. The lawyer lives somewhere to the left of the cocoa drinker.
9. The German lives immediately to the left of the juice drinker.
10. One house separates the Norwegian from the Swede.
11. The doctor lives in the fifth house.
12. The farmer drinks water.
13. The cat's owner is the baker.

## Puzzle hard:zebra_hard-00091

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, chess, painting, tennis, golf
- pet: horse, rabbit, cat, dog, fish
- job: farmer, pilot, lawyer, doctor, teacher
- nationality: Dane, Spaniard, Norwegian, Swede, German

Clues:
1. Neither the Norwegian nor the Spaniard enjoys painting.
2. The dog owner lives further to the right than the person who enjoys tennis.
3. The pilot does not live in the third house from the right.
4. The person who keeps the fish and the teacher are one and the same person.
5. The Norwegian lives somewhere between the Dane and the tennis enthusiast.
6. The left-hand neighbour of the person who keeps the fish works as the doctor.
7. The right-hand neighbour of the cat owner works as the lawyer.
8. Exactly 4 houses lie to the left of the home of the rabbit owner.
9. The chess enthusiast and the Spaniard are one and the same person.
10. The person who enjoys hiking lives two doors away from the Norwegian.
11. The person who enjoys golf lives further to the right than the German.
12. Exactly 4 houses lie to the left of the home of the Spaniard.
13. The German and the person who enjoys hiking are one and the same person.
14. The dog owner and the lawyer are one and the same person.

## Puzzle paraphrase:zebra-00147

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, golf, hiking, tennis, chess
- nationality: German, Swede, Norwegian, Spaniard, Dane
- pet: horse, fish, dog, bird, cat
- color: purple, green, yellow, blue, white

Clues:
1. The fish owner lives in the yellow house.
2. Chess is the hobby of the bird owner.
3. The Dane lives immediately left of the horse owner.
4. The Norwegian lives somewhere to the right of the green house.
5. The cooking enthusiast lives somewhere right of the bird owner.
6. The cat owner is not the Norwegian.
7. The dog owner lives immediately left of the Swede.
8. The horse owner and the white house's occupant are neighbours.
9. The Norwegian and the yellow house's occupant are next-door neighbours.
10. The hiking enthusiast lives next to the purple house.
11. The German lives directly left of the fish owner.
12. Cooking is the Spaniard's hobby.
13. The tennis enthusiast lives in the third house.

## Puzzle plain:zebra-00076

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, lawyer, farmer, baker, pilot
- nationality: Spaniard, Norwegian, Swede, German, Brit
- drink: milk, tea, water, juice, coffee
- color: green, purple, blue, white, red

Clues:
1. The milk drinker lives in the house just left of the one where the tea drinker lives.
2. The occupant of the blue house lives immediately to the right of the Swede.
3. The baker lives in the blue house.
4. The Swede and the tea drinker live in adjacent houses.
5. Whoever lives in the white house either drinks milk or drinks water.
6. Whoever lives in the purple house lives immediately to the right of the milk drinker.
7. The Brit lives in the red house.
8. The farmer and the milk drinker live two houses apart.
9. The German lives in the last house.
10. The lawyer is the Norwegian.
11. The person who drinks coffee and the Swede are neighbours.
12. The Brit lives directly to the left of the occupant of the green house.
13. The doctor either is the Brit or is the German.
14. There is exactly one house between the Norwegian and the water drinker.

## Puzzle paraphrase:zebra-00102

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, painting, chess, hiking, golf
- pet: cat, bird, dog, fish, rabbit
- job: doctor, farmer, teacher, lawyer, pilot
- nationality: Dane, German, Spaniard, Norwegian, Swede

Clues:
1. The golf enthusiast is the Norwegian.
2. The fish owner lives somewhere to the left of the pilot.
3. The cat owner and the German live two houses apart.
4. The bird owner lives in the last house.
5. The cat owner's hobby is either golf or hiking.
6. The rabbit owner lives immediately to the left of the doctor.
7. The farmer lives next door to the tennis enthusiast.
8. The Swede is the doctor.
9. The Dane is a lawyer by profession.
10. The Spaniard lives in house 2.
11. The bird owner and the chess enthusiast are neighbours.
12. The German is the farmer.
13. The Swede owns the dog.
