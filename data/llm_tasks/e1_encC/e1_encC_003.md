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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_003.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle plain:zebra-00094

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, chess, golf, painting, tennis
- color: green, yellow, purple, blue, red
- nationality: Dane, Swede, Spaniard, Brit, Norwegian
- drink: milk, water, coffee, cocoa, tea

Clues:
1. The occupant of the red house either drinks cocoa or drinks milk.
2. Whoever lives in the red house enjoys tennis.
3. The painting enthusiast is the Swede.
4. The Brit lives immediately to the right of whoever lives in the green house.
5. The Spaniard either drinks milk or drinks water.
6. The Dane lives in house 5.
7. The person who enjoys hiking lives next to the person in the yellow house.
8. The golf enthusiast lives directly to the left of the Norwegian.
9. The coffee drinker either is the Dane or is the Norwegian.
10. The Swede lives in the house just left of the one where the person in the red house lives.
11. The hiking enthusiast drinks cocoa.
12. The occupant of the blue house lives in house 1.

## Puzzle hard:zebra_hard-00099

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, lawyer, teacher, pilot, farmer
- drink: water, milk, tea, cocoa, juice
- pet: rabbit, cat, horse, dog, fish
- nationality: German, Dane, Norwegian, Spaniard, Swede

Clues:
1. One of the neighbours of the rabbit owner is the Spaniard.
2. One of the neighbours of the Dane is the Spaniard.
3. Exactly 0 houses lie to the left of the home of the dog owner.
4. Exactly one house separates the person who keeps the cat from the person who keeps the rabbit.
5. The doctor lives two doors away from the person who drinks milk.
6. The right-hand neighbour of the cocoa drinker is the German.
7. The person who drinks cocoa lives in the second house from the right.
8. One of the neighbours of the Swede works as the teacher.
9. The farmer lives two doors away from the person who drinks tea.
10. The fish owner and the lawyer are one and the same person.
11. Exactly one house separates the Norwegian from the water drinker.
12. At least one house separates the Norwegian from the Swede.
13. The German and the person who drinks tea are one and the same person.
14. One of the neighbours of the pilot works as the teacher.

## Puzzle paraphrase:zebra-00122

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, green, blue, purple, red
- drink: tea, cocoa, juice, milk, coffee
- hobby: cooking, tennis, hiking, golf, painting
- pet: rabbit, fish, bird, cat, horse

Clues:
1. The white house lies somewhere to the left of the blue house.
2. The occupant of the green house drinks tea.
3. The hiking enthusiast lives directly to the left of the painting enthusiast.
4. The cat keeper lives immediately to the right of the cocoa drinker.
5. One house separates the cocoa drinker from the cooking enthusiast.
6. The juice drinker lives at one end of the row.
7. The fish keeper and the person in the purple house are next-door neighbours.
8. Exactly one house lies between the blue house and the white house.
9. The horse owner and the rabbit owner live side by side.
10. The milk drinker lives immediately to the right of the juice drinker.
11. The cooking enthusiast drinks tea.
12. The occupant of the red house keeps either the fish or the horse.
13. The golf enthusiast keeps the fish.

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

## Puzzle hard:zebra_hard-00082

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, lawyer, doctor, farmer, pilot
- color: yellow, blue, white, green, purple
- pet: dog, bird, fish, cat, horse
- drink: cocoa, water, coffee, milk, tea

Clues:
1. If the person who keeps the fish does not drink cocoa, then that person drinks coffee.
2. The cocoa drinker lives further to the right than the pilot.
3. The right-hand neighbour of the farmer drinks water.
4. The person who keeps the horse lives in the third house from the right.
5. The farmer and whoever lives in the purple house are one and the same person.
6. The doctor has only one neighbour.
7. The doctor and the occupant of the green house are one and the same person.
8. Exactly 0 houses lie to the left of the home of whoever lives in the blue house.
9. The left-hand neighbour of the teacher keeps the bird.
10. The cocoa drinker and the farmer are one and the same person.
11. The cat owner and the person in the white house are one and the same person.
12. None of the neighbours of the farmer keeps the dog.
13. The occupant of the blue house and the person who drinks tea are one and the same person.

## Puzzle plain:zebra-00072

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, cooking, hiking, painting, chess
- pet: fish, rabbit, dog, cat, horse
- drink: milk, juice, coffee, tea, water
- color: blue, yellow, purple, green, white

Clues:
1. The owner of the horse either drinks tea or drinks water.
2. The occupant of the purple house keeps the fish.
3. Whoever lives in the green house lives next to the rabbit owner.
4. The tea drinker and the person who enjoys tennis live two houses apart.
5. The owner of the cat lives at one end of the row.
6. There is exactly one house between whoever lives in the blue house and the juice drinker.
7. The occupant of the blue house enjoys hiking.
8. The owner of the dog lives in the fourth house.
9. The person in the white house lives in a lower-numbered house than the person who enjoys painting.
10. The milk drinker lives in a lower-numbered house than whoever lives in the white house.
11. The water drinker lives in house 3.
12. The chess enthusiast and the person who drinks water live in adjacent houses.
13. The person in the yellow house lives in the house just left of the one where the person who enjoys tennis lives.

## Puzzle paraphrase:zebra-00120

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, white, yellow, purple, red
- nationality: Brit, Dane, German, Spaniard, Swede
- job: baker, pilot, doctor, farmer, teacher
- drink: juice, tea, water, coffee, cocoa

Clues:
1. The person in the green house lives next door to the Spaniard.
2. The Dane is a pilot by trade.
3. The occupant of the white house lives directly to the left of the Brit.
4. The German is a tea drinker.
5. The white house is one of the two end houses.
6. The coffee drinker is the farmer.
7. The teacher lives right next door to the German, on his right-hand side.
8. The water drinker's house sits immediately to the left of the juice drinker's house.
9. The Brit is the one who drinks water.
10. The occupant of the red house lives further to the left than the baker.
11. The occupant of the red house is either the baker or the doctor.
12. The purple house is not house 3.

## Puzzle plain:zebra-00025

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: cat, horse, dog, bird, rabbit
- color: red, yellow, white, purple, green
- job: teacher, baker, lawyer, farmer, doctor
- hobby: cooking, hiking, golf, painting, tennis

Clues:
1. The person who enjoys painting lives immediately to the right of the teacher.
2. The lawyer either keeps the bird or keeps the cat.
3. The owner of the rabbit lives in the green house.
4. The person who enjoys golf lives somewhere to the left of the farmer.
5. The farmer and the person in the yellow house are neighbours.
6. The horse owner enjoys cooking.
7. The painting enthusiast and the person in the purple house are neighbours.
8. The cooking enthusiast lives in the second house.
9. The doctor and the owner of the rabbit are neighbours.
10. The baker lives immediately to the right of the person who enjoys cooking.
11. The bird owner lives in the house just left of the one where the owner of the rabbit lives.
12. The bird owner lives in the white house.
13. The rabbit owner lives in the house just left of the one where the tennis enthusiast lives.

## Puzzle paraphrase:zebra-00114

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, fish, cat, rabbit, horse
- nationality: Brit, Dane, Spaniard, Swede, Norwegian
- drink: coffee, tea, water, cocoa, juice
- job: lawyer, baker, farmer, teacher, doctor

Clues:
1. The cocoa drinker lives right beside the Spaniard.
2. The water drinker lives in a lower-numbered house than the tea drinker.
3. The fish keeper drinks cocoa.
4. The cocoa drinker is not next door to the juice drinker.
5. The Brit does not live next to the cat owner.
6. The Dane and the Spaniard have exactly one house between them.
7. The bird owner lives next door to the farmer.
8. The Dane lives immediately to the right of the Norwegian.
9. The horse keeper lives directly to the left of the doctor.
10. The Swede drinks water.
11. The lawyer keeps either the bird or the horse.
12. The cat lives in the fifth house.
13. The cocoa drinker is the teacher.
14. The Brit lives right beside the farmer.
15. The tea drinker is the farmer.
