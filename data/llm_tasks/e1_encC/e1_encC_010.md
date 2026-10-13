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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_010.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle hard:zebra_hard-00035

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, juice, cocoa, water, coffee
- job: teacher, lawyer, baker, farmer, doctor
- nationality: Dane, Swede, Brit, German, Spaniard
- hobby: chess, golf, cooking, hiking, painting

Clues:
1. One of the neighbours of the painting enthusiast enjoys hiking.
2. If the lawyer does not drink cocoa, then that person drinks coffee.
3. Exactly 3 houses lie to the left of the home of the teacher.
4. The right-hand neighbour of the person who drinks cocoa is the Brit.
5. The Dane has only one neighbour.
6. If the German is not the doctor, then that person works as the farmer.
7. The right-hand neighbour of the doctor enjoys cooking.
8. The person who enjoys hiking has only one neighbour.
9. Exactly 1 house lies to the left of the home of the person who drinks water.
10. One of the neighbours of the Spaniard works as the teacher.
11. The chess enthusiast and the Spaniard are one and the same person.
12. The doctor lives somewhere between the Brit and the farmer.
13. The left-hand neighbour of the doctor drinks milk.
14. The Brit is not the same person as the juice drinker.

## Puzzle paraphrase:zebra-00112

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, tennis, golf, hiking, chess
- pet: dog, bird, rabbit, cat, horse
- job: farmer, doctor, teacher, pilot, baker
- drink: coffee, milk, tea, juice, water

Clues:
1. House 4 belongs to the milk drinker.
2. The chess enthusiast is not in house 1.
3. The cat keeper lives somewhere to the right of the baker.
4. The milk drinker is the farmer.
5. The baker and the juice drinker live next door to each other.
6. The pilot is the one who keeps the cat.
7. The dog owner does not live next to the water drinker.
8. The water drinker lives immediately to the right of the golf enthusiast.
9. The painting enthusiast keeps the horse.
10. The coffee drinker lives right beside the painting enthusiast.
11. The horse is kept in the third house.
12. The bird owner lives directly to the left of the teacher.
13. The chess enthusiast and the water drinker have exactly one house between them.
14. The hiking enthusiast lives in a house numbered lower than the tennis enthusiast's.

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

## Puzzle hard:zebra_hard-00063

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, coffee, juice, cocoa
- pet: fish, rabbit, dog, bird, horse
- hobby: chess, tennis, cooking, hiking, golf
- color: red, blue, green, purple, white

Clues:
1. Whoever lives in the white house lives somewhere between the bird owner and the occupant of the purple house.
2. Exactly one house separates the person who keeps the bird from the juice drinker.
3. If the person in the purple house does not keep the bird, then that person keeps the dog.
4. Exactly 3 houses lie to the left of the home of the milk drinker.
5. The cocoa drinker is not the same person as the cooking enthusiast.
6. None of the neighbours of the fish owner drinks juice.
7. The person in the green house lives two doors away from whoever lives in the white house.
8. The person who keeps the bird lives somewhere between the coffee drinker and the juice drinker.
9. The occupant of the white house lives somewhere between the person who drinks cocoa and the golf enthusiast.
10. Exactly 3 houses lie to the left of the home of the tennis enthusiast.
11. The person who enjoys chess lives in the fourth house from the right.
12. One of the neighbours of the person who drinks water lives in the red house.
13. The left-hand neighbour of the owner of the fish lives in the purple house.
14. One of the neighbours of the owner of the horse lives in the green house.

## Puzzle paraphrase:zebra-00173

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, farmer, baker, lawyer, teacher
- pet: rabbit, bird, fish, cat, horse
- drink: cocoa, coffee, tea, water, milk
- nationality: Swede, Spaniard, Norwegian, German, Brit

Clues:
1. The Swede does not occupy house 5.
2. The coffee drinker lives immediately to the right of the German.
3. The doctor and the tea drinker are two houses apart.
4. The farmer and the Spaniard are not the same person.
5. The horse belongs to the Spaniard.
6. The Brit is the doctor.
7. The Norwegian lives immediately to the right of the teacher.
8. The cocoa drinker is the lawyer.
9. The cat owner does not live next door to the fish owner.
10. The water drinker lives immediately to the right of the Norwegian.
11. The bird owner and the cat owner have exactly one house between them.
12. The Norwegian owns the rabbit.
13. The tea drinker lives in house 5.

## Puzzle paraphrase:zebra-00183

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, cooking, painting, golf, chess
- color: green, blue, white, red, yellow
- job: farmer, pilot, baker, teacher, lawyer
- pet: dog, rabbit, bird, horse, cat

Clues:
1. The dog owner is not the pilot.
2. The red house's occupant has either the bird or the rabbit.
3. The rabbit belongs to the occupant of the blue house.
4. The golf enthusiast is not the teacher.
5. The cooking enthusiast and the pilot live in neighbouring houses.
6. The green house is home to the cat.
7. The golf enthusiast lives in either the red house or the white house.
8. The lawyer and the teacher have exactly one house between them.
9. The white house lies somewhere to the left of the horse owner.
10. The bird's owner lives somewhere to the right of the teacher.
11. The horse owner and the tennis enthusiast live two houses apart.
12. The yellow house is one of the two end houses.
13. The red house is immediately to the left of the painting enthusiast.
14. The farmer and the painting enthusiast are next-door neighbours.
15. One house separates the green house from the painting enthusiast.
16. The teacher lives somewhere to the left of the cat owner.
17. The cooking enthusiast lives in one of the two end houses.

## Puzzle paraphrase:zebra-00100

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, dog, horse, cat, fish
- drink: tea, water, juice, coffee, milk
- hobby: chess, tennis, painting, cooking, hiking
- job: lawyer, pilot, doctor, baker, farmer

Clues:
1. The doctor and the farmer live next door to each other.
2. Milk is drunk by whoever lives in house 3.
3. Somewhere further left along the row than the chess enthusiast lives the cat owner.
4. The juice drinker's house sits immediately to the left of the cooking enthusiast's house.
5. The coffee drinker and the farmer have exactly one house between them.
6. The cooking enthusiast is the immediate left-hand neighbour of the horse keeper.
7. The doctor's house has a smaller number than the lawyer's.
8. Immediately to the left of the tennis enthusiast lives the dog owner.
9. The fish owner and the tea drinker are next-door neighbours.
10. Two houses separate the cooking enthusiast from the hiking enthusiast in position (they live two houses apart).
11. The doctor and the lawyer live two houses apart.
12. The baker's home is house 2.
13. Whoever owns the bird enjoys hiking.

## Puzzle plain:zebra-00006

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, dog, cat, rabbit, fish
- color: purple, green, yellow, blue, white
- drink: coffee, milk, water, juice, tea
- hobby: chess, hiking, tennis, painting, cooking

Clues:
1. The juice drinker lives in the purple house.
2. There is exactly one house between the fish owner and the person in the green house.
3. The rabbit owner lives in the white house.
4. The person who drinks coffee lives in the blue house.
5. The person who enjoys tennis lives directly to the left of the person who drinks milk.
6. The person who enjoys painting lives in the house just left of the one where the person who enjoys hiking lives.
7. The person who keeps the horse and the person in the white house live two houses apart.
8. Whoever lives in the white house drinks milk.
9. The person in the blue house and whoever lives in the purple house live two houses apart.
10. The painting enthusiast lives next to the tea drinker.
11. The person who enjoys hiking lives somewhere to the right of the person in the white house.
12. The person who drinks juice keeps the cat.
13. The painting enthusiast lives somewhere to the left of the person who keeps the dog.
14. The person who enjoys cooking and the hiking enthusiast are neighbours.

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
4. The farmer does not drink water.
5. The Spaniard is the tea drinker.
6. The painting enthusiast drinks milk.
7. Golf is the teacher's hobby.
8. The German lives in house 5.
9. The hiking enthusiast lives next door to the milk drinker.
10. The doctor is not the milk drinker.
11. The water drinker lives in house 2.
12. The doctor lives somewhere to the right of the tennis enthusiast.
13. The farmer lives immediately left of the doctor.
14. The juice drinker lives immediately left of the baker.
