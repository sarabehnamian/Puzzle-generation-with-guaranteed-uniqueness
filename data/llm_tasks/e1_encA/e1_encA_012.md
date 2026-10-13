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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encA/e1_encA_012.out.json with this exact structure
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
3. The red house's occupant lives immediately left of the blue house's occupant.
4. The coffee drinker lives directly right of the pilot.
5. The juice drinker lives in house 3.
6. The baker lives in house 2.
7. The chess enthusiast lives directly right of the pilot.
8. The chess enthusiast and the water drinker live two houses apart.
9. The green house's occupant lives next to the tea drinker.
10. The pilot lives somewhere to the right of the lawyer.
11. The pilot lives in either the green house or the white house.
12. Hiking is the hobby of the milk drinker.
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
1. The painting enthusiast and the purple house are next-door neighbours.
2. The blue house lies directly to the left of the teacher.
3. The lawyer lives in one of the two end houses.
4. The chess player and the milk drinker live in neighbouring houses.
5. The cooking enthusiast drinks water.
6. The blue house has a lower number than the white house.
7. The doctor lives in a lower-numbered house than the coffee drinker.
8. The pilot lives directly to the left of the doctor.
9. The tennis enthusiast is the teacher.
10. The water drinker lives in the purple house.
11. The golf enthusiast and the teacher are two houses apart.
12. The cocoa drinker lives in one of the two end houses.
13. The coffee drinker lives right next to the milk drinker.
14. The chess player lives directly to the left of the green house.
15. The occupant of the green house is either the doctor or the teacher.

## Puzzle paraphrase:zebra-00169

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, cat, horse, bird, rabbit
- job: baker, lawyer, teacher, doctor, farmer
- drink: cocoa, juice, coffee, milk, water
- nationality: Norwegian, Spaniard, Swede, Dane, Brit

Clues:
1. The baker lives right beside the rabbit owner.
2. The coffee drinker lives directly to the right of the water drinker.
3. House 5 is home to the cocoa drinker.
4. The Dane and the doctor have exactly one house between them.
5. Exactly one house separates the Norwegian from the Swede.
6. The cat owner and the fish owner are neighbours.
7. The cat owner lives immediately to the right of the farmer.
8. The Dane lives next door to the rabbit owner.
9. The cocoa drinker and the farmer live in adjacent houses.
10. The Spaniard owns either the cat or the horse.
11. Water is what the teacher drinks.
12. One house lies between the bird owner and the cat owner.
13. The cocoa drinker lives somewhere to the right of the doctor.
14. The Swede is the rabbit's owner.
15. The doctor and the milk drinker live in neighbouring houses.

## Puzzle paraphrase:zebra-00168

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, fish, horse, bird, cat
- drink: cocoa, coffee, juice, milk, water
- job: pilot, doctor, lawyer, farmer, baker
- nationality: Dane, Brit, Norwegian, Swede, German

Clues:
1. The bird owner and the German have exactly one house between them.
2. The bird owner lives further left than the pilot.
3. The lawyer lives directly to the left of the baker.
4. The cocoa drinker lives immediately to the left of the baker.
5. The pilot lives directly to the left of the Swede.
6. The horse is kept in house 4.
7. The Dane is the one who drinks coffee.
8. The Brit lives immediately to the left of the Dane.
9. The cat owner lives directly to the left of the water drinker.
10. The fish belongs to the pilot.
11. The farmer is the horse owner.
12. The horse owner lives right next door to the juice drinker.

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

## Puzzle paraphrase:zebra-00186

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, German, Brit, Swede, Spaniard
- pet: rabbit, bird, fish, dog, cat
- drink: juice, tea, milk, cocoa, coffee
- hobby: golf, painting, tennis, chess, cooking

Clues:
1. The German does not live next door to the painting enthusiast.
2. The chess enthusiast and the Spaniard live two houses apart.
3. The dog belongs to the Spaniard.
4. Painting is the hobby of the juice drinker.
5. The cooking enthusiast lives in one of the two end houses.
6. One house sits between the fish owner and the juice drinker.
7. Cocoa is what the dog owner drinks.
8. The Swede drinks tea.
9. The juice drinker and the tennis enthusiast have exactly one house between them.
10. The bird lives in house 2.
11. The German lives in one of the two end houses.
12. The milk drinker lives immediately to the left of the juice drinker.
13. The Dane and the tennis enthusiast live two houses apart.
14. The rabbit owner lives in a house with a lower number than the Swede's.
15. The chess enthusiast lives somewhere to the right of the Dane.

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
