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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_003.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle hard:zebra_hard-00065

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, teacher, baker, doctor, lawyer
- hobby: hiking, cooking, painting, golf, chess
- nationality: Dane, Brit, Swede, German, Spaniard
- drink: coffee, juice, cocoa, tea, water

Clues:
1. The baker lives somewhere between the juice drinker and the teacher.
2. If the German does not enjoy cooking, then that person enjoys golf.
3. Neither the golf enthusiast nor the Spaniard works as the lawyer.
4. Exactly one house separates the baker from the Spaniard.
5. The baker and the person who enjoys golf are one and the same person.
6. The chess enthusiast lives in the fifth house from the right.
7. The right-hand neighbour of the person who enjoys painting drinks water.
8. The right-hand neighbour of the Brit is the German.
9. The left-hand neighbour of the coffee drinker enjoys golf.
10. Exactly 0 houses lie to the left of the home of the farmer.
11. The person who drinks coffee and the German are one and the same person.
12. The left-hand neighbour of the person who drinks cocoa is the Dane.
13. The left-hand neighbour of the juice drinker drinks tea.

## Puzzle paraphrase:zebra-00130

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, hiking, painting, cooking
- drink: water, tea, milk, coffee, cocoa
- pet: rabbit, fish, dog, cat, bird
- job: teacher, pilot, farmer, doctor, baker

Clues:
1. Whoever owns the dog drinks cocoa.
2. The doctor and the milk drinker live two houses apart.
3. The coffee drinker lives right next door to the left of the water drinker.
4. The doctor is not a neighbour of the teacher.
5. The baker and the milk drinker live in neighbouring houses.
6. The cat is kept in house 3.
7. The dog's owner is either the doctor or the teacher.
8. The rabbit owner lives directly to the right of the pilot.
9. The golf enthusiast occupies the leftmost house.
10. The chess enthusiast does not live in house 5.
11. The rabbit owner and the teacher live two houses apart.
12. The baker is not the owner of the bird.
13. The cocoa drinker and the painting enthusiast are two houses apart.
14. The cooking enthusiast lives immediately to the left of the water drinker.

## Puzzle hard:zebra_hard-00069

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Swede, Spaniard, Brit, German
- pet: horse, bird, rabbit, fish, cat
- hobby: golf, hiking, tennis, cooking, chess
- drink: milk, tea, coffee, cocoa, water

Clues:
1. The chess enthusiast lives somewhere between the person who enjoys cooking and the Spaniard.
2. The horse owner lives somewhere between the cooking enthusiast and the Swede.
3. If the Swede does not keep the bird, then that person keeps the fish.
4. The left-hand neighbour of the person who drinks milk drinks tea.
5. One of the neighbours of the person who enjoys tennis is the Norwegian.
6. The chess enthusiast lives two doors away from the milk drinker.
7. The person who enjoys golf and the Swede are one and the same person.
8. The left-hand neighbour of the person who enjoys cooking drinks water.
9. The left-hand neighbour of the cooking enthusiast is the Norwegian.
10. The rabbit owner has only one neighbour.
11. If the Brit does not drink milk, then that person drinks water.
12. The hiking enthusiast lives further to the right than the person who drinks coffee.
13. If the tea drinker does not keep the bird, then that person keeps the rabbit.
14. The person who enjoys hiking is not the same person as the person who keeps the rabbit.

## Puzzle plain:zebra-00074

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Swede, Dane, Brit, Norwegian
- color: purple, green, red, yellow, blue
- job: farmer, teacher, pilot, baker, lawyer
- pet: horse, rabbit, bird, fish, dog

Clues:
1. The pilot lives in the house just left of the one where the person who keeps the horse lives.
2. The owner of the dog and the Swede are not neighbours.
3. The Norwegian lives in one of the two end houses.
4. The farmer keeps the horse.
5. The Swede lives in house 5.
6. The person in the green house works as the baker.
7. Whoever lives in the yellow house keeps the bird.
8. The bird owner and the farmer are neighbours.
9. The Swede keeps the rabbit.
10. The Brit lives in the red house.
11. The pilot lives in the house just left of the one where the German lives.
12. The lawyer does not live next to the person who keeps the rabbit.
13. Whoever lives in the blue house lives in the house just left of the one where the German lives.

## Puzzle hard:zebra_hard-00074

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, pilot, lawyer, teacher, doctor
- pet: dog, fish, rabbit, cat, horse
- drink: coffee, milk, water, juice, tea
- nationality: Swede, Spaniard, Brit, Dane, German

Clues:
1. The lawyer and the water drinker are one and the same person.
2. The person who keeps the horse and the pilot are one and the same person.
3. The Brit and the farmer are one and the same person.
4. One of the neighbours of the teacher keeps the horse.
5. The lawyer and the Swede are one and the same person.
6. The right-hand neighbour of the person who keeps the dog keeps the rabbit.
7. One of the neighbours of the lawyer is the Spaniard.
8. One of the neighbours of the owner of the dog drinks coffee.
9. The person who keeps the cat and the coffee drinker are one and the same person.
10. One of the neighbours of the person who keeps the horse drinks coffee.
11. The farmer lives in the third house from the right.
12. The Dane and the person who drinks tea are one and the same person.
13. The pilot lives somewhere between the person who drinks juice and the person who keeps the rabbit.
14. The person who drinks milk does not live in the rightmost house.

## Puzzle plain:zebra-00071

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, purple, red, yellow, blue
- job: pilot, teacher, farmer, lawyer, baker
- nationality: Swede, Spaniard, Dane, Norwegian, German
- drink: water, cocoa, milk, juice, tea

Clues:
1. The Spaniard lives in the house just left of the one where the occupant of the red house lives.
2. Whoever lives in the white house drinks juice.
3. The person in the blue house lives somewhere to the right of the Dane.
4. The German lives in house 5.
5. The baker lives in the purple house.
6. The farmer lives directly to the left of the Spaniard.
7. The Spaniard lives in the middle house.
8. The person who drinks cocoa is the Swede.
9. The pilot and the Swede live in adjacent houses.
10. The person who drinks tea lives in the house just left of the one where the teacher lives.
11. The Dane either drinks cocoa or drinks milk.
12. The Norwegian lives in the house just left of the one where the baker lives.
13. The farmer either drinks cocoa or drinks juice.

## Puzzle hard:zebra_hard-00046

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, cat, rabbit, fish, horse
- drink: juice, water, tea, coffee, milk
- job: lawyer, farmer, teacher, pilot, baker
- hobby: cooking, tennis, hiking, chess, painting

Clues:
1. The person who keeps the bird has only one neighbour.
2. The lawyer and the owner of the rabbit are one and the same person.
3. The left-hand neighbour of the person who drinks tea works as the lawyer.
4. The right-hand neighbour of the pilot drinks coffee.
5. If the person who enjoys tennis does not drink coffee, then that person drinks water.
6. One of the neighbours of the chess enthusiast enjoys tennis.
7. The coffee drinker lives in the third house from the right.
8. The person who keeps the cat lives somewhere between the person who enjoys chess and the hiking enthusiast.
9. The person who drinks juice and the painting enthusiast are one and the same person.
10. Neither the owner of the bird nor the person who drinks milk works as the baker.
11. If the person who keeps the fish does not enjoy chess, then that person enjoys cooking.
12. The tennis enthusiast lives somewhere between the milk drinker and the teacher.
13. One of the neighbours of the painting enthusiast works as the farmer.
14. The person who enjoys hiking lives two doors away from the pilot.

## Puzzle paraphrase:zebra-00194

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, farmer, baker, teacher, lawyer
- pet: horse, dog, cat, bird, rabbit
- nationality: Dane, German, Norwegian, Brit, Swede
- color: green, white, red, blue, yellow

Clues:
1. The farmer lives in one of the two end houses.
2. The lawyer is the horse keeper.
3. The yellow house stands immediately to the left of the cat owner's house.
4. The bird keeper and the lawyer live next door to each other.
5. The baker and the Swede have exactly one house between them.
6. The Swede lives in either the blue house or the green house.
7. The horse owner lives in either the blue house or the white house.
8. The occupant of the red house is either the lawyer or the teacher.
9. The baker lives next door to the Brit.
10. The German lives in the leftmost house.
11. The Norwegian keeps the rabbit.
12. The Dane lives next door to the teacher.
13. The red house's occupant keeps the dog.
14. The green house and the red house are not next to each other.

## Puzzle hard:zebra_hard-00047

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, painting, chess, golf, hiking
- color: white, red, purple, blue, yellow
- nationality: Brit, German, Spaniard, Dane, Norwegian
- pet: horse, bird, rabbit, dog, cat

Clues:
1. Exactly one house separates the person who enjoys painting from the Spaniard.
2. The left-hand neighbour of the owner of the horse enjoys painting.
3. Exactly 4 houses lie to the left of the home of the owner of the cat.
4. The person in the red house lives somewhere between the person who enjoys hiking and the horse owner.
5. If the tennis enthusiast does not live in the purple house, then that person lives in the yellow house.
6. The Norwegian and the person in the white house are one and the same person.
7. The person who enjoys chess and the Norwegian are one and the same person.
8. The left-hand neighbour of the Dane keeps the rabbit.
9. The German and the occupant of the purple house are one and the same person.
10. Exactly one house separates the painting enthusiast from the owner of the rabbit.
11. The Norwegian lives two doors away from the person in the yellow house.
12. Neither the occupant of the blue house nor the Brit keeps the dog.
13. The Brit lives in the fourth house from the right.
14. The right-hand neighbour of the person in the red house is the Norwegian.

## Puzzle plain:zebra-00039

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, juice, water, coffee, tea
- nationality: German, Spaniard, Brit, Norwegian, Dane
- job: lawyer, baker, pilot, teacher, doctor
- color: yellow, red, blue, white, green

Clues:
1. The juice drinker either is the German or is the Spaniard.
2. The cocoa drinker is the Brit.
3. The occupant of the red house lives at one end of the row.
4. The occupant of the white house lives in the house just left of the one where the doctor lives.
5. The teacher and the person who drinks water are neighbours.
6. The Norwegian drinks tea.
7. The Brit and whoever lives in the red house live two houses apart.
8. The lawyer lives in the white house.
9. The person in the red house is not the baker.
10. There is exactly one house between the Brit and the Dane.
11. The Spaniard lives in the blue house.
12. The teacher drinks juice.
13. The Dane lives in a lower-numbered house than the Norwegian.
14. The person in the green house and the person who drinks juice are not neighbours.
15. The German either lives in the blue house or lives in the white house.
