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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encA/e1_encA_005.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle plain:zebra-00041

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, cat, bird, fish, dog
- color: purple, white, red, blue, green
- hobby: chess, painting, tennis, golf, hiking
- drink: water, tea, coffee, cocoa, juice

Clues:
1. The chess enthusiast lives in the first house.
2. The owner of the cat lives in a lower-numbered house than the person who enjoys hiking.
3. The occupant of the red house lives immediately to the right of the golf enthusiast.
4. The bird owner and the owner of the horse live two houses apart.
5. The person who drinks coffee lives in the white house.
6. The water drinker lives in the house just left of the one where the person in the green house lives.
7. The occupant of the blue house drinks water.
8. The cocoa drinker lives immediately to the right of the juice drinker.
9. The person who enjoys hiking lives in the house just left of the one where the owner of the horse lives.
10. Whoever lives in the white house lives somewhere to the left of the hiking enthusiast.
11. The owner of the dog lives in house 5.
12. The person who enjoys tennis lives in the fourth house.

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

## Puzzle hard:zebra_hard-00019

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, hiking, cooking, chess
- drink: coffee, milk, juice, water, cocoa
- pet: fish, bird, horse, rabbit, dog
- job: doctor, baker, pilot, teacher, lawyer

Clues:
1. The person who enjoys painting lives somewhere between the person who enjoys chess and the milk drinker.
2. The person who drinks coffee lives somewhere between the baker and the fish owner.
3. The water drinker lives further to the right than the baker.
4. The doctor lives somewhere between the person who keeps the bird and the chess enthusiast.
5. Exactly one house separates the doctor from the person who drinks milk.
6. The bird owner does not live in the fifth house from the right.
7. If the teacher does not enjoy cooking, then that person enjoys painting.
8. One of the neighbours of the painting enthusiast works as the baker.
9. The cocoa drinker and the lawyer are one and the same person.
10. The lawyer and the rabbit owner are one and the same person.
11. If the person who keeps the bird does not enjoy hiking, then that person enjoys painting.
12. The cooking enthusiast lives two doors away from the person who enjoys tennis.
13. The lawyer lives further to the right than the person who drinks coffee.
14. At least one house separates the person who drinks water from the person who enjoys hiking.
15. Neither the painting enthusiast nor the water drinker works as the teacher.
16. If the horse owner does not drink coffee, then that person drinks water.

## Puzzle plain:zebra-00005

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

## Puzzle plain:zebra-00030

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Dane, Brit, Spaniard, Swede
- color: red, yellow, purple, green, white
- pet: bird, cat, dog, rabbit, fish
- drink: juice, water, tea, milk, coffee

Clues:
1. The water drinker lives directly to the left of the person in the green house.
2. The Norwegian drinks tea.
3. The rabbit owner drinks coffee.
4. The Spaniard and the occupant of the yellow house are neighbours.
5. The tea drinker lives directly to the left of the juice drinker.
6. The Swede and the occupant of the white house live in adjacent houses.
7. The occupant of the green house lives directly to the left of the Brit.
8. The Norwegian does not live next to the rabbit owner.
9. The owner of the cat and whoever lives in the white house live two houses apart.
10. The Norwegian keeps the dog.
11. The Dane keeps the fish.
12. The person who drinks juice lives immediately to the right of the person in the white house.
13. The occupant of the red house drinks water.

## Puzzle plain:zebra-00096

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Norwegian, Brit, Dane, Spaniard
- pet: fish, bird, cat, dog, rabbit
- drink: juice, tea, cocoa, water, coffee
- color: green, purple, white, yellow, blue

Clues:
1. The person who drinks cocoa lives next to the person who keeps the fish.
2. The person in the blue house and the owner of the cat live two houses apart.
3. The owner of the bird lives directly to the left of the person in the blue house.
4. The Swede does not live in the white house.
5. The person in the blue house and the Spaniard are neighbours.
6. The Norwegian lives in a lower-numbered house than the owner of the cat.
7. The rabbit owner lives next to the person who drinks tea.
8. The cocoa drinker and the juice drinker live in adjacent houses.
9. The bird owner and whoever lives in the green house are different people.
10. The person in the green house lives next to the Norwegian.
11. The person who keeps the fish does not live next to whoever lives in the yellow house.
12. The coffee drinker lives at one end of the row.
13. The rabbit owner lives in the last house.
14. The tea drinker lives in the house just left of the one where the occupant of the white house lives.
15. The cat owner either is the Dane or is the Spaniard.
16. The bird owner lives somewhere to the left of the person in the yellow house.
17. The cocoa drinker lives somewhere to the left of the Swede.

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
