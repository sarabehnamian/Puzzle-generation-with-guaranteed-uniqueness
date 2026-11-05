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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_004.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00104

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, coffee, tea, water, milk
- nationality: Swede, Spaniard, Dane, Norwegian, German
- hobby: chess, painting, golf, tennis, cooking
- color: blue, red, yellow, white, purple

Clues:
1. The red house's occupant and the Spaniard live in adjacent houses.
2. The milk drinker and the white house's occupant live two houses apart.
3. The Norwegian lives directly to the right of the Spaniard.
4. The cooking enthusiast lives next door to the German.
5. The German lives immediately to the left of the coffee drinker.
6. The coffee drinker doesn't live next to the water drinker.
7. The coffee drinker and the golf enthusiast are not neighbours.
8. The Norwegian lives in house 5.
9. The milk drinker's hobby is either chess or cooking.
10. The Dane lives immediately to the left of the blue house's occupant.
11. The cocoa drinker lives in the leftmost house.
12. The yellow house's occupant enjoys painting.
13. The painting enthusiast lives directly to the left of the water drinker.
14. The red house's occupant drinks water.

## Puzzle hard:zebra_hard-00064

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, chess, golf, cooking, painting
- pet: bird, rabbit, dog, cat, fish
- color: blue, red, yellow, white, green
- job: lawyer, farmer, pilot, baker, teacher

Clues:
1. The bird owner and the pilot are one and the same person.
2. The right-hand neighbour of the painting enthusiast enjoys cooking.
3. If the person in the green house is not the lawyer, then that person works as the pilot.
4. The person who enjoys chess has only one neighbour.
5. Neither the owner of the bird nor the chess enthusiast lives in the blue house.
6. The right-hand neighbour of the person who enjoys cooking lives in the white house.
7. The occupant of the green house and the person who enjoys tennis are one and the same person.
8. Exactly 1 house lies to the left of the home of whoever lives in the yellow house.
9. The baker lives further to the right than the bird owner.
10. The owner of the fish lives further to the right than the farmer.
11. At least one house separates the cooking enthusiast from the owner of the cat.
12. The person who keeps the cat lives two doors away from the person who keeps the dog.
13. Exactly 1 house lies to the left of the home of the person who keeps the dog.
14. The person who enjoys painting and the teacher are one and the same person.
15. The golf enthusiast lives somewhere between whoever lives in the blue house and whoever lives in the red house.

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

## Puzzle paraphrase:zebra-00108

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, German, Spaniard, Dane, Swede
- hobby: hiking, chess, golf, painting, tennis
- job: farmer, teacher, pilot, doctor, lawyer
- pet: rabbit, horse, cat, bird, dog

Clues:
1. The rabbit owner lives in house 3.
2. One house lies between the golf enthusiast and the hiker.
3. The Spaniard lives immediately to the left of the dog owner.
4. The Swede lives in house 2.
5. One house separates the lawyer from the tennis enthusiast.
6. The Dane does not live next to the painting enthusiast.
7. The Dane and the teacher live in adjacent houses.
8. The golf enthusiast and the pilot live next door to each other.
9. The hiker is the lawyer.
10. The doctor lives in house 5.
11. The cat owner lives immediately to the left of the bird owner.
12. The Dane and the Norwegian are neighbours.
13. The horse owner lives in house 1.

## Puzzle plain:zebra-00080

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, blue, yellow, green
- hobby: tennis, chess, hiking, cooking, golf
- job: doctor, farmer, pilot, lawyer, teacher
- pet: bird, cat, horse, rabbit, dog

Clues:
1. The owner of the dog enjoys chess.
2. The teacher lives somewhere to the left of the owner of the bird.
3. The person in the blue house lives somewhere to the right of the farmer.
4. The person who keeps the rabbit lives directly to the left of the teacher.
5. The person who enjoys chess either lives in the red house or lives in the yellow house.
6. The person who enjoys hiking and the occupant of the yellow house are neighbours.
7. The lawyer enjoys tennis.
8. Whoever lives in the green house and the person who enjoys hiking live in adjacent houses.
9. The doctor and the rabbit owner live two houses apart.
10. The person who keeps the cat lives in the house just left of the one where the golf enthusiast lives.
11. The person in the red house lives next to whoever lives in the white house.
12. There is exactly one house between the occupant of the blue house and the rabbit owner.
13. The occupant of the green house and the golf enthusiast are different people.
14. The cat owner and the person who enjoys cooking are neighbours.

## Puzzle paraphrase:zebra-00171

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Dane, German, Spaniard, Swede
- color: blue, purple, white, green, yellow
- drink: coffee, cocoa, tea, water, milk
- job: baker, farmer, lawyer, doctor, pilot

Clues:
1. The Dane is the one who drinks tea.
2. The resident of the blue house is either the Dane or the German.
3. The milk drinker lives next door to the pilot.
4. The Dane and the Spaniard live in neighbouring houses.
5. The Norwegian lives next to the purple house.
6. The resident of the yellow house is either the Dane or the Swede.
7. The doctor drinks either coffee or water.
8. The Swede lives in house 1.
9. The pilot is not the person in the green house.
10. The farmer's house has a lower number than the green house.
11. The Norwegian lives right beside the water drinker.
12. The milk drinker lives in one of the two end houses.
13. The farmer lives somewhere to the left of the yellow house.
14. The green house's occupant does not drink cocoa.
15. The baker lives next door to the white house.
16. The doctor and the Spaniard are next-door neighbours.

## Puzzle paraphrase:zebra-00144

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, water, tea, juice, coffee
- pet: horse, fish, dog, rabbit, cat
- nationality: Spaniard, Dane, Norwegian, Swede, Brit
- color: green, purple, red, blue, yellow

Clues:
1. Water is drunk by the person in house 4.
2. The Dane is the water drinker.
3. The Spaniard lives in house 5.
4. The Brit and the yellow house's occupant are two houses apart.
5. The green house's occupant drinks water.
6. The rabbit owner and the tea drinker live two houses apart.
7. Juice is drunk in the yellow house.
8. The purple house and the water drinker are two houses apart.
9. The fish keeper lives in one of the two end houses.
10. One house separates the coffee drinker from the juice drinker.
11. The cat owner lives somewhere right of the fish keeper.
12. The blue house's occupant and the cat owner are not neighbours.
13. One end of the row is where the Norwegian lives.
14. The blue house's occupant keeps the horse.
15. The Spaniard is the person in the red house.

## Puzzle paraphrase:zebra-00189

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, farmer, teacher, doctor, baker
- hobby: painting, tennis, cooking, hiking, golf
- pet: horse, rabbit, fish, dog, bird
- nationality: German, Dane, Swede, Spaniard, Brit

Clues:
1. The rabbit owner and the tennis player live two houses apart.
2. The Spaniard is the painter.
3. The bird owner lives immediately to the left of the doctor.
4. The Dane lives next door to the farmer.
5. The Spaniard lives immediately to the right of the fish owner.
6. The golfer lives immediately to the left of the dog owner.
7. The lawyer lives in house 4.
8. The Swede and the teacher have exactly one house between them.
9. The German lives immediately to the left of the dog owner.
10. The Swede lives somewhere to the left of the Spaniard.
11. The painter does not live in house 5.
12. The Dane and the horse owner live two houses apart.
13. The cooking enthusiast is the farmer.

## Puzzle plain:zebra-00088

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, baker, pilot, farmer
- pet: horse, bird, cat, fish, dog
- hobby: hiking, painting, cooking, chess, golf
- color: green, blue, yellow, red, purple

Clues:
1. The baker lives somewhere to the right of the teacher.
2. The person who keeps the cat lives in the red house.
3. The person who keeps the dog lives in house 4.
4. The pilot lives in the middle house.
5. The person who enjoys chess and whoever lives in the red house live two houses apart.
6. There is exactly one house between the hiking enthusiast and the painting enthusiast.
7. Whoever lives in the blue house enjoys hiking.
8. The occupant of the red house works as the farmer.
9. The owner of the cat enjoys golf.
10. The doctor lives in the fourth house.
11. The occupant of the yellow house lives in house 1.
12. The pilot lives in the purple house.
13. The person who enjoys golf lives somewhere to the left of the person who keeps the fish.
14. The occupant of the purple house keeps the horse.

## Puzzle plain:zebra-00055

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, fish, rabbit, cat
- drink: cocoa, juice, tea, milk, water
- nationality: Brit, German, Norwegian, Dane, Swede
- hobby: tennis, hiking, cooking, chess, painting

Clues:
1. The Swede lives immediately to the right of the chess enthusiast.
2. The cat owner lives next to the Swede.
3. The horse owner drinks juice.
4. The Brit and the person who keeps the cat are neighbours.
5. The person who enjoys chess and the horse owner live in adjacent houses.
6. The Norwegian lives next to the Swede.
7. The painting enthusiast lives in the fourth house.
8. The owner of the horse does not live in the first house.
9. The person who enjoys hiking lives immediately to the right of the cocoa drinker.
10. The water drinker and the Dane are different people.
11. The person who keeps the dog and the person who enjoys hiking are neighbours.
12. The German keeps the cat.
13. The owner of the fish drinks water.
14. The Brit enjoys tennis.
15. The tea drinker either enjoys hiking or enjoys tennis.
