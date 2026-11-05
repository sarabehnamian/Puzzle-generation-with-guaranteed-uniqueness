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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_025.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00083

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, chess, golf, painting, hiking
- job: lawyer, baker, teacher, farmer, doctor
- nationality: Dane, Spaniard, Brit, Norwegian, German
- color: purple, blue, yellow, red, white

Clues:
1. The German does not live next to the occupant of the red house.
2. The occupant of the blue house enjoys chess.
3. Whoever lives in the purple house is the Dane.
4. The farmer and the person who enjoys tennis are neighbours.
5. Whoever lives in the blue house does not live next to the person in the white house.
6. The Brit and the Norwegian are neighbours.
7. The person in the red house lives directly to the left of the lawyer.
8. The golf enthusiast either works as the doctor or works as the lawyer.
9. Whoever lives in the blue house lives at one end of the row.
10. The Brit lives in the fifth house.
11. The person who enjoys painting and the tennis enthusiast live two houses apart.
12. The baker does not live next to the lawyer.
13. The Dane either enjoys chess or enjoys hiking.
14. The Spaniard lives directly to the left of the tennis enthusiast.
15. The teacher lives in one of the two end houses.

## Puzzle hard:zebra_hard-00021

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, hiking, cooking, chess, tennis
- pet: fish, bird, cat, dog, horse
- drink: juice, water, tea, milk, coffee
- color: white, yellow, purple, blue, green

Clues:
1. The hiking enthusiast does not live in the rightmost house.
2. The person who enjoys golf and the horse owner are one and the same person.
3. The person who drinks tea and the person in the yellow house are one and the same person.
4. The cooking enthusiast and the tea drinker are one and the same person.
5. The owner of the dog lives in the fifth house from the right.
6. The chess enthusiast and the dog owner are one and the same person.
7. The person who enjoys chess lives two doors away from the golf enthusiast.
8. The owner of the bird does not live in the rightmost house.
9. If the person who drinks juice does not live in the blue house, then that person lives in the green house.
10. The person in the blue house has only one neighbour.
11. If the fish owner does not enjoy cooking, then that person enjoys tennis.
12. The right-hand neighbour of the person in the purple house lives in the yellow house.
13. The person who enjoys tennis and the water drinker are one and the same person.
14. Whoever lives in the blue house is not the same person as the fish owner.
15. The chess enthusiast and the coffee drinker are one and the same person.
16. The right-hand neighbour of the person who enjoys golf lives in the green house.

## Puzzle hard:zebra_hard-00048

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, blue, white, purple, red
- hobby: golf, tennis, chess, painting, hiking
- drink: cocoa, coffee, juice, tea, water
- nationality: German, Swede, Spaniard, Dane, Norwegian

Clues:
1. The left-hand neighbour of the tea drinker enjoys hiking.
2. The person who enjoys golf and the occupant of the white house are one and the same person.
3. One of the neighbours of the Spaniard is the Swede.
4. Exactly one house separates the person who drinks water from whoever lives in the white house.
5. The German lives two doors away from the Spaniard.
6. The person who enjoys hiking lives two doors away from whoever lives in the purple house.
7. The person who enjoys chess lives somewhere between the German and the person in the white house.
8. The right-hand neighbour of the Dane lives in the blue house.
9. The person who enjoys chess and the coffee drinker are one and the same person.
10. The tennis enthusiast and the water drinker are one and the same person.
11. The Swede and whoever lives in the yellow house are one and the same person.
12. The person in the blue house and the person who drinks juice are one and the same person.

## Puzzle plain:zebra-00009

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, hiking, cooking, tennis, golf
- pet: rabbit, dog, cat, bird, fish
- color: red, yellow, blue, purple, green
- drink: juice, water, milk, tea, coffee

Clues:
1. The person who drinks coffee and the tea drinker live two houses apart.
2. The cat owner and the person in the purple house live in adjacent houses.
3. The owner of the cat lives in the fourth house.
4. The person who drinks tea lives somewhere to the right of the occupant of the blue house.
5. The fish owner lives in the leftmost house.
6. The occupant of the green house enjoys chess.
7. The occupant of the green house either drinks coffee or drinks milk.
8. The tennis enthusiast either keeps the cat or keeps the dog.
9. There is exactly one house between the person who enjoys golf and the person in the green house.
10. The person who drinks juice enjoys cooking.
11. The person who drinks juice keeps the rabbit.
12. The person who drinks milk either keeps the cat or keeps the dog.
13. The person in the red house lives directly to the left of the tea drinker.
14. The water drinker keeps the cat.

## Puzzle paraphrase:zebra-00191

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, golf, cooking, chess, tennis
- job: pilot, baker, lawyer, teacher, farmer
- pet: horse, bird, fish, cat, dog
- nationality: Norwegian, Swede, Spaniard, Brit, Dane

Clues:
1. The Dane and the dog owner live in neighbouring houses.
2. The horse keeper lives immediately to the right of the chess enthusiast.
3. The tennis enthusiast is a pilot by profession.
4. The cat owner lives next door to the Swede.
5. The Swede lives right before the horse owner's house.
6. The bird owner is the lawyer.
7. The teacher lives somewhere to the right of the pilot.
8. The cooking enthusiast is the farmer.
9. The painting enthusiast keeps the cat.
10. The horse owner lives just to the left of the dog owner.
11. The Spaniard is the cooking enthusiast.
12. The tennis enthusiast keeps the horse.
13. The Brit is the pilot.

## Puzzle plain:zebra-00012

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

## Puzzle paraphrase:zebra-00190

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, German, Brit, Norwegian, Dane
- hobby: hiking, painting, cooking, chess, tennis
- drink: milk, juice, cocoa, tea, water
- pet: fish, dog, rabbit, horse, cat

Clues:
1. Whoever enjoys chess keeps a rabbit.
2. Somewhere to the left of the juice drinker lives the cocoa drinker.
3. The Dane's pet is either the dog or the fish.
4. The cooking enthusiast occupies house 1.
5. The cat owner and the painting enthusiast have exactly one house between them.
6. The German is the one who drinks tea.
7. House 4 belongs to the hiking enthusiast.
8. The cooking enthusiast and the milk drinker live two houses apart.
9. The tennis enthusiast lives right next door to the right of the chess enthusiast.
10. The horse owner drinks either milk or water.
11. The Swede lives directly to the left of the water drinker.
12. The dog owner's drink is either juice or water.
13. The Brit lives immediately to the right of the Norwegian.

## Puzzle plain:zebra-00066

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Brit, Spaniard, Norwegian, Dane
- job: lawyer, baker, doctor, pilot, farmer
- color: purple, yellow, white, green, blue
- hobby: tennis, painting, chess, cooking, golf

Clues:
1. The lawyer and whoever lives in the white house live in adjacent houses.
2. The farmer lives next to the person in the purple house.
3. The occupant of the yellow house either is the Brit or is the Norwegian.
4. The chess enthusiast lives in the blue house.
5. The golf enthusiast lives next to the person in the white house.
6. The Norwegian lives next to the Swede.
7. The farmer lives in house 2.
8. The baker and the person who enjoys painting live in adjacent houses.
9. The golf enthusiast lives somewhere to the right of whoever lives in the green house.
10. Whoever lives in the yellow house lives directly to the left of the doctor.
11. The person who enjoys cooking and the Dane live two houses apart.
12. The person who enjoys painting and the Spaniard live two houses apart.
13. The cooking enthusiast and the baker are different people.

## Puzzle plain:zebra-00031

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, tennis, painting, chess, hiking
- job: doctor, pilot, lawyer, teacher, baker
- nationality: Dane, Norwegian, Swede, Spaniard, German
- color: purple, yellow, white, green, blue

Clues:
1. The pilot lives in the house just left of the one where the teacher lives.
2. The baker and the hiking enthusiast live two houses apart.
3. The Swede lives at one end of the row.
4. The Swede works as the lawyer.
5. There is exactly one house between the chess enthusiast and the Norwegian.
6. The person who enjoys painting lives in the second house.
7. The Dane lives next to the occupant of the yellow house.
8. The Spaniard lives immediately to the right of the cooking enthusiast.
9. The chess enthusiast lives at one end of the row.
10. The doctor either lives in the blue house or lives in the yellow house.
11. The doctor lives in the house just left of the one where the cooking enthusiast lives.
12. Whoever lives in the green house either enjoys cooking or enjoys hiking.
13. The painting enthusiast and the person in the purple house live in adjacent houses.
14. The person in the yellow house lives directly to the left of the person in the blue house.

## Puzzle plain:zebra-00070

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, chess, golf, painting, hiking
- job: teacher, baker, doctor, farmer, lawyer
- pet: dog, fish, cat, bird, rabbit
- nationality: Spaniard, Norwegian, Dane, German, Swede

Clues:
1. The bird owner enjoys chess.
2. The doctor and the Norwegian are neighbours.
3. The German enjoys chess.
4. The person who enjoys golf and the Spaniard live two houses apart.
5. The lawyer lives next to the person who enjoys painting.
6. The cooking enthusiast is the Swede.
7. The Dane lives in the last house.
8. The person who keeps the fish lives in the second house.
9. The Dane and the lawyer live two houses apart.
10. There is exactly one house between the farmer and the Norwegian.
11. The painting enthusiast lives in a lower-numbered house than the Norwegian.
12. The owner of the dog and the teacher live two houses apart.
13. The person who keeps the cat does not live in the fourth house.
