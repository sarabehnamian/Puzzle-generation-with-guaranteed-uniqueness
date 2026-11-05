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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_000.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle paraphrase:zebra-00193

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, German, Brit, Spaniard, Dane
- job: baker, doctor, teacher, farmer, pilot
- pet: fish, dog, cat, rabbit, horse
- color: green, blue, yellow, white, red

Clues:
1. The white house and the yellow house are next to each other.
2. The Dane is the doctor.
3. The cat keeper lives immediately to the right of the Swede.
4. The green house's occupant keeps either the cat or the dog.
5. The German and the red house's occupant are not neighbours.
6. The Brit lives next door to the farmer.
7. The Swede is the pilot.
8. The Dane and the occupant of the yellow house live two houses apart.
9. The German lives next door to the pilot.
10. The blue house is directly to the left of the yellow house.
11. The dog keeper lives somewhere to the right of the German.
12. The rabbit owner is either the doctor or the pilot.
13. The fish keeper is the teacher.
14. Somewhere to the right of the Brit lives the teacher.

## Puzzle plain:zebra-00033

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, rabbit, dog, horse, cat
- nationality: Swede, German, Spaniard, Norwegian, Dane
- hobby: chess, hiking, golf, tennis, cooking
- job: pilot, teacher, lawyer, doctor, baker

Clues:
1. The pilot lives next to the Swede.
2. The teacher lives in the first house.
3. The owner of the dog either enjoys chess or enjoys golf.
4. The cooking enthusiast lives somewhere to the right of the person who enjoys tennis.
5. The person who keeps the cat enjoys cooking.
6. The person who enjoys chess either keeps the horse or keeps the rabbit.
7. The owner of the rabbit lives directly to the left of the horse owner.
8. The doctor lives in the house just left of the one where the rabbit owner lives.
9. The chess enthusiast lives in the house just left of the one where the Dane lives.
10. The baker and the person who keeps the rabbit live two houses apart.
11. The Dane and the German live two houses apart.
12. There is exactly one house between the person who enjoys hiking and the rabbit owner.
13. The Spaniard lives immediately to the right of the owner of the rabbit.

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

## Puzzle hard:zebra_hard-00016

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, dog, cat, fish, rabbit
- drink: milk, juice, water, tea, coffee
- hobby: painting, golf, tennis, cooking, hiking
- color: yellow, white, blue, purple, green

Clues:
1. One of the neighbours of the person in the purple house enjoys golf.
2. The right-hand neighbour of whoever lives in the purple house lives in the white house.
3. One of the neighbours of the person who keeps the dog lives in the yellow house.
4. The occupant of the blue house has only one neighbour.
5. If the owner of the fish does not enjoy cooking, then that person enjoys painting.
6. The person who enjoys tennis lives somewhere between the tea drinker and the person who drinks water.
7. One of the neighbours of the person who drinks water lives in the green house.
8. The milk drinker and the tennis enthusiast are one and the same person.
9. The cat owner and the cooking enthusiast are one and the same person.
10. One of the neighbours of the tea drinker keeps the cat.
11. Exactly 0 houses lie to the left of the home of the juice drinker.
12. Exactly 1 house lies to the left of the home of the person who keeps the horse.
13. One of the neighbours of the person who enjoys painting lives in the yellow house.
14. The person who enjoys cooking lives in the fifth house from the right.

## Puzzle hard:zebra_hard-00085

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, pilot, lawyer, farmer, doctor
- hobby: tennis, cooking, painting, hiking, chess
- color: white, red, blue, yellow, green
- pet: cat, rabbit, horse, fish, bird

Clues:
1. One of the neighbours of the doctor enjoys hiking.
2. The bird owner and the doctor are one and the same person.
3. The person who keeps the horse and the person in the yellow house are one and the same person.
4. The owner of the rabbit is not the same person as whoever lives in the red house.
5. Neither the owner of the rabbit nor the occupant of the yellow house enjoys cooking.
6. Exactly one house separates the farmer from the occupant of the yellow house.
7. The left-hand neighbour of the owner of the cat works as the lawyer.
8. The left-hand neighbour of whoever lives in the white house enjoys chess.
9. Whoever lives in the green house lives somewhere between the cooking enthusiast and the person who keeps the rabbit.
10. If the occupant of the white house is not the farmer, then that person works as the pilot.
11. The pilot lives somewhere between the farmer and the owner of the rabbit.
12. The right-hand neighbour of the bird owner enjoys cooking.
13. One of the neighbours of the tennis enthusiast works as the farmer.

## Puzzle paraphrase:zebra-00131

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, painting, golf, hiking, cooking
- nationality: Swede, Spaniard, Norwegian, Dane, German
- job: doctor, baker, farmer, lawyer, teacher
- drink: milk, cocoa, tea, juice, water

Clues:
1. The cocoa drinker lives next door to the doctor.
2. Whoever drinks juice enjoys either chess or golf.
3. The painting enthusiast drinks water.
4. The baker lives directly to the right of the water drinker.
5. The cooking enthusiast is either the farmer or the teacher.
6. The teacher lives in house 1.
7. The tea drinker is either the doctor or the lawyer.
8. The Dane lives directly to the right of the milk drinker.
9. The farmer lives in house 5.
10. The German does not live in house 5.
11. The Spaniard lives somewhere to the left of the juice drinker.
12. The tea drinker lives immediately to the left of the German.
13. The doctor and the hiking enthusiast are next-door neighbours.
14. The Norwegian lives next door to the water drinker.
15. The golf enthusiast is either the lawyer or the teacher.

## Puzzle plain:zebra-00024

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, green, yellow, red, blue
- job: doctor, lawyer, baker, farmer, teacher
- nationality: German, Norwegian, Brit, Dane, Spaniard
- pet: rabbit, dog, cat, horse, fish

Clues:
1. The person in the blue house works as the lawyer.
2. The occupant of the purple house works as the teacher.
3. There is exactly one house between the person in the blue house and the occupant of the red house.
4. The doctor and the Norwegian live two houses apart.
5. The Dane either keeps the dog or keeps the horse.
6. The Brit keeps the rabbit.
7. The horse owner and the occupant of the purple house live in adjacent houses.
8. The Dane lives in one of the two end houses.
9. The Spaniard lives in the third house.
10. The Brit lives next to the occupant of the yellow house.
11. The owner of the cat lives next to the person who keeps the rabbit.
12. The person who keeps the horse lives somewhere to the right of the owner of the cat.
13. The person in the blue house lives in the leftmost house.
14. The baker lives somewhere to the right of the German.
15. The Norwegian lives somewhere to the right of the fish owner.
16. The German lives in a lower-numbered house than the Brit.
