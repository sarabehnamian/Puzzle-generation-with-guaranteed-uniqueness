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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_000.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00077

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, hiking, painting, chess, golf
- nationality: Dane, Brit, Swede, Spaniard, Norwegian
- drink: tea, juice, coffee, milk, water
- pet: bird, fish, dog, cat, rabbit

Clues:
1. The Norwegian and the Spaniard are neighbours.
2. The juice drinker lives in a lower-numbered house than the Brit.
3. The Spaniard lives directly to the left of the tea drinker.
4. The painting enthusiast lives immediately to the right of the owner of the rabbit.
5. The person who drinks milk lives next to the tennis enthusiast.
6. The person who keeps the bird and the owner of the rabbit live in adjacent houses.
7. The person who enjoys golf lives next to the hiking enthusiast.
8. The milk drinker either is the Spaniard or is the Swede.
9. The Spaniard enjoys golf.
10. The Dane lives next to the person who drinks milk.
11. The Dane lives in the house just left of the one where the Brit lives.
12. There is exactly one house between the owner of the cat and the hiking enthusiast.
13. The Spaniard either keeps the cat or keeps the fish.
14. The Norwegian drinks coffee.

## Puzzle hard:zebra_hard-00017

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, bird, cat, horse, fish
- drink: water, milk, coffee, juice, cocoa
- hobby: hiking, chess, painting, golf, tennis
- color: blue, yellow, green, white, purple

Clues:
1. The person who drinks coffee lives further to the right than the person who enjoys chess.
2. The occupant of the purple house does not live in the fifth house from the right.
3. One of the neighbours of the person in the blue house enjoys hiking.
4. At least one house separates the painting enthusiast from the person who drinks milk.
5. Exactly 3 houses lie to the left of the home of the occupant of the blue house.
6. The owner of the cat and the person who enjoys tennis are one and the same person.
7. The person who drinks juice and whoever lives in the white house are one and the same person.
8. One of the neighbours of the golf enthusiast keeps the horse.
9. If the occupant of the white house does not enjoy golf, then that person enjoys hiking.
10. None of the neighbours of the person who keeps the horse lives in the purple house.
11. One of the neighbours of the person who enjoys tennis drinks water.
12. The coffee drinker and the person in the green house are one and the same person.
13. If the owner of the horse does not drink cocoa, then that person drinks coffee.
14. The person who keeps the bird and the chess enthusiast are one and the same person.
15. Exactly one house separates the golf enthusiast from the person who drinks water.
16. If the person who enjoys tennis does not live in the blue house, then that person lives in the yellow house.
17. If the cocoa drinker does not keep the cat, then that person keeps the dog.

## Puzzle paraphrase:zebra-00119

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, pilot, baker, farmer
- color: green, white, blue, red, yellow
- hobby: cooking, tennis, chess, hiking, painting
- pet: horse, dog, cat, bird, rabbit

Clues:
1. The white house's occupant lives somewhere to the left of the bird owner.
2. The yellow house's occupant lives in house 5.
3. The tennis enthusiast is the lawyer.
4. The rabbit keeper lives in the leftmost house.
5. The cooking enthusiast and the lawyer live two houses apart.
6. The blue house's occupant enjoys chess.
7. Exactly one house lies between the horse owner and the red house's occupant.
8. The blue house's occupant is not the doctor.
9. The cooking enthusiast and the white house's occupant live two houses apart.
10. The horse owner enjoys hiking.
11. The baker lives in house 2.
12. The pilot's hobby is either painting or tennis.
13. The chess enthusiast and the white house's occupant are not neighbours.
14. The dog owner is the pilot.

## Puzzle plain:zebra-00018

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: pilot, doctor, teacher, lawyer, farmer
- nationality: Dane, Brit, Norwegian, German, Swede
- drink: juice, water, tea, coffee, cocoa
- hobby: golf, tennis, painting, chess, cooking

Clues:
1. The person who drinks water lives in one of the two end houses.
2. The golf enthusiast and the juice drinker are not neighbours.
3. The Brit and the Dane are not neighbours.
4. The coffee drinker and the cooking enthusiast live two houses apart.
5. The person who enjoys cooking works as the doctor.
6. The Norwegian lives somewhere to the right of the person who drinks cocoa.
7. The teacher is the Norwegian.
8. The person who drinks juice lives next to the Norwegian.
9. The teacher lives at one end of the row.
10. The person who enjoys painting lives directly to the left of the Swede.
11. The person who drinks tea works as the lawyer.
12. The Brit and the painting enthusiast live two houses apart.
13. The person who enjoys tennis lives in the house just left of the one where the Dane lives.
14. The farmer does not live in house 3.
15. There is exactly one house between the person who drinks juice and the pilot.

## Puzzle hard:zebra_hard-00080

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, cat, rabbit, horse, dog
- nationality: Brit, German, Swede, Norwegian, Dane
- drink: tea, coffee, juice, water, milk
- hobby: cooking, painting, chess, tennis, hiking

Clues:
1. If the person who drinks water does not keep the dog, then that person keeps the horse.
2. One of the neighbours of the person who drinks juice keeps the dog.
3. If the Swede does not enjoy cooking, then that person enjoys painting.
4. The right-hand neighbour of the Norwegian keeps the dog.
5. If the German does not drink milk, then that person drinks water.
6. The Brit lives two doors away from the rabbit owner.
7. The person who enjoys hiking has only one neighbour.
8. One of the neighbours of the owner of the horse enjoys tennis.
9. The tea drinker lives in the fourth house from the right.
10. One of the neighbours of the person who enjoys cooking drinks milk.
11. Exactly 0 houses lie to the left of the home of the person who drinks milk.
12. The left-hand neighbour of the owner of the cat is the Swede.
13. Exactly 4 houses lie to the left of the home of the Brit.
14. Exactly 4 houses lie to the left of the home of the owner of the dog.

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

## Puzzle paraphrase:zebra-00163

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, lawyer, teacher, baker, farmer
- pet: bird, horse, dog, rabbit, fish
- hobby: painting, hiking, golf, tennis, chess
- drink: cocoa, water, tea, juice, coffee

Clues:
1. The chess player lives somewhere to the left of the golfer.
2. The golfer does not live next to the water drinker.
3. The doctor's hobby is hiking.
4. The cocoa drinker enjoys chess.
5. The rabbit owner lives in house 5.
6. The horse owner lives at one end of the row.
7. The chess player does not keep the fish.
8. The chess player lives next to the farmer.
9. The hiker and the horse owner live two houses apart.
10. The juice drinker lives directly to the left of the lawyer.
11. The baker and the doctor are not neighbours.
12. The water drinker lives at one end of the row.
13. The dog owner lives in the middle house.
14. The horse owner lives immediately to the left of the chess player.
15. The tennis enthusiast is the baker.
16. The coffee drinker and the doctor live two houses apart.
