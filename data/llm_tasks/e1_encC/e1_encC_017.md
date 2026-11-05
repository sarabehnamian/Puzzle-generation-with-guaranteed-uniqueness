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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encC\e1_encC_017.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00148

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, golf, painting, cooking, chess
- pet: fish, bird, dog, rabbit, horse
- nationality: Spaniard, Dane, Norwegian, Brit, German
- drink: tea, milk, water, juice, coffee

Clues:
1. The bird owner and the fish owner are not neighbours.
2. The chess enthusiast and the tea drinker live next door to each other.
3. The Spaniard lives in a lower-numbered house than the water drinker.
4. The dog owner plays tennis.
5. The rabbit owner lives immediately left of the golf enthusiast.
6. The coffee drinker does not live in house 3.
7. The Brit and the Dane do not live next to each other.
8. Two houses separate the German from the rabbit owner.
9. The fish owner lives directly right of the rabbit owner.
10. The coffee drinker keeps either the fish or the horse.
11. The Spaniard is the coffee drinker.
12. Painting is the Brit's hobby.
13. The water drinker is the chess enthusiast.
14. The milk drinker keeps either the dog or the rabbit.
15. The tea drinker lives somewhere to the right of the Brit.
16. The tennis enthusiast lives somewhere left of the fish owner.

## Puzzle paraphrase:zebra-00178

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, blue, green, purple, red
- job: farmer, doctor, baker, lawyer, teacher
- drink: juice, coffee, cocoa, milk, tea
- pet: cat, fish, rabbit, bird, horse

Clues:
1. The farmer lives immediately to the left of the cocoa drinker.
2. The doctor lives in house 5.
3. The green house's occupant keeps the horse.
4. The bird owner and the fish keeper live next door to each other.
5. The red house's occupant keeps either the cat or the horse.
6. The teacher lives immediately to the right of the yellow house.
7. The bird keeper lives somewhere to the right of the teacher.
8. The juice drinker does not live next door to the teacher.
9. The yellow house's occupant drinks either coffee or milk.
10. The yellow house is immediately to the left of the coffee drinker.
11. The red house is house 5.
12. The lawyer lives immediately to the left of the bird keeper.
13. The cocoa drinker and the purple house are two houses apart.

## Puzzle paraphrase:zebra-00137

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Spaniard, Brit, Norwegian, German
- drink: milk, juice, coffee, cocoa, water
- hobby: cooking, golf, tennis, hiking, painting
- pet: horse, rabbit, fish, bird, cat

Clues:
1. The juice drinker lives immediately to the left of the Swede.
2. The Norwegian drinks coffee.
3. The German lives directly to the left of the hiking enthusiast.
4. The cooking enthusiast and the hiking enthusiast live two houses apart.
5. The bird is kept in the second house.
6. The water drinker lives immediately to the right of the German.
7. The rabbit owner is either the Brit or the Spaniard.
8. The cat owner lives somewhere to the right of the Spaniard.
9. The hiking enthusiast and the horse owner live next door to each other.
10. The tennis enthusiast lives in the second house.
11. The milk drinker lives next door to the Spaniard.
12. The Spaniard keeps either the fish or the rabbit.
13. The Swede is the golf enthusiast.

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

## Puzzle paraphrase:zebra-00179

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Dane, Swede, Spaniard, Brit
- color: yellow, blue, red, green, white
- drink: cocoa, tea, coffee, water, juice
- job: lawyer, doctor, baker, pilot, farmer

Clues:
1. The German does not live next door to the water drinker.
2. The red house is immediately to the right of the tea drinker.
3. The Dane lives in the first house.
4. The baker lives at one end of the row.
5. The farmer lives next door to the German.
6. The lawyer is the tea drinker.
7. The green house and the juice drinker are two houses apart.
8. The pilot lives in the blue house.
9. One house lies between the red house and the yellow house.
10. The farmer is the Brit.
11. The white house is immediately to the left of the Spaniard.
12. The Brit lives at one end of the row.
13. The Brit lives somewhere to the right of the cocoa drinker.
14. The red house's occupant drinks coffee.

## Puzzle paraphrase:zebra-00165

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, lawyer, teacher, pilot, doctor
- drink: tea, juice, milk, cocoa, coffee
- nationality: Norwegian, German, Swede, Brit, Spaniard
- hobby: chess, hiking, cooking, golf, tennis

Clues:
1. The Norwegian lives in house 1.
2. The tea drinker lives immediately to the left of the lawyer.
3. The German lives immediately to the left of the farmer.
4. The milk drinker does not enjoy chess.
5. The golfer is the lawyer.
6. The farmer lives immediately to the left of the coffee drinker.
7. One house separates the Brit from the pilot.
8. The cocoa drinker lives immediately to the left of the cooking enthusiast.
9. The farmer and the Spaniard live in adjacent houses.
10. The doctor drinks either cocoa or juice.
11. The milk drinker lives immediately to the left of the tennis enthusiast.
12. The cooking enthusiast and the milk drinker live two houses apart.
13. The cocoa drinker lives next door to the doctor.

## Puzzle hard:zebra_hard-00005

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, doctor, lawyer, pilot, baker
- hobby: chess, golf, painting, tennis, hiking
- color: green, white, red, purple, blue
- pet: dog, rabbit, horse, bird, cat

Clues:
1. Exactly one house separates the owner of the bird from the person who enjoys chess.
2. The right-hand neighbour of the occupant of the blue house keeps the dog.
3. The lawyer and the occupant of the white house are one and the same person.
4. The occupant of the purple house and the teacher are one and the same person.
5. The pilot lives somewhere between the baker and the bird owner.
6. If the person who enjoys painting does not keep the cat, then that person keeps the dog.
7. If the painting enthusiast does not live in the blue house, then that person lives in the white house.
8. The left-hand neighbour of whoever lives in the red house enjoys golf.
9. Whoever lives in the white house lives further to the right than the teacher.
10. If the doctor does not enjoy golf, then that person enjoys tennis.
11. If the doctor does not keep the dog, then that person keeps the horse.
12. The lawyer does not live in the second house from the right.
13. The right-hand neighbour of the person who enjoys painting lives in the purple house.

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
