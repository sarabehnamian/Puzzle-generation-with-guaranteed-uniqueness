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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_002.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00033

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, rabbit, dog, horse, cat
- nationality: Swede, German, Spaniard, Norwegian, Dane
- hobby: chess, hiking, golf, tennis, cooking
- job: pilot, teacher, lawyer, doctor, baker

Clues:
1. The pilot lives next to the Swede.
2. The teacher lives in the first house.
3. The owner of the dog either enjoys chess or enjoys golf.
4. The cooking enthusiast lives somewhere to the right of the person who enjoys tennis.
5. The person who keeps the cat enjoys cooking.
6. The person who enjoys chess either keeps the horse or keeps the rabbit.
7. The owner of the rabbit lives directly to the left of the horse owner.
8. The doctor lives in the house just left of the one where the rabbit owner lives.
9. The chess enthusiast lives in the house just left of the one where the Dane lives.
10. The baker and the person who keeps the rabbit live two houses apart.
11. The Dane and the German live two houses apart.
12. There is exactly one house between the person who enjoys hiking and the rabbit owner.
13. The Spaniard lives immediately to the right of the owner of the rabbit.

## Puzzle hard:zebra_hard-00059

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, cooking, painting, chess, golf
- nationality: Swede, German, Brit, Dane, Norwegian
- drink: cocoa, water, juice, milk, tea
- job: baker, doctor, pilot, teacher, lawyer

Clues:
1. The pilot and the person who drinks tea are one and the same person.
2. If the doctor does not enjoy painting, then that person enjoys tennis.
3. The person who drinks milk lives somewhere between the baker and the person who drinks water.
4. The left-hand neighbour of the person who drinks juice is the Dane.
5. Neither the Norwegian nor the person who drinks water works as the doctor.
6. The right-hand neighbour of the painting enthusiast works as the teacher.
7. The German and the teacher are one and the same person.
8. Neither the doctor nor the person who drinks juice is the Swede.
9. The left-hand neighbour of the German drinks juice.
10. The cooking enthusiast lives two doors away from the pilot.
11. One of the neighbours of the German enjoys chess.
12. If the person who enjoys chess is not the Brit, then that person is the Dane.

## Puzzle hard:zebra_hard-00061

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, cat, bird, dog, horse
- hobby: tennis, golf, hiking, cooking, chess
- color: green, blue, red, yellow, white
- drink: water, coffee, juice, milk, tea

Clues:
1. Exactly 1 house lies to the left of the home of the person who drinks tea.
2. The person who enjoys golf lives somewhere between the person who drinks coffee and the horse owner.
3. The person in the blue house and the juice drinker are one and the same person.
4. One of the neighbours of the person who keeps the cat enjoys chess.
5. Whoever lives in the blue house and the person who enjoys cooking are one and the same person.
6. One of the neighbours of the person who enjoys cooking lives in the white house.
7. The person who enjoys hiking lives two doors away from the occupant of the red house.
8. One of the neighbours of the occupant of the white house drinks milk.
9. The left-hand neighbour of the chess enthusiast drinks water.
10. The owner of the cat and whoever lives in the red house are one and the same person.
11. Exactly one house separates the person who keeps the fish from the person in the green house.
12. One of the neighbours of the owner of the dog enjoys chess.

## Puzzle plain:zebra-00084

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, purple, yellow, white, blue
- pet: bird, cat, rabbit, dog, horse
- drink: coffee, juice, milk, cocoa, water
- nationality: Swede, Brit, Dane, German, Spaniard

Clues:
1. The bird owner lives in the fifth house.
2. The cat owner lives in the house just left of the one where the Spaniard lives.
3. The water drinker lives immediately to the right of the dog owner.
4. The dog owner drinks cocoa.
5. The person who drinks milk lives in the red house.
6. The Dane lives in house 2.
7. The juice drinker lives in the house just left of the one where the person in the yellow house lives.
8. The owner of the dog lives next to whoever lives in the yellow house.
9. The person in the yellow house lives in the house just left of the one where the person in the blue house lives.
10. The coffee drinker lives somewhere to the left of the occupant of the purple house.
11. The owner of the bird lives next to the Swede.
12. The owner of the cat does not live next to the milk drinker.
13. The occupant of the yellow house lives immediately to the right of the rabbit owner.
14. The German lives in house 1.

## Puzzle plain:zebra-00098

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, hiking, golf, chess, painting
- drink: tea, juice, coffee, water, milk
- pet: rabbit, bird, fish, cat, horse
- job: farmer, baker, doctor, teacher, pilot

Clues:
1. The owner of the fish and the teacher live in adjacent houses.
2. The pilot lives in the house just left of the one where the person who keeps the horse lives.
3. The owner of the horse and the water drinker are neighbours.
4. The chess enthusiast drinks water.
5. The person who drinks tea lives directly to the left of the owner of the fish.
6. The coffee drinker lives in one of the two end houses.
7. The owner of the cat and the farmer live two houses apart.
8. The farmer enjoys painting.
9. The person who keeps the bird lives next to the person who drinks milk.
10. The owner of the fish lives in house 3.
11. The doctor and the person who enjoys golf live in adjacent houses.
12. The person who enjoys cooking either works as the baker or works as the teacher.
13. The owner of the cat works as the baker.

## Puzzle hard:zebra_hard-00076

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, cat, rabbit, horse, dog
- job: farmer, baker, teacher, doctor, pilot
- hobby: painting, golf, chess, tennis, cooking
- color: red, white, green, blue, purple

Clues:
1. If the person who enjoys golf is not the baker, then that person works as the doctor.
2. The person who enjoys painting lives two doors away from the pilot.
3. One of the neighbours of the person in the green house enjoys chess.
4. None of the neighbours of the owner of the cat keeps the dog.
5. The owner of the cat and the doctor are one and the same person.
6. The person who enjoys chess lives in the second house from the right.
7. The doctor and the person in the red house are one and the same person.
8. The person in the purple house lives further to the right than the person who enjoys cooking.
9. The owner of the cat lives in the third house from the right.
10. The owner of the fish and whoever lives in the white house are one and the same person.
11. The farmer and the person who keeps the horse are one and the same person.
12. The cooking enthusiast lives somewhere between the owner of the fish and the horse owner.
13. If the baker does not keep the fish, then that person keeps the horse.

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

## Puzzle hard:zebra_hard-00052

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, yellow, red, purple, white
- hobby: tennis, hiking, painting, golf, cooking
- nationality: Brit, Spaniard, Swede, Dane, German
- pet: cat, dog, rabbit, bird, horse

Clues:
1. Exactly one house separates the person who keeps the bird from the person who enjoys tennis.
2. The hiking enthusiast and the Spaniard are one and the same person.
3. The person who keeps the horse lives further to the right than the cooking enthusiast.
4. Whoever lives in the white house lives in the second house from the right.
5. If the person who enjoys tennis is not the Dane, then that person is the Spaniard.
6. Exactly 2 houses lie to the left of the home of the horse owner.
7. The right-hand neighbour of whoever lives in the red house keeps the cat.
8. The person who enjoys hiking and the person who keeps the rabbit are one and the same person.
9. If the German does not live in the purple house, then that person lives in the white house.
10. The occupant of the purple house lives somewhere between the person who enjoys painting and the occupant of the white house.
11. The cat owner and the person who enjoys painting are one and the same person.
12. If the Brit does not live in the blue house, then that person lives in the purple house.

## Puzzle plain:zebra-00007

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

## Puzzle paraphrase:zebra-00166

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, cooking, chess, painting, hiking
- job: pilot, farmer, teacher, doctor, baker
- pet: dog, cat, fish, rabbit, horse
- color: yellow, purple, red, blue, green

Clues:
1. The hiker lives next door to the rabbit owner.
2. The red house's occupant keeps the cat.
3. The doctor keeps the fish.
4. The golfer and the horse owner live in adjacent houses.
5. The yellow house's occupant is the baker.
6. Exactly one house lies between the horse owner and the rabbit owner.
7. The baker's hobby is cooking.
8. The blue house's occupant lives next to the fish owner.
9. The fish owner lives in one of the two end houses.
10. One house separates the horse owner from the yellow house.
11. The farmer lives in a lower-numbered house than the teacher.
12. The green house is immediately to the right of the blue house.
13. One house separates the pilot from the purple house.
14. Exactly one house lies between the horse owner and the painter.
