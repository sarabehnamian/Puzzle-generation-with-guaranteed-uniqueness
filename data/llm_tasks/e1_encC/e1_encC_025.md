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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_025.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00102

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, painting, chess, hiking, golf
- pet: cat, bird, dog, fish, rabbit
- job: doctor, farmer, teacher, lawyer, pilot
- nationality: Dane, German, Spaniard, Norwegian, Swede

Clues:
1. The Norwegian is the one who enjoys golf.
2. The fish keeper lives somewhere to the left of the pilot.
3. The cat owner and the German live two houses apart.
4. The bird owner lives in the last house.
5. The cat owner's hobby is either golf or hiking.
6. The rabbit owner lives immediately to the left of the doctor.
7. The farmer lives next door to the tennis enthusiast.
8. The Swede is the doctor.
9. The lawyer is the Dane.
10. The Spaniard's home is house 2.
11. The bird keeper and the chess enthusiast are neighbours.
12. The farmer is the German.
13. The Swede is the dog owner.

## Puzzle paraphrase:zebra-00123

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, coffee, juice, milk, tea
- job: pilot, teacher, baker, farmer, lawyer
- nationality: Norwegian, Brit, Swede, German, Spaniard
- pet: cat, dog, bird, horse, rabbit

Clues:
1. The dog owner is the teacher.
2. The Norwegian lives in the fifth house.
3. The Swede drinks either juice or milk.
4. The Swede is the pilot.
5. The tea drinker keeps the rabbit.
6. The dog owner lives next door to the Norwegian.
7. The Spaniard is a milk drinker.
8. The milk drinker and the water drinker have exactly one house between them.
9. The farmer lives in the house immediately to the right of the dog owner.
10. The baker's house adjoins the cat keeper's.
11. The farmer and the horse owner live two houses apart.
12. The German lives directly to the right of the rabbit keeper.

## Puzzle paraphrase:zebra-00110

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, hiking, cooking, golf, tennis
- pet: horse, rabbit, fish, bird, dog
- drink: milk, cocoa, tea, coffee, juice
- nationality: Dane, Swede, Spaniard, Norwegian, Brit

Clues:
1. Whoever drinks juice is a golf enthusiast.
2. The Brit and the rabbit keeper are separated by exactly one house.
3. The cocoa drinker's house sits immediately to the left of the Dane's.
4. The one who loves cooking keeps a horse.
5. The rabbit is kept in house 5.
6. The coffee drinker lives somewhere further right along the row than the Dane.
7. The tennis player lives right next door on the left of the chess player.
8. The dog's owner drinks juice.
9. The hiking fan lives directly to the left of the dog owner.
10. The Swede occupies the leftmost house.
11. The Norwegian lives immediately to the right of the golfer.
12. The fish keeper and the milk drinker are next-door neighbours.

## Puzzle hard:zebra_hard-00067

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, water, milk, tea, coffee
- nationality: Norwegian, Swede, Brit, Spaniard, Dane
- job: pilot, farmer, doctor, teacher, baker
- hobby: golf, painting, chess, cooking, tennis

Clues:
1. The golf enthusiast and the Norwegian are one and the same person.
2. The Brit and the person who drinks cocoa are one and the same person.
3. The person who enjoys painting is not the same person as the teacher.
4. The chess enthusiast lives further to the right than the farmer.
5. At least one house separates the painting enthusiast from the baker.
6. The milk drinker and the Norwegian are one and the same person.
7. The person who enjoys cooking is not the same person as the teacher.
8. The right-hand neighbour of the teacher enjoys chess.
9. The tennis enthusiast lives further to the right than the milk drinker.
10. The pilot and the Swede are one and the same person.
11. The Swede does not live to the right of the Dane.
12. Exactly one house separates the coffee drinker from the tea drinker.
13. If the person who enjoys tennis does not drink milk, then that person drinks tea.
14. The Norwegian lives somewhere between the Spaniard and the person who drinks tea.
15. Exactly 3 houses lie to the left of the home of the doctor.

## Puzzle paraphrase:zebra-00109

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Norwegian, Swede, Spaniard, German
- job: doctor, baker, lawyer, farmer, pilot
- hobby: golf, hiking, painting, cooking, chess
- pet: fish, dog, cat, rabbit, horse

Clues:
1. The chess enthusiast lives in house 4.
2. The doctor's hobby is cooking.
3. The painting enthusiast lives immediately to the left of the hiking enthusiast.
4. The Brit and the Spaniard are next-door neighbours.
5. The rabbit owner is the farmer.
6. The pilot lives immediately to the right of the baker.
7. The farmer and the Norwegian have exactly one house between them.
8. The baker lives somewhere to the left of the horse owner.
9. The hiking enthusiast keeps the dog.
10. The fish owner lives immediately to the left of the baker.
11. The lawyer lives immediately to the left of the German.
12. The Spaniard does not own the fish.

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

## Puzzle plain:zebra-00093

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, lawyer, baker, teacher, farmer
- nationality: Spaniard, Brit, German, Swede, Norwegian
- color: white, blue, yellow, purple, green
- drink: coffee, water, tea, cocoa, milk

Clues:
1. The Swede lives in a lower-numbered house than the Norwegian.
2. The water drinker is the Norwegian.
3. The person in the green house lives next to the teacher.
4. The German lives next to the Swede.
5. The Swede either works as the doctor or works as the farmer.
6. There is exactly one house between the person who drinks coffee and whoever lives in the yellow house.
7. Whoever lives in the yellow house works as the doctor.
8. The baker lives next to the person in the blue house.
9. The baker and the milk drinker are neighbours.
10. There is exactly one house between the Spaniard and the Swede.
11. The person in the purple house works as the baker.
12. There is exactly one house between the baker and the tea drinker.
13. There is exactly one house between whoever lives in the purple house and the Spaniard.

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

## Puzzle hard:zebra_hard-00081

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, milk, tea, juice, water
- nationality: Swede, Dane, Brit, Norwegian, Spaniard
- hobby: painting, tennis, hiking, cooking, chess
- job: teacher, lawyer, doctor, pilot, farmer

Clues:
1. The person who drinks coffee lives further to the right than the Norwegian.
2. The tea drinker does not live to the right of the juice drinker.
3. The left-hand neighbour of the person who drinks water enjoys painting.
4. Neither the person who enjoys chess nor the doctor is the Dane.
5. Exactly one house separates the farmer from the lawyer.
6. The Spaniard and the person who enjoys tennis are one and the same person.
7. The person who enjoys chess lives in the third house from the right.
8. The farmer and the Norwegian are one and the same person.
9. The person who enjoys cooking lives in the fourth house from the right.
10. Exactly one house separates the person who enjoys chess from the Dane.
11. One of the neighbours of the farmer drinks juice.
12. The Swede lives two doors away from the teacher.
13. Exactly one house separates the chess enthusiast from the person who drinks milk.
14. If the Swede does not drink coffee, then that person drinks milk.

## Puzzle plain:zebra-00027

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, painting, chess, tennis, cooking
- nationality: Dane, German, Spaniard, Norwegian, Brit
- color: green, purple, white, yellow, red
- drink: tea, milk, water, cocoa, coffee

Clues:
1. The coffee drinker and the person in the red house are neighbours.
2. The chess enthusiast lives somewhere to the right of whoever lives in the white house.
3. The occupant of the red house lives in the house just left of the one where the cocoa drinker lives.
4. The person who drinks water lives immediately to the right of the person who enjoys hiking.
5. The person in the purple house lives in the fourth house.
6. The person who enjoys painting is the Spaniard.
7. The Dane lives in the leftmost house.
8. Whoever lives in the purple house and the tea drinker are not neighbours.
9. The Brit lives in the house just left of the one where the Spaniard lives.
10. The person who enjoys tennis lives in the house just left of the one where the occupant of the purple house lives.
11. The person who enjoys hiking lives in the house just left of the one where the Norwegian lives.
12. The tennis enthusiast lives next to the occupant of the yellow house.
