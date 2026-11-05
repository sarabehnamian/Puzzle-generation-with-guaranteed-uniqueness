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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_020.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00029

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, horse, rabbit, bird, cat
- drink: tea, water, coffee, milk, cocoa
- color: purple, white, green, blue, red
- job: lawyer, farmer, pilot, doctor, teacher

Clues:
1. The cocoa drinker lives in house 1.
2. Whoever lives in the purple house keeps the cat.
3. The farmer lives in the blue house.
4. The lawyer lives in the house just left of the one where the horse owner lives.
5. The person in the blue house and the owner of the fish live two houses apart.
6. The pilot either lives in the blue house or lives in the red house.
7. The person who keeps the horse lives immediately to the right of the person in the white house.
8. The person in the purple house lives directly to the left of the person who drinks milk.
9. The person who keeps the horse and the person who drinks tea are neighbours.
10. The tea drinker lives somewhere to the left of the doctor.
11. The owner of the rabbit either lives in the purple house or lives in the white house.
12. The lawyer lives in house 3.
13. The person in the blue house and the person who drinks water are neighbours.

## Puzzle plain:zebra-00004

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Brit, German, Swede, Norwegian
- color: purple, green, yellow, blue, white
- pet: rabbit, horse, bird, fish, dog
- job: baker, doctor, teacher, farmer, lawyer

Clues:
1. The farmer is the Brit.
2. The person in the purple house lives directly to the left of the owner of the rabbit.
3. The German lives in the house just left of the one where the dog owner lives.
4. Whoever lives in the yellow house either keeps the fish or keeps the horse.
5. Whoever lives in the green house lives in the fourth house.
6. The person in the blue house and the person who keeps the dog live two houses apart.
7. The baker does not live next to the German.
8. The person who keeps the dog works as the farmer.
9. The fish owner lives in the leftmost house.
10. The Norwegian and the Spaniard are neighbours.
11. The Norwegian does not live next to the person in the yellow house.
12. Whoever lives in the purple house works as the lawyer.
13. The teacher lives in the yellow house.
14. The horse owner lives directly to the left of the person in the green house.

## Puzzle paraphrase:zebra-00104

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, coffee, tea, water, milk
- nationality: Swede, Spaniard, Dane, Norwegian, German
- hobby: chess, painting, golf, tennis, cooking
- color: blue, red, yellow, white, purple

Clues:
1. The red house's occupant and the Spaniard live in adjacent houses.
2. The milk drinker and the white house's occupant live two houses apart.
3. The Norwegian lives directly to the right of the Spaniard.
4. The cooking enthusiast lives next door to the German.
5. The German lives immediately to the left of the coffee drinker.
6. The coffee drinker doesn't live next to the water drinker.
7. The coffee drinker and the golf enthusiast are not neighbours.
8. The Norwegian lives in house 5.
9. The milk drinker's hobby is either chess or cooking.
10. The Dane lives immediately to the left of the blue house's occupant.
11. The cocoa drinker lives in the leftmost house.
12. The yellow house's occupant enjoys painting.
13. The painting enthusiast lives directly to the left of the water drinker.
14. The red house's occupant drinks water.

## Puzzle plain:zebra-00064

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Norwegian, Brit, Spaniard, Dane
- job: lawyer, baker, farmer, doctor, pilot
- color: green, purple, yellow, white, blue
- drink: coffee, cocoa, juice, milk, water

Clues:
1. The Dane and the milk drinker live in adjacent houses.
2. The occupant of the yellow house either is the Brit or is the Norwegian.
3. The occupant of the blue house and the farmer live two houses apart.
4. There is exactly one house between whoever lives in the purple house and the person who drinks water.
5. The person who drinks cocoa and the milk drinker live in adjacent houses.
6. The doctor drinks juice.
7. The Spaniard lives in house 4.
8. The baker is the German.
9. The baker and the Dane live two houses apart.
10. The person who drinks juice and the Norwegian live in adjacent houses.
11. The pilot lives in a lower-numbered house than the farmer.
12. The juice drinker lives somewhere to the right of the person in the green house.
13. The farmer and the pilot live two houses apart.
14. The Dane lives in the house just left of the one where the person who drinks coffee lives.

## Puzzle plain:zebra-00088

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, baker, pilot, farmer
- pet: horse, bird, cat, fish, dog
- hobby: hiking, painting, cooking, chess, golf
- color: green, blue, yellow, red, purple

Clues:
1. The baker lives somewhere to the right of the teacher.
2. The person who keeps the cat lives in the red house.
3. The person who keeps the dog lives in house 4.
4. The pilot lives in the middle house.
5. The person who enjoys chess and whoever lives in the red house live two houses apart.
6. There is exactly one house between the hiking enthusiast and the painting enthusiast.
7. Whoever lives in the blue house enjoys hiking.
8. The occupant of the red house works as the farmer.
9. The owner of the cat enjoys golf.
10. The doctor lives in the fourth house.
11. The occupant of the yellow house lives in house 1.
12. The pilot lives in the purple house.
13. The person who enjoys golf lives somewhere to the left of the person who keeps the fish.
14. The occupant of the purple house keeps the horse.

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

## Puzzle hard:zebra_hard-00010

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, Brit, German, Swede, Spaniard
- hobby: golf, painting, cooking, tennis, chess
- drink: juice, water, coffee, tea, cocoa
- job: doctor, baker, farmer, teacher, lawyer

Clues:
1. The baker lives somewhere between the doctor and the German.
2. At least one house separates the farmer from the teacher.
3. The person who enjoys painting and the teacher are one and the same person.
4. The baker and the person who enjoys tennis are one and the same person.
5. The left-hand neighbour of the Swede is the Spaniard.
6. The person who enjoys cooking lives further to the right than the farmer.
7. One of the neighbours of the water drinker drinks coffee.
8. The person who enjoys cooking and the lawyer are one and the same person.
9. The coffee drinker and the golf enthusiast are one and the same person.
10. The teacher lives somewhere between the Brit and the person who enjoys chess.
11. The person who drinks cocoa and the Swede are one and the same person.
12. The water drinker lives somewhere between the farmer and the lawyer.
13. The baker and the juice drinker are one and the same person.

## Puzzle hard:zebra_hard-00006

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Norwegian, Dane, Swede, Brit
- color: red, white, blue, green, purple
- drink: coffee, water, juice, cocoa, tea
- job: baker, pilot, doctor, farmer, lawyer

Clues:
1. The occupant of the green house and the lawyer are one and the same person.
2. The person who drinks coffee lives somewhere between the German and the juice drinker.
3. The left-hand neighbour of the pilot is the Norwegian.
4. The person in the purple house lives in the third house from the right.
5. The occupant of the green house lives somewhere between the person who drinks cocoa and the German.
6. The person in the blue house and the farmer are one and the same person.
7. Whoever lives in the blue house lives further to the right than the Norwegian.
8. The pilot lives somewhere between the doctor and the farmer.
9. The cocoa drinker and the Swede are one and the same person.
10. The right-hand neighbour of the person who drinks cocoa drinks tea.
11. The right-hand neighbour of the person who drinks juice is the Dane.
12. Exactly one house separates the person in the red house from the Swede.

## Puzzle plain:zebra-00046

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Dane, Norwegian, Spaniard, Swede
- color: yellow, blue, green, purple, white
- drink: milk, tea, water, cocoa, coffee
- hobby: golf, tennis, hiking, chess, painting

Clues:
1. The German and the person who enjoys painting are neighbours.
2. The Norwegian either enjoys painting or enjoys tennis.
3. The Dane either lives in the blue house or lives in the white house.
4. The Norwegian lives in the white house.
5. The person in the yellow house lives in a lower-numbered house than whoever lives in the white house.
6. Whoever lives in the green house lives next to the milk drinker.
7. The Spaniard lives in the yellow house.
8. The person who enjoys golf lives in the house just left of the one where the hiking enthusiast lives.
9. The tennis enthusiast lives in a lower-numbered house than the person who drinks milk.
10. The person who enjoys golf is the Swede.
11. The tennis enthusiast drinks coffee.
12. The water drinker lives at one end of the row.
13. The person who drinks cocoa lives immediately to the right of the person who enjoys tennis.
14. The occupant of the purple house lives somewhere to the right of the golf enthusiast.
15. The Dane and the person in the white house live two houses apart.

## Puzzle plain:zebra-00007

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, German, Swede, Norwegian
- color: blue, purple, red, white, yellow
- drink: milk, cocoa, juice, coffee, tea
- pet: dog, fish, cat, bird, horse

Clues:
1. The owner of the cat lives in the house just left of the one where the Dane lives.
2. The Norwegian lives in the blue house.
3. The owner of the cat lives directly to the left of the person who keeps the dog.
4. The occupant of the white house either is the Brit or is the Dane.
5. The person who drinks coffee lives in the house just left of the one where the occupant of the blue house lives.
6. The Swede either keeps the bird or keeps the dog.
7. The occupant of the purple house lives directly to the left of the Brit.
8. The person who drinks milk lives in the leftmost house.
9. The person who drinks tea either lives in the blue house or lives in the red house.
10. The milk drinker and the Swede live in adjacent houses.
11. The Brit and the person who drinks coffee live in adjacent houses.
12. The cocoa drinker and the Dane are not neighbours.
13. The owner of the fish lives next to the person in the red house.
