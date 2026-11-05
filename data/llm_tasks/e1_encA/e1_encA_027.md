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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_027.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00136

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, cocoa, juice, coffee, tea
- job: lawyer, baker, pilot, farmer, doctor
- color: red, purple, white, yellow, green
- pet: fish, bird, dog, rabbit, horse

Clues:
1. The white house's occupant is not the baker.
2. The green house is right next to the red house.
3. The fish owner lives directly to the right of the cocoa drinker.
4. One house separates the dog owner from the purple house.
5. One house lies between the doctor and the pilot.
6. The coffee drinker lives in house 1.
7. The horse owner lives immediately to the left of the doctor.
8. The purple house is next door to the tea drinker.
9. The horse owner is the lawyer.
10. The green house lies somewhere to the right of the doctor.
11. The rabbit owner lives immediately to the left of the farmer.
12. The dog owner and the lawyer are not neighbours.
13. The green house is directly to the right of the cocoa drinker.
14. The doctor does not own the rabbit.
15. One house lies between the green house and the milk drinker.

## Puzzle hard:zebra_hard-00095

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, German, Brit, Dane, Spaniard
- color: white, purple, green, yellow, red
- pet: cat, dog, horse, bird, fish
- drink: tea, milk, coffee, cocoa, water

Clues:
1. None of the neighbours of the milk drinker keeps the cat.
2. The right-hand neighbour of the Spaniard drinks water.
3. The person who keeps the cat and the Spaniard are one and the same person.
4. The occupant of the green house and the milk drinker are one and the same person.
5. The person who keeps the horse and whoever lives in the yellow house are one and the same person.
6. The German has only one neighbour.
7. Exactly one house separates the person who keeps the bird from whoever lives in the green house.
8. The milk drinker lives somewhere between the Brit and the person who keeps the fish.
9. The left-hand neighbour of the cocoa drinker keeps the dog.
10. None of the neighbours of the tea drinker keeps the fish.
11. The left-hand neighbour of the Swede keeps the horse.
12. The person who drinks coffee lives two doors away from the person who keeps the dog.
13. One of the neighbours of the occupant of the white house is the Brit.
14. The left-hand neighbour of whoever lives in the purple house keeps the dog.

## Puzzle paraphrase:zebra-00159

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, cooking, golf, chess, hiking
- pet: cat, bird, horse, fish, dog
- drink: juice, milk, water, cocoa, coffee
- color: blue, green, white, purple, red

Clues:
1. The cocoa drinker and the golfer live two houses apart.
2. The milk drinker lives in house 5.
3. The purple house is house 2.
4. The painter drinks either coffee or water.
5. The red house is the third house.
6. The fish keeper and the water drinker live two houses apart.
7. The cat's owner lives in the third house.
8. The chess player keeps the fish.
9. The dog owner lives in the green house.
10. The cocoa drinker keeps the cat.
11. The fish owner and the white house's occupant live two houses apart.
12. The horse owner drinks either cocoa or juice.
13. The cocoa drinker lives in a lower-numbered house than the cooking enthusiast.

## Puzzle plain:zebra-00036

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Norwegian, Spaniard, Brit, German
- drink: milk, juice, cocoa, water, tea
- pet: dog, fish, bird, cat, horse
- hobby: chess, hiking, golf, painting, cooking

Clues:
1. The Brit and the chess enthusiast are different people.
2. The person who keeps the bird lives in the leftmost house.
3. The person who enjoys golf either is the Brit or is the German.
4. The painting enthusiast and the Spaniard live in adjacent houses.
5. The owner of the horse lives in the middle house.
6. The chess enthusiast lives somewhere to the left of the German.
7. The person who drinks milk lives in the second house.
8. The German lives in the third house.
9. The painting enthusiast drinks cocoa.
10. The Spaniard lives somewhere to the right of the fish owner.
11. The Brit and the person who enjoys hiking are not neighbours.
12. The owner of the horse either drinks cocoa or drinks water.
13. The person who enjoys hiking lives in one of the two end houses.
14. The cooking enthusiast lives immediately to the right of the person who drinks juice.
15. The Swede keeps the cat.

## Puzzle hard:zebra_hard-00058

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, doctor, pilot, lawyer, farmer
- pet: horse, cat, dog, fish, bird
- color: red, yellow, blue, white, green
- drink: tea, water, coffee, juice, milk

Clues:
1. The farmer lives somewhere between the fish owner and the tea drinker.
2. The lawyer and the occupant of the red house are one and the same person.
3. None of the neighbours of the person who keeps the bird keeps the horse.
4. The left-hand neighbour of the cat owner works as the pilot.
5. The right-hand neighbour of the teacher lives in the blue house.
6. The right-hand neighbour of whoever lives in the yellow house lives in the red house.
7. The dog owner lives two doors away from the farmer.
8. The water drinker lives somewhere between the lawyer and the person who drinks tea.
9. The person who keeps the bird lives further to the right than the farmer.
10. The occupant of the yellow house lives somewhere between the person in the red house and the person who drinks water.
11. The person who drinks juice lives two doors away from the lawyer.
12. The occupant of the green house lives two doors away from the occupant of the yellow house.
13. Exactly one house separates the person who keeps the cat from the coffee drinker.

## Puzzle plain:zebra-00034

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, chess, hiking, golf, cooking
- nationality: Swede, Brit, German, Spaniard, Dane
- job: lawyer, baker, pilot, teacher, farmer
- color: green, red, purple, yellow, blue

Clues:
1. The German lives in the house just left of the one where the golf enthusiast lives.
2. The farmer either enjoys golf or enjoys hiking.
3. Whoever lives in the blue house lives in the second house.
4. The Brit lives in the fourth house.
5. The baker lives in house 1.
6. The Dane works as the farmer.
7. The German lives in the house just left of the one where the Swede lives.
8. The person who enjoys chess and the person who enjoys hiking are neighbours.
9. There is exactly one house between the German and the occupant of the yellow house.
10. The pilot and the person in the red house live in adjacent houses.
11. The painting enthusiast either is the Brit or is the Spaniard.
12. The teacher lives in one of the two end houses.
13. The person in the green house lives directly to the left of the golf enthusiast.

## Puzzle paraphrase:zebra-00160

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, dog, cat, rabbit, horse
- job: lawyer, teacher, baker, doctor, farmer
- hobby: chess, cooking, tennis, golf, painting
- drink: juice, water, coffee, cocoa, milk

Clues:
1. Whoever enjoys tennis drinks juice.
2. The cat owner and the painting enthusiast live next door to each other.
3. The golfer doesn't drink milk.
4. The lawyer occupies the middle house.
5. The chess player lives immediately to the left of the painting enthusiast.
6. The bird keeper is the doctor.
7. The dog owner drinks milk.
8. The farmer does not live in house 2.
9. The golfer is the baker.
10. The farmer and the water drinker are next-door neighbours.
11. The rabbit owner lives in house 1.
12. The cocoa drinker's hobby is either painting or tennis.
13. The water drinker lives immediately to the left of the coffee drinker.

## Puzzle hard:zebra_hard-00035

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, juice, cocoa, water, coffee
- job: teacher, lawyer, baker, farmer, doctor
- nationality: Dane, Swede, Brit, German, Spaniard
- hobby: chess, golf, cooking, hiking, painting

Clues:
1. One of the neighbours of the painting enthusiast enjoys hiking.
2. If the lawyer does not drink cocoa, then that person drinks coffee.
3. Exactly 3 houses lie to the left of the home of the teacher.
4. The right-hand neighbour of the person who drinks cocoa is the Brit.
5. The Dane has only one neighbour.
6. If the German is not the doctor, then that person works as the farmer.
7. The right-hand neighbour of the doctor enjoys cooking.
8. The person who enjoys hiking has only one neighbour.
9. Exactly 1 house lies to the left of the home of the person who drinks water.
10. One of the neighbours of the Spaniard works as the teacher.
11. The chess enthusiast and the Spaniard are one and the same person.
12. The doctor lives somewhere between the Brit and the farmer.
13. The left-hand neighbour of the doctor drinks milk.
14. The Brit is not the same person as the juice drinker.

## Puzzle hard:zebra_hard-00012

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, hiking, painting, chess, tennis
- job: lawyer, doctor, baker, teacher, pilot
- color: blue, red, yellow, green, white
- pet: cat, dog, fish, rabbit, horse

Clues:
1. The person who keeps the horse is not the same person as the tennis enthusiast.
2. The left-hand neighbour of the fish owner keeps the rabbit.
3. If the doctor does not keep the dog, then that person keeps the horse.
4. If the occupant of the white house does not enjoy painting, then that person enjoys tennis.
5. The left-hand neighbour of the person who keeps the fish works as the teacher.
6. The occupant of the white house lives somewhere between the baker and the person who keeps the dog.
7. The left-hand neighbour of the person who enjoys chess keeps the cat.
8. If the occupant of the yellow house does not keep the fish, then that person keeps the rabbit.
9. At least one house separates the person who enjoys tennis from the person who keeps the fish.
10. The person who enjoys tennis does not live to the right of the person who enjoys painting.
11. One of the neighbours of the lawyer lives in the blue house.
12. The person in the green house and the teacher are one and the same person.
13. The person who keeps the fish and the person who enjoys golf are one and the same person.
14. The chess enthusiast has only one neighbour.

## Puzzle paraphrase:zebra-00152

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, juice, water, milk
- job: farmer, teacher, lawyer, doctor, baker
- hobby: cooking, tennis, golf, chess, hiking
- pet: bird, cat, horse, dog, fish

Clues:
1. The cooking enthusiast lives immediately to the right of the fish keeper.
2. The juice drinker's hobby is golf.
3. The tea drinker's hobby is either chess or cooking.
4. The bird keeper lives next door to the milk drinker.
5. The milk drinker keeps either the bird or the dog.
6. The juice drinker lives in one of the two end houses.
7. Exactly one house separates the farmer from the juice drinker.
8. The lawyer lives in a lower-numbered house than the dog's owner.
9. The baker drinks water.
10. The hiking enthusiast is either the baker or the teacher.
11. The baker and the hiking enthusiast live two houses apart.
12. The cat's keeper is the farmer.
13. The chess player lives in a lower-numbered house than the golfer.
14. The dog owner and the tennis player live next to each other.
