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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encB/e1_encB_013.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00142

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, cooking, golf, tennis, painting
- job: farmer, pilot, lawyer, teacher, baker
- pet: bird, rabbit, cat, horse, fish
- color: yellow, purple, blue, green, red

Clues:
1. The golf enthusiast lives immediately left of the blue house's occupant.
2. The pilot and the rabbit owner are separated by exactly one house.
3. The painting enthusiast lives in house 4.
4. House 2 is home to the cooking enthusiast.
5. The bird owner lives immediately left of the purple house's occupant.
6. The red house's occupant is the teacher.
7. The baker lives in house 2.
8. The tennis enthusiast lives next door to the occupant of the blue house.
9. The farmer is not a neighbour of the rabbit owner.
10. The fish keeper and the rabbit owner live next to each other.
11. Exactly one house lies between the blue house and the green house.
12. The tennis enthusiast is either the farmer or the lawyer.
13. The fish owner lives next door to the person in the blue house.
14. The bird keeper lives next door to the horse owner.
15. The teacher lives in the middle house.

## Puzzle hard:zebra_hard-00066

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, horse, bird, fish, cat
- color: red, yellow, purple, green, white
- drink: juice, coffee, water, milk, cocoa
- job: farmer, teacher, doctor, lawyer, baker

Clues:
1. The person who keeps the horse lives in the third house from the right.
2. One of the neighbours of the farmer works as the doctor.
3. The owner of the bird and the person who drinks cocoa are one and the same person.
4. Exactly 4 houses lie to the left of the home of the person who drinks water.
5. The right-hand neighbour of the person who keeps the horse keeps the rabbit.
6. The baker and the bird owner are one and the same person.
7. The person who keeps the cat lives further to the right than the lawyer.
8. The owner of the cat lives two doors away from the occupant of the yellow house.
9. One of the neighbours of the person who drinks milk drinks juice.
10. If the fish owner does not live in the purple house, then that person lives in the white house.
11. Neither the doctor nor whoever lives in the white house drinks milk.
12. Whoever lives in the purple house lives somewhere between the owner of the bird and whoever lives in the red house.
13. None of the neighbours of the person who drinks juice keeps the fish.
14. The person who drinks milk lives in the second house from the right.
15. The teacher and the occupant of the yellow house are one and the same person.

## Puzzle hard:zebra_hard-00009

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, horse, cat, rabbit, dog
- job: baker, doctor, farmer, teacher, pilot
- drink: tea, cocoa, coffee, milk, juice
- hobby: chess, hiking, painting, tennis, golf

Clues:
1. The tea drinker lives somewhere between the fish owner and the tennis enthusiast.
2. Neither the cocoa drinker nor the pilot keeps the dog.
3. One of the neighbours of the person who drinks juice keeps the rabbit.
4. At least one house separates the owner of the horse from the fish owner.
5. If the owner of the dog is not the doctor, then that person works as the teacher.
6. The right-hand neighbour of the person who drinks tea enjoys golf.
7. The person who keeps the fish and the teacher are one and the same person.
8. The fish owner lives somewhere between the baker and the chess enthusiast.
9. The right-hand neighbour of the person who enjoys tennis works as the baker.
10. If the farmer does not enjoy chess, then that person enjoys tennis.
11. Exactly 0 houses lie to the left of the home of the dog owner.
12. The left-hand neighbour of the painting enthusiast enjoys hiking.
13. The left-hand neighbour of the milk drinker keeps the rabbit.

## Puzzle hard:zebra_hard-00018

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, red, blue, white, purple
- job: pilot, doctor, farmer, baker, lawyer
- hobby: hiking, cooking, chess, tennis, golf
- nationality: Dane, Swede, Norwegian, Brit, German

Clues:
1. Neither the person who enjoys chess nor the cooking enthusiast is the Brit.
2. One of the neighbours of the person who enjoys cooking works as the pilot.
3. The Swede does not live to the right of the Norwegian.
4. The left-hand neighbour of the occupant of the purple house is the Dane.
5. The left-hand neighbour of the lawyer enjoys hiking.
6. The lawyer lives further to the right than the Dane.
7. If the German is not the baker, then that person works as the farmer.
8. The person who enjoys chess and the person in the green house are one and the same person.
9. Whoever lives in the green house lives somewhere between whoever lives in the purple house and the tennis enthusiast.
10. One of the neighbours of the baker is the Brit.
11. The German lives somewhere between the Dane and whoever lives in the white house.
12. The right-hand neighbour of the pilot works as the lawyer.
13. The left-hand neighbour of the person who enjoys golf lives in the blue house.
14. One of the neighbours of the Swede lives in the blue house.
15. One of the neighbours of the German enjoys chess.

## Puzzle hard:zebra_hard-00002

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, green, white, yellow, purple
- job: baker, teacher, pilot, lawyer, doctor
- hobby: tennis, hiking, golf, painting, cooking
- pet: bird, horse, rabbit, cat, dog

Clues:
1. The right-hand neighbour of the cat owner enjoys golf.
2. One of the neighbours of the horse owner keeps the dog.
3. The occupant of the red house lives further to the right than the owner of the bird.
4. The owner of the dog is not the same person as whoever lives in the yellow house.
5. Neither the cat owner nor whoever lives in the green house works as the teacher.
6. The lawyer lives somewhere between the occupant of the red house and whoever lives in the white house.
7. If the teacher does not keep the cat, then that person keeps the rabbit.
8. The pilot lives two doors away from the teacher.
9. The cooking enthusiast and the pilot are one and the same person.
10. The painting enthusiast lives somewhere between the horse owner and the person who enjoys tennis.
11. If the person in the purple house is not the doctor, then that person works as the pilot.
12. At least one house separates the owner of the bird from the horse owner.
13. The teacher lives in the fourth house from the right.
14. One of the neighbours of the teacher works as the doctor.
15. One of the neighbours of the lawyer lives in the yellow house.

## Puzzle hard:zebra_hard-00083

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Swede, German, Dane, Brit
- color: purple, red, yellow, blue, green
- drink: coffee, water, cocoa, tea, milk
- job: teacher, lawyer, baker, doctor, pilot

Clues:
1. The milk drinker and the Swede are one and the same person.
2. If the doctor does not live in the green house, then that person lives in the red house.
3. The right-hand neighbour of the person who drinks water is the Brit.
4. The German lives somewhere between the Swede and the person in the yellow house.
5. The person who drinks cocoa and the person in the green house are one and the same person.
6. The right-hand neighbour of the cocoa drinker lives in the yellow house.
7. The right-hand neighbour of the baker works as the pilot.
8. The coffee drinker lives two doors away from the Spaniard.
9. One of the neighbours of the lawyer lives in the blue house.
10. Exactly 1 house lies to the left of the home of the occupant of the yellow house.
11. At least one house separates the Dane from the baker.
12. The pilot lives somewhere between the doctor and the person in the yellow house.
13. If the pilot is not the German, then that person is the Spaniard.

## Puzzle plain:zebra-00067

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, white, green, blue, purple
- hobby: golf, cooking, chess, painting, hiking
- nationality: Brit, Norwegian, Spaniard, German, Dane
- job: doctor, farmer, pilot, teacher, baker

Clues:
1. The Dane lives in a lower-numbered house than the baker.
2. The Norwegian lives next to the occupant of the purple house.
3. The cooking enthusiast and the Norwegian live in adjacent houses.
4. The person in the green house and the pilot live two houses apart.
5. The person in the blue house is the Spaniard.
6. Whoever lives in the red house lives in a lower-numbered house than the person in the white house.
7. Whoever lives in the red house enjoys chess.
8. The Norwegian lives next to the teacher.
9. The Brit enjoys golf.
10. The hiking enthusiast lives in the middle house.
11. The person in the green house and the occupant of the purple house live two houses apart.
12. The farmer and the person who enjoys hiking are neighbours.
13. The person in the red house works as the doctor.
14. The German lives next to the hiking enthusiast.

## Puzzle paraphrase:zebra-00156

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, water, juice, coffee
- color: purple, red, yellow, green, blue
- hobby: golf, hiking, cooking, chess, tennis
- pet: fish, bird, dog, horse, rabbit

Clues:
1. The green house is directly to the left of the golfer.
2. The juice drinker lives right next to the yellow house.
3. The fish keeper lives immediately to the left of the juice drinker.
4. The yellow house is directly to the right of the bird keeper.
5. Cooking is the hobby of the rabbit keeper.
6. One house lies between the chess player and the coffee drinker.
7. The purple house lies somewhere to the right of the hiker.
8. The cocoa drinker lives directly to the left of the tea drinker.
9. Exactly one house separates the hiker from the red house.
10. The dog owner lives in the fourth house.
11. The rabbit owner lives immediately to the right of the yellow house.
12. The yellow house's occupant drinks either juice or tea.

## Puzzle plain:zebra-00084

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: red, purple, yellow, white, blue
- pet: bird, cat, rabbit, dog, horse
- drink: coffee, juice, milk, cocoa, water
- nationality: Swede, Brit, Dane, German, Spaniard

Clues:
1. The bird owner lives in the fifth house.
2. The cat owner lives in the house just left of the one where the Spaniard lives.
3. The water drinker lives immediately to the right of the dog owner.
4. The dog owner drinks cocoa.
5. The person who drinks milk lives in the red house.
6. The Dane lives in house 2.
7. The juice drinker lives in the house just left of the one where the person in the yellow house lives.
8. The owner of the dog lives next to whoever lives in the yellow house.
9. The person in the yellow house lives in the house just left of the one where the person in the blue house lives.
10. The coffee drinker lives somewhere to the left of the occupant of the purple house.
11. The owner of the bird lives next to the Swede.
12. The owner of the cat does not live next to the milk drinker.
13. The occupant of the yellow house lives immediately to the right of the rabbit owner.
14. The German lives in house 1.

## Puzzle paraphrase:zebra-00157

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, painting, golf, tennis, cooking
- nationality: Spaniard, Norwegian, Dane, Swede, Brit
- color: red, green, blue, white, purple
- pet: bird, rabbit, cat, dog, fish

Clues:
1. The painter lives directly to the right of the red house.
2. The Dane and the white house are in adjacent houses.
3. The fish keeper lives right next to the white house.
4. The fish keeper lives somewhere to the right of the Dane.
5. The rabbit owner and the Swede are not next-door neighbours.
6. The red house's occupant has either painting or tennis as a hobby.
7. The dog owner is either the Brit or the Spaniard.
8. The hiker does not live in the blue house.
9. The Swede is the golfer.
10. The green house and the white house are neighbours.
11. The Brit lives in house 5.
12. The purple house is where the rabbit is kept.
13. The painter lives somewhere to the left of the rabbit owner.
14. The bird owner lives immediately to the left of the rabbit owner.
