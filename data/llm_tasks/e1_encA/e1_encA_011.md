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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encA/e1_encA_011.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00023

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, cat, horse, rabbit, bird
- color: yellow, purple, white, red, blue
- hobby: tennis, chess, cooking, golf, hiking
- nationality: Dane, Norwegian, Brit, Spaniard, Swede

Clues:
1. The Swede enjoys golf.
2. The Dane lives somewhere to the left of the person who keeps the cat.
3. The person in the yellow house lives in the fourth house.
4. The hiking enthusiast does not live in the fourth house.
5. The owner of the rabbit lives somewhere to the right of the person in the purple house.
6. The dog owner lives directly to the left of the owner of the rabbit.
7. The hiking enthusiast lives somewhere to the left of the person in the red house.
8. The Spaniard lives in the house just left of the one where the occupant of the blue house lives.
9. The person who enjoys chess lives in the second house.
10. The Spaniard lives at one end of the row.
11. The hiking enthusiast lives directly to the left of the Brit.
12. The Dane lives next to the occupant of the purple house.
13. The horse owner and the person in the red house live in adjacent houses.
14. The person who enjoys cooking lives directly to the left of the person who keeps the dog.

## Puzzle paraphrase:zebra-00106

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, painting, golf, tennis, chess
- color: yellow, red, green, blue, purple
- job: pilot, doctor, baker, lawyer, teacher
- nationality: Dane, Norwegian, German, Spaniard, Swede

Clues:
1. The Spaniard's home is the second house.
2. The cooking enthusiast is either the lawyer or the pilot.
3. The Swede lives immediately to the right of the green house's occupant.
4. The golf enthusiast and the pilot have exactly one house between them.
5. The doctor lives immediately to the right of the Norwegian.
6. The lawyer lives immediately to the left of the tennis enthusiast.
7. The teacher lives in house 2.
8. The Dane lives immediately to the left of the red house's occupant.
9. The golf enthusiast lives in the purple house.
10. The chess enthusiast lives in the blue house.
11. The Norwegian lives somewhere to the left of the yellow house's occupant.
12. The tennis enthusiast lives in the fourth house.

## Puzzle paraphrase:zebra-00161

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, cocoa, milk, water, coffee
- job: lawyer, teacher, doctor, farmer, baker
- pet: bird, cat, dog, fish, horse
- hobby: golf, tennis, painting, cooking, hiking

Clues:
1. House 1 is home to the cocoa drinker.
2. The tea drinker's house is right beside the teacher's.
3. The farmer and the cocoa drinker are next-door neighbours.
4. The bird belongs to the hiker.
5. The coffee drinker has either the dog or the fish.
6. The bird's owner lives next door to the fish's owner.
7. The lawyer lives somewhere further right than the painting enthusiast.
8. The farmer is the one who owns the horse.
9. The cat owner lives in the centre house.
10. The milk drinker is not the horse owner.
11. The golfer lives somewhere to the left of the milk drinker.
12. The baker's hobby is painting.
13. The cooking enthusiast lives right beside the dog owner.
14. The tea drinker lives in one of the two end houses.

## Puzzle paraphrase:zebra-00179

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: German, Dane, Swede, Spaniard, Brit
- color: yellow, blue, red, green, white
- drink: cocoa, tea, coffee, water, juice
- job: lawyer, doctor, baker, pilot, farmer

Clues:
1. The German does not live next door to the water drinker.
2. The tea drinker lives immediately to the left of the red house's occupant.
3. The Dane occupies the first house.
4. The baker lives at one of the two ends of the row.
5. The farmer is a neighbour of the German.
6. The lawyer is the tea drinker.
7. The green house's occupant and the juice drinker are two houses apart.
8. The pilot is the one in the blue house.
9. The red house and the yellow house have exactly one house between them.
10. The Brit is the farmer.
11. The Spaniard lives immediately to the right of the white house's occupant.
12. The Brit lives at one end of the row.
13. The Brit lives somewhere to the right of the cocoa drinker.
14. The occupant of the red house drinks coffee.

## Puzzle plain:zebra-00093

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, lawyer, baker, teacher, farmer
- nationality: Spaniard, Brit, German, Swede, Norwegian
- color: white, blue, yellow, purple, green
- drink: coffee, water, tea, cocoa, milk

Clues:
1. The Swede lives in a lower-numbered house than the Norwegian.
2. The water drinker is the Norwegian.
3. The person in the green house lives next to the teacher.
4. The German lives next to the Swede.
5. The Swede either works as the doctor or works as the farmer.
6. There is exactly one house between the person who drinks coffee and whoever lives in the yellow house.
7. Whoever lives in the yellow house works as the doctor.
8. The baker lives next to the person in the blue house.
9. The baker and the milk drinker are neighbours.
10. There is exactly one house between the Spaniard and the Swede.
11. The person in the purple house works as the baker.
12. There is exactly one house between the baker and the tea drinker.
13. There is exactly one house between whoever lives in the purple house and the Spaniard.

## Puzzle paraphrase:zebra-00105

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: dog, horse, rabbit, bird, cat
- job: lawyer, farmer, teacher, pilot, doctor
- drink: juice, tea, milk, water, coffee
- color: green, blue, white, red, purple

Clues:
1. The green house belongs to the lawyer.
2. House 4 is where the coffee drinker lives.
3. Somewhere to the right of the blue house's occupant lives the occupant of the red house.
4. The cat owner lives immediately to the right of the dog owner.
5. The bird owner and the doctor live in neighbouring houses.
6. The tea drinker lives immediately to the right of the rabbit owner.
7. The farmer lives in the red house.
8. The juice drinker lives immediately to the left of the purple house's occupant.
9. The coffee drinker and the doctor have exactly one house between them.
10. The coffee drinker and the pilot live next door to each other.
11. The horse is kept by the occupant of the blue house.
12. The water drinker lives immediately to the left of the lawyer.

## Puzzle hard:zebra_hard-00015

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, painting, hiking, chess, tennis
- nationality: Spaniard, Norwegian, Dane, Swede, Brit
- color: red, yellow, green, white, purple
- drink: juice, tea, coffee, milk, cocoa

Clues:
1. One of the neighbours of the Swede enjoys painting.
2. If the person who enjoys chess does not drink coffee, then that person drinks tea.
3. The person in the white house lives somewhere between the occupant of the purple house and the Spaniard.
4. The left-hand neighbour of the hiking enthusiast lives in the purple house.
5. The Dane lives somewhere between the person who drinks juice and whoever lives in the white house.
6. One of the neighbours of the occupant of the green house drinks milk.
7. None of the neighbours of the occupant of the yellow house drinks milk.
8. None of the neighbours of the juice drinker drinks tea.
9. The Swede is not the same person as the occupant of the white house.
10. The Brit and the tennis enthusiast are one and the same person.
11. The right-hand neighbour of whoever lives in the yellow house enjoys tennis.
12. One of the neighbours of the cocoa drinker is the Swede.
13. The person in the yellow house lives somewhere between the milk drinker and whoever lives in the purple house.

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

## Puzzle plain:zebra-00038

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: pilot, lawyer, farmer, baker, doctor
- nationality: Swede, Brit, Dane, German, Norwegian
- color: green, blue, purple, yellow, white
- drink: cocoa, tea, milk, juice, coffee

Clues:
1. The Norwegian lives in house 1.
2. The occupant of the purple house is the Dane.
3. The lawyer and the tea drinker live in adjacent houses.
4. Whoever lives in the purple house drinks milk.
5. The farmer lives in the first house.
6. The German lives next to the Swede.
7. The doctor drinks milk.
8. The occupant of the white house lives immediately to the right of the baker.
9. The coffee drinker lives in a lower-numbered house than whoever lives in the white house.
10. The tea drinker lives in house 2.
11. The cocoa drinker either is the Dane or is the German.
12. Whoever lives in the blue house drinks cocoa.
13. Whoever lives in the yellow house lives in the leftmost house.

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
