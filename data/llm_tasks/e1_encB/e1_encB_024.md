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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encB/e1_encB_024.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00062

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, German, Brit, Norwegian, Dane
- color: white, blue, purple, red, yellow
- drink: juice, water, coffee, cocoa, tea
- hobby: cooking, golf, painting, hiking, tennis

Clues:
1. The coffee drinker lives somewhere between the cooking enthusiast and the person who enjoys tennis.
2. Whoever lives in the blue house lives somewhere between the German and the Spaniard.
3. Neither the Dane nor the person who enjoys golf lives in the red house.
4. Exactly one house separates the person who enjoys painting from the occupant of the yellow house.
5. If the person who drinks juice does not enjoy painting, then that person enjoys tennis.
6. The left-hand neighbour of the Norwegian enjoys cooking.
7. The person who enjoys cooking lives further to the right than the German.
8. The occupant of the red house and the tea drinker are one and the same person.
9. The juice drinker lives somewhere between the cocoa drinker and whoever lives in the white house.
10. The occupant of the white house lives somewhere between the person in the blue house and the German.
11. The occupant of the blue house does not live to the right of the person in the red house.
12. The right-hand neighbour of the Dane drinks cocoa.

## Puzzle plain:zebra-00026

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, cocoa, milk, tea, juice
- nationality: Dane, Swede, Spaniard, Brit, German
- color: blue, red, purple, yellow, white
- job: teacher, lawyer, doctor, pilot, farmer

Clues:
1. The German either drinks milk or drinks tea.
2. The occupant of the red house lives next to the Spaniard.
3. The farmer drinks juice.
4. The person who drinks cocoa lives in a lower-numbered house than the Spaniard.
5. The teacher lives immediately to the right of the Dane.
6. Whoever lives in the blue house lives directly to the left of whoever lives in the yellow house.
7. The person in the purple house lives in the house just left of the one where the Dane lives.
8. There is exactly one house between the Dane and the doctor.
9. The Spaniard lives next to the teacher.
10. The Swede lives in the leftmost house.
11. The teacher drinks milk.
12. The milk drinker lives next to the pilot.
13. There is exactly one house between the occupant of the blue house and the lawyer.
14. The German lives in the last house.

## Puzzle hard:zebra_hard-00093

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, cat, dog, horse, bird
- nationality: Brit, Norwegian, Swede, German, Spaniard
- hobby: painting, tennis, cooking, hiking, chess
- job: farmer, teacher, lawyer, pilot, doctor

Clues:
1. The right-hand neighbour of the Norwegian works as the lawyer.
2. Exactly 0 houses lie to the left of the home of the doctor.
3. Exactly 2 houses lie to the left of the home of the German.
4. The teacher has only one neighbour.
5. Exactly one house separates the owner of the dog from the Swede.
6. The cooking enthusiast and the Norwegian are one and the same person.
7. If the pilot does not enjoy hiking, then that person enjoys painting.
8. Exactly one house separates the doctor from the person who keeps the horse.
9. If the person who keeps the bird is not the Brit, then that person is the German.
10. The person who enjoys cooking lives in the fourth house from the right.
11. The painting enthusiast lives two doors away from the Spaniard.
12. The person who keeps the cat lives two doors away from the German.
13. The bird owner lives further to the right than the chess enthusiast.

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

## Puzzle paraphrase:zebra-00116

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, red, green, white, yellow
- nationality: Brit, Spaniard, Dane, Swede, German
- hobby: golf, tennis, chess, cooking, hiking
- job: baker, lawyer, pilot, doctor, teacher

Clues:
1. The golf enthusiast is either the Brit or the Spaniard.
2. The doctor lives next door to the golf enthusiast.
3. The cooking enthusiast lives right beside the purple house.
4. The Swede lives somewhere to the right of the tennis enthusiast.
5. The Swede is the teacher.
6. The white house and the yellow house are two houses apart.
7. The baker and the pilot are next-door neighbours.
8. The lawyer and the yellow house's occupant live in adjacent houses.
9. The chess enthusiast lives in the red house.
10. The Brit is the lawyer.
11. The Dane does not live in the fourth house.
12. The purple house is directly to the left of the pilot.
13. The German lives in the purple house.
14. The hiking enthusiast lives immediately to the right of the red house.

## Puzzle plain:zebra-00073

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, juice, water, milk, tea
- nationality: Norwegian, Swede, Dane, Spaniard, Brit
- hobby: tennis, cooking, painting, chess, hiking
- job: teacher, lawyer, baker, doctor, farmer

Clues:
1. The Norwegian and the Spaniard live two houses apart.
2. The doctor and the Swede live in adjacent houses.
3. The cooking enthusiast lives next to the person who drinks tea.
4. There is exactly one house between the Dane and the person who drinks water.
5. The baker and the hiking enthusiast live two houses apart.
6. The Brit works as the baker.
7. The person who enjoys tennis lives directly to the left of the juice drinker.
8. The Swede and the teacher live two houses apart.
9. The farmer lives in house 4.
10. The Brit lives directly to the left of the Spaniard.
11. The milk drinker enjoys painting.
12. The person who enjoys painting lives in house 5.

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

## Puzzle hard:zebra_hard-00078

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, green, red, purple, yellow
- pet: fish, dog, bird, horse, rabbit
- nationality: Norwegian, Dane, German, Brit, Swede
- job: teacher, farmer, baker, doctor, lawyer

Clues:
1. The right-hand neighbour of the person who keeps the dog is the German.
2. Exactly 1 house lies to the left of the home of the occupant of the red house.
3. Neither the person who keeps the rabbit nor the occupant of the white house works as the teacher.
4. One of the neighbours of the occupant of the yellow house keeps the bird.
5. The person who keeps the bird and whoever lives in the white house are one and the same person.
6. Exactly one house separates the doctor from the person in the white house.
7. If the Brit is not the doctor, then that person works as the lawyer.
8. The Swede lives further to the right than the fish owner.
9. One of the neighbours of the farmer keeps the fish.
10. The Dane lives somewhere between the German and whoever lives in the green house.
11. The baker and the person who keeps the rabbit are one and the same person.
12. The German and whoever lives in the red house are one and the same person.
13. One of the neighbours of the German keeps the rabbit.
