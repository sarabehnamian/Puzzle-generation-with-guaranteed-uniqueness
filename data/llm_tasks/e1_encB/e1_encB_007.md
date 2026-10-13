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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encB/e1_encB_007.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00040

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, coffee, cocoa, water, tea
- hobby: golf, tennis, chess, hiking, painting
- job: farmer, baker, lawyer, pilot, teacher
- nationality: Dane, German, Brit, Norwegian, Swede

Clues:
1. There is exactly one house between the Dane and the teacher.
2. The person who drinks cocoa enjoys painting.
3. The farmer and the tea drinker live in adjacent houses.
4. The Brit lives in house 2.
5. The pilot and the person who drinks tea are not neighbours.
6. The farmer enjoys chess.
7. The person who drinks cocoa is the Norwegian.
8. The Dane and the farmer live in adjacent houses.
9. The Dane lives in house 4.
10. The milk drinker lives in the house just left of the one where the person who enjoys golf lives.
11. The farmer and the lawyer live two houses apart.
12. The tea drinker lives next to the water drinker.
13. The German lives immediately to the right of the person who enjoys tennis.
14. The Norwegian lives in house 5.
15. The pilot lives in one of the two end houses.

## Puzzle plain:zebra-00050

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, bird, fish, cat
- drink: tea, water, cocoa, juice, milk
- job: pilot, baker, farmer, doctor, teacher
- hobby: cooking, painting, golf, hiking, tennis

Clues:
1. The pilot lives in the house just left of the one where the juice drinker lives.
2. The doctor lives somewhere to the right of the person who enjoys tennis.
3. The hiking enthusiast lives at one end of the row.
4. The milk drinker lives directly to the left of the baker.
5. The horse owner lives in house 2.
6. The cocoa drinker and the juice drinker are neighbours.
7. The hiking enthusiast lives somewhere to the left of the cooking enthusiast.
8. The painting enthusiast lives in the house just left of the one where the baker lives.
9. The farmer lives directly to the left of the person who enjoys golf.
10. The farmer and the person who drinks water live two houses apart.
11. The bird owner either works as the pilot or works as the teacher.
12. There is exactly one house between the person who keeps the cat and the person who keeps the dog.
13. There is exactly one house between the person who keeps the cat and the pilot.

## Puzzle paraphrase:zebra-00118

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, chess, cooking, hiking, painting
- job: pilot, teacher, lawyer, doctor, farmer
- color: blue, white, yellow, red, green
- pet: dog, fish, horse, cat, bird

Clues:
1. The cat lives in the yellow house.
2. The hiking enthusiast is either the lawyer or the pilot.
3. The bird owner lives right next to the white house.
4. The fish owner lives directly to the left of the hiking enthusiast.
5. The farmer is the cooking enthusiast.
6. The chess enthusiast and the green house's occupant have exactly one house between them.
7. The painting enthusiast and the teacher live in adjacent houses.
8. The cooking enthusiast lives in one of the two end houses.
9. The horse is kept in the blue house.
10. The tennis enthusiast lives in either the blue house or the red house.
11. The dog owner and the horse owner live in adjacent houses.
12. The hiking enthusiast and the lawyer live in neighbouring houses.
13. The painting enthusiast lives immediately to the left of the cat owner.
14. Exactly one house lies between the blue house and the fish owner.

## Puzzle hard:zebra_hard-00051

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Brit, Swede, Spaniard, Dane
- color: purple, green, yellow, blue, white
- job: teacher, pilot, farmer, lawyer, baker
- hobby: cooking, painting, golf, tennis, hiking

Clues:
1. One of the neighbours of the Brit works as the baker.
2. If the person who enjoys painting is not the farmer, then that person works as the lawyer.
3. If whoever lives in the white house is not the Dane, then that person is the Swede.
4. None of the neighbours of the baker lives in the blue house.
5. At least one house separates the occupant of the green house from the occupant of the yellow house.
6. The left-hand neighbour of the pilot enjoys tennis.
7. The left-hand neighbour of the lawyer is the Dane.
8. The person who enjoys cooking and the occupant of the white house are one and the same person.
9. The left-hand neighbour of the person who enjoys tennis works as the baker.
10. The person who enjoys hiking is not the same person as the pilot.
11. Neither the Brit nor the Spaniard enjoys tennis.
12. One of the neighbours of the person who enjoys cooking is the Swede.
13. Neither the cooking enthusiast nor the pilot is the Norwegian.
14. The farmer lives further to the right than the cooking enthusiast.
15. The person in the yellow house lives somewhere between whoever lives in the green house and the occupant of the white house.

## Puzzle hard:zebra_hard-00001

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, baker, farmer, lawyer, teacher
- nationality: Brit, Swede, Spaniard, German, Dane
- drink: milk, juice, water, tea, cocoa
- pet: bird, horse, rabbit, dog, cat

Clues:
1. Neither the cat owner nor the milk drinker works as the doctor.
2. The right-hand neighbour of the German is the Brit.
3. The left-hand neighbour of the baker keeps the horse.
4. The person who drinks cocoa and the doctor are one and the same person.
5. The person who keeps the rabbit lives somewhere between the bird owner and the farmer.
6. The owner of the bird and the teacher are one and the same person.
7. The left-hand neighbour of the Spaniard drinks tea.
8. One of the neighbours of the person who drinks juice keeps the cat.
9. The Dane lives in the fifth house from the right.
10. One of the neighbours of the person who drinks water keeps the bird.
11. The right-hand neighbour of the person who keeps the cat drinks tea.
12. The baker and the water drinker are one and the same person.

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

## Puzzle hard:zebra_hard-00027

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Brit, Norwegian, Swede, Dane
- color: green, blue, purple, yellow, white
- drink: coffee, milk, cocoa, water, juice
- pet: dog, horse, fish, cat, bird

Clues:
1. The person who keeps the fish and the Spaniard are one and the same person.
2. If the Dane does not keep the fish, then that person keeps the horse.
3. The person who keeps the fish lives two doors away from the person who drinks milk.
4. One of the neighbours of the dog owner drinks cocoa.
5. The Swede lives somewhere between the person who drinks cocoa and the person in the yellow house.
6. The right-hand neighbour of the Dane lives in the green house.
7. The right-hand neighbour of the cat owner lives in the purple house.
8. Exactly one house separates the juice drinker from the Swede.
9. The person who drinks coffee lives two doors away from the Dane.
10. Whoever lives in the yellow house lives somewhere between the cat owner and the person who keeps the fish.
11. The Brit and whoever lives in the white house are one and the same person.
12. The cat owner and the person who drinks coffee are one and the same person.

## Puzzle plain:zebra-00025

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: cat, horse, dog, bird, rabbit
- color: red, yellow, white, purple, green
- job: teacher, baker, lawyer, farmer, doctor
- hobby: cooking, hiking, golf, painting, tennis

Clues:
1. The person who enjoys painting lives immediately to the right of the teacher.
2. The lawyer either keeps the bird or keeps the cat.
3. The owner of the rabbit lives in the green house.
4. The person who enjoys golf lives somewhere to the left of the farmer.
5. The farmer and the person in the yellow house are neighbours.
6. The horse owner enjoys cooking.
7. The painting enthusiast and the person in the purple house are neighbours.
8. The cooking enthusiast lives in the second house.
9. The doctor and the owner of the rabbit are neighbours.
10. The baker lives immediately to the right of the person who enjoys cooking.
11. The bird owner lives in the house just left of the one where the owner of the rabbit lives.
12. The bird owner lives in the white house.
13. The rabbit owner lives in the house just left of the one where the tennis enthusiast lives.

## Puzzle hard:zebra_hard-00087

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, yellow, white, purple, green
- hobby: cooking, hiking, tennis, golf, chess
- nationality: Brit, German, Swede, Dane, Norwegian
- drink: coffee, water, cocoa, milk, tea

Clues:
1. If the person who enjoys chess does not live in the purple house, then that person lives in the yellow house.
2. The tea drinker lives somewhere between the cocoa drinker and whoever lives in the purple house.
3. One of the neighbours of the person who drinks coffee lives in the blue house.
4. One of the neighbours of the Norwegian enjoys cooking.
5. Exactly 2 houses lie to the left of the home of the golf enthusiast.
6. The person who drinks cocoa and the Dane are one and the same person.
7. At least one house separates the cooking enthusiast from the occupant of the yellow house.
8. The person who enjoys hiking and the Swede are one and the same person.
9. The Brit lives two doors away from the person who enjoys hiking.
10. The person who drinks milk and the Norwegian are one and the same person.
11. The occupant of the blue house lives somewhere between the person who enjoys golf and the person who drinks water.
12. Exactly 1 house lies to the left of the home of whoever lives in the white house.

## Puzzle paraphrase:zebra-00151

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, water, juice, milk, cocoa
- color: red, green, yellow, blue, purple
- nationality: Swede, Spaniard, Brit, Dane, Norwegian
- job: teacher, lawyer, farmer, pilot, baker

Clues:
1. The lawyer's house is red.
2. Somewhere further to the right of the Swede lives the baker.
3. The Brit's house is at one of the two ends of the row.
4. The Norwegian lives right next door to the right of the milk drinker.
5. The yellow house's occupant is either the farmer or the pilot.
6. The Norwegian's house is immediately right of the green house.
7. The blue house's occupant and the Swede live two houses apart.
8. The Spaniard is the one living in the blue house.
9. The Dane is the baker.
10. A single house lies between the farmer and the occupant of the red house.
11. The juice drinker and the milk drinker live two houses apart.
12. The red house stands directly to the left of the juice drinker's house.
13. The teacher's house number is lower than the Spaniard's.
14. The Norwegian lives somewhere to the left of the water drinker.
15. The blue house's occupant and the coffee drinker do not live next door to each other.
