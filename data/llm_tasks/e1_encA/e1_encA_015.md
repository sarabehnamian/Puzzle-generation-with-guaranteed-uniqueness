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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encA/e1_encA_015.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00063

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, yellow, purple, blue, green
- hobby: cooking, tennis, golf, hiking, painting
- pet: bird, cat, fish, rabbit, horse
- job: baker, doctor, teacher, pilot, farmer

Clues:
1. The doctor enjoys hiking.
2. The owner of the rabbit lives somewhere to the left of whoever lives in the purple house.
3. The person who enjoys cooking lives next to the person who keeps the horse.
4. The cat owner lives directly to the left of the baker.
5. Whoever lives in the blue house lives immediately to the right of the tennis enthusiast.
6. The person who enjoys painting lives directly to the left of whoever lives in the green house.
7. The cooking enthusiast and the teacher live in adjacent houses.
8. Whoever lives in the red house lives directly to the left of the pilot.
9. The hiking enthusiast and whoever lives in the purple house live in adjacent houses.
10. The person who enjoys hiking lives in the third house.
11. The teacher either lives in the green house or lives in the red house.
12. The occupant of the blue house does not live next to the teacher.
13. The person who keeps the bird lives in house 1.

## Puzzle hard:zebra_hard-00026

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, blue, white, purple, yellow
- job: lawyer, teacher, doctor, farmer, pilot
- drink: coffee, tea, cocoa, milk, water
- hobby: cooking, chess, hiking, tennis, golf

Clues:
1. If the occupant of the yellow house does not enjoy golf, then that person enjoys hiking.
2. Whoever lives in the green house lives somewhere between the coffee drinker and the golf enthusiast.
3. The milk drinker lives somewhere between the coffee drinker and the lawyer.
4. The left-hand neighbour of the lawyer drinks water.
5. One of the neighbours of the pilot lives in the blue house.
6. Whoever lives in the blue house and the cocoa drinker are one and the same person.
7. The pilot and the occupant of the purple house are one and the same person.
8. The chess enthusiast and whoever lives in the green house are one and the same person.
9. The person in the blue house and the golf enthusiast are one and the same person.
10. None of the neighbours of the person who drinks cocoa enjoys cooking.
11. The milk drinker lives somewhere between the farmer and the lawyer.
12. The teacher and whoever lives in the white house are one and the same person.
13. One of the neighbours of the occupant of the purple house lives in the yellow house.

## Puzzle plain:zebra-00099

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, water, cocoa, coffee, tea
- job: pilot, farmer, lawyer, teacher, baker
- color: red, purple, white, blue, yellow
- hobby: golf, hiking, tennis, painting, chess

Clues:
1. The tea drinker lives in the house just left of the one where the occupant of the yellow house lives.
2. The person who drinks coffee lives next to the person who enjoys painting.
3. Whoever lives in the blue house and whoever lives in the red house are neighbours.
4. The water drinker enjoys chess.
5. The person in the purple house lives in a lower-numbered house than the painting enthusiast.
6. The person in the yellow house works as the farmer.
7. The baker and the cocoa drinker live in adjacent houses.
8. The person who drinks cocoa and the teacher live two houses apart.
9. The tennis enthusiast lives in the second house.
10. The cocoa drinker lives in the fourth house.
11. The person in the red house either drinks cocoa or drinks juice.
12. The lawyer drinks cocoa.
13. The person who enjoys chess and the tea drinker are not neighbours.
14. The hiking enthusiast and the water drinker live two houses apart.
15. The farmer and the person in the purple house live two houses apart.

## Puzzle hard:zebra_hard-00011

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, chess, painting, hiking, cooking
- drink: coffee, water, juice, milk, cocoa
- nationality: Norwegian, Brit, German, Swede, Dane
- pet: rabbit, dog, cat, fish, horse

Clues:
1. The person who enjoys tennis lives somewhere between the person who drinks cocoa and the person who enjoys hiking.
2. The person who enjoys painting and the Swede are one and the same person.
3. The person who drinks water lives somewhere between the juice drinker and the milk drinker.
4. The right-hand neighbour of the person who keeps the cat keeps the horse.
5. None of the neighbours of the Brit is the German.
6. The person who keeps the dog lives two doors away from the horse owner.
7. The person who drinks cocoa and the fish owner are one and the same person.
8. The Dane and the person who enjoys tennis are one and the same person.
9. Exactly one house separates the juice drinker from the Swede.
10. Exactly 3 houses lie to the left of the home of the fish owner.
11. If the person who drinks cocoa does not enjoy cooking, then that person enjoys tennis.
12. The person who enjoys chess and the milk drinker are one and the same person.
13. The right-hand neighbour of the rabbit owner is the Brit.

## Puzzle hard:zebra_hard-00049

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, chess, golf, hiking, painting
- job: pilot, doctor, baker, lawyer, teacher
- pet: bird, cat, fish, horse, dog
- color: white, yellow, red, purple, blue

Clues:
1. The owner of the dog and the person who enjoys hiking are one and the same person.
2. Exactly 4 houses lie to the left of the home of the fish owner.
3. The bird owner and the person in the yellow house are one and the same person.
4. The right-hand neighbour of the doctor works as the baker.
5. Exactly 2 houses lie to the left of the home of the chess enthusiast.
6. The doctor and the horse owner are one and the same person.
7. If the person who enjoys golf does not live in the blue house, then that person lives in the yellow house.
8. Exactly one house separates the lawyer from whoever lives in the white house.
9. Exactly one house separates the person who enjoys painting from the person in the purple house.
10. Exactly one house separates the lawyer from the teacher.
11. If the teacher does not enjoy chess, then that person enjoys tennis.
12. The person who keeps the cat has only one neighbour.

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

## Puzzle hard:zebra_hard-00004

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: pilot, lawyer, baker, doctor, farmer
- nationality: Swede, German, Spaniard, Dane, Brit
- color: purple, yellow, red, white, green
- pet: cat, rabbit, dog, horse, bird

Clues:
1. Neither the German nor the Swede keeps the dog.
2. The baker lives two doors away from the doctor.
3. The person who keeps the rabbit lives two doors away from the Spaniard.
4. The lawyer and the person in the white house are one and the same person.
5. One of the neighbours of the farmer is the Brit.
6. The doctor lives somewhere between the person who keeps the horse and the Swede.
7. Whoever lives in the purple house and the rabbit owner are one and the same person.
8. The cat owner lives in the third house from the right.
9. One of the neighbours of the owner of the dog keeps the cat.
10. One of the neighbours of the person who keeps the rabbit lives in the red house.
11. If the horse owner does not live in the purple house, then that person lives in the yellow house.
12. One of the neighbours of the person in the purple house keeps the dog.
13. Neither whoever lives in the purple house nor whoever lives in the yellow house works as the baker.
14. The Dane and the person who keeps the horse are one and the same person.
15. The baker lives further to the right than the owner of the bird.

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

## Puzzle paraphrase:zebra-00178

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, blue, green, purple, red
- job: farmer, doctor, baker, lawyer, teacher
- drink: juice, coffee, cocoa, milk, tea
- pet: cat, fish, rabbit, bird, horse

Clues:
1. The cocoa drinker lives immediately to the right of the farmer.
2. The doctor occupies house 5.
3. The horse is kept by the occupant of the green house.
4. The bird owner and the fish owner live next door to each other.
5. The occupant of the red house keeps either the cat or the horse.
6. The teacher lives immediately to the right of the yellow house's occupant.
7. The bird owner lives somewhere to the right of the teacher.
8. The juice drinker is not a neighbour of the teacher.
9. The occupant of the yellow house drinks either coffee or milk.
10. The coffee drinker lives immediately to the right of the yellow house's occupant.
11. The red house is house 5.
12. The bird owner lives immediately to the right of the lawyer.
13. The cocoa drinker and the purple house's occupant are two houses apart.
