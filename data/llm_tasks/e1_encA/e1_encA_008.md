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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_008.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00009

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, horse, cat, rabbit, dog
- job: baker, doctor, farmer, teacher, pilot
- drink: tea, cocoa, coffee, milk, juice
- hobby: chess, hiking, painting, tennis, golf

Clues:
1. The tea drinker lives somewhere between the fish owner and the tennis enthusiast.
2. Neither the cocoa drinker nor the pilot keeps the dog.
3. One of the neighbours of the person who drinks juice keeps the rabbit.
4. At least one house separates the owner of the horse from the fish owner.
5. If the owner of the dog is not the doctor, then that person works as the teacher.
6. The right-hand neighbour of the person who drinks tea enjoys golf.
7. The person who keeps the fish and the teacher are one and the same person.
8. The fish owner lives somewhere between the baker and the chess enthusiast.
9. The right-hand neighbour of the person who enjoys tennis works as the baker.
10. If the farmer does not enjoy chess, then that person enjoys tennis.
11. Exactly 0 houses lie to the left of the home of the dog owner.
12. The left-hand neighbour of the painting enthusiast enjoys hiking.
13. The left-hand neighbour of the milk drinker keeps the rabbit.

## Puzzle hard:zebra_hard-00046

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, cat, rabbit, fish, horse
- drink: juice, water, tea, coffee, milk
- job: lawyer, farmer, teacher, pilot, baker
- hobby: cooking, tennis, hiking, chess, painting

Clues:
1. The person who keeps the bird has only one neighbour.
2. The lawyer and the owner of the rabbit are one and the same person.
3. The left-hand neighbour of the person who drinks tea works as the lawyer.
4. The right-hand neighbour of the pilot drinks coffee.
5. If the person who enjoys tennis does not drink coffee, then that person drinks water.
6. One of the neighbours of the chess enthusiast enjoys tennis.
7. The coffee drinker lives in the third house from the right.
8. The person who keeps the cat lives somewhere between the person who enjoys chess and the hiking enthusiast.
9. The person who drinks juice and the painting enthusiast are one and the same person.
10. Neither the owner of the bird nor the person who drinks milk works as the baker.
11. If the person who keeps the fish does not enjoy chess, then that person enjoys cooking.
12. The tennis enthusiast lives somewhere between the milk drinker and the teacher.
13. One of the neighbours of the painting enthusiast works as the farmer.
14. The person who enjoys hiking lives two doors away from the pilot.

## Puzzle plain:zebra-00075

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, teacher, baker, pilot
- color: yellow, white, red, green, blue
- hobby: golf, painting, tennis, hiking, cooking
- nationality: Brit, Norwegian, Swede, Spaniard, Dane

Clues:
1. The doctor does not live next to whoever lives in the yellow house.
2. The pilot lives immediately to the right of the tennis enthusiast.
3. Whoever lives in the red house lives somewhere to the right of the baker.
4. The golf enthusiast lives in the red house.
5. There is exactly one house between the hiking enthusiast and the lawyer.
6. Whoever lives in the blue house lives in the house just left of the one where the person in the red house lives.
7. The Dane lives in the house just left of the one where the Swede lives.
8. The person who enjoys painting and the person in the white house live in adjacent houses.
9. Whoever lives in the white house either is the Brit or is the Swede.
10. The doctor lives in the house just left of the one where the pilot lives.
11. The baker lives at one end of the row.
12. The Brit lives somewhere to the left of the golf enthusiast.
13. The Norwegian lives directly to the left of the lawyer.
14. The person who enjoys cooking lives directly to the left of the person who enjoys golf.

## Puzzle hard:zebra_hard-00063

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, coffee, juice, cocoa
- pet: fish, rabbit, dog, bird, horse
- hobby: chess, tennis, cooking, hiking, golf
- color: red, blue, green, purple, white

Clues:
1. Whoever lives in the white house lives somewhere between the bird owner and the occupant of the purple house.
2. Exactly one house separates the person who keeps the bird from the juice drinker.
3. If the person in the purple house does not keep the bird, then that person keeps the dog.
4. Exactly 3 houses lie to the left of the home of the milk drinker.
5. The cocoa drinker is not the same person as the cooking enthusiast.
6. None of the neighbours of the fish owner drinks juice.
7. The person in the green house lives two doors away from whoever lives in the white house.
8. The person who keeps the bird lives somewhere between the coffee drinker and the juice drinker.
9. The occupant of the white house lives somewhere between the person who drinks cocoa and the golf enthusiast.
10. Exactly 3 houses lie to the left of the home of the tennis enthusiast.
11. The person who enjoys chess lives in the fourth house from the right.
12. One of the neighbours of the person who drinks water lives in the red house.
13. The left-hand neighbour of the owner of the fish lives in the purple house.
14. One of the neighbours of the owner of the horse lives in the green house.

## Puzzle paraphrase:zebra-00173

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, farmer, baker, lawyer, teacher
- pet: rabbit, bird, fish, cat, horse
- drink: cocoa, coffee, tea, water, milk
- nationality: Swede, Spaniard, Norwegian, German, Brit

Clues:
1. The Swede does not live in house 5.
2. The German lives immediately to the left of the coffee drinker.
3. The doctor and the tea drinker are two houses apart.
4. The farmer is not the Spaniard.
5. The Spaniard is the horse keeper.
6. The Brit is the doctor.
7. The teacher lives immediately to the left of the Norwegian.
8. The cocoa drinker is the lawyer.
9. The cat owner does not live next door to the fish owner.
10. The Norwegian lives immediately to the left of the water drinker.
11. One house lies between the bird owner and the cat owner.
12. The Norwegian keeps the rabbit.
13. The tea drinker lives in the fifth house.

## Puzzle hard:zebra_hard-00030

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, cocoa, juice, water, milk
- color: white, red, blue, yellow, green
- job: lawyer, teacher, pilot, farmer, doctor
- nationality: Swede, Dane, Norwegian, Brit, German

Clues:
1. The occupant of the white house has only one neighbour.
2. The occupant of the yellow house lives somewhere between the person who drinks milk and the person in the red house.
3. The juice drinker and the occupant of the yellow house are one and the same person.
4. The doctor is not the same person as the person who drinks tea.
5. The left-hand neighbour of the pilot is the Brit.
6. None of the neighbours of the person in the red house lives in the green house.
7. The Brit and the person who drinks tea are one and the same person.
8. The water drinker lives further to the right than the Norwegian.
9. Whoever lives in the red house lives in the fifth house from the right.
10. The Dane and the teacher are one and the same person.
11. The Dane and the person in the yellow house are one and the same person.
12. One of the neighbours of the doctor is the German.
13. The left-hand neighbour of the lawyer lives in the yellow house.
14. The right-hand neighbour of the person who drinks juice drinks water.

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

## Puzzle plain:zebra-00097

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, golf, tennis, hiking, painting
- pet: bird, rabbit, horse, dog, fish
- nationality: Spaniard, Brit, Swede, Norwegian, German
- color: green, purple, blue, white, red

Clues:
1. The person who enjoys cooking lives in the house just left of the one where the owner of the fish lives.
2. The Brit lives in the purple house.
3. The Swede lives immediately to the right of the painting enthusiast.
4. The person who keeps the rabbit and the tennis enthusiast are not neighbours.
5. The person who keeps the bird lives somewhere to the right of the Spaniard.
6. The person who keeps the fish lives somewhere to the right of the rabbit owner.
7. The golf enthusiast either keeps the dog or keeps the fish.
8. The person in the red house lives directly to the left of the Brit.
9. The Spaniard keeps the horse.
10. The German lives in house 2.
11. The person who enjoys cooking and the person who enjoys tennis live in adjacent houses.
12. The owner of the dog lives immediately to the right of the person in the purple house.
13. The occupant of the white house lives in the house just left of the one where the cooking enthusiast lives.
14. The Norwegian lives in the green house.

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

## Puzzle hard:zebra_hard-00096

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, German, Swede, Spaniard, Norwegian
- job: baker, pilot, teacher, farmer, doctor
- pet: fish, horse, bird, cat, rabbit
- color: red, white, blue, yellow, purple

Clues:
1. The right-hand neighbour of the person who keeps the fish works as the doctor.
2. The left-hand neighbour of the German lives in the yellow house.
3. The occupant of the blue house and the German are one and the same person.
4. One of the neighbours of the Dane works as the teacher.
5. The occupant of the white house does not live in the fifth house from the right.
6. The person who keeps the horse and the Norwegian are one and the same person.
7. Exactly one house separates the occupant of the blue house from the rabbit owner.
8. Exactly one house separates the occupant of the purple house from whoever lives in the white house.
9. The right-hand neighbour of the horse owner is the German.
10. Exactly 0 houses lie to the left of the home of the Dane.
11. One of the neighbours of the person in the red house is the Swede.
12. The pilot lives somewhere between the person who keeps the bird and the German.
13. The rabbit owner lives further to the right than the farmer.
