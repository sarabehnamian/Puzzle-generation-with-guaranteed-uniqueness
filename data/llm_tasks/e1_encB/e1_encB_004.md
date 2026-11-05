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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_004.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle paraphrase:zebra-00158

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, chess, cooking, hiking
- color: white, green, red, purple, blue
- nationality: Spaniard, Brit, Dane, German, Swede
- pet: dog, fish, rabbit, horse, bird

Clues:
1. The hiker keeps the fish.
2. The green house's occupant lives next door to the Swede.
3. The German lives immediately to the left of the white house.
4. The purple house's occupant and the rabbit owner are neighbours.
5. The painter lives in the red house.
6. The purple house's occupant doesn't play tennis.
7. The cooking enthusiast and the Dane live next to each other.
8. The rabbit keeper's hobby is cooking.
9. The bird owner lives next door to the Swede.
10. The Dane keeps the horse.
11. The blue house's occupant is the Brit.
12. The Brit and the red house's occupant live two houses apart.
13. The red house's occupant is the Swede.

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

## Puzzle paraphrase:zebra-00174

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, milk, tea, water, coffee
- job: teacher, pilot, baker, farmer, doctor
- nationality: Dane, German, Swede, Norwegian, Brit
- color: blue, yellow, white, green, red

Clues:
1. The German lives immediately to the left of the coffee drinker.
2. The doctor and the juice drinker have exactly one house between them.
3. The teacher lives immediately to the left of the green house.
4. The blue house and the coffee drinker are in adjacent houses.
5. The water drinker does not live in the first house.
6. The tea drinker lives immediately to the left of the farmer.
7. The Brit is the juice drinker.
8. The blue house and the Swede are two houses apart.
9. The teacher is the coffee drinker.
10. The Dane lives immediately to the left of the pilot.
11. The farmer lives in the white house.
12. The German works as either the baker or the pilot.
13. The red house and the white house are next to each other.

## Puzzle plain:zebra-00042

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, yellow, blue, purple
- drink: water, coffee, juice, tea, cocoa
- pet: rabbit, dog, fish, bird, horse
- hobby: tennis, painting, cooking, golf, chess

Clues:
1. The person who enjoys golf does not live in the blue house.
2. The person who enjoys cooking lives next to the fish owner.
3. The cocoa drinker enjoys chess.
4. The person who drinks coffee and the person who enjoys painting are neighbours.
5. The person who drinks tea lives at one end of the row.
6. The person who enjoys cooking and the juice drinker live in adjacent houses.
7. The juice drinker keeps the bird.
8. The person who drinks coffee lives directly to the left of the bird owner.
9. The person in the blue house and the owner of the rabbit live two houses apart.
10. The person who drinks juice lives immediately to the right of whoever lives in the red house.
11. The cooking enthusiast either keeps the horse or keeps the rabbit.
12. The person who enjoys golf lives in the fifth house.
13. The person who drinks juice lives immediately to the right of the dog owner.
14. The person who enjoys cooking lives directly to the left of the person in the yellow house.
15. The person who enjoys painting and whoever lives in the white house live in adjacent houses.

## Puzzle hard:zebra_hard-00070

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, blue, yellow, green, white
- nationality: Dane, Brit, Spaniard, Swede, German
- hobby: tennis, painting, golf, chess, hiking
- pet: cat, fish, rabbit, dog, bird

Clues:
1. The dog owner is not the same person as the occupant of the yellow house.
2. The German lives somewhere between the golf enthusiast and the person who enjoys hiking.
3. The tennis enthusiast is not the same person as the occupant of the white house.
4. The occupant of the blue house has only one neighbour.
5. The right-hand neighbour of the owner of the bird is the Brit.
6. If the person who keeps the bird does not enjoy hiking, then that person enjoys tennis.
7. Whoever lives in the green house lives two doors away from the Spaniard.
8. One of the neighbours of the person who keeps the bird keeps the fish.
9. One of the neighbours of the Swede enjoys hiking.
10. The left-hand neighbour of the person who enjoys tennis enjoys hiking.
11. The person who enjoys painting lives somewhere between the owner of the rabbit and the occupant of the yellow house.
12. None of the neighbours of the owner of the fish enjoys chess.
13. One of the neighbours of the occupant of the green house keeps the bird.
14. Whoever lives in the blue house and the Swede are one and the same person.
15. The right-hand neighbour of the person in the yellow house keeps the bird.

## Puzzle plain:zebra-00038

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: pilot, lawyer, farmer, baker, doctor
- nationality: Swede, Brit, Dane, German, Norwegian
- color: green, blue, purple, yellow, white
- drink: cocoa, tea, milk, juice, coffee

Clues:
1. The Norwegian lives in house 1.
2. The occupant of the purple house is the Dane.
3. The lawyer and the tea drinker live in adjacent houses.
4. Whoever lives in the purple house drinks milk.
5. The farmer lives in the first house.
6. The German lives next to the Swede.
7. The doctor drinks milk.
8. The occupant of the white house lives immediately to the right of the baker.
9. The coffee drinker lives in a lower-numbered house than whoever lives in the white house.
10. The tea drinker lives in house 2.
11. The cocoa drinker either is the Dane or is the German.
12. Whoever lives in the blue house drinks cocoa.
13. Whoever lives in the yellow house lives in the leftmost house.

## Puzzle paraphrase:zebra-00117

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, cocoa, water, juice, coffee
- pet: rabbit, dog, bird, cat, fish
- hobby: hiking, painting, chess, cooking, tennis
- job: lawyer, pilot, teacher, baker, farmer

Clues:
1. The chess enthusiast lives in house 5.
2. The baker drinks tea.
3. The cooking enthusiast lives immediately to the right of the cocoa drinker.
4. The bird owner drinks either coffee or water.
5. The cat keeper and the pilot live two houses apart.
6. The bird owner lives immediately to the right of the fish owner.
7. The farmer drinks either coffee or juice.
8. The fish owner lives immediately to the right of the dog keeper.
9. The coffee drinker and the hiking enthusiast live two houses apart.
10. The lawyer lives directly to the left of the pilot.
11. The tennis enthusiast is the baker.
12. The teacher does not live in the third house.
13. The bird owner is a hiking enthusiast.
