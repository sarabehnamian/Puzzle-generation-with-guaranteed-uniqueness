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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_001.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle paraphrase:zebra-00128

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, pilot, lawyer, farmer
- nationality: Spaniard, Norwegian, German, Dane, Brit
- color: blue, purple, white, yellow, red
- hobby: tennis, hiking, golf, cooking, painting

Clues:
1. The Norwegian is the lawyer.
2. The blue house is house 2.
3. The Dane's hobby is either golf or painting.
4. The pilot lives in the leftmost house.
5. The white house belongs to the Dane.
6. The red house lies directly right of the teacher.
7. The Spaniard's hobby is golf.
8. The white house is directly to the left of the teacher's house.
9. The teacher and the tennis player live two houses apart.
10. The blue house's occupant is either the Dane or the German.
11. The red house's occupant enjoys hiking.
12. The doctor and the German live two houses apart.
13. The purple house's occupant enjoys either golf or painting.

## Puzzle paraphrase:zebra-00100

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, dog, horse, cat, fish
- drink: tea, water, juice, coffee, milk
- hobby: chess, tennis, painting, cooking, hiking
- job: lawyer, pilot, doctor, baker, farmer

Clues:
1. The doctor and the farmer live next door to each other.
2. The milk drinker lives in house 3.
3. Somewhere to the left of the chess enthusiast lives the cat owner.
4. The juice drinker lives directly to the left of the cooking enthusiast.
5. One house separates the coffee drinker from the farmer.
6. The cooking enthusiast lives right next to the horse keeper, on the left side.
7. The doctor's house has a lower number than the lawyer's.
8. The dog owner lives immediately to the left of the tennis enthusiast.
9. The fish owner and the tea drinker are neighbours.
10. Two houses separate the cooking enthusiast's home from the hiker's... that is, they live two houses apart.
11. The doctor and the lawyer live two houses apart.
12. The baker occupies house 2.
13. The person who keeps the bird loves hiking.

## Puzzle plain:zebra-00086

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, water, coffee, juice, tea
- pet: horse, cat, dog, rabbit, fish
- hobby: painting, cooking, hiking, chess, golf
- nationality: Brit, Norwegian, German, Swede, Spaniard

Clues:
1. The Norwegian lives in house 4.
2. The fish owner lives in a lower-numbered house than the person who drinks cocoa.
3. The juice drinker lives in house 2.
4. The golf enthusiast lives in the house just left of the one where the chess enthusiast lives.
5. The person who enjoys hiking either is the German or is the Spaniard.
6. The horse owner is the Spaniard.
7. The owner of the rabbit is the Swede.
8. The person who enjoys chess lives next to the person who drinks cocoa.
9. The Brit lives directly to the left of the owner of the fish.
10. The person who drinks coffee and the water drinker live two houses apart.
11. The Brit and the person who enjoys golf live in adjacent houses.
12. The Spaniard drinks water.
13. The person who keeps the dog enjoys cooking.
14. The water drinker lives in a lower-numbered house than the coffee drinker.

## Puzzle plain:zebra-00022

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, water, juice, tea, coffee
- pet: rabbit, cat, bird, horse, dog
- job: lawyer, pilot, farmer, teacher, doctor
- hobby: chess, cooking, painting, golf, hiking

Clues:
1. The owner of the rabbit enjoys chess.
2. The hiking enthusiast drinks cocoa.
3. The person who enjoys cooking lives in the house just left of the one where the coffee drinker lives.
4. The person who keeps the horse and the person who keeps the rabbit are not neighbours.
5. The tea drinker lives in the fifth house.
6. The dog owner lives in one of the two end houses.
7. The golf enthusiast and the juice drinker live two houses apart.
8. The doctor either keeps the bird or keeps the cat.
9. The person who keeps the bird lives in house 2.
10. The teacher lives in the house just left of the one where the cooking enthusiast lives.
11. The person who enjoys painting lives somewhere to the right of the pilot.
12. The juice drinker either works as the farmer or works as the lawyer.
13. The lawyer either enjoys chess or enjoys hiking.

## Puzzle plain:zebra-00085

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, juice, cocoa, tea, milk
- job: farmer, pilot, teacher, baker, lawyer
- nationality: Dane, German, Brit, Swede, Spaniard
- color: green, purple, yellow, white, blue

Clues:
1. There is exactly one house between the Brit and the farmer.
2. The person who drinks coffee lives in a lower-numbered house than the Spaniard.
3. The coffee drinker and the pilot live in adjacent houses.
4. The milk drinker lives at one end of the row.
5. The person who drinks cocoa lives in the leftmost house.
6. The person who drinks tea lives directly to the left of the Dane.
7. The lawyer lives next to the occupant of the white house.
8. The occupant of the blue house lives at one end of the row.
9. Whoever lives in the yellow house lives in the house just left of the one where the occupant of the white house lives.
10. The baker drinks coffee.
11. The Swede lives in the white house.
12. The person who drinks milk and whoever lives in the purple house live two houses apart.
13. The person in the purple house works as the baker.
14. The farmer lives immediately to the right of the lawyer.

## Puzzle hard:zebra_hard-00073

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Swede, Dane, Brit, German
- pet: bird, cat, dog, horse, fish
- job: doctor, baker, pilot, lawyer, teacher
- drink: cocoa, juice, water, tea, coffee

Clues:
1. One of the neighbours of the fish owner works as the teacher.
2. The right-hand neighbour of the water drinker works as the pilot.
3. If the person who drinks water is not the lawyer, then that person works as the teacher.
4. The left-hand neighbour of the Dane keeps the dog.
5. The Dane lives two doors away from the Swede.
6. One of the neighbours of the Brit is the Dane.
7. The juice drinker and the Swede are one and the same person.
8. The owner of the cat is not the same person as the Swede.
9. The person who keeps the horse lives in the fifth house from the right.
10. The lawyer and the Spaniard are one and the same person.
11. The baker and the person who drinks cocoa are one and the same person.
12. The cocoa drinker lives two doors away from the person who drinks coffee.
13. The left-hand neighbour of the owner of the fish works as the pilot.

## Puzzle paraphrase:zebra-00167

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, farmer, pilot, baker
- drink: juice, coffee, tea, cocoa, milk
- color: red, green, purple, yellow, white
- pet: fish, cat, horse, dog, bird

Clues:
1. The fish owner and the lawyer live two houses apart.
2. The purple house is directly to the left of the tea drinker.
3. The coffee drinker lives next door to the dog owner.
4. The juice drinker and the white house's occupant live in adjacent houses.
5. The milk drinker lives in one of the two end houses.
6. The purple house is immediately to the right of the white house.
7. The coffee drinker keeps the bird.
8. The dog owner lives in the purple house.
9. The baker keeps the cat.
10. The doctor lives next door to the dog owner.
11. Exactly one house lies between the green house and the red house.
12. The farmer lives directly to the left of the purple house.
13. The green house is the middle house.
14. The green house and the horse owner are two houses apart.

## Puzzle hard:zebra_hard-00024

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, green, red, purple, white
- hobby: golf, cooking, tennis, painting, chess
- nationality: Spaniard, Swede, Norwegian, German, Brit
- job: farmer, pilot, doctor, teacher, lawyer

Clues:
1. The farmer and the tennis enthusiast are one and the same person.
2. None of the neighbours of the farmer is the Swede.
3. The person who enjoys cooking and the person in the green house are one and the same person.
4. Exactly 1 house lies to the left of the home of the tennis enthusiast.
5. The German lives somewhere between the Brit and whoever lives in the green house.
6. Exactly one house separates the doctor from the person who enjoys golf.
7. If the tennis enthusiast is not the Brit, then that person is the Norwegian.
8. The chess enthusiast is not the same person as the lawyer.
9. The pilot does not live to the right of the lawyer.
10. The right-hand neighbour of whoever lives in the white house works as the pilot.
11. The German and whoever lives in the red house are one and the same person.
12. Whoever lives in the purple house and the Swede are one and the same person.
13. The person who enjoys chess lives further to the right than the Spaniard.
14. Exactly 4 houses lie to the left of the home of whoever lives in the green house.

## Puzzle paraphrase:zebra-00175

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, painting, golf, hiking, cooking
- job: pilot, baker, lawyer, teacher, doctor
- drink: water, tea, cocoa, coffee, milk
- color: purple, blue, white, yellow, red

Clues:
1. One house lies between the cocoa drinker and the painting enthusiast.
2. The milk drinker lives in the blue house.
3. The teacher and the water drinker live two houses apart.
4. The lawyer lives in the last house.
5. The pilot lives immediately to the left of the yellow house.
6. The golf enthusiast lives next door to the tennis enthusiast.
7. The water drinker and the yellow house's occupant are two houses apart.
8. The golf enthusiast drinks coffee.
9. The coffee drinker is next door to the lawyer.
10. The milk drinker's hobby is hiking.
11. The purple house is immediately to the left of the tea drinker.
12. The cocoa drinker lives in house 1.
13. The baker lives immediately to the left of the red house.
