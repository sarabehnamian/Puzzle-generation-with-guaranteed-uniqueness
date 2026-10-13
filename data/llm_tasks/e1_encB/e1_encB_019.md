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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encB/e1_encB_019.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00115

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Brit, Dane, Swede, Norwegian
- drink: coffee, tea, cocoa, water, milk
- color: blue, yellow, purple, red, green
- job: doctor, teacher, pilot, lawyer, farmer

Clues:
1. The Norwegian lives directly to the left of the milk drinker.
2. The red house stands immediately to the left of the blue house.
3. The farmer drinks coffee.
4. The Brit lives in either the green house or the red house.
5. The Dane lives in the fifth house.
6. The cocoa drinker and the purple house's occupant have exactly one house between them.
7. Exactly one house separates the Brit from the Norwegian.
8. The Spaniard lives immediately to the right of the green house.
9. The farmer lives next door to the teacher.
10. The yellow house is immediately to the right of the Spaniard's.
11. The doctor drinks water.
12. The farmer lives in the yellow house.
13. The farmer and the pilot have exactly one house between them.

## Puzzle plain:zebra-00075

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, teacher, baker, pilot
- color: yellow, white, red, green, blue
- hobby: golf, painting, tennis, hiking, cooking
- nationality: Brit, Norwegian, Swede, Spaniard, Dane

Clues:
1. The doctor does not live next to whoever lives in the yellow house.
2. The pilot lives immediately to the right of the tennis enthusiast.
3. Whoever lives in the red house lives somewhere to the right of the baker.
4. The golf enthusiast lives in the red house.
5. There is exactly one house between the hiking enthusiast and the lawyer.
6. Whoever lives in the blue house lives in the house just left of the one where the person in the red house lives.
7. The Dane lives in the house just left of the one where the Swede lives.
8. The person who enjoys painting and the person in the white house live in adjacent houses.
9. Whoever lives in the white house either is the Brit or is the Swede.
10. The doctor lives in the house just left of the one where the pilot lives.
11. The baker lives at one end of the row.
12. The Brit lives somewhere to the left of the golf enthusiast.
13. The Norwegian lives directly to the left of the lawyer.
14. The person who enjoys cooking lives directly to the left of the person who enjoys golf.

## Puzzle plain:zebra-00078

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, coffee, cocoa, juice, water
- hobby: golf, tennis, chess, painting, cooking
- color: white, yellow, red, green, blue
- nationality: Norwegian, Swede, Spaniard, German, Dane

Clues:
1. The person in the blue house and the juice drinker live in adjacent houses.
2. The occupant of the green house lives directly to the left of the golf enthusiast.
3. The occupant of the green house and whoever lives in the yellow house live two houses apart.
4. The German lives next to the person who enjoys golf.
5. The person in the yellow house is the Swede.
6. The person who drinks coffee lives immediately to the right of the person who drinks milk.
7. The painting enthusiast lives directly to the left of the occupant of the white house.
8. Whoever lives in the green house either enjoys chess or enjoys painting.
9. The Dane enjoys painting.
10. The German drinks milk.
11. The water drinker lives in house 2.
12. The person who drinks juice enjoys tennis.
13. The occupant of the yellow house lives immediately to the right of the Norwegian.

## Puzzle paraphrase:zebra-00189

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, farmer, teacher, doctor, baker
- hobby: painting, tennis, cooking, hiking, golf
- pet: horse, rabbit, fish, dog, bird
- nationality: German, Dane, Swede, Spaniard, Brit

Clues:
1. The rabbit owner and the tennis enthusiast live two houses apart.
2. The Spaniard is the painting enthusiast.
3. The bird's owner lives immediately to the left of the doctor.
4. The Dane and the farmer live in neighbouring houses.
5. The Spaniard lives immediately to the right of the fish owner.
6. The golf enthusiast lives immediately to the left of the dog owner.
7. The lawyer occupies the fourth house.
8. One house lies between the Swede and the teacher.
9. The German lives immediately to the left of the dog owner.
10. The Swede lives somewhere to the left of the Spaniard.
11. The painting enthusiast does not live in house 5.
12. The Dane and the horse owner live two houses apart.
13. The cooking enthusiast is the farmer.

## Puzzle hard:zebra_hard-00042

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, lawyer, farmer, baker, teacher
- nationality: Spaniard, Swede, Norwegian, Brit, German
- pet: bird, dog, horse, cat, rabbit
- color: blue, yellow, red, purple, white

Clues:
1. If the bird owner is not the doctor, then that person works as the teacher.
2. One of the neighbours of the baker is the Brit.
3. The person who keeps the bird and the occupant of the blue house are one and the same person.
4. The person in the red house lives two doors away from the Spaniard.
5. The owner of the cat lives in the second house from the right.
6. One of the neighbours of the person who keeps the rabbit works as the doctor.
7. The teacher lives in the fourth house from the right.
8. The right-hand neighbour of the cat owner works as the farmer.
9. The right-hand neighbour of whoever lives in the yellow house works as the lawyer.
10. The right-hand neighbour of the horse owner is the Norwegian.
11. The owner of the dog and the German are one and the same person.
12. One of the neighbours of the person who keeps the bird lives in the white house.

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

## Puzzle plain:zebra-00095

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, juice, milk, water, coffee
- pet: cat, bird, horse, rabbit, dog
- nationality: German, Swede, Dane, Norwegian, Brit
- hobby: chess, hiking, cooking, golf, painting

Clues:
1. The German and the person who drinks water live in adjacent houses.
2. The cat owner drinks water.
3. There is exactly one house between the Brit and the dog owner.
4. The cocoa drinker and the cooking enthusiast live in adjacent houses.
5. The owner of the cat and the juice drinker are neighbours.
6. The Dane either drinks coffee or drinks water.
7. The golf enthusiast and the Norwegian are neighbours.
8. The juice drinker enjoys painting.
9. The Brit does not live next to the hiking enthusiast.
10. The hiking enthusiast and the person who drinks juice are neighbours.
11. The owner of the bird lives immediately to the right of the rabbit owner.
12. The person who enjoys cooking lives directly to the left of the person who keeps the rabbit.
13. The person who keeps the cat and the person who keeps the rabbit are neighbours.
14. The Brit lives in the house just left of the one where the Dane lives.

## Puzzle hard:zebra_hard-00084

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, farmer, pilot, teacher
- hobby: golf, chess, tennis, cooking, painting
- nationality: Spaniard, Dane, Swede, Norwegian, Brit
- pet: cat, dog, fish, bird, horse

Clues:
1. The left-hand neighbour of the farmer keeps the fish.
2. The right-hand neighbour of the person who enjoys painting keeps the bird.
3. The right-hand neighbour of the person who enjoys cooking works as the teacher.
4. The left-hand neighbour of the doctor is the Dane.
5. The left-hand neighbour of the golf enthusiast enjoys cooking.
6. One of the neighbours of the person who enjoys tennis works as the teacher.
7. The Brit lives two doors away from the person who keeps the cat.
8. The owner of the fish lives two doors away from the person who keeps the horse.
9. The left-hand neighbour of the dog owner is the Norwegian.
10. If the lawyer is not the Norwegian, then that person is the Swede.
11. The right-hand neighbour of the teacher is the Swede.
12. The left-hand neighbour of the person who keeps the fish keeps the cat.

## Puzzle plain:zebra-00081

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, tennis, cooking, chess, golf
- job: pilot, teacher, doctor, baker, lawyer
- color: white, yellow, red, purple, green
- drink: water, cocoa, tea, coffee, juice

Clues:
1. The cocoa drinker lives in the leftmost house.
2. The golf enthusiast lives in the middle house.
3. The hiking enthusiast works as the baker.
4. The tea drinker lives in house 4.
5. The teacher lives immediately to the right of the person who enjoys hiking.
6. The person who enjoys cooking either drinks coffee or drinks tea.
7. The doctor either lives in the green house or lives in the yellow house.
8. Whoever lives in the purple house works as the pilot.
9. Whoever lives in the yellow house lives in the house just left of the one where the person who enjoys tennis lives.
10. Whoever lives in the white house enjoys cooking.
11. Whoever lives in the green house lives directly to the left of the person in the yellow house.
12. The doctor enjoys chess.
13. The person who drinks juice and the pilot live two houses apart.

## Puzzle plain:zebra-00051

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, tennis, chess, painting, golf
- job: pilot, farmer, baker, lawyer, teacher
- color: yellow, white, purple, red, green
- nationality: Spaniard, Brit, German, Swede, Dane

Clues:
1. The person who enjoys tennis and the farmer are different people.
2. The person who enjoys painting lives directly to the left of the person who enjoys golf.
3. The Swede and the person in the white house live two houses apart.
4. The baker lives in the house just left of the one where the Swede lives.
5. The teacher and the occupant of the yellow house are neighbours.
6. The Dane lives in the green house.
7. The cooking enthusiast lives in the red house.
8. The baker lives directly to the left of the person who enjoys chess.
9. Whoever lives in the white house lives in a lower-numbered house than the person who enjoys chess.
10. The lawyer and the teacher live two houses apart.
11. The teacher lives immediately to the right of the person who enjoys cooking.
12. The occupant of the red house and the Swede live in adjacent houses.
13. The Spaniard and the Swede live in adjacent houses.
14. The German lives in house 3.
