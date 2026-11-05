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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encC\e1_encC_024.out.json with this exact structure
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
3. The dog owner lives in house 5.
4. The milk drinker and the rabbit owner live two houses apart.
5. One house separates the hiking enthusiast from the horse owner.
6. The milk drinker lives next to the tennis enthusiast.
7. The baker and the tea drinker are neighbours.
8. The chess enthusiast and the rabbit owner live two houses apart.
9. The cooking enthusiast and the teacher live next to each other.
10. One house lies between the coffee drinker and the tea drinker.
11. One house lies between the doctor and the water drinker.
12. The lawyer keeps the cat.
13. The tea drinker lives somewhere to the left of the water drinker.
14. The baker lives at one of the two ends of the row.
15. The pilot and the teacher do not live next to each other.

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

## Puzzle paraphrase:zebra-00172

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, dog, fish, cat, bird
- job: lawyer, pilot, doctor, baker, teacher
- nationality: Swede, Norwegian, German, Brit, Dane
- color: blue, yellow, white, red, purple

Clues:
1. The yellow house's occupant is the doctor.
2. The German is not next door to the pilot.
3. The cat owner lives in either the blue house or the white house.
4. The red house and the yellow house are two houses apart.
5. The dog owner lives immediately to the left of the yellow house.
6. The bird owner lives somewhere to the left of the Dane.
7. Exactly one house lies between the lawyer and the white house.
8. The teacher lives immediately to the left of the fish owner.
9. One house separates the Brit from the pilot.
10. The lawyer and the Norwegian have exactly one house between them.
11. The Brit and the Dane are not neighbours.
12. The rabbit owner lives in house 2.
13. The Norwegian lives immediately to the left of the purple house.

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

## Puzzle paraphrase:zebra-00183

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, cooking, painting, golf, chess
- color: green, blue, white, red, yellow
- job: farmer, pilot, baker, teacher, lawyer
- pet: dog, rabbit, bird, horse, cat

Clues:
1. The dog owner is not the pilot.
2. The red house's occupant has either the bird or the rabbit.
3. The rabbit lives in the blue house.
4. The golfer is not the teacher.
5. The cooking enthusiast and the pilot live in neighbouring houses.
6. The green house is where the cat lives.
7. The golfer lives in either the red house or the white house.
8. The lawyer and the teacher have exactly one house between them.
9. The white house is somewhere to the left of the horse owner.
10. The bird owner lives somewhere to the right of the teacher.
11. The horse owner and the tennis player live two houses apart.
12. The yellow house is at one of the two ends of the row.
13. The red house is immediately to the left of the painting enthusiast.
14. The farmer and the painter live next door to each other.
15. One house separates the green house from the painter.
16. The teacher lives somewhere to the left of the cat owner.
17. The cooking enthusiast lives in one of the end houses.

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
1. The leftmost house is the Dane's.
2. The cooking enthusiast is either the Brit or the Dane.
3. Golf is the Dane's hobby.
4. The baker and the chess enthusiast live in adjacent houses.
5. The hiking enthusiast lives in the second house.
6. The doctor drinks coffee.
7. The coffee drinker and the Spaniard live next door to each other.
8. The baker lives next to the water drinker.
9. Two houses separate the coffee drinker from the tea drinker.
10. The Norwegian lives next to the tennis enthusiast.
11. One house lies between the hiking enthusiast and the lawyer.
12. The pilot is the tennis enthusiast.
13. Cocoa is the Norwegian's drink.
