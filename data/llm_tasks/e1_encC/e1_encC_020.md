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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_020.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00009

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, hiking, cooking, tennis, golf
- pet: rabbit, dog, cat, bird, fish
- color: red, yellow, blue, purple, green
- drink: juice, water, milk, tea, coffee

Clues:
1. The person who drinks coffee and the tea drinker live two houses apart.
2. The cat owner and the person in the purple house live in adjacent houses.
3. The owner of the cat lives in the fourth house.
4. The person who drinks tea lives somewhere to the right of the occupant of the blue house.
5. The fish owner lives in the leftmost house.
6. The occupant of the green house enjoys chess.
7. The occupant of the green house either drinks coffee or drinks milk.
8. The tennis enthusiast either keeps the cat or keeps the dog.
9. There is exactly one house between the person who enjoys golf and the person in the green house.
10. The person who drinks juice enjoys cooking.
11. The person who drinks juice keeps the rabbit.
12. The person who drinks milk either keeps the cat or keeps the dog.
13. The person in the red house lives directly to the left of the tea drinker.
14. The water drinker keeps the cat.

## Puzzle hard:zebra_hard-00023

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, farmer, lawyer, baker
- color: red, yellow, purple, green, white
- drink: juice, tea, milk, coffee, cocoa
- pet: fish, bird, horse, dog, rabbit

Clues:
1. The teacher lives further to the right than the person in the red house.
2. One of the neighbours of the person who drinks milk lives in the green house.
3. The lawyer lives two doors away from the person who drinks tea.
4. Whoever lives in the green house and the rabbit owner are one and the same person.
5. The cocoa drinker and the owner of the fish are one and the same person.
6. The person in the green house has only one neighbour.
7. The farmer lives in the second house from the right.
8. The dog owner does not live to the right of the person who keeps the fish.
9. The person who keeps the fish and whoever lives in the yellow house are one and the same person.
10. The person who keeps the bird lives in the fourth house from the right.
11. The tea drinker and the occupant of the white house are one and the same person.
12. The right-hand neighbour of the baker drinks cocoa.
13. If whoever lives in the red house does not drink cocoa, then that person drinks coffee.

## Puzzle paraphrase:zebra-00153

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, pilot, farmer, teacher, baker
- nationality: Spaniard, German, Norwegian, Brit, Swede
- hobby: hiking, golf, tennis, painting, chess
- drink: water, milk, tea, cocoa, coffee

Clues:
1. The hiker lives directly to the left of the milk drinker.
2. The farmer and the Norwegian are next-door neighbours.
3. House 4 belongs to the water drinker.
4. The tennis player lives immediately to the left of the chess player.
5. The coffee drinker's hobby is chess.
6. The Brit lives directly to the left of the coffee drinker.
7. The baker is the one who drinks tea.
8. The lawyer and the pilot live next door to each other.
9. One house lies between the German and the teacher.
10. The painter and the tea drinker live two houses apart.
11. The milk drinker lives immediately to the left of the teacher.
12. The Swede lives directly to the right of the pilot.

## Puzzle hard:zebra_hard-00071

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, tennis, cooking, chess, hiking
- nationality: Norwegian, Dane, Swede, Brit, Spaniard
- color: red, yellow, blue, green, white
- drink: coffee, cocoa, water, juice, milk

Clues:
1. If the person in the green house does not enjoy cooking, then that person enjoys golf.
2. The Brit lives two doors away from the person who drinks water.
3. Neither the Brit nor the water drinker lives in the red house.
4. One of the neighbours of the person in the blue house is the Spaniard.
5. The chess enthusiast and the Norwegian are one and the same person.
6. The right-hand neighbour of the hiking enthusiast is the Norwegian.
7. The person who enjoys cooking is not the same person as the Spaniard.
8. The chess enthusiast lives further to the right than the person in the red house.
9. One of the neighbours of the occupant of the yellow house enjoys tennis.
10. The milk drinker lives somewhere between the person who drinks cocoa and the Dane.
11. The Brit and the person who drinks coffee are one and the same person.
12. If the person in the green house does not drink coffee, then that person drinks milk.
13. The Brit and the person who enjoys hiking are one and the same person.
14. One of the neighbours of the person who enjoys tennis is the Dane.

## Puzzle hard:zebra_hard-00043

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, pilot, baker, lawyer
- hobby: golf, chess, tennis, hiking, cooking
- pet: fish, rabbit, dog, bird, horse
- nationality: Brit, Swede, Spaniard, Norwegian, German

Clues:
1. Exactly 2 houses lie to the left of the home of the bird owner.
2. The right-hand neighbour of the tennis enthusiast enjoys chess.
3. If the teacher does not enjoy chess, then that person enjoys cooking.
4. One of the neighbours of the German works as the doctor.
5. The right-hand neighbour of the teacher is the Brit.
6. The left-hand neighbour of the person who enjoys cooking enjoys chess.
7. Exactly one house separates the fish owner from the person who keeps the horse.
8. Neither the Brit nor the pilot enjoys golf.
9. The Spaniard lives somewhere between the person who keeps the dog and the Norwegian.
10. Exactly 4 houses lie to the left of the home of the German.
11. The horse owner lives somewhere between the person who keeps the dog and the fish owner.
12. The person who keeps the horse and the lawyer are one and the same person.
13. Neither the owner of the bird nor the owner of the horse enjoys tennis.

## Puzzle hard:zebra_hard-00041

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Brit, German, Dane, Swede
- color: yellow, blue, green, purple, red
- hobby: cooking, painting, hiking, golf, tennis
- drink: cocoa, tea, milk, juice, water

Clues:
1. The occupant of the red house lives further to the right than the hiking enthusiast.
2. The right-hand neighbour of the German drinks tea.
3. Neither the occupant of the blue house nor the person who enjoys golf drinks juice.
4. The person who enjoys golf and the tea drinker are one and the same person.
5. Whoever lives in the blue house and the Dane are one and the same person.
6. The cocoa drinker and the German are one and the same person.
7. One of the neighbours of the person who enjoys painting lives in the green house.
8. Exactly 1 house lies to the left of the home of the person who enjoys cooking.
9. Exactly one house separates the person who enjoys hiking from the Swede.
10. None of the neighbours of the hiking enthusiast lives in the yellow house.
11. The water drinker lives in the second house from the right.
12. One of the neighbours of the Swede is the Norwegian.
13. The person in the green house does not live in the third house from the right.
14. The left-hand neighbour of the person in the red house is the Norwegian.

## Puzzle hard:zebra_hard-00050

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, cooking, painting, golf, hiking
- job: pilot, lawyer, farmer, doctor, teacher
- pet: bird, rabbit, fish, horse, dog
- drink: tea, cocoa, water, milk, coffee

Clues:
1. The left-hand neighbour of the horse owner works as the doctor.
2. If the tea drinker is not the doctor, then that person works as the lawyer.
3. The person who enjoys cooking lives in the rightmost house.
4. The lawyer lives somewhere between the owner of the bird and the person who keeps the rabbit.
5. The right-hand neighbour of the milk drinker enjoys hiking.
6. The person who enjoys cooking and the pilot are one and the same person.
7. Neither the farmer nor the person who drinks tea enjoys tennis.
8. The owner of the bird and the person who drinks tea are one and the same person.
9. The left-hand neighbour of the lawyer enjoys golf.
10. One of the neighbours of the owner of the bird keeps the fish.
11. The person who keeps the bird lives two doors away from the lawyer.
12. Exactly 0 houses lie to the left of the home of the person who drinks coffee.
13. The person who drinks cocoa and the teacher are one and the same person.

## Puzzle hard:zebra_hard-00051

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Brit, Swede, Spaniard, Dane
- color: purple, green, yellow, blue, white
- job: teacher, pilot, farmer, lawyer, baker
- hobby: cooking, painting, golf, tennis, hiking

Clues:
1. One of the neighbours of the Brit works as the baker.
2. If the person who enjoys painting is not the farmer, then that person works as the lawyer.
3. If whoever lives in the white house is not the Dane, then that person is the Swede.
4. None of the neighbours of the baker lives in the blue house.
5. At least one house separates the occupant of the green house from the occupant of the yellow house.
6. The left-hand neighbour of the pilot enjoys tennis.
7. The left-hand neighbour of the lawyer is the Dane.
8. The person who enjoys cooking and the occupant of the white house are one and the same person.
9. The left-hand neighbour of the person who enjoys tennis works as the baker.
10. The person who enjoys hiking is not the same person as the pilot.
11. Neither the Brit nor the Spaniard enjoys tennis.
12. One of the neighbours of the person who enjoys cooking is the Swede.
13. Neither the cooking enthusiast nor the pilot is the Norwegian.
14. The farmer lives further to the right than the cooking enthusiast.
15. The person in the yellow house lives somewhere between whoever lives in the green house and the occupant of the white house.

## Puzzle hard:zebra_hard-00037

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Swede, Spaniard, Dane, Norwegian
- hobby: tennis, cooking, chess, golf, hiking
- pet: fish, horse, cat, bird, rabbit
- drink: tea, coffee, water, milk, juice

Clues:
1. The juice drinker and the person who keeps the rabbit are one and the same person.
2. The right-hand neighbour of the Spaniard is the Swede.
3. If the person who drinks coffee does not enjoy golf, then that person enjoys hiking.
4. The left-hand neighbour of the owner of the horse keeps the cat.
5. The person who drinks juice and the Spaniard are one and the same person.
6. The owner of the cat and the person who enjoys cooking are one and the same person.
7. The left-hand neighbour of the bird owner is the Spaniard.
8. The left-hand neighbour of the Norwegian drinks tea.
9. The chess enthusiast and the tea drinker are one and the same person.
10. The tennis enthusiast has only one neighbour.
11. The Spaniard lives somewhere between the coffee drinker and the water drinker.
12. The German and the water drinker are one and the same person.
13. The person who enjoys golf lives further to the right than the Spaniard.

## Puzzle hard:zebra_hard-00079

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, pilot, baker, teacher
- pet: fish, bird, rabbit, horse, cat
- hobby: tennis, chess, painting, cooking, hiking
- color: red, yellow, white, purple, blue

Clues:
1. If the occupant of the yellow house does not enjoy cooking, then that person enjoys tennis.
2. Exactly one house separates the person who keeps the rabbit from whoever lives in the yellow house.
3. If the cat owner is not the baker, then that person works as the lawyer.
4. The occupant of the yellow house lives in the fourth house from the right.
5. One of the neighbours of the person who keeps the horse lives in the purple house.
6. The person who enjoys tennis lives somewhere between the owner of the bird and whoever lives in the blue house.
7. The person who enjoys painting and whoever lives in the red house are one and the same person.
8. The teacher lives further to the right than the owner of the fish.
9. One of the neighbours of the person who enjoys chess keeps the fish.
10. The right-hand neighbour of whoever lives in the yellow house enjoys painting.
11. The doctor and whoever lives in the white house are one and the same person.
12. The owner of the cat and the cooking enthusiast are one and the same person.
13. The baker and the painting enthusiast are one and the same person.
