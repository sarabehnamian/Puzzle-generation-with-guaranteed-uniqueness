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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encC\e1_encC_019.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00049

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, horse, cat, dog, fish
- hobby: hiking, golf, chess, painting, tennis
- job: farmer, baker, lawyer, doctor, teacher
- nationality: Swede, Brit, German, Norwegian, Spaniard

Clues:
1. The owner of the cat lives in a lower-numbered house than the Norwegian.
2. The cat owner lives in the house just left of the one where the person who keeps the horse lives.
3. The person who enjoys painting lives in the house just left of the one where the golf enthusiast lives.
4. The person who keeps the dog lives somewhere to the right of the owner of the cat.
5. The baker and the hiking enthusiast are not neighbours.
6. The owner of the bird works as the doctor.
7. The owner of the cat either is the German or is the Swede.
8. The Brit and the doctor live in adjacent houses.
9. The person who keeps the cat and the teacher are neighbours.
10. The owner of the cat enjoys chess.
11. The person who enjoys painting works as the farmer.
12. The owner of the horse is the German.
13. The baker and the bird owner live two houses apart.
14. The lawyer and the Norwegian are neighbours.

## Puzzle hard:zebra_hard-00069

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Swede, Spaniard, Brit, German
- pet: horse, bird, rabbit, fish, cat
- hobby: golf, hiking, tennis, cooking, chess
- drink: milk, tea, coffee, cocoa, water

Clues:
1. The chess enthusiast lives somewhere between the person who enjoys cooking and the Spaniard.
2. The horse owner lives somewhere between the cooking enthusiast and the Swede.
3. If the Swede does not keep the bird, then that person keeps the fish.
4. The left-hand neighbour of the person who drinks milk drinks tea.
5. One of the neighbours of the person who enjoys tennis is the Norwegian.
6. The chess enthusiast lives two doors away from the milk drinker.
7. The person who enjoys golf and the Swede are one and the same person.
8. The left-hand neighbour of the person who enjoys cooking drinks water.
9. The left-hand neighbour of the cooking enthusiast is the Norwegian.
10. The rabbit owner has only one neighbour.
11. If the Brit does not drink milk, then that person drinks water.
12. The hiking enthusiast lives further to the right than the person who drinks coffee.
13. If the tea drinker does not keep the bird, then that person keeps the rabbit.
14. The person who enjoys hiking is not the same person as the person who keeps the rabbit.

## Puzzle hard:zebra_hard-00075

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: pilot, lawyer, teacher, farmer, baker
- hobby: chess, golf, painting, cooking, tennis
- pet: cat, bird, fish, rabbit, horse
- nationality: Dane, Spaniard, German, Brit, Swede

Clues:
1. If the tennis enthusiast does not keep the cat, then that person keeps the horse.
2. The left-hand neighbour of the lawyer is the Dane.
3. One of the neighbours of the pilot enjoys cooking.
4. Exactly one house separates the Brit from the Swede.
5. The left-hand neighbour of the owner of the bird enjoys painting.
6. One of the neighbours of the Spaniard keeps the rabbit.
7. The baker lives two doors away from the owner of the cat.
8. The left-hand neighbour of the person who enjoys golf is the German.
9. The Spaniard and the teacher are one and the same person.
10. The Swede lives two doors away from the person who enjoys tennis.
11. The right-hand neighbour of the painting enthusiast is the Dane.
12. The owner of the fish lives further to the right than the German.
13. The person who enjoys painting has only one neighbour.

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

## Puzzle hard:zebra_hard-00098

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: cat, horse, rabbit, bird, dog
- color: blue, white, yellow, purple, green
- drink: milk, tea, water, cocoa, coffee
- nationality: Norwegian, Swede, German, Brit, Dane

Clues:
1. The Dane lives two doors away from the person who drinks water.
2. Neither whoever lives in the blue house nor the Norwegian drinks milk.
3. The right-hand neighbour of the tea drinker is the Dane.
4. Exactly 0 houses lie to the left of the home of the occupant of the blue house.
5. The Brit and the person who drinks coffee are one and the same person.
6. Exactly one house separates the person in the blue house from whoever lives in the green house.
7. Exactly 0 houses lie to the left of the home of the owner of the rabbit.
8. The left-hand neighbour of the owner of the bird is the Norwegian.
9. The German lives in the fifth house from the right.
10. Exactly one house separates the Norwegian from whoever lives in the purple house.
11. One of the neighbours of the dog owner keeps the horse.
12. One of the neighbours of the horse owner keeps the cat.
13. The Brit and the person who keeps the dog are one and the same person.
14. The Norwegian and the occupant of the white house are one and the same person.

## Puzzle plain:zebra-00032

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, juice, cocoa, coffee, milk
- pet: cat, horse, fish, bird, rabbit
- job: lawyer, doctor, teacher, pilot, farmer
- nationality: Dane, Spaniard, Brit, German, Norwegian

Clues:
1. The owner of the cat lives in the middle house.
2. The Norwegian lives immediately to the right of the doctor.
3. The person who drinks coffee lives directly to the left of the pilot.
4. The lawyer drinks juice.
5. The person who keeps the horse lives in the house just left of the one where the doctor lives.
6. The person who drinks milk lives directly to the left of the lawyer.
7. The person who drinks coffee keeps the fish.
8. The German does not live next to the owner of the rabbit.
9. The Spaniard lives next to the person who drinks water.
10. The pilot lives in the house just left of the one where the German lives.
11. There is exactly one house between the Brit and the farmer.

## Puzzle plain:zebra-00045

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, juice, water, milk, coffee
- job: teacher, doctor, pilot, baker, farmer
- nationality: Swede, Dane, Norwegian, German, Spaniard
- hobby: tennis, golf, cooking, painting, chess

Clues:
1. The teacher and the person who enjoys chess are different people.
2. The baker lives immediately to the right of the person who enjoys cooking.
3. The milk drinker lives immediately to the right of the water drinker.
4. The German and the Spaniard live two houses apart.
5. The doctor either drinks coffee or drinks milk.
6. The Swede lives in house 5.
7. The Dane and the person who drinks milk live in adjacent houses.
8. The person who enjoys golf lives somewhere to the left of the juice drinker.
9. The person who enjoys painting lives in one of the two end houses.
10. The German lives immediately to the right of the chess enthusiast.
11. The Dane and the doctor live two houses apart.
12. The pilot lives in the middle house.
13. The person who drinks juice is the Spaniard.
14. The baker lives in the fourth house.

## Puzzle hard:zebra_hard-00033

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, cocoa, tea, juice, coffee
- color: blue, red, green, white, purple
- hobby: golf, cooking, painting, tennis, chess
- job: lawyer, pilot, teacher, doctor, farmer

Clues:
1. The golf enthusiast and the water drinker are one and the same person.
2. The person who enjoys painting lives two doors away from the pilot.
3. The person who enjoys chess and the occupant of the green house are one and the same person.
4. The person who enjoys tennis lives somewhere between the person who enjoys cooking and the teacher.
5. One of the neighbours of the cocoa drinker lives in the purple house.
6. The doctor lives two doors away from the tennis enthusiast.
7. At least one house separates the lawyer from the teacher.
8. The occupant of the blue house and the doctor are one and the same person.
9. The chess enthusiast and the lawyer are one and the same person.
10. The left-hand neighbour of the person who drinks cocoa enjoys tennis.
11. The doctor is not the same person as the person who enjoys golf.
12. Exactly 3 houses lie to the left of the home of the occupant of the red house.
13. The juice drinker and the person who enjoys tennis are one and the same person.
14. One of the neighbours of the person who drinks coffee enjoys golf.

## Puzzle hard:zebra_hard-00077

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, chess, painting, tennis, golf
- pet: rabbit, fish, dog, bird, horse
- job: pilot, teacher, baker, lawyer, doctor
- nationality: Spaniard, German, Brit, Dane, Swede

Clues:
1. The Dane lives further to the right than the person who enjoys painting.
2. The pilot lives somewhere between the doctor and the Swede.
3. The person who keeps the dog and the lawyer are one and the same person.
4. Exactly one house separates the lawyer from the painting enthusiast.
5. The person who enjoys golf and the Swede are one and the same person.
6. Exactly 0 houses lie to the left of the home of the Brit.
7. Exactly 2 houses lie to the left of the home of the Spaniard.
8. The person who keeps the rabbit lives somewhere between the doctor and the hiking enthusiast.
9. The right-hand neighbour of the painting enthusiast enjoys golf.
10. The Spaniard lives further to the right than the lawyer.
11. One of the neighbours of the person who enjoys painting works as the baker.
12. One of the neighbours of the person who keeps the bird enjoys hiking.
13. None of the neighbours of the owner of the fish enjoys golf.
14. The doctor and the tennis enthusiast are one and the same person.

## Puzzle paraphrase:zebra-00193

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, German, Brit, Spaniard, Dane
- job: baker, doctor, teacher, farmer, pilot
- pet: fish, dog, cat, rabbit, horse
- color: green, blue, yellow, white, red

Clues:
1. The white house and the yellow house are next to each other.
2. The Dane is the doctor.
3. The cat keeper lives immediately to the right of the Swede.
4. The green house's occupant keeps either the cat or the dog.
5. The German and the red house's occupant are not neighbours.
6. The Brit lives next door to the farmer.
7. The Swede is the pilot.
8. The Dane and the occupant of the yellow house live two houses apart.
9. The German lives next door to the pilot.
10. The blue house is directly to the left of the yellow house.
11. The dog keeper lives somewhere to the right of the German.
12. The rabbit owner is either the doctor or the pilot.
13. The fish keeper is the teacher.
14. Somewhere to the right of the Brit lives the teacher.
