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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_023.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00053

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, cooking, painting, hiking, tennis
- job: lawyer, pilot, teacher, doctor, baker
- color: blue, purple, green, yellow, red
- pet: horse, bird, fish, rabbit, cat

Clues:
1. The chess enthusiast and the pilot are one and the same person.
2. The person who keeps the cat does not live to the right of the rabbit owner.
3. None of the neighbours of the doctor works as the teacher.
4. The right-hand neighbour of the doctor enjoys cooking.
5. The left-hand neighbour of the person who enjoys painting works as the teacher.
6. Whoever lives in the blue house lives two doors away from the person who keeps the horse.
7. The tennis enthusiast lives somewhere between the person who keeps the rabbit and whoever lives in the yellow house.
8. The person who enjoys chess and the occupant of the red house are one and the same person.
9. The owner of the bird and the person who enjoys hiking are one and the same person.
10. Exactly one house separates whoever lives in the purple house from whoever lives in the red house.
11. Whoever lives in the blue house is not the same person as the owner of the cat.
12. Exactly 1 house lies to the left of the home of the person in the blue house.
13. Whoever lives in the purple house lives two doors away from the teacher.
14. At least one house separates the lawyer from the person who enjoys chess.

## Puzzle plain:zebra-00035

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Spaniard, Dane, Swede, German
- hobby: golf, hiking, chess, painting, cooking
- job: baker, doctor, pilot, farmer, teacher
- drink: tea, coffee, juice, water, milk

Clues:
1. The person who drinks milk and the teacher live two houses apart.
2. The person who drinks tea either works as the farmer or works as the pilot.
3. There is exactly one house between the person who enjoys chess and the person who enjoys hiking.
4. The Brit enjoys hiking.
5. The chess enthusiast either is the Brit or is the Swede.
6. The pilot lives directly to the left of the teacher.
7. The farmer lives somewhere to the left of the water drinker.
8. The baker drinks milk.
9. The Spaniard is not the doctor.
10. The German either drinks milk or drinks tea.
11. The person who drinks juice lives in house 4.
12. The person who enjoys cooking lives next to the person who enjoys hiking.
13. The person who drinks coffee lives in the second house.
14. The tea drinker is the Brit.
15. The baker either enjoys chess or enjoys painting.

## Puzzle plain:zebra-00079

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, tennis, cooking, golf, chess
- color: purple, yellow, green, white, blue
- pet: bird, dog, cat, fish, rabbit
- job: doctor, baker, pilot, farmer, lawyer

Clues:
1. The person who keeps the fish lives immediately to the right of the person who keeps the dog.
2. The pilot lives directly to the left of the farmer.
3. The pilot and the owner of the rabbit live two houses apart.
4. The occupant of the yellow house either works as the baker or works as the pilot.
5. The farmer lives somewhere to the right of the occupant of the purple house.
6. The fish owner either enjoys chess or enjoys golf.
7. The person in the blue house either works as the farmer or works as the pilot.
8. The person in the purple house does not live in house 2.
9. The baker enjoys hiking.
10. The person who keeps the rabbit lives in a lower-numbered house than the person who keeps the cat.
11. The occupant of the white house is not the lawyer.
12. The person who enjoys cooking lives immediately to the right of the fish owner.
13. The golf enthusiast lives in the house just left of the one where the person in the purple house lives.
14. The pilot and the person in the white house live two houses apart.
15. The person who enjoys tennis either lives in the blue house or lives in the green house.

## Puzzle plain:zebra-00037

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: cat, rabbit, dog, fish, bird
- hobby: tennis, painting, hiking, chess, cooking
- job: lawyer, doctor, pilot, teacher, baker
- nationality: Spaniard, Brit, Dane, German, Norwegian

Clues:
1. The owner of the cat lives next to the Spaniard.
2. The Dane lives in the third house.
3. The person who enjoys painting is the Dane.
4. The hiking enthusiast lives in the second house.
5. There is exactly one house between the owner of the dog and the rabbit owner.
6. The lawyer lives immediately to the right of the teacher.
7. The doctor lives in the house just left of the one where the person who keeps the cat lives.
8. The person who enjoys tennis lives somewhere to the left of the person who enjoys cooking.
9. The cooking enthusiast and the person who enjoys hiking live two houses apart.
10. The cat owner and the Norwegian live two houses apart.
11. The person who keeps the fish either enjoys chess or enjoys cooking.
12. The pilot and the person who keeps the rabbit live two houses apart.
13. The teacher lives in the leftmost house.
14. The German and the owner of the rabbit live in adjacent houses.

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

## Puzzle plain:zebra-00069

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, green, yellow, blue, white
- job: pilot, baker, doctor, teacher, farmer
- pet: fish, rabbit, bird, horse, dog
- hobby: hiking, tennis, cooking, chess, painting

Clues:
1. The doctor lives directly to the left of the hiking enthusiast.
2. The baker lives immediately to the right of the person who enjoys cooking.
3. The occupant of the blue house works as the baker.
4. The occupant of the yellow house lives in the second house.
5. The tennis enthusiast lives in the third house.
6. The chess enthusiast and the pilot live in adjacent houses.
7. The fish owner lives in a lower-numbered house than the chess enthusiast.
8. The dog owner and the owner of the rabbit are not neighbours.
9. The teacher lives in the white house.
10. The owner of the dog lives immediately to the right of the doctor.
11. The owner of the bird lives in the fourth house.
12. The fish owner either lives in the green house or lives in the yellow house.
13. There is exactly one house between the farmer and the pilot.

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

## Puzzle plain:zebra-00003

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, hiking, cooking, tennis, golf
- nationality: Dane, Norwegian, Brit, Spaniard, Swede
- pet: bird, fish, horse, rabbit, dog
- job: farmer, baker, doctor, lawyer, pilot

Clues:
1. The owner of the horse enjoys chess.
2. The Swede either works as the farmer or works as the lawyer.
3. The Swede lives in the third house.
4. The Spaniard lives immediately to the right of the pilot.
5. The owner of the fish and the person who enjoys golf live two houses apart.
6. The Dane is not the farmer.
7. The person who keeps the horse lives somewhere to the left of the hiking enthusiast.
8. The person who keeps the fish lives in a lower-numbered house than the person who enjoys hiking.
9. The person who enjoys cooking works as the pilot.
10. The Norwegian keeps the rabbit.
11. The chess enthusiast either works as the lawyer or works as the pilot.
12. The Brit lives in one of the two end houses.
13. The baker lives immediately to the right of the Norwegian.
14. The owner of the rabbit lives next to the tennis enthusiast.
15. There is exactly one house between the bird owner and the owner of the horse.

## Puzzle hard:zebra_hard-00013

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, bird, dog, cat, rabbit
- job: farmer, pilot, teacher, doctor, baker
- drink: juice, coffee, milk, tea, cocoa
- color: green, blue, yellow, white, purple

Clues:
1. The doctor lives somewhere between the coffee drinker and the person who keeps the dog.
2. The fish owner lives somewhere between the dog owner and the person who keeps the rabbit.
3. One of the neighbours of the doctor lives in the green house.
4. If the person who drinks juice is not the baker, then that person works as the teacher.
5. The cat owner lives further to the right than the coffee drinker.
6. The teacher lives somewhere between the farmer and the juice drinker.
7. Exactly one house separates the cocoa drinker from whoever lives in the yellow house.
8. At least one house separates the fish owner from the person in the white house.
9. The baker lives in the fourth house from the right.
10. The person who drinks cocoa lives somewhere between the farmer and the occupant of the green house.
11. The left-hand neighbour of the occupant of the blue house drinks milk.
12. The owner of the bird lives in the fourth house from the right.
13. The pilot and whoever lives in the purple house are one and the same person.

## Puzzle plain:zebra-00002

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
