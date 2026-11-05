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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_012.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00054

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, milk, water, tea, cocoa
- nationality: Spaniard, Dane, Norwegian, Swede, German
- pet: fish, cat, dog, horse, bird
- hobby: cooking, hiking, chess, painting, golf

Clues:
1. The Swede lives directly to the left of the water drinker.
2. The cat owner lives in the middle house.
3. The horse owner lives in the house just left of the one where the cocoa drinker lives.
4. The cocoa drinker lives directly to the left of the Norwegian.
5. The person who enjoys golf drinks tea.
6. There is exactly one house between the person who drinks coffee and the person who enjoys hiking.
7. The cocoa drinker keeps the bird.
8. The person who enjoys chess keeps the fish.
9. The hiking enthusiast lives in the house just left of the one where the person who drinks milk lives.
10. The fish owner and the Spaniard live two houses apart.
11. The owner of the fish lives directly to the left of the painting enthusiast.
12. The German lives in the last house.

## Puzzle paraphrase:zebra-00141

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, tennis, golf, hiking, chess
- pet: horse, dog, bird, fish, cat
- job: teacher, farmer, lawyer, pilot, doctor
- drink: milk, tea, cocoa, juice, water

Clues:
1. Exactly one house separates the doctor from the lawyer.
2. The cat owner and the tea drinker live next door to each other.
3. The water drinker lives immediately left of the farmer.
4. The bird owner and the tennis enthusiast are neighbours.
5. The dog owner and the hiking enthusiast live in adjacent houses.
6. The juice drinker lives directly right of the horse owner.
7. The tea drinker lives in a lower-numbered house than the cocoa drinker.
8. The golf enthusiast lives directly right of the doctor.
9. The cooking enthusiast lives directly right of the pilot.
10. The water drinker's hobby is either chess or hiking.
11. The bird owner lives in one of the two end houses.
12. The chess enthusiast and the milk drinker are next-door neighbours.
13. The horse owner lives immediately left of the farmer.

## Puzzle hard:zebra_hard-00021

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, hiking, cooking, chess, tennis
- pet: fish, bird, cat, dog, horse
- drink: juice, water, tea, milk, coffee
- color: white, yellow, purple, blue, green

Clues:
1. The hiking enthusiast does not live in the rightmost house.
2. The person who enjoys golf and the horse owner are one and the same person.
3. The person who drinks tea and the person in the yellow house are one and the same person.
4. The cooking enthusiast and the tea drinker are one and the same person.
5. The owner of the dog lives in the fifth house from the right.
6. The chess enthusiast and the dog owner are one and the same person.
7. The person who enjoys chess lives two doors away from the golf enthusiast.
8. The owner of the bird does not live in the rightmost house.
9. If the person who drinks juice does not live in the blue house, then that person lives in the green house.
10. The person in the blue house has only one neighbour.
11. If the fish owner does not enjoy cooking, then that person enjoys tennis.
12. The right-hand neighbour of the person in the purple house lives in the yellow house.
13. The person who enjoys tennis and the water drinker are one and the same person.
14. Whoever lives in the blue house is not the same person as the fish owner.
15. The chess enthusiast and the coffee drinker are one and the same person.
16. The right-hand neighbour of the person who enjoys golf lives in the green house.

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

## Puzzle plain:zebra-00036

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Norwegian, Spaniard, Brit, German
- drink: milk, juice, cocoa, water, tea
- pet: dog, fish, bird, cat, horse
- hobby: chess, hiking, golf, painting, cooking

Clues:
1. The Brit and the chess enthusiast are different people.
2. The person who keeps the bird lives in the leftmost house.
3. The person who enjoys golf either is the Brit or is the German.
4. The painting enthusiast and the Spaniard live in adjacent houses.
5. The owner of the horse lives in the middle house.
6. The chess enthusiast lives somewhere to the left of the German.
7. The person who drinks milk lives in the second house.
8. The German lives in the third house.
9. The painting enthusiast drinks cocoa.
10. The Spaniard lives somewhere to the right of the fish owner.
11. The Brit and the person who enjoys hiking are not neighbours.
12. The owner of the horse either drinks cocoa or drinks water.
13. The person who enjoys hiking lives in one of the two end houses.
14. The cooking enthusiast lives immediately to the right of the person who drinks juice.
15. The Swede keeps the cat.

## Puzzle paraphrase:zebra-00164

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, painting, chess, golf, tennis
- drink: coffee, milk, water, cocoa, tea
- nationality: Norwegian, Spaniard, Swede, Dane, Brit
- color: blue, purple, red, white, yellow

Clues:
1. The painter lives in the blue house.
2. Exactly one house lies between the milk drinker and the Norwegian.
3. The blue house's occupant and the water drinker live next door to each other.
4. The purple house's occupant drinks tea.
5. The hiker lives in a lower-numbered house than the Dane.
6. The Swede lives somewhere to the left of the red house.
7. The tennis enthusiast lives in house 4.
8. The Brit lives next door to the cocoa drinker.
9. The white house is the middle house.
10. The water drinker lives immediately to the left of the golfer.
11. The purple house's occupant lives next to the Swede.
12. The hiker lives immediately to the right of the Spaniard.

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

## Puzzle hard:zebra_hard-00072

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: rabbit, fish, bird, dog, cat
- nationality: Swede, German, Norwegian, Dane, Spaniard
- job: teacher, farmer, pilot, doctor, lawyer
- hobby: cooking, golf, tennis, hiking, painting

Clues:
1. The doctor and the hiking enthusiast are one and the same person.
2. The Dane and the pilot are one and the same person.
3. Neither the hiking enthusiast nor the person who enjoys painting keeps the dog.
4. One of the neighbours of the cat owner works as the doctor.
5. The left-hand neighbour of the Spaniard enjoys cooking.
6. One of the neighbours of the Norwegian is the Dane.
7. The fish owner lives further to the right than the hiking enthusiast.
8. The cat owner lives somewhere between the person who enjoys cooking and the lawyer.
9. The Norwegian lives somewhere between the painting enthusiast and the person who enjoys tennis.
10. The person who enjoys cooking lives two doors away from the person who enjoys golf.
11. The person who keeps the rabbit and the person who enjoys tennis are one and the same person.
12. The farmer lives two doors away from the Swede.

## Puzzle paraphrase:zebra-00162

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, white, yellow, red, green
- hobby: hiking, cooking, painting, golf, tennis
- pet: horse, dog, bird, cat, rabbit
- drink: juice, cocoa, milk, water, coffee

Clues:
1. The hiker and the juice drinker live in adjacent houses.
2. The tennis enthusiast lives immediately to the right of the green house's occupant.
3. The white house is the last house.
4. The hiker lives in the purple house.
5. The hiker lives immediately to the right of the cooking enthusiast.
6. The rabbit owner lives in the white house.
7. The dog owner and the juice drinker are next-door neighbours.
8. The green house's occupant and the water drinker are neighbours.
9. The occupant of the green house lives next to the milk drinker.
10. The hiker keeps either the bird or the cat.
11. The tennis enthusiast lives immediately to the right of the cat owner.
12. The golfer lives in house 5.
13. The milk drinker lives in a lower-numbered house than the water drinker.
14. The cocoa drinker lives next door to the hiker.
15. Exactly one house separates the green house from the yellow house.
