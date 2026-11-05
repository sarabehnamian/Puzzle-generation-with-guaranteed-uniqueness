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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_012.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00002

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, green, white, yellow, purple
- job: baker, teacher, pilot, lawyer, doctor
- hobby: tennis, hiking, golf, painting, cooking
- pet: bird, horse, rabbit, cat, dog

Clues:
1. The right-hand neighbour of the cat owner enjoys golf.
2. One of the neighbours of the horse owner keeps the dog.
3. The occupant of the red house lives further to the right than the owner of the bird.
4. The owner of the dog is not the same person as whoever lives in the yellow house.
5. Neither the cat owner nor whoever lives in the green house works as the teacher.
6. The lawyer lives somewhere between the occupant of the red house and whoever lives in the white house.
7. If the teacher does not keep the cat, then that person keeps the rabbit.
8. The pilot lives two doors away from the teacher.
9. The cooking enthusiast and the pilot are one and the same person.
10. The painting enthusiast lives somewhere between the horse owner and the person who enjoys tennis.
11. If the person in the purple house is not the doctor, then that person works as the pilot.
12. At least one house separates the owner of the bird from the horse owner.
13. The teacher lives in the fourth house from the right.
14. One of the neighbours of the teacher works as the doctor.
15. One of the neighbours of the lawyer lives in the yellow house.

## Puzzle hard:zebra_hard-00060

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, horse, dog, cat, bird
- nationality: Brit, German, Spaniard, Swede, Norwegian
- hobby: tennis, hiking, painting, cooking, chess
- drink: coffee, juice, water, tea, cocoa

Clues:
1. The left-hand neighbour of the tennis enthusiast is the Swede.
2. The Norwegian and the rabbit owner are one and the same person.
3. The left-hand neighbour of the painting enthusiast drinks juice.
4. Exactly 0 houses lie to the left of the home of the Spaniard.
5. If the person who enjoys tennis is not the German, then that person is the Spaniard.
6. If the hiking enthusiast does not keep the bird, then that person keeps the dog.
7. The Brit and the person who keeps the horse are one and the same person.
8. If the person who keeps the cat does not enjoy chess, then that person enjoys painting.
9. The cat owner lives in the fourth house from the right.
10. The left-hand neighbour of the tea drinker drinks coffee.
11. The rabbit owner lives somewhere between the owner of the bird and the horse owner.
12. None of the neighbours of the chess enthusiast keeps the bird.
13. The person who keeps the bird and the water drinker are one and the same person.

## Puzzle paraphrase:zebra-00143

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, cooking, chess, tennis, painting
- color: yellow, blue, green, red, white
- job: doctor, baker, pilot, farmer, lawyer
- drink: tea, coffee, water, juice, milk

Clues:
1. The juice drinker and the tennis enthusiast live two houses apart.
2. The chess enthusiast lives next door to the hiking enthusiast.
3. The red house is immediately left of the blue house.
4. The coffee drinker lives directly right of the pilot.
5. The juice drinker lives in the middle house, number 3.
6. The baker lives in house 2.
7. The chess enthusiast lives directly right of the pilot.
8. Two houses separate the chess enthusiast from the water drinker.
9. The green house's occupant lives next to the tea drinker.
10. The pilot lives somewhere to the right of the lawyer.
11. The pilot lives in either the green house or the white house.
12. The milk drinker enjoys hiking.
13. The painting enthusiast lives immediately left of the farmer.

## Puzzle plain:zebra-00087

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, coffee, tea, cocoa
- hobby: cooking, tennis, hiking, chess, golf
- job: baker, pilot, lawyer, farmer, teacher
- pet: bird, cat, fish, horse, rabbit

Clues:
1. The person who drinks cocoa and the person who drinks water live in adjacent houses.
2. The chess enthusiast lives somewhere to the right of the tennis enthusiast.
3. The pilot keeps the rabbit.
4. The person who keeps the cat lives directly to the left of the owner of the fish.
5. The water drinker either keeps the fish or keeps the rabbit.
6. The cocoa drinker and the person who enjoys tennis are neighbours.
7. The rabbit owner enjoys chess.
8. The lawyer keeps the fish.
9. The coffee drinker either keeps the fish or keeps the horse.
10. The person who enjoys hiking does not keep the fish.
11. The baker and the person who drinks coffee are not neighbours.
12. The person who enjoys cooking lives in house 2.
13. The person who keeps the bird lives immediately to the right of the owner of the horse.
14. The farmer enjoys cooking.
15. The tennis enthusiast lives in a lower-numbered house than the milk drinker.
16. The tennis enthusiast drinks tea.

## Puzzle paraphrase:zebra-00138

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, yellow, white, green
- hobby: tennis, painting, cooking, chess, golf
- job: lawyer, baker, doctor, pilot, teacher
- drink: juice, cocoa, milk, water, coffee

Clues:
1. The painting enthusiast lives next to the purple house.
2. The blue house is directly to the left of the teacher.
3. The lawyer lives at one end of the row.
4. The chess enthusiast and the milk drinker are neighbours.
5. The cooking enthusiast drinks water.
6. The blue house is at a lower number than the white house.
7. The doctor lives in a lower-numbered house than the coffee drinker.
8. The pilot lives directly to the left of the doctor.
9. The teacher is the tennis enthusiast.
10. The water drinker lives in the purple house.
11. The golf enthusiast and the teacher live two houses apart.
12. The cocoa drinker lives in one of the two end houses.
13. The coffee drinker lives next door to the milk drinker.
14. The chess enthusiast lives immediately to the left of the green house.
15. The occupant of the green house is either the doctor or the teacher.

## Puzzle paraphrase:zebra-00170

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, green, white, yellow, red
- nationality: Norwegian, German, Dane, Swede, Brit
- drink: tea, milk, water, cocoa, coffee
- hobby: hiking, chess, painting, tennis, golf

Clues:
1. The hiker is either the German or the Swede.
2. The tea drinker lives right next to the tennis enthusiast.
3. The Norwegian and the resident of the white house are separated by exactly one house.
4. The painting enthusiast lives immediately to the right of the hiker.
5. One house separates the tennis enthusiast from the water drinker.
6. The hiker and the tennis enthusiast have exactly one house between them.
7. The Swede's house lies somewhere to the right of the white house.
8. Whoever is in the red house is either the golf enthusiast or the hiker.
9. The Dane's hobby is golf.
10. The Brit's house is adjacent to the German's.
11. The milk drinker is not next door to the tea drinker.
12. The coffee drinker lives next door to the Dane.
13. The Swede lives right beside the yellow house.
14. The chess enthusiast lives immediately to the right of the green house.
15. The tennis enthusiast lives somewhere to the right of the Brit.
16. The coffee drinker lives somewhere to the left of the cocoa drinker.

## Puzzle paraphrase:zebra-00169

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, cat, horse, bird, rabbit
- job: baker, lawyer, teacher, doctor, farmer
- drink: cocoa, juice, coffee, milk, water
- nationality: Norwegian, Spaniard, Swede, Dane, Brit

Clues:
1. The baker lives next door to the rabbit owner.
2. The coffee drinker lives immediately to the right of the water drinker.
3. The cocoa drinker lives in house 5.
4. Exactly one house lies between the Dane and the doctor.
5. One house separates the Norwegian from the Swede.
6. The cat owner and the fish owner live in adjacent houses.
7. The cat owner lives immediately to the right of the farmer.
8. The Dane lives next door to the rabbit owner.
9. The cocoa drinker and the farmer are neighbours.
10. The Spaniard keeps either the cat or the horse.
11. The teacher drinks water.
12. Exactly one house lies between the bird keeper and the cat owner.
13. The cocoa drinker lives somewhere to the right of the doctor.
14. The rabbit owner is the Swede.
15. The doctor lives next door to the milk drinker.

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

## Puzzle paraphrase:zebra-00187

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, tea, milk, water, coffee
- pet: dog, bird, rabbit, horse, fish
- hobby: painting, chess, tennis, cooking, golf
- color: green, red, yellow, blue, purple

Clues:
1. The green house is immediately to the left of the bird owner.
2. The yellow house's occupant drinks juice.
3. The tea drinker's hobby is painting.
4. The rabbit owner and the tea drinker are not neighbours.
5. The tennis enthusiast lives in house 1.
6. One house lies between the milk drinker and the rabbit owner.
7. The yellow house is immediately to the left of the horse owner.
8. The painter lives immediately to the left of the blue house.
9. The golfer lives immediately to the right of the yellow house.
10. The fish owner lives somewhere to the right of the green house.
11. The cooking enthusiast has either the dog or the rabbit.
12. The red house is the second house.
13. The juice drinker lives immediately to the left of the water drinker.

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
