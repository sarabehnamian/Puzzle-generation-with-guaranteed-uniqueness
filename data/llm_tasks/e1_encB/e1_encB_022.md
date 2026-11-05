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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_022.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle hard:zebra_hard-00025

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, tennis, painting, hiking, cooking
- color: white, yellow, purple, red, green
- nationality: Spaniard, Brit, German, Swede, Dane
- drink: water, tea, juice, cocoa, milk

Clues:
1. If the Swede does not enjoy hiking, then that person enjoys tennis.
2. One of the neighbours of the person who drinks milk is the Spaniard.
3. If the person who enjoys cooking is not the Dane, then that person is the German.
4. The person who enjoys tennis lives somewhere between the Brit and the person in the yellow house.
5. The Spaniard lives somewhere between the chess enthusiast and the person who enjoys cooking.
6. The right-hand neighbour of the person who enjoys cooking lives in the purple house.
7. The cocoa drinker and whoever lives in the green house are one and the same person.
8. Exactly 3 houses lie to the left of the home of whoever lives in the green house.
9. Neither the chess enthusiast nor the tennis enthusiast lives in the yellow house.
10. The person who drinks water lives somewhere between the cooking enthusiast and the person who enjoys hiking.
11. The cooking enthusiast lives further to the right than the Spaniard.
12. The person who drinks cocoa lives somewhere between the juice drinker and the person who drinks milk.
13. Neither the Dane nor the Spaniard lives in the red house.
14. The cooking enthusiast is not the same person as the Dane.

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

## Puzzle paraphrase:zebra-00154

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, golf, cooking, tennis, hiking
- nationality: Brit, Swede, Norwegian, Dane, Spaniard
- drink: cocoa, water, milk, tea, coffee
- job: farmer, baker, teacher, doctor, lawyer

Clues:
1. The Dane and the Norwegian are not next-door neighbours.
2. The milk drinker lives directly to the left of the tea drinker.
3. The golfer lives in one of the end houses.
4. The hiker is the lawyer.
5. The doctor's hobby is cooking.
6. The Swede lives at one end of the row.
7. The farmer lives in a lower-numbered house than the lawyer.
8. The baker and the golfer live in adjacent houses.
9. The coffee drinker lives next door to the painter.
10. The teacher lives immediately to the left of the tea drinker.
11. The coffee drinker and the water drinker are next-door neighbours.
12. The Dane's hobby is either golf or tennis.
13. The Spaniard's hobby is hiking.
14. The Brit lives in the fourth house.

## Puzzle paraphrase:zebra-00150

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, German, Spaniard, Swede
- job: pilot, lawyer, doctor, farmer, teacher
- hobby: golf, tennis, cooking, painting, chess
- color: white, purple, green, yellow, blue

Clues:
1. The teacher and the resident of the yellow house are separated by exactly one house.
2. The Brit and the Spaniard are next-door neighbours.
3. The Swede's hobby is painting.
4. Whoever plays tennis lives in either the green house or the yellow house.
5. The green house is one of the two end houses.
6. The farmer lives somewhere to the right of the painter.
7. The white house is immediately to the left of the lawyer's house.
8. Exactly one house sits between the Dane and the resident of the purple house.
9. The German and the green house's occupant live two doors apart.
10. The chess player lives directly to the left of the doctor.
11. The Spaniard lives in the yellow house.
12. The farmer's hobby is chess.
13. The Brit's hobby is golf.

## Puzzle paraphrase:zebra-00140

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, tennis, hiking, painting, golf
- drink: tea, water, milk, cocoa, juice
- color: white, red, green, yellow, purple
- pet: cat, bird, horse, fish, rabbit

Clues:
1. The yellow house's resident does not play tennis.
2. Cocoa is drunk by whoever lives in the white house.
3. House 2 is home to the water drinker.
4. Whoever owns the rabbit loves hiking.
5. The painting enthusiast lives in one of the two end houses.
6. The red house's occupant keeps a horse.
7. The tea drinker is not the one who keeps the horse.
8. The purple house and the tennis player are next-door neighbours.
9. Whoever drinks juice enjoys golf.
10. The chess enthusiast is not the person living in the yellow house.
11. The cat owner lives directly to the right of the tennis player.
12. The bird keeper lives right next to the juice drinker, on the right side.
13. The white house's occupant keeps the rabbit.
14. The horse owner lives in house 5.

## Puzzle hard:zebra_hard-00043

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, pilot, baker, lawyer
- hobby: golf, chess, tennis, hiking, cooking
- pet: fish, rabbit, dog, bird, horse
- nationality: Brit, Swede, Spaniard, Norwegian, German

Clues:
1. Exactly 2 houses lie to the left of the home of the bird owner.
2. The right-hand neighbour of the tennis enthusiast enjoys chess.
3. If the teacher does not enjoy chess, then that person enjoys cooking.
4. One of the neighbours of the German works as the doctor.
5. The right-hand neighbour of the teacher is the Brit.
6. The left-hand neighbour of the person who enjoys cooking enjoys chess.
7. Exactly one house separates the fish owner from the person who keeps the horse.
8. Neither the Brit nor the pilot enjoys golf.
9. The Spaniard lives somewhere between the person who keeps the dog and the Norwegian.
10. Exactly 4 houses lie to the left of the home of the German.
11. The horse owner lives somewhere between the person who keeps the dog and the fish owner.
12. The person who keeps the horse and the lawyer are one and the same person.
13. Neither the owner of the bird nor the owner of the horse enjoys tennis.

## Puzzle plain:zebra-00057

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Swede, Spaniard, Norwegian, Dane
- drink: juice, coffee, cocoa, water, tea
- hobby: tennis, hiking, painting, cooking, chess
- job: farmer, teacher, doctor, baker, lawyer

Clues:
1. The person who enjoys hiking and the tennis enthusiast live two houses apart.
2. The person who drinks cocoa is the Norwegian.
3. The chess enthusiast either is the Norwegian or is the Spaniard.
4. The water drinker is the Dane.
5. The farmer drinks juice.
6. The tennis enthusiast works as the teacher.
7. The baker and the painting enthusiast live in adjacent houses.
8. There is exactly one house between the hiking enthusiast and the juice drinker.
9. The chess enthusiast lives directly to the left of the coffee drinker.
10. The juice drinker lives immediately to the right of the Brit.
11. The Spaniard lives at one end of the row.
12. The baker does not live next to the lawyer.

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

## Puzzle hard:zebra_hard-00089

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, coffee, juice, water, tea
- pet: rabbit, cat, horse, bird, dog
- job: farmer, teacher, doctor, lawyer, pilot
- hobby: tennis, painting, hiking, cooking, chess

Clues:
1. The juice drinker lives somewhere between the cooking enthusiast and the horse owner.
2. The right-hand neighbour of the rabbit owner works as the teacher.
3. The right-hand neighbour of the doctor enjoys cooking.
4. The right-hand neighbour of the lawyer works as the doctor.
5. The farmer and the person who drinks juice are one and the same person.
6. The owner of the cat and the teacher are one and the same person.
7. The left-hand neighbour of the milk drinker enjoys painting.
8. The coffee drinker lives in the fifth house from the right.
9. The person who enjoys tennis lives somewhere between the person who drinks milk and the tea drinker.
10. The tennis enthusiast lives somewhere between the owner of the dog and the owner of the horse.
11. The left-hand neighbour of the hiking enthusiast enjoys painting.
