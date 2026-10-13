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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encB/e1_encB_028.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00176

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, farmer, teacher, doctor, lawyer
- nationality: Swede, Spaniard, Dane, Brit, German
- color: red, green, yellow, white, blue
- pet: bird, horse, rabbit, cat, dog

Clues:
1. The German lives somewhere to the right of the blue house's occupant.
2. The Swede lives in house 3.
3. The Dane lives in house 4.
4. The cat belongs to the occupant of the green house.
5. The bird belongs to either the German or the Spaniard.
6. The Brit is the farmer.
7. The teacher lives immediately to the right of the Brit.
8. The Dane is the doctor.
9. The horse is kept in the yellow house.
10. The white house's occupant keeps the rabbit.
11. The dog owner and the yellow house's occupant do not live next to each other.
12. The baker and the occupant of the blue house are two houses apart.
13. Two houses separate the baker from the teacher.
14. The bird owner is a neighbour of whoever is in the green house.
15. The yellow house lies somewhere to the right of the baker.

## Puzzle plain:zebra-00098

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, hiking, golf, chess, painting
- drink: tea, juice, coffee, water, milk
- pet: rabbit, bird, fish, cat, horse
- job: farmer, baker, doctor, teacher, pilot

Clues:
1. The owner of the fish and the teacher live in adjacent houses.
2. The pilot lives in the house just left of the one where the person who keeps the horse lives.
3. The owner of the horse and the water drinker are neighbours.
4. The chess enthusiast drinks water.
5. The person who drinks tea lives directly to the left of the owner of the fish.
6. The coffee drinker lives in one of the two end houses.
7. The owner of the cat and the farmer live two houses apart.
8. The farmer enjoys painting.
9. The person who keeps the bird lives next to the person who drinks milk.
10. The owner of the fish lives in house 3.
11. The doctor and the person who enjoys golf live in adjacent houses.
12. The person who enjoys cooking either works as the baker or works as the teacher.
13. The owner of the cat works as the baker.

## Puzzle paraphrase:zebra-00103

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, coffee, juice, water
- nationality: Spaniard, German, Brit, Swede, Norwegian
- hobby: hiking, golf, painting, cooking, chess
- color: red, purple, blue, green, white

Clues:
1. The coffee drinker's hobby is cooking.
2. The Brit lives in the purple house.
3. The cocoa drinker lives immediately to the right of the hiking enthusiast.
4. One house separates the blue house's occupant from the Norwegian.
5. Juice is drunk by whoever lives in house 2.
6. The cocoa drinker lives somewhere to the right of the Swede.
7. The German and the occupant of the purple house have exactly one house between them.
8. Immediately to the left of the Brit lives the painting enthusiast.
9. The white house's occupant enjoys hiking.
10. The Norwegian is not a tea drinker.
11. The blue house is house 3.
12. The red house's occupant enjoys golf.
13. The coffee drinker lives in the leftmost house.

## Puzzle hard:zebra_hard-00096

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, German, Swede, Spaniard, Norwegian
- job: baker, pilot, teacher, farmer, doctor
- pet: fish, horse, bird, cat, rabbit
- color: red, white, blue, yellow, purple

Clues:
1. The right-hand neighbour of the person who keeps the fish works as the doctor.
2. The left-hand neighbour of the German lives in the yellow house.
3. The occupant of the blue house and the German are one and the same person.
4. One of the neighbours of the Dane works as the teacher.
5. The occupant of the white house does not live in the fifth house from the right.
6. The person who keeps the horse and the Norwegian are one and the same person.
7. Exactly one house separates the occupant of the blue house from the rabbit owner.
8. Exactly one house separates the occupant of the purple house from whoever lives in the white house.
9. The right-hand neighbour of the horse owner is the German.
10. Exactly 0 houses lie to the left of the home of the Dane.
11. One of the neighbours of the person in the red house is the Swede.
12. The pilot lives somewhere between the person who keeps the bird and the German.
13. The rabbit owner lives further to the right than the farmer.

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

## Puzzle paraphrase:zebra-00197

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, bird, horse, dog, cat
- drink: tea, cocoa, juice, milk, coffee
- nationality: Swede, German, Norwegian, Brit, Spaniard
- color: blue, red, purple, yellow, green

Clues:
1. The bird owner lives in the house immediately to the right of the milk drinker's.
2. Exactly one house lies between the horse owner and the milk drinker.
3. The cocoa drinker is either the German or the Spaniard.
4. The German is the horse owner.
5. The Brit lives next door to the yellow house's resident.
6. The cat owner lives immediately to the right of the fish owner.
7. The coffee drinker lives next door to the red house's resident.
8. The yellow house's occupant drinks juice.
9. The tea drinker lives in house 3.
10. The fish owner lives in the purple house.
11. The tea drinker is either the Brit or the German.
12. The cat owner lives in the green house.
13. The fish owner and the Swede are two houses apart.

## Puzzle hard:zebra_hard-00056

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, milk, juice, cocoa, coffee
- nationality: Norwegian, Dane, Spaniard, Brit, German
- pet: dog, bird, fish, rabbit, cat
- job: baker, pilot, teacher, lawyer, farmer

Clues:
1. One of the neighbours of the dog owner is the Dane.
2. The Dane and the lawyer are one and the same person.
3. The Norwegian does not live to the right of the Dane.
4. The left-hand neighbour of the cat owner keeps the fish.
5. The left-hand neighbour of the person who drinks tea works as the baker.
6. The baker and the person who drinks juice are one and the same person.
7. The lawyer lives somewhere between the person who keeps the bird and the owner of the cat.
8. The person who drinks milk lives somewhere between the cocoa drinker and the owner of the fish.
9. The person who drinks juice and the Spaniard are one and the same person.
10. One of the neighbours of the milk drinker is the German.
11. One of the neighbours of the person who drinks cocoa keeps the rabbit.
12. The farmer lives further to the right than the person who drinks coffee.
13. Exactly 1 house lies to the left of the home of the milk drinker.
14. The person who keeps the cat and the teacher are one and the same person.

## Puzzle plain:zebra-00000

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, dog, bird, fish, rabbit
- job: farmer, teacher, baker, doctor, lawyer
- hobby: golf, tennis, chess, hiking, cooking
- nationality: Brit, German, Spaniard, Norwegian, Swede

Clues:
1. The Spaniard lives in the house just left of the one where the hiking enthusiast lives.
2. The German lives next to the teacher.
3. The baker keeps the rabbit.
4. The tennis enthusiast lives in house 4.
5. The Norwegian keeps the rabbit.
6. The person who keeps the bird and the person who enjoys golf are neighbours.
7. The cooking enthusiast and the German live two houses apart.
8. The lawyer lives directly to the left of the farmer.
9. The owner of the bird works as the teacher.
10. The cooking enthusiast and the person who keeps the dog are neighbours.
11. There is exactly one house between the farmer and the horse owner.
12. The Swede lives in the house just left of the one where the horse owner lives.

## Puzzle paraphrase:zebra-00127

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, milk, juice, coffee, tea
- color: blue, red, green, yellow, white
- nationality: Spaniard, Brit, Swede, Dane, German
- pet: fish, bird, horse, cat, rabbit

Clues:
1. The cocoa drinker and the Swede live next door to each other.
2. The cat owner does not live next door to the Swede.
3. The Spaniard is the rabbit keeper.
4. The Dane lives directly to the left of the fish owner.
5. The milk drinker lives immediately to the left of the fish owner.
6. The German and the green house's occupant live two houses apart.
7. The rabbit owner lives somewhere to the right of the fish owner.
8. The coffee drinker lives in either the blue house or the white house.
9. The German lives in house 4.
10. The juice drinker lives in the blue house.
11. The milk drinker lives in the yellow house.
12. The German is not next door to the horse owner.
13. The blue house stands directly to the left of the Spaniard.
14. The cat keeper lives next door to the Spaniard.

## Puzzle hard:zebra_hard-00031

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Swede, Spaniard, Norwegian, German
- color: yellow, white, green, blue, purple
- hobby: golf, chess, tennis, hiking, cooking
- drink: water, cocoa, tea, juice, milk

Clues:
1. The left-hand neighbour of the golf enthusiast drinks tea.
2. Exactly 2 houses lie to the left of the home of the Brit.
3. The occupant of the blue house and the hiking enthusiast are one and the same person.
4. At least one house separates the person who drinks juice from the German.
5. The person who enjoys chess and the person who drinks tea are one and the same person.
6. Exactly one house separates whoever lives in the purple house from the person who enjoys tennis.
7. The Spaniard lives somewhere between whoever lives in the green house and the person in the yellow house.
8. Exactly one house separates the Swede from the person in the yellow house.
9. The right-hand neighbour of the person in the purple house drinks cocoa.
10. One of the neighbours of the occupant of the white house enjoys cooking.
11. The person who drinks water lives somewhere between whoever lives in the blue house and the person who enjoys golf.
12. The juice drinker and the Norwegian are one and the same person.
