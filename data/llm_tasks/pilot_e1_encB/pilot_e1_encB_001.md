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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/pilot_e1_encB/pilot_e1_encB_001.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle zebra-00002

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

## Puzzle zebra-00007

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, German, Swede, Norwegian
- color: blue, purple, red, white, yellow
- drink: milk, cocoa, juice, coffee, tea
- pet: dog, fish, cat, bird, horse

Clues:
1. The owner of the cat lives in the house just left of the one where the Dane lives.
2. The Norwegian lives in the blue house.
3. The owner of the cat lives directly to the left of the person who keeps the dog.
4. The occupant of the white house either is the Brit or is the Dane.
5. The person who drinks coffee lives in the house just left of the one where the occupant of the blue house lives.
6. The Swede either keeps the bird or keeps the dog.
7. The occupant of the purple house lives directly to the left of the Brit.
8. The person who drinks milk lives in the leftmost house.
9. The person who drinks tea either lives in the blue house or lives in the red house.
10. The milk drinker and the Swede live in adjacent houses.
11. The Brit and the person who drinks coffee live in adjacent houses.
12. The cocoa drinker and the Dane are not neighbours.
13. The owner of the fish lives next to the person in the red house.

## Puzzle zebra-00005

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, lawyer, teacher, pilot, baker
- hobby: painting, tennis, cooking, hiking, chess
- color: purple, green, yellow, white, blue
- pet: fish, rabbit, bird, cat, dog

Clues:
1. The chess enthusiast lives in house 4.
2. The person who enjoys tennis lives in the house just left of the one where the person who enjoys hiking lives.
3. The hiking enthusiast lives directly to the left of the owner of the cat.
4. Whoever lives in the yellow house keeps the rabbit.
5. The person in the white house lives immediately to the right of the person in the green house.
6. The owner of the bird works as the baker.
7. The person in the blue house lives directly to the left of the teacher.
8. The lawyer lives in the white house.
9. The person who keeps the dog lives immediately to the right of the pilot.
10. The dog owner lives immediately to the right of the person who enjoys painting.
11. Whoever lives in the green house works as the farmer.

## Puzzle zebra-00015

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, cat, fish, rabbit, dog
- job: teacher, farmer, pilot, lawyer, baker
- color: purple, green, blue, white, yellow
- nationality: Dane, Brit, Norwegian, Spaniard, German

Clues:
1. The occupant of the white house is the Spaniard.
2. Whoever lives in the blue house and the German live in adjacent houses.
3. The person who keeps the rabbit either lives in the purple house or lives in the white house.
4. The person who keeps the fish and whoever lives in the green house live in adjacent houses.
5. The person who keeps the fish lives somewhere to the right of the Norwegian.
6. The teacher lives somewhere to the left of the person who keeps the horse.
7. The farmer lives next to the Norwegian.
8. The occupant of the white house lives in the house just left of the one where the Dane lives.
9. The person who keeps the horse lives in the house just left of the one where the occupant of the yellow house lives.
10. There is exactly one house between the occupant of the blue house and the Spaniard.
11. The owner of the horse either works as the lawyer or works as the pilot.
12. The farmer keeps the cat.
13. The person in the blue house and the pilot live in adjacent houses.
14. The baker and the Brit live two houses apart.

## Puzzle zebra-00017

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

## Puzzle zebra-00000

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, dog, bird, fish, rabbit
- job: farmer, teacher, baker, doctor, lawyer
- hobby: golf, tennis, chess, hiking, cooking
- nationality: Brit, German, Spaniard, Norwegian, Swede

Clues:
1. The Spaniard lives in the house just left of the one where the hiking enthusiast lives.
2. The German lives next to the teacher.
3. The baker keeps the rabbit.
4. The tennis enthusiast lives in house 4.
5. The Norwegian keeps the rabbit.
6. The person who keeps the bird and the person who enjoys golf are neighbours.
7. The cooking enthusiast and the German live two houses apart.
8. The lawyer lives directly to the left of the farmer.
9. The owner of the bird works as the teacher.
10. The cooking enthusiast and the person who keeps the dog are neighbours.
11. There is exactly one house between the farmer and the horse owner.
12. The Swede lives in the house just left of the one where the horse owner lives.

## Puzzle zebra-00008

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

## Puzzle zebra-00014

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

## Puzzle zebra-00011

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, baker, pilot, farmer
- nationality: German, Brit, Norwegian, Swede, Spaniard
- hobby: chess, cooking, painting, tennis, golf
- color: red, purple, white, green, yellow

Clues:
1. The German lives somewhere to the left of whoever lives in the yellow house.
2. The painting enthusiast works as the doctor.
3. There is exactly one house between the cooking enthusiast and the occupant of the red house.
4. The occupant of the white house lives somewhere to the left of the person who enjoys tennis.
5. Whoever lives in the green house works as the baker.
6. The Spaniard lives next to the person who enjoys tennis.
7. The Brit and the Swede are neighbours.
8. There is exactly one house between the cooking enthusiast and the Spaniard.
9. The farmer either is the Norwegian or is the Swede.
10. The golf enthusiast and the teacher are neighbours.
11. The baker is the Brit.
12. The German and the person in the purple house live two houses apart.
13. The golf enthusiast lives directly to the left of the baker.

## Puzzle zebra-00012

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, cocoa, coffee, milk, juice
- hobby: cooking, tennis, painting, hiking, chess
- job: lawyer, pilot, farmer, doctor, teacher
- color: green, blue, white, yellow, purple

Clues:
1. The chess enthusiast lives in the second house.
2. The person in the green house and the person in the purple house live in adjacent houses.
3. The farmer drinks cocoa.
4. The farmer lives in the house just left of the one where the lawyer lives.
5. The tennis enthusiast works as the farmer.
6. The person who drinks coffee lives next to the hiking enthusiast.
7. There is exactly one house between whoever lives in the blue house and the person who drinks juice.
8. The teacher lives in the third house.
9. The person who drinks tea and the tennis enthusiast live two houses apart.
10. Whoever lives in the green house does not live in house 4.
11. The person who enjoys chess lives in the white house.
12. The person who enjoys painting and whoever lives in the white house live in adjacent houses.
13. The person who drinks tea lives directly to the left of the pilot.
