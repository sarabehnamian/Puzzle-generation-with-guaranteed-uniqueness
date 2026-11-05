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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encC\e1_encC_000.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00085

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, pilot, lawyer, farmer, doctor
- hobby: tennis, cooking, painting, hiking, chess
- color: white, red, blue, yellow, green
- pet: cat, rabbit, horse, fish, bird

Clues:
1. One of the neighbours of the doctor enjoys hiking.
2. The bird owner and the doctor are one and the same person.
3. The person who keeps the horse and the person in the yellow house are one and the same person.
4. The owner of the rabbit is not the same person as whoever lives in the red house.
5. Neither the owner of the rabbit nor the occupant of the yellow house enjoys cooking.
6. Exactly one house separates the farmer from the occupant of the yellow house.
7. The left-hand neighbour of the owner of the cat works as the lawyer.
8. The left-hand neighbour of whoever lives in the white house enjoys chess.
9. Whoever lives in the green house lives somewhere between the cooking enthusiast and the person who keeps the rabbit.
10. If the occupant of the white house is not the farmer, then that person works as the pilot.
11. The pilot lives somewhere between the farmer and the owner of the rabbit.
12. The right-hand neighbour of the bird owner enjoys cooking.
13. One of the neighbours of the tennis enthusiast works as the farmer.

## Puzzle hard:zebra_hard-00088

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, hiking, painting, cooking, golf
- nationality: Spaniard, Brit, German, Swede, Dane
- color: blue, red, white, yellow, green
- pet: fish, bird, horse, cat, rabbit

Clues:
1. If the occupant of the white house does not keep the cat, then that person keeps the horse.
2. The owner of the horse and whoever lives in the yellow house are one and the same person.
3. Exactly 4 houses lie to the left of the home of the owner of the cat.
4. The right-hand neighbour of the person who keeps the fish is the Swede.
5. The Brit lives somewhere between the person in the red house and the occupant of the yellow house.
6. The hiking enthusiast and the person in the white house are one and the same person.
7. The Spaniard lives in the fifth house from the right.
8. One of the neighbours of the person in the green house keeps the cat.
9. The right-hand neighbour of the person who keeps the bird enjoys chess.
10. The left-hand neighbour of whoever lives in the yellow house enjoys painting.
11. The German and the person who enjoys golf are one and the same person.

## Puzzle hard:zebra_hard-00091

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, chess, painting, tennis, golf
- pet: horse, rabbit, cat, dog, fish
- job: farmer, pilot, lawyer, doctor, teacher
- nationality: Dane, Spaniard, Norwegian, Swede, German

Clues:
1. Neither the Norwegian nor the Spaniard enjoys painting.
2. The dog owner lives further to the right than the person who enjoys tennis.
3. The pilot does not live in the third house from the right.
4. The person who keeps the fish and the teacher are one and the same person.
5. The Norwegian lives somewhere between the Dane and the tennis enthusiast.
6. The left-hand neighbour of the person who keeps the fish works as the doctor.
7. The right-hand neighbour of the cat owner works as the lawyer.
8. Exactly 4 houses lie to the left of the home of the rabbit owner.
9. The chess enthusiast and the Spaniard are one and the same person.
10. The person who enjoys hiking lives two doors away from the Norwegian.
11. The person who enjoys golf lives further to the right than the German.
12. Exactly 4 houses lie to the left of the home of the Spaniard.
13. The German and the person who enjoys hiking are one and the same person.
14. The dog owner and the lawyer are one and the same person.

## Puzzle paraphrase:zebra-00154

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, golf, cooking, tennis, hiking
- nationality: Brit, Swede, Norwegian, Dane, Spaniard
- drink: cocoa, water, milk, tea, coffee
- job: farmer, baker, teacher, doctor, lawyer

Clues:
1. The Dane and the Norwegian are not next-door neighbours.
2. The milk drinker lives directly to the left of the tea drinker.
3. The golfer lives in one of the end houses.
4. The hiker is the lawyer.
5. The doctor's hobby is cooking.
6. The Swede lives at one end of the row.
7. The farmer lives in a lower-numbered house than the lawyer.
8. The baker and the golfer live in adjacent houses.
9. The coffee drinker lives next door to the painter.
10. The teacher lives immediately to the left of the tea drinker.
11. The coffee drinker and the water drinker are next-door neighbours.
12. The Dane's hobby is either golf or tennis.
13. The Spaniard's hobby is hiking.
14. The Brit lives in the fourth house.

## Puzzle paraphrase:zebra-00157

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, painting, golf, tennis, cooking
- nationality: Spaniard, Norwegian, Dane, Swede, Brit
- color: red, green, blue, white, purple
- pet: bird, rabbit, cat, dog, fish

Clues:
1. The painter lives immediately to the right of the red house's occupant.
2. The Dane and the white house's occupant live in adjacent houses.
3. The fish keeper lives next door to the white house's occupant.
4. The fish keeper lives somewhere to the right of the Dane.
5. The rabbit owner and the Swede are not neighbours.
6. The red house's occupant enjoys either painting or tennis.
7. The dog owner is either the Brit or the Spaniard.
8. The hiker does not live in the blue house.
9. The golfer is the Swede.
10. The green house and the white house are next-door neighbours.
11. The Brit lives in house 5.
12. The purple house's occupant keeps the rabbit.
13. The painter lives somewhere to the left of the rabbit owner.
14. The bird owner lives immediately to the left of the rabbit keeper.

## Puzzle plain:zebra-00055

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, fish, rabbit, cat
- drink: cocoa, juice, tea, milk, water
- nationality: Brit, German, Norwegian, Dane, Swede
- hobby: tennis, hiking, cooking, chess, painting

Clues:
1. The Swede lives immediately to the right of the chess enthusiast.
2. The cat owner lives next to the Swede.
3. The horse owner drinks juice.
4. The Brit and the person who keeps the cat are neighbours.
5. The person who enjoys chess and the horse owner live in adjacent houses.
6. The Norwegian lives next to the Swede.
7. The painting enthusiast lives in the fourth house.
8. The owner of the horse does not live in the first house.
9. The person who enjoys hiking lives immediately to the right of the cocoa drinker.
10. The water drinker and the Dane are different people.
11. The person who keeps the dog and the person who enjoys hiking are neighbours.
12. The German keeps the cat.
13. The owner of the fish drinks water.
14. The Brit enjoys tennis.
15. The tea drinker either enjoys hiking or enjoys tennis.

## Puzzle plain:zebra-00008

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Spaniard, Swede, Norwegian, Dane
- drink: milk, cocoa, coffee, tea, juice
- color: blue, purple, red, yellow, green
- pet: dog, bird, cat, horse, rabbit

Clues:
1. The person who drinks coffee lives in the middle house.
2. The horse owner lives in house 5.
3. The bird owner lives in the blue house.
4. The occupant of the green house keeps the cat.
5. The coffee drinker lives next to the juice drinker.
6. The cat owner and the person who drinks coffee are neighbours.
7. Whoever lives in the yellow house lives in house 5.
8. The milk drinker lives in the fourth house.
9. The Spaniard either keeps the horse or keeps the rabbit.
10. The coffee drinker and the Swede live two houses apart.
11. The occupant of the blue house does not live next to the German.
12. The Dane does not live next to the German.
13. The person who drinks tea lives in a lower-numbered house than whoever lives in the purple house.
14. The occupant of the blue house lives in the third house.
15. The rabbit owner lives directly to the left of the owner of the horse.
16. The juice drinker lives next to the Norwegian.

## Puzzle plain:zebra-00060

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, cat, dog, fish, rabbit
- drink: coffee, tea, juice, water, cocoa
- hobby: hiking, tennis, chess, painting, golf
- color: blue, red, white, purple, green

Clues:
1. The person in the purple house lives in the house just left of the one where whoever lives in the red house lives.
2. The person who enjoys hiking and the juice drinker are neighbours.
3. The person in the green house and the person who enjoys tennis are neighbours.
4. The water drinker either keeps the fish or keeps the rabbit.
5. The person in the blue house keeps the rabbit.
6. The owner of the fish enjoys golf.
7. The coffee drinker either keeps the cat or keeps the rabbit.
8. The person who drinks tea lives in the purple house.
9. There is exactly one house between the cat owner and the occupant of the red house.
10. The person in the purple house lives in the third house.
11. The person who drinks water and whoever lives in the white house live in adjacent houses.
12. The owner of the dog and the painting enthusiast live two houses apart.
13. The person who drinks coffee enjoys chess.

## Puzzle paraphrase:zebra-00135

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, cooking, painting, chess, tennis
- color: blue, red, green, white, yellow
- pet: cat, rabbit, dog, horse, bird
- job: lawyer, farmer, doctor, teacher, baker

Clues:
1. The yellow house is the fourth house.
2. The dog owner lives immediately to the left of the rabbit owner.
3. The baker's hobby is cooking.
4. The bird owner does not live in the first house.
5. The white house is directly to the left of the green house.
6. The farmer keeps the dog.
7. The bird owner is the lawyer.
8. The cat owner lives somewhere to the right of the baker.
9. One house lies between the blue house and the rabbit owner.
10. The occupant of the blue house is either the doctor or the farmer.
11. The green house lies somewhere to the left of the farmer.
12. The painting enthusiast lives in the fourth house.
13. The chess enthusiast lives in one of the two end houses.
14. The tennis enthusiast lives directly to the left of the painting enthusiast.

## Puzzle paraphrase:zebra-00116

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, red, green, white, yellow
- nationality: Brit, Spaniard, Dane, Swede, German
- hobby: golf, tennis, chess, cooking, hiking
- job: baker, lawyer, pilot, doctor, teacher

Clues:
1. The golf enthusiast is either the Brit or the Spaniard.
2. The doctor lives next door to the golf enthusiast.
3. The cooking enthusiast lives next to the purple house's occupant.
4. The Swede lives somewhere to the right of the tennis enthusiast.
5. The Swede is the teacher.
6. The white house and the yellow house are two houses apart.
7. The baker and the pilot are next-door neighbours.
8. The lawyer lives in a house adjacent to the yellow house.
9. The chess enthusiast lives in the red house.
10. The Brit is the lawyer.
11. The Dane does not live in the fourth house.
12. The purple house is immediately to the left of the pilot's.
13. The occupant of the purple house is the German.
14. The hiking enthusiast lives immediately to the right of the red house.
