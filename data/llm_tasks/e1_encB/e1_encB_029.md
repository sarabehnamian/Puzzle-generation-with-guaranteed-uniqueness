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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_029.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00092

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, purple, blue, green
- pet: horse, fish, dog, bird, rabbit
- nationality: Dane, German, Swede, Norwegian, Spaniard
- drink: cocoa, juice, milk, tea, water

Clues:
1. The person who keeps the horse lives in the second house.
2. The German lives directly to the left of the person who drinks cocoa.
3. The person who drinks tea lives directly to the left of the person who drinks cocoa.
4. The milk drinker lives in one of the two end houses.
5. The Dane keeps the rabbit.
6. Whoever lives in the purple house drinks juice.
7. The fish owner and the tea drinker are neighbours.
8. The Dane lives immediately to the right of the owner of the dog.
9. The person in the green house and the water drinker live two houses apart.
10. The Spaniard lives immediately to the right of the tea drinker.
11. The bird owner does not live next to the Swede.
12. The person in the red house and the water drinker live in adjacent houses.
13. The Dane lives in the last house.
14. The person in the white house lives directly to the left of the person who drinks juice.
15. The owner of the fish lives in the leftmost house.

## Puzzle hard:zebra_hard-00057

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Swede, German, Norwegian, Spaniard
- pet: fish, dog, cat, horse, bird
- job: farmer, lawyer, baker, doctor, teacher
- drink: coffee, milk, juice, water, tea

Clues:
1. The tea drinker lives in the fourth house from the right.
2. The owner of the fish lives in the fifth house from the right.
3. The right-hand neighbour of the owner of the horse drinks water.
4. The baker and the Swede are one and the same person.
5. The left-hand neighbour of the person who drinks coffee works as the lawyer.
6. One of the neighbours of the owner of the cat works as the lawyer.
7. The left-hand neighbour of the milk drinker is the Brit.
8. The Norwegian lives in the rightmost house.
9. The baker does not live to the right of the doctor.
10. Exactly 1 house lies to the left of the home of the person who keeps the dog.
11. The Spaniard is not the same person as the tea drinker.
12. The left-hand neighbour of the person who keeps the horse works as the doctor.
13. If the water drinker is not the baker, then that person works as the teacher.

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

## Puzzle plain:zebra-00047

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Brit, Dane, Spaniard, Swede
- drink: tea, cocoa, juice, water, coffee
- pet: cat, rabbit, fish, horse, dog
- color: red, green, blue, white, yellow

Clues:
1. Whoever lives in the blue house lives in a lower-numbered house than the owner of the rabbit.
2. The Norwegian lives in the house just left of the one where the fish owner lives.
3. The Spaniard does not live next to whoever lives in the white house.
4. The person in the white house lives in house 3.
5. The owner of the dog either is the Dane or is the Swede.
6. The person in the blue house lives in the leftmost house.
7. The person who drinks tea does not live in house 5.
8. The Brit keeps the fish.
9. The person who drinks juice and the occupant of the red house live two houses apart.
10. The person who drinks coffee lives in the house just left of the one where the cat owner lives.
11. The horse owner lives in the white house.
12. The person who drinks tea lives in the yellow house.
13. The cocoa drinker keeps the cat.
14. The Dane either lives in the green house or lives in the red house.
15. The fish owner and whoever lives in the red house live in adjacent houses.

## Puzzle hard:zebra_hard-00008

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, baker, teacher, doctor, pilot
- pet: bird, fish, horse, cat, rabbit
- drink: cocoa, coffee, juice, tea, water
- color: red, yellow, purple, white, blue

Clues:
1. At least one house separates the teacher from the fish owner.
2. The person who drinks cocoa lives further to the right than the rabbit owner.
3. The doctor and the juice drinker are one and the same person.
4. The pilot lives somewhere between the owner of the rabbit and the occupant of the white house.
5. The water drinker lives further to the right than the pilot.
6. If the person in the purple house does not keep the fish, then that person keeps the horse.
7. One of the neighbours of the bird owner lives in the red house.
8. The right-hand neighbour of the person who keeps the horse drinks tea.
9. One of the neighbours of the fish owner lives in the red house.
10. Whoever lives in the white house does not live to the right of the occupant of the blue house.
11. The right-hand neighbour of the fish owner drinks cocoa.
12. The baker and whoever lives in the white house are one and the same person.
13. The person in the white house lives two doors away from the person in the yellow house.

## Puzzle plain:zebra-00063

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, yellow, purple, blue, green
- hobby: cooking, tennis, golf, hiking, painting
- pet: bird, cat, fish, rabbit, horse
- job: baker, doctor, teacher, pilot, farmer

Clues:
1. The doctor enjoys hiking.
2. The owner of the rabbit lives somewhere to the left of whoever lives in the purple house.
3. The person who enjoys cooking lives next to the person who keeps the horse.
4. The cat owner lives directly to the left of the baker.
5. Whoever lives in the blue house lives immediately to the right of the tennis enthusiast.
6. The person who enjoys painting lives directly to the left of whoever lives in the green house.
7. The cooking enthusiast and the teacher live in adjacent houses.
8. Whoever lives in the red house lives directly to the left of the pilot.
9. The hiking enthusiast and whoever lives in the purple house live in adjacent houses.
10. The person who enjoys hiking lives in the third house.
11. The teacher either lives in the green house or lives in the red house.
12. The occupant of the blue house does not live next to the teacher.
13. The person who keeps the bird lives in house 1.

## Puzzle hard:zebra_hard-00022

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, coffee, juice, cocoa, water
- pet: fish, horse, cat, bird, dog
- nationality: Brit, Dane, Swede, Norwegian, Spaniard
- hobby: golf, tennis, painting, hiking, cooking

Clues:
1. One of the neighbours of the fish owner drinks water.
2. The person who drinks cocoa lives two doors away from the milk drinker.
3. None of the neighbours of the Spaniard enjoys tennis.
4. The right-hand neighbour of the tennis enthusiast is the Swede.
5. The fish owner lives further to the right than the cooking enthusiast.
6. Exactly one house separates the cat owner from the painting enthusiast.
7. Neither the person who drinks coffee nor the person who enjoys hiking keeps the fish.
8. The horse owner and the water drinker are one and the same person.
9. The left-hand neighbour of the Dane drinks milk.
10. Exactly 1 house lies to the left of the home of the bird owner.
11. If the tennis enthusiast is not the Dane, then that person is the Swede.
12. The juice drinker does not live in the third house from the right.
13. The right-hand neighbour of the person who keeps the fish is the Brit.
14. Exactly one house separates the golf enthusiast from the hiking enthusiast.

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
