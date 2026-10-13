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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_022.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00047

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, painting, chess, golf, hiking
- color: white, red, purple, blue, yellow
- nationality: Brit, German, Spaniard, Dane, Norwegian
- pet: horse, bird, rabbit, dog, cat

Clues:
1. Exactly one house separates the person who enjoys painting from the Spaniard.
2. The left-hand neighbour of the owner of the horse enjoys painting.
3. Exactly 4 houses lie to the left of the home of the owner of the cat.
4. The person in the red house lives somewhere between the person who enjoys hiking and the horse owner.
5. If the tennis enthusiast does not live in the purple house, then that person lives in the yellow house.
6. The Norwegian and the person in the white house are one and the same person.
7. The person who enjoys chess and the Norwegian are one and the same person.
8. The left-hand neighbour of the Dane keeps the rabbit.
9. The German and the occupant of the purple house are one and the same person.
10. Exactly one house separates the painting enthusiast from the owner of the rabbit.
11. The Norwegian lives two doors away from the person in the yellow house.
12. Neither the occupant of the blue house nor the Brit keeps the dog.
13. The Brit lives in the fourth house from the right.
14. The right-hand neighbour of the person in the red house is the Norwegian.

## Puzzle hard:zebra_hard-00018

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, red, blue, white, purple
- job: pilot, doctor, farmer, baker, lawyer
- hobby: hiking, cooking, chess, tennis, golf
- nationality: Dane, Swede, Norwegian, Brit, German

Clues:
1. Neither the person who enjoys chess nor the cooking enthusiast is the Brit.
2. One of the neighbours of the person who enjoys cooking works as the pilot.
3. The Swede does not live to the right of the Norwegian.
4. The left-hand neighbour of the occupant of the purple house is the Dane.
5. The left-hand neighbour of the lawyer enjoys hiking.
6. The lawyer lives further to the right than the Dane.
7. If the German is not the baker, then that person works as the farmer.
8. The person who enjoys chess and the person in the green house are one and the same person.
9. Whoever lives in the green house lives somewhere between whoever lives in the purple house and the tennis enthusiast.
10. One of the neighbours of the baker is the Brit.
11. The German lives somewhere between the Dane and whoever lives in the white house.
12. The right-hand neighbour of the pilot works as the lawyer.
13. The left-hand neighbour of the person who enjoys golf lives in the blue house.
14. One of the neighbours of the Swede lives in the blue house.
15. One of the neighbours of the German enjoys chess.

## Puzzle plain:zebra-00000

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, dog, bird, fish, rabbit
- job: farmer, teacher, baker, doctor, lawyer
- hobby: golf, tennis, chess, hiking, cooking
- nationality: Brit, German, Spaniard, Norwegian, Swede

Clues:
1. The Spaniard lives in the house just left of the one where the hiking enthusiast lives.
2. The German lives next to the teacher.
3. The baker keeps the rabbit.
4. The tennis enthusiast lives in house 4.
5. The Norwegian keeps the rabbit.
6. The person who keeps the bird and the person who enjoys golf are neighbours.
7. The cooking enthusiast and the German live two houses apart.
8. The lawyer lives directly to the left of the farmer.
9. The owner of the bird works as the teacher.
10. The cooking enthusiast and the person who keeps the dog are neighbours.
11. There is exactly one house between the farmer and the horse owner.
12. The Swede lives in the house just left of the one where the horse owner lives.

## Puzzle paraphrase:zebra-00125

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, juice, coffee, water, milk
- pet: rabbit, horse, dog, fish, bird
- color: red, green, blue, yellow, white
- hobby: hiking, golf, cooking, chess, tennis

Clues:
1. The milk drinker is the bird keeper.
2. The green house stands immediately to the right of the milk drinker.
3. The tea drinker lives somewhere to the left of the dog keeper.
4. The coffee drinker lives directly to the left of the white house.
5. The white house's occupant keeps either the dog or the rabbit.
6. The golf enthusiast keeps the rabbit.
7. The occupant of the white house enjoys hiking.
8. The cooking enthusiast lives next door to the hiking enthusiast.
9. The rabbit owner drinks coffee.
10. The blue house stands immediately to the right of the green house.
11. The tennis enthusiast lives directly to the left of the rabbit owner.
12. The yellow house's occupant is not the fish owner.
13. The fish owner drinks water.

## Puzzle hard:zebra_hard-00022

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, coffee, juice, cocoa, water
- pet: fish, horse, cat, bird, dog
- nationality: Brit, Dane, Swede, Norwegian, Spaniard
- hobby: golf, tennis, painting, hiking, cooking

Clues:
1. One of the neighbours of the fish owner drinks water.
2. The person who drinks cocoa lives two doors away from the milk drinker.
3. None of the neighbours of the Spaniard enjoys tennis.
4. The right-hand neighbour of the tennis enthusiast is the Swede.
5. The fish owner lives further to the right than the cooking enthusiast.
6. Exactly one house separates the cat owner from the painting enthusiast.
7. Neither the person who drinks coffee nor the person who enjoys hiking keeps the fish.
8. The horse owner and the water drinker are one and the same person.
9. The left-hand neighbour of the Dane drinks milk.
10. Exactly 1 house lies to the left of the home of the bird owner.
11. If the tennis enthusiast is not the Dane, then that person is the Swede.
12. The juice drinker does not live in the third house from the right.
13. The right-hand neighbour of the person who keeps the fish is the Brit.
14. Exactly one house separates the golf enthusiast from the hiking enthusiast.

## Puzzle plain:zebra-00089

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, baker, pilot, doctor, farmer
- color: red, blue, green, yellow, white
- drink: tea, cocoa, water, milk, juice
- nationality: Swede, Dane, Brit, Spaniard, German

Clues:
1. Whoever lives in the yellow house either drinks cocoa or drinks tea.
2. The German lives directly to the left of the person in the green house.
3. The farmer and the Spaniard are not neighbours.
4. The baker lives immediately to the right of the pilot.
5. The person who drinks juice lives next to the lawyer.
6. The doctor lives in the blue house.
7. The baker lives in the second house.
8. The person who drinks cocoa lives directly to the left of the person who drinks juice.
9. The German drinks tea.
10. The farmer and the person in the red house are not neighbours.
11. The Dane lives in house 2.
12. The German lives in the house just left of the one where the Brit lives.
13. The German and the person who drinks milk live two houses apart.
14. The occupant of the white house lives in house 1.

## Puzzle plain:zebra-00022

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, water, juice, tea, coffee
- pet: rabbit, cat, bird, horse, dog
- job: lawyer, pilot, farmer, teacher, doctor
- hobby: chess, cooking, painting, golf, hiking

Clues:
1. The owner of the rabbit enjoys chess.
2. The hiking enthusiast drinks cocoa.
3. The person who enjoys cooking lives in the house just left of the one where the coffee drinker lives.
4. The person who keeps the horse and the person who keeps the rabbit are not neighbours.
5. The tea drinker lives in the fifth house.
6. The dog owner lives in one of the two end houses.
7. The golf enthusiast and the juice drinker live two houses apart.
8. The doctor either keeps the bird or keeps the cat.
9. The person who keeps the bird lives in house 2.
10. The teacher lives in the house just left of the one where the cooking enthusiast lives.
11. The person who enjoys painting lives somewhere to the right of the pilot.
12. The juice drinker either works as the farmer or works as the lawyer.
13. The lawyer either enjoys chess or enjoys hiking.

## Puzzle hard:zebra_hard-00086

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, green, white, red, purple
- drink: tea, water, juice, coffee, cocoa
- hobby: chess, tennis, painting, hiking, golf
- nationality: Norwegian, Swede, Dane, German, Brit

Clues:
1. One of the neighbours of the person who enjoys tennis lives in the blue house.
2. The left-hand neighbour of the cocoa drinker enjoys chess.
3. The hiking enthusiast lives somewhere between the cocoa drinker and the person who enjoys painting.
4. The juice drinker and the tennis enthusiast are one and the same person.
5. The right-hand neighbour of the Brit is the Dane.
6. At least one house separates whoever lives in the red house from the occupant of the blue house.
7. The coffee drinker has only one neighbour.
8. The occupant of the white house has only one neighbour.
9. The left-hand neighbour of the German enjoys painting.
10. The Dane lives in the rightmost house.
11. The person in the green house and the person who drinks water are one and the same person.
12. Neither the cocoa drinker nor the occupant of the green house is the Norwegian.
13. The cocoa drinker lives somewhere between the person who enjoys tennis and the person in the white house.

## Puzzle hard:zebra_hard-00055

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, painting, chess, hiking, tennis
- drink: tea, juice, cocoa, coffee, water
- job: baker, pilot, teacher, lawyer, farmer
- nationality: German, Spaniard, Swede, Dane, Norwegian

Clues:
1. The person who enjoys golf and the person who drinks juice are one and the same person.
2. Exactly one house separates the farmer from the person who enjoys painting.
3. The farmer and the person who drinks tea are one and the same person.
4. The right-hand neighbour of the teacher is the Spaniard.
5. The left-hand neighbour of the lawyer enjoys tennis.
6. The right-hand neighbour of the farmer is the Norwegian.
7. The person who drinks juice does not live to the right of the person who drinks water.
8. The person who enjoys chess is not the same person as the Spaniard.
9. The left-hand neighbour of the Spaniard is the Swede.
10. The person who drinks cocoa and the Dane are one and the same person.
11. The cocoa drinker and the tennis enthusiast are one and the same person.
12. One of the neighbours of the pilot enjoys painting.

## Puzzle plain:zebra-00064

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Norwegian, Brit, Spaniard, Dane
- job: lawyer, baker, farmer, doctor, pilot
- color: green, purple, yellow, white, blue
- drink: coffee, cocoa, juice, milk, water

Clues:
1. The Dane and the milk drinker live in adjacent houses.
2. The occupant of the yellow house either is the Brit or is the Norwegian.
3. The occupant of the blue house and the farmer live two houses apart.
4. There is exactly one house between whoever lives in the purple house and the person who drinks water.
5. The person who drinks cocoa and the milk drinker live in adjacent houses.
6. The doctor drinks juice.
7. The Spaniard lives in house 4.
8. The baker is the German.
9. The baker and the Dane live two houses apart.
10. The person who drinks juice and the Norwegian live in adjacent houses.
11. The pilot lives in a lower-numbered house than the farmer.
12. The juice drinker lives somewhere to the right of the person in the green house.
13. The farmer and the pilot live two houses apart.
14. The Dane lives in the house just left of the one where the person who drinks coffee lives.
