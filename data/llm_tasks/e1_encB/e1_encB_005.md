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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_005.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00163

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, lawyer, teacher, baker, farmer
- pet: bird, horse, dog, rabbit, fish
- hobby: painting, hiking, golf, tennis, chess
- drink: cocoa, water, tea, juice, coffee

Clues:
1. The chess player lives somewhere to the left of the golfer.
2. The golfer does not live next to the water drinker.
3. The doctor's hobby is hiking.
4. The cocoa drinker enjoys chess.
5. The rabbit owner lives in house 5.
6. The horse owner lives at one end of the row.
7. The chess player does not keep the fish.
8. The chess player lives next to the farmer.
9. The hiker and the horse owner live two houses apart.
10. The juice drinker lives directly to the left of the lawyer.
11. The baker and the doctor are not neighbours.
12. The water drinker lives at one end of the row.
13. The dog owner lives in the middle house.
14. The horse owner lives immediately to the left of the chess player.
15. The tennis enthusiast is the baker.
16. The coffee drinker and the doctor live two houses apart.

## Puzzle plain:zebra-00041

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, cat, bird, fish, dog
- color: purple, white, red, blue, green
- hobby: chess, painting, tennis, golf, hiking
- drink: water, tea, coffee, cocoa, juice

Clues:
1. The chess enthusiast lives in the first house.
2. The owner of the cat lives in a lower-numbered house than the person who enjoys hiking.
3. The occupant of the red house lives immediately to the right of the golf enthusiast.
4. The bird owner and the owner of the horse live two houses apart.
5. The person who drinks coffee lives in the white house.
6. The water drinker lives in the house just left of the one where the person in the green house lives.
7. The occupant of the blue house drinks water.
8. The cocoa drinker lives immediately to the right of the juice drinker.
9. The person who enjoys hiking lives in the house just left of the one where the owner of the horse lives.
10. Whoever lives in the white house lives somewhere to the left of the hiking enthusiast.
11. The owner of the dog lives in house 5.
12. The person who enjoys tennis lives in the fourth house.

## Puzzle hard:zebra_hard-00058

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, doctor, pilot, lawyer, farmer
- pet: horse, cat, dog, fish, bird
- color: red, yellow, blue, white, green
- drink: tea, water, coffee, juice, milk

Clues:
1. The farmer lives somewhere between the fish owner and the tea drinker.
2. The lawyer and the occupant of the red house are one and the same person.
3. None of the neighbours of the person who keeps the bird keeps the horse.
4. The left-hand neighbour of the cat owner works as the pilot.
5. The right-hand neighbour of the teacher lives in the blue house.
6. The right-hand neighbour of whoever lives in the yellow house lives in the red house.
7. The dog owner lives two doors away from the farmer.
8. The water drinker lives somewhere between the lawyer and the person who drinks tea.
9. The person who keeps the bird lives further to the right than the farmer.
10. The occupant of the yellow house lives somewhere between the person in the red house and the person who drinks water.
11. The person who drinks juice lives two doors away from the lawyer.
12. The occupant of the green house lives two doors away from the occupant of the yellow house.
13. Exactly one house separates the person who keeps the cat from the coffee drinker.

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

## Puzzle plain:zebra-00017

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, horse, dog, fish, bird
- nationality: Spaniard, German, Norwegian, Dane, Swede
- job: baker, doctor, farmer, pilot, lawyer
- color: yellow, blue, white, green, red

Clues:
1. The horse owner either is the German or is the Spaniard.
2. The owner of the fish lives in the house just left of the one where the dog owner lives.
3. The doctor lives in house 4.
4. The bird owner does not live in the fifth house.
5. Whoever lives in the blue house works as the doctor.
6. The rabbit owner lives directly to the left of the farmer.
7. The lawyer lives in the green house.
8. There is exactly one house between the occupant of the green house and the occupant of the yellow house.
9. The occupant of the red house is not the German.
10. The German lives in the second house.
11. The Norwegian does not live in the third house.
12. The pilot lives next to the Spaniard.
13. The Swede lives in the green house.
14. The baker and the owner of the dog live two houses apart.

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

## Puzzle plain:zebra-00001

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, German, Dane, Spaniard, Brit
- pet: fish, dog, bird, cat, rabbit
- job: teacher, doctor, farmer, lawyer, baker
- drink: cocoa, juice, coffee, milk, water

Clues:
1. The baker and the Brit live two houses apart.
2. The person who keeps the bird lives in the third house.
3. The Spaniard does not live in house 2.
4. The person who drinks coffee lives in the leftmost house.
5. The teacher lives directly to the left of the cocoa drinker.
6. The farmer drinks water.
7. The doctor lives in the first house.
8. The German drinks water.
9. The dog owner lives in the first house.
10. The person who keeps the cat lives directly to the left of the Dane.
11. The juice drinker is the Brit.
12. The juice drinker either keeps the dog or keeps the fish.

## Puzzle plain:zebra-00052

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: cat, rabbit, fish, bird, horse
- color: blue, white, green, yellow, purple
- drink: milk, juice, cocoa, tea, water
- hobby: hiking, golf, chess, painting, tennis

Clues:
1. Whoever lives in the purple house lives directly to the left of the person in the blue house.
2. The cocoa drinker lives directly to the left of the tennis enthusiast.
3. The chess enthusiast lives immediately to the right of the cat owner.
4. The painting enthusiast lives in the leftmost house.
5. The person who drinks tea lives immediately to the right of the chess enthusiast.
6. The owner of the fish lives next to the person who drinks milk.
7. There is exactly one house between the occupant of the green house and the person who drinks juice.
8. There is exactly one house between the golf enthusiast and the person who enjoys hiking.
9. The occupant of the green house either enjoys golf or enjoys painting.
10. The bird owner lives immediately to the right of the painting enthusiast.
11. The person who keeps the fish and the person in the yellow house are neighbours.
12. The occupant of the white house lives in the first house.
13. The milk drinker keeps the horse.

## Puzzle paraphrase:zebra-00139

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, purple, red, white, blue
- pet: bird, rabbit, dog, horse, cat
- hobby: golf, chess, painting, tennis, cooking
- nationality: Brit, Spaniard, Dane, Norwegian, Swede

Clues:
1. The blue house's occupant is either the Brit or the Spaniard.
2. The Spaniard's hobby is tennis.
3. The dog owner lives directly to the right of the white house.
4. The Brit owns the horse.
5. The white house is directly to the left of the cooking enthusiast.
6. The Norwegian lives immediately to the left of the chess enthusiast.
7. The Norwegian and the Spaniard live in adjacent houses.
8. The bird owner and the yellow house are neighbours.
9. The Norwegian lives next door to the red house.
10. The cooking enthusiast lives immediately to the left of the Dane.
11. The painting enthusiast lives somewhere to the right of the rabbit owner.
12. The cooking enthusiast lives somewhere to the right of the yellow house.
13. The rabbit owner lives in a lower-numbered house than the cooking enthusiast.

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
