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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_011.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00007

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, cat, dog, fish, horse
- nationality: Norwegian, Spaniard, Brit, Swede, Dane
- hobby: golf, tennis, cooking, painting, hiking
- drink: milk, juice, coffee, tea, cocoa

Clues:
1. One of the neighbours of the person who enjoys hiking is the Swede.
2. The left-hand neighbour of the Dane keeps the dog.
3. The right-hand neighbour of the owner of the cat drinks coffee.
4. At least one house separates the dog owner from the person who enjoys cooking.
5. One of the neighbours of the coffee drinker keeps the dog.
6. The fish owner and the tennis enthusiast are one and the same person.
7. The cocoa drinker and the person who enjoys painting are one and the same person.
8. Neither the person who keeps the cat nor the tennis enthusiast drinks milk.
9. The tea drinker lives further to the right than the person who keeps the cat.
10. At least one house separates the Spaniard from the Norwegian.
11. One of the neighbours of the Spaniard keeps the dog.
12. The person who drinks milk and the Swede are one and the same person.
13. The cooking enthusiast and the person who drinks tea are one and the same person.
14. One of the neighbours of the horse owner is the Norwegian.

## Puzzle hard:zebra_hard-00008

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, baker, teacher, doctor, pilot
- pet: bird, fish, horse, cat, rabbit
- drink: cocoa, coffee, juice, tea, water
- color: red, yellow, purple, white, blue

Clues:
1. At least one house separates the teacher from the fish owner.
2. The person who drinks cocoa lives further to the right than the rabbit owner.
3. The doctor and the juice drinker are one and the same person.
4. The pilot lives somewhere between the owner of the rabbit and the occupant of the white house.
5. The water drinker lives further to the right than the pilot.
6. If the person in the purple house does not keep the fish, then that person keeps the horse.
7. One of the neighbours of the bird owner lives in the red house.
8. The right-hand neighbour of the person who keeps the horse drinks tea.
9. One of the neighbours of the fish owner lives in the red house.
10. Whoever lives in the white house does not live to the right of the occupant of the blue house.
11. The right-hand neighbour of the fish owner drinks cocoa.
12. The baker and whoever lives in the white house are one and the same person.
13. The person in the white house lives two doors away from the person in the yellow house.

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

## Puzzle paraphrase:zebra-00126

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, tea, milk, water, coffee
- job: pilot, baker, teacher, lawyer, doctor
- nationality: Spaniard, Norwegian, Dane, German, Swede
- color: blue, white, green, yellow, red

Clues:
1. The yellow house is the first house.
2. The occupant of the blue house does not drink tea.
3. The cocoa drinker and the Norwegian do not live next door to each other.
4. The water drinker and the white house have exactly one house between them.
5. The blue house's occupant and the cocoa drinker are not the same person.
6. The doctor and the water drinker live two houses apart.
7. The blue house stands directly to the left of the Dane's house.
8. The red house is not next door to the teacher.
9. The lawyer and the Spaniard live two houses apart.
10. The pilot and the tea drinker live next door to each other.
11. One house separates the cocoa drinker from the Spaniard.
12. The German lives right beside the white house.
13. The green house stands directly to the left of the cocoa drinker's house.
14. The coffee drinker lives in the white house.

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

## Puzzle plain:zebra-00070

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, chess, golf, painting, hiking
- job: teacher, baker, doctor, farmer, lawyer
- pet: dog, fish, cat, bird, rabbit
- nationality: Spaniard, Norwegian, Dane, German, Swede

Clues:
1. The bird owner enjoys chess.
2. The doctor and the Norwegian are neighbours.
3. The German enjoys chess.
4. The person who enjoys golf and the Spaniard live two houses apart.
5. The lawyer lives next to the person who enjoys painting.
6. The cooking enthusiast is the Swede.
7. The Dane lives in the last house.
8. The person who keeps the fish lives in the second house.
9. The Dane and the lawyer live two houses apart.
10. There is exactly one house between the farmer and the Norwegian.
11. The painting enthusiast lives in a lower-numbered house than the Norwegian.
12. The owner of the dog and the teacher live two houses apart.
13. The person who keeps the cat does not live in the fourth house.

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
