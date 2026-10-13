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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encA/e1_encA_004.out.json with this exact structure
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
1. The red house's occupant and the Spaniard live in neighbouring houses.
2. The milk drinker and the occupant of the white house live two houses apart.
3. The Norwegian lives right next to the Spaniard, on the right.
4. The cooking enthusiast lives next door to the German.
5. The coffee drinker lives immediately to the right of the German.
6. The coffee drinker is not a neighbour of the water drinker.
7. The coffee drinker and the golf enthusiast do not live next door to each other.
8. The Norwegian lives in house 5.
9. The milk drinker's hobby is either chess or cooking.
10. The Dane lives immediately to the left of the blue house's occupant.
11. The cocoa drinker lives in the leftmost house.
12. The yellow house's occupant enjoys painting.
13. The painting enthusiast lives immediately to the left of the water drinker.
14. The occupant of the red house drinks water.

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
1. House 3 is where the rabbit owner lives.
2. The golf enthusiast and the hiking enthusiast have exactly one house between them.
3. The Spaniard lives immediately to the left of the dog owner.
4. The Swede's home is house 2.
5. The lawyer and the tennis enthusiast have exactly one house between them.
6. The Dane does not live next door to the painting enthusiast.
7. The Dane and the teacher live in neighbouring houses.
8. The golf enthusiast and the pilot are next-door neighbours.
9. The hiking enthusiast is the lawyer.
10. The doctor lives in house 5.
11. The cat owner lives immediately to the left of the bird owner.
12. The Dane and the Norwegian live next door to each other.
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

## Puzzle paraphrase:zebra-00170

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, green, white, yellow, red
- nationality: Norwegian, German, Dane, Swede, Brit
- drink: tea, milk, water, cocoa, coffee
- hobby: hiking, chess, painting, tennis, golf

Clues:
1. The hiking fan is either the German or the Swede.
2. Next door to the tea drinker lives the tennis enthusiast.
3. Between the Norwegian and the resident of the white house there are exactly two houses' worth of distance: they are two houses apart.
4. The person who enjoys painting lives immediately to the right of the person who enjoys hiking.
5. The tennis enthusiast and the water drinker have exactly one house between them.
6. One house separates the person who enjoys hiking from the person who enjoys tennis.
7. Somewhere to the right of the white house's occupant lives the Swede.
8. Whoever lives in the red house enjoys either golf or hiking.
9. The Dane's hobby is golf.
10. The Brit is the German's neighbour.
11. The milk drinker is not a neighbour of the person who drinks tea.
12. The coffee drinker's house is right beside the Dane's.
13. The Swede's neighbour is the person in the yellow house.
14. The person who enjoys chess lives immediately to the right of the green house's occupant.
15. The tennis enthusiast lives further along to the right than the Brit.
16. Further to the left than the cocoa drinker lives the coffee drinker.

## Puzzle paraphrase:zebra-00144

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, water, tea, juice, coffee
- pet: horse, fish, dog, rabbit, cat
- nationality: Spaniard, Dane, Norwegian, Swede, Brit
- color: green, purple, red, blue, yellow

Clues:
1. The water drinker lives in house 4.
2. The Dane is the one who drinks water.
3. The Spaniard lives in house 5.
4. Two houses separate the Brit from the yellow house's occupant.
5. Water is what the green house's occupant drinks.
6. The rabbit owner and the tea drinker live two houses apart.
7. The juice drinker lives in the yellow house.
8. The purple house and the water drinker's home are two houses apart.
9. The fish keeper lives in one of the two end houses.
10. Exactly one house sits between the coffee drinker and the juice drinker.
11. The cat owner lives somewhere to the right of the fish keeper.
12. The blue house's occupant and the cat owner do not live next to each other.
13. The Norwegian lives at one end of the row.
14. The horse belongs to the occupant of the blue house.
15. The Spaniard is the one in the red house.

## Puzzle paraphrase:zebra-00188

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, baker, teacher, pilot, lawyer
- drink: water, tea, coffee, milk, juice
- nationality: Spaniard, Brit, Swede, Norwegian, Dane
- hobby: tennis, hiking, chess, painting, cooking

Clues:
1. The tennis enthusiast lives in a house with a lower number than the teacher's.
2. The Brit lives immediately to the right of the juice drinker.
3. The Brit and the teacher are next-door neighbours.
4. The Spaniard is the lawyer.
5. Tea is drunk in the last house.
6. The Norwegian does not live in the second house.
7. The Swede is the hiking enthusiast.
8. The Brit and the farmer have one house between them.
9. The lawyer lives immediately to the left of the water drinker.
10. The cooking enthusiast and the Swede live two houses apart.
11. The baker's hobby is tennis.
12. The milk drinker lives immediately to the left of the baker.
13. Chess is the lawyer's hobby.

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
