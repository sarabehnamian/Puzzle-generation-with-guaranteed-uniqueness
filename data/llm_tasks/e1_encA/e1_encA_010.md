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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_010.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle plain:zebra-00008

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Spaniard, Swede, Norwegian, Dane
- drink: milk, cocoa, coffee, tea, juice
- color: blue, purple, red, yellow, green
- pet: dog, bird, cat, horse, rabbit

Clues:
1. The person who drinks coffee lives in the middle house.
2. The horse owner lives in house 5.
3. The bird owner lives in the blue house.
4. The occupant of the green house keeps the cat.
5. The coffee drinker lives next to the juice drinker.
6. The cat owner and the person who drinks coffee are neighbours.
7. Whoever lives in the yellow house lives in house 5.
8. The milk drinker lives in the fourth house.
9. The Spaniard either keeps the horse or keeps the rabbit.
10. The coffee drinker and the Swede live two houses apart.
11. The occupant of the blue house does not live next to the German.
12. The Dane does not live next to the German.
13. The person who drinks tea lives in a lower-numbered house than whoever lives in the purple house.
14. The occupant of the blue house lives in the third house.
15. The rabbit owner lives directly to the left of the owner of the horse.
16. The juice drinker lives next to the Norwegian.

## Puzzle hard:zebra_hard-00028

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, doctor, farmer, lawyer, baker
- drink: tea, juice, water, cocoa, milk
- pet: cat, dog, rabbit, fish, bird
- nationality: Norwegian, German, Brit, Spaniard, Dane

Clues:
1. The Brit lives two doors away from the owner of the rabbit.
2. Neither the person who keeps the rabbit nor the person who drinks tea works as the farmer.
3. At least one house separates the fish owner from the water drinker.
4. One of the neighbours of the person who drinks juice is the Dane.
5. The water drinker does not live in the third house from the right.
6. The juice drinker and the Spaniard are one and the same person.
7. The person who drinks cocoa has only one neighbour.
8. If the farmer does not drink milk, then that person drinks tea.
9. The owner of the dog lives further to the right than the doctor.
10. One of the neighbours of the Brit keeps the dog.
11. The bird owner lives further to the right than the cocoa drinker.
12. Exactly one house separates the Spaniard from the tea drinker.
13. The baker and the person who drinks juice are one and the same person.
14. The German lives somewhere between the owner of the bird and the person who drinks juice.
15. The left-hand neighbour of the lawyer is the German.
16. One of the neighbours of the lawyer keeps the bird.

## Puzzle hard:zebra_hard-00032

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, chess, hiking, cooking
- nationality: Spaniard, Norwegian, German, Swede, Brit
- job: farmer, pilot, doctor, teacher, lawyer
- pet: bird, dog, fish, horse, cat

Clues:
1. At least one house separates the doctor from the farmer.
2. The cooking enthusiast lives somewhere between the person who enjoys hiking and the Norwegian.
3. Exactly 3 houses lie to the left of the home of the pilot.
4. The German lives two doors away from the tennis enthusiast.
5. The Swede is not the same person as the teacher.
6. Neither the German nor the Norwegian enjoys hiking.
7. The person who keeps the dog and the lawyer are one and the same person.
8. One of the neighbours of the chess enthusiast works as the pilot.
9. One of the neighbours of the person who keeps the fish enjoys painting.
10. The dog owner has only one neighbour.
11. Exactly 0 houses lie to the left of the home of the farmer.
12. One of the neighbours of the bird owner is the Norwegian.
13. If the pilot is not the Spaniard, then that person is the Swede.
14. Exactly one house separates the owner of the cat from the pilot.
15. The right-hand neighbour of the Norwegian is the Spaniard.

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

## Puzzle plain:zebra-00082

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, milk, tea, juice, water
- hobby: hiking, tennis, painting, chess, cooking
- pet: bird, horse, dog, cat, fish
- nationality: Swede, Norwegian, Brit, Spaniard, Dane

Clues:
1. The chess enthusiast and the hiking enthusiast live two houses apart.
2. The cat owner lives immediately to the right of the person who enjoys chess.
3. The person who drinks milk lives next to the Spaniard.
4. The dog owner lives at one end of the row.
5. The cat owner either is the Norwegian or is the Swede.
6. The water drinker either enjoys cooking or enjoys painting.
7. The person who drinks coffee lives in house 1.
8. The coffee drinker keeps the horse.
9. The coffee drinker and the Swede live two houses apart.
10. The Brit does not live next to the Spaniard.
11. The person who enjoys painting lives directly to the left of the person who drinks juice.
12. The Spaniard keeps the fish.
13. The tea drinker lives in one of the two end houses.

## Puzzle paraphrase:zebra-00198

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, tea, milk, coffee, cocoa
- color: red, green, yellow, blue, purple
- hobby: painting, tennis, chess, cooking, hiking
- job: baker, lawyer, teacher, pilot, farmer

Clues:
1. The tea drinker lives immediately to the left of the blue house.
2. The baker lives directly to the left of the coffee drinker.
3. The farmer is the one who drinks juice.
4. Somewhere to the left of the hiking enthusiast lives the milk drinker.
5. The farmer and the tennis enthusiast live two houses apart.
6. The pilot lives immediately to the right of the milk drinker.
7. The hiking enthusiast lives next door to the purple house's occupant.
8. The chess enthusiast lives in house 5.
9. The lawyer and the yellow house's occupant are neighbours.
10. The purple house is immediately to the right of the juice drinker.
11. The pilot does not enjoy painting.
12. The cooking enthusiast lives directly to the left of the green house.

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

## Puzzle hard:zebra_hard-00067

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, water, milk, tea, coffee
- nationality: Norwegian, Swede, Brit, Spaniard, Dane
- job: pilot, farmer, doctor, teacher, baker
- hobby: golf, painting, chess, cooking, tennis

Clues:
1. The golf enthusiast and the Norwegian are one and the same person.
2. The Brit and the person who drinks cocoa are one and the same person.
3. The person who enjoys painting is not the same person as the teacher.
4. The chess enthusiast lives further to the right than the farmer.
5. At least one house separates the painting enthusiast from the baker.
6. The milk drinker and the Norwegian are one and the same person.
7. The person who enjoys cooking is not the same person as the teacher.
8. The right-hand neighbour of the teacher enjoys chess.
9. The tennis enthusiast lives further to the right than the milk drinker.
10. The pilot and the Swede are one and the same person.
11. The Swede does not live to the right of the Dane.
12. Exactly one house separates the coffee drinker from the tea drinker.
13. If the person who enjoys tennis does not drink milk, then that person drinks tea.
14. The Norwegian lives somewhere between the Spaniard and the person who drinks tea.
15. Exactly 3 houses lie to the left of the home of the doctor.
