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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_011.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00019

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, doctor, lawyer, farmer, pilot
- nationality: Norwegian, Brit, Swede, German, Spaniard
- drink: milk, cocoa, tea, water, coffee
- color: yellow, purple, red, white, green

Clues:
1. The cocoa drinker lives in the yellow house.
2. The German lives immediately to the right of whoever lives in the yellow house.
3. The person in the green house either is the Brit or is the Norwegian.
4. There is exactly one house between the Swede and the person in the white house.
5. The baker lives somewhere to the left of the pilot.
6. The doctor either drinks coffee or drinks tea.
7. The Swede lives in the second house.
8. The occupant of the purple house drinks tea.
9. The Brit works as the farmer.
10. The person who drinks cocoa lives directly to the left of the lawyer.
11. The cocoa drinker lives somewhere to the left of the Norwegian.
12. The Norwegian works as the doctor.
13. The farmer does not live in the green house.
14. The person who drinks milk is the German.
15. The baker lives next to the lawyer.

## Puzzle plain:zebra-00049

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, horse, cat, dog, fish
- hobby: hiking, golf, chess, painting, tennis
- job: farmer, baker, lawyer, doctor, teacher
- nationality: Swede, Brit, German, Norwegian, Spaniard

Clues:
1. The owner of the cat lives in a lower-numbered house than the Norwegian.
2. The cat owner lives in the house just left of the one where the person who keeps the horse lives.
3. The person who enjoys painting lives in the house just left of the one where the golf enthusiast lives.
4. The person who keeps the dog lives somewhere to the right of the owner of the cat.
5. The baker and the hiking enthusiast are not neighbours.
6. The owner of the bird works as the doctor.
7. The owner of the cat either is the German or is the Swede.
8. The Brit and the doctor live in adjacent houses.
9. The person who keeps the cat and the teacher are neighbours.
10. The owner of the cat enjoys chess.
11. The person who enjoys painting works as the farmer.
12. The owner of the horse is the German.
13. The baker and the bird owner live two houses apart.
14. The lawyer and the Norwegian are neighbours.

## Puzzle plain:zebra-00020

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, horse, rabbit, cat, bird
- job: doctor, teacher, lawyer, farmer, pilot
- color: purple, blue, yellow, red, green
- hobby: painting, hiking, golf, cooking, chess

Clues:
1. The person who enjoys golf lives in one of the two end houses.
2. The person who keeps the bird lives immediately to the right of the lawyer.
3. The owner of the cat enjoys cooking.
4. The person in the green house lives directly to the left of the owner of the bird.
5. The person in the yellow house lives in the house just left of the one where the painting enthusiast lives.
6. Whoever lives in the blue house lives in the third house.
7. The cooking enthusiast works as the doctor.
8. The pilot keeps the fish.
9. The chess enthusiast either keeps the fish or keeps the rabbit.
10. There is exactly one house between the farmer and the occupant of the purple house.
11. The doctor lives in the house just left of the one where whoever lives in the red house lives.
12. The person who enjoys painting lives in the house just left of the one where the chess enthusiast lives.

## Puzzle hard:zebra_hard-00068

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, fish, cat, horse, dog
- color: red, blue, yellow, purple, white
- nationality: Dane, Norwegian, Brit, Swede, Spaniard
- drink: coffee, cocoa, juice, tea, water

Clues:
1. One of the neighbours of the Norwegian is the Dane.
2. Exactly 2 houses lie to the left of the home of the owner of the dog.
3. The juice drinker and the occupant of the yellow house are one and the same person.
4. One of the neighbours of the person who keeps the horse drinks coffee.
5. Neither the person who drinks cocoa nor the coffee drinker keeps the bird.
6. The occupant of the blue house has only one neighbour.
7. Exactly 3 houses lie to the left of the home of the Brit.
8. The Norwegian has only one neighbour.
9. The fish owner lives somewhere between the owner of the horse and the Swede.
10. Exactly 0 houses lie to the left of the home of the occupant of the purple house.
11. The left-hand neighbour of the fish owner drinks cocoa.
12. The left-hand neighbour of the owner of the dog lives in the yellow house.
13. The right-hand neighbour of the occupant of the red house is the Swede.
14. Exactly 4 houses lie to the left of the home of the tea drinker.

## Puzzle hard:zebra_hard-00075

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: pilot, lawyer, teacher, farmer, baker
- hobby: chess, golf, painting, cooking, tennis
- pet: cat, bird, fish, rabbit, horse
- nationality: Dane, Spaniard, German, Brit, Swede

Clues:
1. If the tennis enthusiast does not keep the cat, then that person keeps the horse.
2. The left-hand neighbour of the lawyer is the Dane.
3. One of the neighbours of the pilot enjoys cooking.
4. Exactly one house separates the Brit from the Swede.
5. The left-hand neighbour of the owner of the bird enjoys painting.
6. One of the neighbours of the Spaniard keeps the rabbit.
7. The baker lives two doors away from the owner of the cat.
8. The left-hand neighbour of the person who enjoys golf is the German.
9. The Spaniard and the teacher are one and the same person.
10. The Swede lives two doors away from the person who enjoys tennis.
11. The right-hand neighbour of the painting enthusiast is the Dane.
12. The owner of the fish lives further to the right than the German.
13. The person who enjoys painting has only one neighbour.

## Puzzle paraphrase:zebra-00199

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, pilot, baker, farmer, doctor
- drink: milk, tea, coffee, juice, cocoa
- hobby: chess, painting, tennis, cooking, hiking
- nationality: Brit, Dane, German, Norwegian, Spaniard

Clues:
1. The doctor does not drink milk.
2. The baker lives immediately to the right of the pilot.
3. The chess enthusiast lives directly to the left of the Brit.
4. The farmer lives just left of the pilot.
5. The painting enthusiast lives immediately to the right of the Brit.
6. The Dane drinks tea.
7. The tea drinker lives next door to the tennis enthusiast.
8. The chess enthusiast drinks coffee.
9. The Brit and the farmer have exactly one house between them.
10. The Norwegian lives immediately to the right of the cooking enthusiast.
11. The juice drinker lives next door to the Norwegian.
12. The Spaniard is the lawyer.
13. The farmer lives immediately to the right of the doctor.

## Puzzle paraphrase:zebra-00149

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, golf, hiking, tennis, painting
- job: teacher, baker, pilot, farmer, doctor
- nationality: Swede, Dane, Norwegian, Spaniard, German
- drink: juice, water, tea, cocoa, milk

Clues:
1. Cooking is the pilot's hobby.
2. The golf enthusiast lives directly right of the Swede.
3. The Dane is the farmer.
4. The water drinker is not the farmer.
5. The Spaniard is the tea drinker.
6. The painting enthusiast drinks milk.
7. Golf is the teacher's hobby.
8. The German lives in house 5.
9. The hiking enthusiast lives next to the milk drinker.
10. The doctor is not the milk drinker.
11. The second house belongs to the water drinker.
12. The doctor lives somewhere right of the tennis enthusiast.
13. The farmer lives immediately left of the doctor.
14. The juice drinker lives immediately left of the baker.

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

## Puzzle paraphrase:zebra-00125

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, juice, coffee, water, milk
- pet: rabbit, horse, dog, fish, bird
- color: red, green, blue, yellow, white
- hobby: hiking, golf, cooking, chess, tennis

Clues:
1. The milk drinker keeps the bird.
2. The green house stands directly to the right of the milk drinker.
3. The tea drinker lives somewhere to the left of the dog owner.
4. The coffee drinker lives directly left of the white house.
5. The white house's occupant keeps either the dog or the rabbit.
6. The golfer keeps the rabbit.
7. The white house's occupant likes hiking.
8. The cooking enthusiast and the hiker live next door to each other.
9. The rabbit owner drinks coffee.
10. The blue house is immediately to the right of the green house.
11. The tennis player lives directly to the left of the rabbit owner.
12. The yellow house's occupant and the fish owner are not the same person.
13. The fish owner drinks water.

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
