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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_024.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00065

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, baker, doctor, farmer, pilot
- pet: cat, bird, horse, fish, dog
- drink: juice, tea, water, milk, cocoa
- color: green, white, purple, blue, yellow

Clues:
1. There is exactly one house between the doctor and the person who drinks tea.
2. The owner of the cat lives directly to the left of the water drinker.
3. The baker lives in a lower-numbered house than the person who keeps the fish.
4. The dog owner lives in house 5.
5. The person who keeps the fish works as the farmer.
6. There is exactly one house between the owner of the dog and the occupant of the green house.
7. The owner of the fish and the person who drinks tea live in adjacent houses.
8. The baker lives next to the owner of the horse.
9. Whoever lives in the white house lives in the first house.
10. The pilot lives in the house just left of the one where the person in the purple house lives.
11. The person who keeps the cat lives in house 1.
12. The occupant of the yellow house is not the pilot.
13. The juice drinker lives directly to the left of the person in the blue house.
14. The person who keeps the cat lives next to the doctor.
15. The person who drinks cocoa lives somewhere to the left of the milk drinker.

## Puzzle paraphrase:zebra-00132

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, baker, teacher, lawyer, pilot
- pet: fish, horse, dog, cat, rabbit
- drink: milk, tea, coffee, water, cocoa
- hobby: chess, golf, hiking, tennis, cooking

Clues:
1. The cooking enthusiast lives next door to the dog owner.
2. The baker's hobby is hiking.
3. The dog owner lives in the fifth house.
4. The milk drinker and the rabbit owner are two houses apart.
5. Exactly one house lies between the hiking enthusiast and the horse owner.
6. The milk drinker lives right next to the tennis enthusiast.
7. The baker and the tea drinker are next-door neighbours.
8. The chess player and the rabbit owner are two houses apart.
9. The cooking enthusiast and the teacher live next to each other.
10. One house stands between the coffee drinker and the tea drinker.
11. One house stands between the doctor and the water drinker.
12. The cat belongs to the lawyer.
13. The tea drinker lives somewhere to the left of the water drinker.
14. The baker lives in one of the two end houses.
15. The pilot and the teacher are not next-door neighbours.

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

## Puzzle hard:zebra_hard-00014

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, baker, farmer, teacher, pilot
- pet: cat, bird, horse, fish, dog
- drink: water, milk, juice, coffee, cocoa
- color: blue, green, purple, red, white

Clues:
1. If the occupant of the blue house is not the baker, then that person works as the teacher.
2. One of the neighbours of the person in the purple house lives in the green house.
3. The left-hand neighbour of whoever lives in the white house lives in the green house.
4. The cat owner does not live in the fourth house from the right.
5. If the person who keeps the cat does not drink cocoa, then that person drinks milk.
6. Exactly one house separates the person who drinks coffee from the teacher.
7. Exactly one house separates the farmer from the pilot.
8. One of the neighbours of the occupant of the purple house drinks cocoa.
9. Exactly one house separates the person who keeps the dog from the person who drinks milk.
10. The left-hand neighbour of the person who keeps the cat works as the teacher.
11. The farmer and the person in the purple house are one and the same person.
12. One of the neighbours of the bird owner lives in the white house.
13. The coffee drinker and the person who keeps the horse are one and the same person.
14. The pilot and the water drinker are one and the same person.

## Puzzle paraphrase:zebra-00171

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Dane, German, Spaniard, Swede
- color: blue, purple, white, green, yellow
- drink: coffee, cocoa, tea, water, milk
- job: baker, farmer, lawyer, doctor, pilot

Clues:
1. The Dane is the one who drinks tea.
2. The occupant of the blue house is either the Dane or the German.
3. The milk drinker is next door to the pilot.
4. The Dane and the Spaniard live in adjacent houses.
5. The Norwegian lives beside the occupant of the purple house.
6. The occupant of the yellow house is either the Dane or the Swede.
7. The doctor drinks either coffee or water.
8. The Swede occupies house 1.
9. The pilot is not the person in the green house.
10. The farmer's house has a lower number than the green house's.
11. The Norwegian and the water drinker are next-door neighbours.
12. The milk drinker lives in one of the two end houses.
13. The farmer lives further to the left than the occupant of the yellow house.
14. Cocoa is not what the person in the green house drinks.
15. The baker lives next to whoever is in the white house.
16. The doctor and the Spaniard live side by side.

## Puzzle hard:zebra_hard-00004

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: pilot, lawyer, baker, doctor, farmer
- nationality: Swede, German, Spaniard, Dane, Brit
- color: purple, yellow, red, white, green
- pet: cat, rabbit, dog, horse, bird

Clues:
1. Neither the German nor the Swede keeps the dog.
2. The baker lives two doors away from the doctor.
3. The person who keeps the rabbit lives two doors away from the Spaniard.
4. The lawyer and the person in the white house are one and the same person.
5. One of the neighbours of the farmer is the Brit.
6. The doctor lives somewhere between the person who keeps the horse and the Swede.
7. Whoever lives in the purple house and the rabbit owner are one and the same person.
8. The cat owner lives in the third house from the right.
9. One of the neighbours of the owner of the dog keeps the cat.
10. One of the neighbours of the person who keeps the rabbit lives in the red house.
11. If the horse owner does not live in the purple house, then that person lives in the yellow house.
12. One of the neighbours of the person in the purple house keeps the dog.
13. Neither whoever lives in the purple house nor whoever lives in the yellow house works as the baker.
14. The Dane and the person who keeps the horse are one and the same person.
15. The baker lives further to the right than the owner of the bird.

## Puzzle paraphrase:zebra-00182

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, cat, horse, dog, bird
- nationality: Swede, Brit, German, Spaniard, Norwegian
- hobby: tennis, golf, hiking, painting, cooking
- color: blue, green, yellow, white, red

Clues:
1. The tennis player lives immediately to the right of the green house.
2. The Brit occupies the leftmost house.
3. House 3 belongs to the cooking enthusiast.
4. The dog's house is immediately to the right of the white house.
5. The cat owner lives next door to the cooking enthusiast.
6. The bird belongs to the Spaniard.
7. The Swede is the one who owns the cat.
8. Hiking is the Spaniard's hobby.
9. One house lies between the blue house and the cooking enthusiast.
10. The tennis player lives in the fifth house.
11. The red house and the white house are not next to each other.
12. The horse owner lives immediately to the left of the Spaniard.
13. The Norwegian and the painting enthusiast live two houses apart.

## Puzzle plain:zebra-00014

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, juice, cocoa, water, milk
- job: pilot, teacher, doctor, farmer, baker
- pet: fish, horse, cat, rabbit, dog
- hobby: hiking, cooking, painting, chess, tennis

Clues:
1. There is exactly one house between the baker and the person who drinks milk.
2. The pilot lives at one end of the row.
3. The person who drinks coffee enjoys tennis.
4. The juice drinker either keeps the horse or keeps the rabbit.
5. The person who drinks water works as the pilot.
6. The owner of the cat works as the baker.
7. The person who keeps the rabbit enjoys hiking.
8. The person who enjoys chess lives in one of the two end houses.
9. The coffee drinker lives at one end of the row.
10. The teacher lives in the third house.
11. The doctor lives immediately to the right of the person who keeps the rabbit.
12. The person who enjoys cooking does not live in the fourth house.
13. The person who enjoys tennis lives directly to the left of the dog owner.

## Puzzle hard:zebra_hard-00000

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, baker, pilot, teacher, doctor
- color: white, red, blue, purple, yellow
- hobby: hiking, painting, chess, tennis, golf
- drink: juice, tea, milk, cocoa, water

Clues:
1. The person in the yellow house lives somewhere between whoever lives in the blue house and the water drinker.
2. Exactly one house separates the chess enthusiast from the golf enthusiast.
3. The cocoa drinker lives in the second house from the right.
4. The right-hand neighbour of the milk drinker works as the pilot.
5. One of the neighbours of whoever lives in the white house lives in the blue house.
6. The right-hand neighbour of the doctor lives in the blue house.
7. The teacher lives somewhere between the lawyer and the person who drinks milk.
8. If the chess enthusiast does not live in the blue house, then that person lives in the white house.
9. The left-hand neighbour of whoever lives in the red house works as the pilot.
10. The golf enthusiast lives further to the right than the person who drinks juice.
11. The right-hand neighbour of the tennis enthusiast enjoys hiking.
12. The person who enjoys golf and the pilot are one and the same person.

## Puzzle paraphrase:zebra-00146

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Brit, Dane, Spaniard, Norwegian
- job: teacher, baker, pilot, doctor, lawyer
- hobby: cooking, hiking, golf, chess, tennis
- drink: cocoa, coffee, tea, juice, water

Clues:
1. The Dane occupies the leftmost house.
2. The cooking enthusiast is either the Brit or the Dane.
3. Golf is the Dane's hobby.
4. The baker lives next to the chess enthusiast.
5. The hiking enthusiast lives in house 2.
6. The doctor is a coffee drinker.
7. The coffee drinker and the Spaniard live side by side.
8. The baker lives next door to the water drinker.
9. The coffee drinker and the tea drinker live two houses apart.
10. The Norwegian lives next door to the tennis enthusiast.
11. The hiking enthusiast and the lawyer have exactly one house between them.
12. The tennis enthusiast is the pilot.
13. The Norwegian drinks cocoa.
