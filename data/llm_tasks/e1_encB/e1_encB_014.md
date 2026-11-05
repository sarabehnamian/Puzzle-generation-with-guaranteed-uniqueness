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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_014.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00014

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, juice, cocoa, water, milk
- job: pilot, teacher, doctor, farmer, baker
- pet: fish, horse, cat, rabbit, dog
- hobby: hiking, cooking, painting, chess, tennis

Clues:
1. There is exactly one house between the baker and the person who drinks milk.
2. The pilot lives at one end of the row.
3. The person who drinks coffee enjoys tennis.
4. The juice drinker either keeps the horse or keeps the rabbit.
5. The person who drinks water works as the pilot.
6. The owner of the cat works as the baker.
7. The person who keeps the rabbit enjoys hiking.
8. The person who enjoys chess lives in one of the two end houses.
9. The coffee drinker lives at one end of the row.
10. The teacher lives in the third house.
11. The doctor lives immediately to the right of the person who keeps the rabbit.
12. The person who enjoys cooking does not live in the fourth house.
13. The person who enjoys tennis lives directly to the left of the dog owner.

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

## Puzzle hard:zebra_hard-00012

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, hiking, painting, chess, tennis
- job: lawyer, doctor, baker, teacher, pilot
- color: blue, red, yellow, green, white
- pet: cat, dog, fish, rabbit, horse

Clues:
1. The person who keeps the horse is not the same person as the tennis enthusiast.
2. The left-hand neighbour of the fish owner keeps the rabbit.
3. If the doctor does not keep the dog, then that person keeps the horse.
4. If the occupant of the white house does not enjoy painting, then that person enjoys tennis.
5. The left-hand neighbour of the person who keeps the fish works as the teacher.
6. The occupant of the white house lives somewhere between the baker and the person who keeps the dog.
7. The left-hand neighbour of the person who enjoys chess keeps the cat.
8. If the occupant of the yellow house does not keep the fish, then that person keeps the rabbit.
9. At least one house separates the person who enjoys tennis from the person who keeps the fish.
10. The person who enjoys tennis does not live to the right of the person who enjoys painting.
11. One of the neighbours of the lawyer lives in the blue house.
12. The person in the green house and the teacher are one and the same person.
13. The person who keeps the fish and the person who enjoys golf are one and the same person.
14. The chess enthusiast has only one neighbour.

## Puzzle hard:zebra_hard-00097

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, fish, cat, horse, bird
- color: green, purple, red, blue, yellow
- nationality: Swede, Spaniard, Norwegian, Brit, Dane
- job: teacher, baker, farmer, lawyer, pilot

Clues:
1. The teacher lives somewhere between the bird owner and the occupant of the blue house.
2. The left-hand neighbour of the person who keeps the horse keeps the rabbit.
3. The right-hand neighbour of the pilot is the Dane.
4. The lawyer lives somewhere between the Brit and the Swede.
5. One of the neighbours of the occupant of the green house keeps the horse.
6. The lawyer and the Spaniard are one and the same person.
7. The right-hand neighbour of the person in the red house keeps the rabbit.
8. If whoever lives in the purple house does not keep the cat, then that person keeps the horse.
9. The occupant of the green house lives somewhere between the Dane and the person in the yellow house.
10. Neither the person in the blue house nor the occupant of the red house works as the lawyer.
11. Exactly 2 houses lie to the left of the home of the lawyer.
12. If the Dane does not live in the green house, then that person lives in the purple house.
13. The Brit and the farmer are one and the same person.

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

## Puzzle hard:zebra_hard-00032

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, chess, hiking, cooking
- nationality: Spaniard, Norwegian, German, Swede, Brit
- job: farmer, pilot, doctor, teacher, lawyer
- pet: bird, dog, fish, horse, cat

Clues:
1. At least one house separates the doctor from the farmer.
2. The cooking enthusiast lives somewhere between the person who enjoys hiking and the Norwegian.
3. Exactly 3 houses lie to the left of the home of the pilot.
4. The German lives two doors away from the tennis enthusiast.
5. The Swede is not the same person as the teacher.
6. Neither the German nor the Norwegian enjoys hiking.
7. The person who keeps the dog and the lawyer are one and the same person.
8. One of the neighbours of the chess enthusiast works as the pilot.
9. One of the neighbours of the person who keeps the fish enjoys painting.
10. The dog owner has only one neighbour.
11. Exactly 0 houses lie to the left of the home of the farmer.
12. One of the neighbours of the bird owner is the Norwegian.
13. If the pilot is not the Spaniard, then that person is the Swede.
14. Exactly one house separates the owner of the cat from the pilot.
15. The right-hand neighbour of the Norwegian is the Spaniard.

## Puzzle plain:zebra-00035

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Spaniard, Dane, Swede, German
- hobby: golf, hiking, chess, painting, cooking
- job: baker, doctor, pilot, farmer, teacher
- drink: tea, coffee, juice, water, milk

Clues:
1. The person who drinks milk and the teacher live two houses apart.
2. The person who drinks tea either works as the farmer or works as the pilot.
3. There is exactly one house between the person who enjoys chess and the person who enjoys hiking.
4. The Brit enjoys hiking.
5. The chess enthusiast either is the Brit or is the Swede.
6. The pilot lives directly to the left of the teacher.
7. The farmer lives somewhere to the left of the water drinker.
8. The baker drinks milk.
9. The Spaniard is not the doctor.
10. The German either drinks milk or drinks tea.
11. The person who drinks juice lives in house 4.
12. The person who enjoys cooking lives next to the person who enjoys hiking.
13. The person who drinks coffee lives in the second house.
14. The tea drinker is the Brit.
15. The baker either enjoys chess or enjoys painting.

## Puzzle plain:zebra-00002

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, tennis, hiking, painting, cooking
- drink: cocoa, milk, coffee, water, juice
- pet: cat, fish, bird, rabbit, dog
- job: farmer, lawyer, doctor, pilot, baker

Clues:
1. The dog owner does not live in the first house.
2. The golf enthusiast lives directly to the left of the pilot.
3. The farmer lives directly to the left of the cocoa drinker.
4. The dog owner drinks coffee.
5. The person who drinks milk does not enjoy hiking.
6. The farmer lives directly to the left of the cooking enthusiast.
7. The cocoa drinker and the lawyer are neighbours.
8. The baker keeps the cat.
9. There is exactly one house between the juice drinker and the person who enjoys tennis.
10. The bird owner drinks juice.
11. The owner of the rabbit drinks cocoa.
12. The rabbit owner lives somewhere to the left of the baker.
13. The milk drinker works as the pilot.

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

## Puzzle hard:zebra_hard-00019

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, hiking, cooking, chess
- drink: coffee, milk, juice, water, cocoa
- pet: fish, bird, horse, rabbit, dog
- job: doctor, baker, pilot, teacher, lawyer

Clues:
1. The person who enjoys painting lives somewhere between the person who enjoys chess and the milk drinker.
2. The person who drinks coffee lives somewhere between the baker and the fish owner.
3. The water drinker lives further to the right than the baker.
4. The doctor lives somewhere between the person who keeps the bird and the chess enthusiast.
5. Exactly one house separates the doctor from the person who drinks milk.
6. The bird owner does not live in the fifth house from the right.
7. If the teacher does not enjoy cooking, then that person enjoys painting.
8. One of the neighbours of the painting enthusiast works as the baker.
9. The cocoa drinker and the lawyer are one and the same person.
10. The lawyer and the rabbit owner are one and the same person.
11. If the person who keeps the bird does not enjoy hiking, then that person enjoys painting.
12. The cooking enthusiast lives two doors away from the person who enjoys tennis.
13. The lawyer lives further to the right than the person who drinks coffee.
14. At least one house separates the person who drinks water from the person who enjoys hiking.
15. Neither the painting enthusiast nor the water drinker works as the teacher.
16. If the horse owner does not drink coffee, then that person drinks water.
