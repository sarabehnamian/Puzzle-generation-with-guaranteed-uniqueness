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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encA\e1_encA_019.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle plain:zebra-00095

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, juice, milk, water, coffee
- pet: cat, bird, horse, rabbit, dog
- nationality: German, Swede, Dane, Norwegian, Brit
- hobby: chess, hiking, cooking, golf, painting

Clues:
1. The German and the person who drinks water live in adjacent houses.
2. The cat owner drinks water.
3. There is exactly one house between the Brit and the dog owner.
4. The cocoa drinker and the cooking enthusiast live in adjacent houses.
5. The owner of the cat and the juice drinker are neighbours.
6. The Dane either drinks coffee or drinks water.
7. The golf enthusiast and the Norwegian are neighbours.
8. The juice drinker enjoys painting.
9. The Brit does not live next to the hiking enthusiast.
10. The hiking enthusiast and the person who drinks juice are neighbours.
11. The owner of the bird lives immediately to the right of the rabbit owner.
12. The person who enjoys cooking lives directly to the left of the person who keeps the rabbit.
13. The person who keeps the cat and the person who keeps the rabbit are neighbours.
14. The Brit lives in the house just left of the one where the Dane lives.

## Puzzle plain:zebra-00091

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, water, juice, milk, tea
- nationality: Dane, Swede, Brit, German, Norwegian
- job: teacher, farmer, lawyer, pilot, doctor
- pet: rabbit, cat, fish, dog, horse

Clues:
1. The pilot lives in house 2.
2. The water drinker either works as the farmer or works as the lawyer.
3. The person who drinks juice lives immediately to the right of the tea drinker.
4. The person who keeps the fish is the German.
5. The Dane and the tea drinker are neighbours.
6. The farmer is the Brit.
7. The water drinker and the German are different people.
8. The Norwegian lives directly to the left of the milk drinker.
9. The owner of the horse lives in one of the two end houses.
10. The Brit lives somewhere to the right of the person who keeps the fish.
11. The owner of the rabbit either drinks tea or drinks water.
12. The water drinker lives directly to the left of the coffee drinker.
13. The Dane lives somewhere to the left of the person who keeps the dog.
14. The juice drinker works as the teacher.

## Puzzle hard:zebra_hard-00086

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: blue, green, white, red, purple
- drink: tea, water, juice, coffee, cocoa
- hobby: chess, tennis, painting, hiking, golf
- nationality: Norwegian, Swede, Dane, German, Brit

Clues:
1. One of the neighbours of the person who enjoys tennis lives in the blue house.
2. The left-hand neighbour of the cocoa drinker enjoys chess.
3. The hiking enthusiast lives somewhere between the cocoa drinker and the person who enjoys painting.
4. The juice drinker and the tennis enthusiast are one and the same person.
5. The right-hand neighbour of the Brit is the Dane.
6. At least one house separates whoever lives in the red house from the occupant of the blue house.
7. The coffee drinker has only one neighbour.
8. The occupant of the white house has only one neighbour.
9. The left-hand neighbour of the German enjoys painting.
10. The Dane lives in the rightmost house.
11. The person in the green house and the person who drinks water are one and the same person.
12. Neither the cocoa drinker nor the occupant of the green house is the Norwegian.
13. The cocoa drinker lives somewhere between the person who enjoys tennis and the person in the white house.

## Puzzle paraphrase:zebra-00181

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Brit, Dane, Swede, Spaniard
- color: white, green, yellow, blue, purple
- job: doctor, baker, farmer, teacher, lawyer
- pet: cat, dog, rabbit, horse, fish

Clues:
1. The blue house and the dog owner are next-door neighbours.
2. The doctor lives in the yellow house.
3. The Norwegian has the rabbit.
4. The doctor is not in house 5.
5. The Dane lives in house 2.
6. The green house belongs to the horse owner.
7. The farmer lives next door to the Norwegian.
8. The purple house's occupant keeps the dog.
9. The horse owner lives in house 3.
10. The lawyer lives right after the blue house, immediately to its right.
11. The Spaniard lives in house 4.
12. The Swede lives immediately to the left of the baker.
13. The fish owner is a neighbour of the Norwegian.

## Puzzle paraphrase:zebra-00176

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: baker, farmer, teacher, doctor, lawyer
- nationality: Swede, Spaniard, Dane, Brit, German
- color: red, green, yellow, white, blue
- pet: bird, horse, rabbit, cat, dog

Clues:
1. The German lives somewhere to the right of the blue house.
2. The Swede lives in house 3.
3. The Dane lives in house 4.
4. The green house's occupant keeps the cat.
5. The bird owner is either the German or the Spaniard.
6. The Brit is the farmer.
7. The Brit lives immediately to the left of the teacher.
8. The Dane is the doctor.
9. The horse keeper lives in the yellow house.
10. The white house's occupant keeps the rabbit.
11. The dog owner is not next door to the yellow house.
12. The baker and the blue house are two houses apart.
13. The baker and the teacher are two houses apart.
14. The bird keeper lives right beside the green house.
15. The yellow house lies somewhere to the right of the baker.

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

## Puzzle plain:zebra-00092

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, purple, blue, green
- pet: horse, fish, dog, bird, rabbit
- nationality: Dane, German, Swede, Norwegian, Spaniard
- drink: cocoa, juice, milk, tea, water

Clues:
1. The person who keeps the horse lives in the second house.
2. The German lives directly to the left of the person who drinks cocoa.
3. The person who drinks tea lives directly to the left of the person who drinks cocoa.
4. The milk drinker lives in one of the two end houses.
5. The Dane keeps the rabbit.
6. Whoever lives in the purple house drinks juice.
7. The fish owner and the tea drinker are neighbours.
8. The Dane lives immediately to the right of the owner of the dog.
9. The person in the green house and the water drinker live two houses apart.
10. The Spaniard lives immediately to the right of the tea drinker.
11. The bird owner does not live next to the Swede.
12. The person in the red house and the water drinker live in adjacent houses.
13. The Dane lives in the last house.
14. The person in the white house lives directly to the left of the person who drinks juice.
15. The owner of the fish lives in the leftmost house.

## Puzzle plain:zebra-00002

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, tennis, hiking, painting, cooking
- drink: cocoa, milk, coffee, water, juice
- pet: cat, fish, bird, rabbit, dog
- job: farmer, lawyer, doctor, pilot, baker

Clues:
1. The dog owner does not live in the first house.
2. The golf enthusiast lives directly to the left of the pilot.
3. The farmer lives directly to the left of the cocoa drinker.
4. The dog owner drinks coffee.
5. The person who drinks milk does not enjoy hiking.
6. The farmer lives directly to the left of the cooking enthusiast.
7. The cocoa drinker and the lawyer are neighbours.
8. The baker keeps the cat.
9. There is exactly one house between the juice drinker and the person who enjoys tennis.
10. The bird owner drinks juice.
11. The owner of the rabbit drinks cocoa.
12. The rabbit owner lives somewhere to the left of the baker.
13. The milk drinker works as the pilot.

## Puzzle plain:zebra-00076

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, lawyer, farmer, baker, pilot
- nationality: Spaniard, Norwegian, Swede, German, Brit
- drink: milk, tea, water, juice, coffee
- color: green, purple, blue, white, red

Clues:
1. The milk drinker lives in the house just left of the one where the tea drinker lives.
2. The occupant of the blue house lives immediately to the right of the Swede.
3. The baker lives in the blue house.
4. The Swede and the tea drinker live in adjacent houses.
5. Whoever lives in the white house either drinks milk or drinks water.
6. Whoever lives in the purple house lives immediately to the right of the milk drinker.
7. The Brit lives in the red house.
8. The farmer and the milk drinker live two houses apart.
9. The German lives in the last house.
10. The lawyer is the Norwegian.
11. The person who drinks coffee and the Swede are neighbours.
12. The Brit lives directly to the left of the occupant of the green house.
13. The doctor either is the Brit or is the German.
14. There is exactly one house between the Norwegian and the water drinker.

## Puzzle plain:zebra-00068

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, horse, fish, cat, rabbit
- drink: milk, tea, juice, water, cocoa
- job: teacher, baker, farmer, pilot, lawyer
- nationality: Norwegian, Dane, German, Brit, Spaniard

Clues:
1. The bird owner lives in the first house.
2. The baker and the German live two houses apart.
3. The owner of the fish drinks water.
4. The person who keeps the bird either is the Dane or is the Norwegian.
5. The lawyer drinks tea.
6. The Spaniard lives somewhere to the right of the farmer.
7. The cat owner does not live next to the juice drinker.
8. The Norwegian is not the pilot.
9. The baker lives directly to the left of the owner of the horse.
10. The pilot lives directly to the left of the person who drinks milk.
11. There is exactly one house between the horse owner and the teacher.
12. The milk drinker lives in the house just left of the one where the person who drinks cocoa lives.
13. The person who drinks water lives in one of the two end houses.
14. The Norwegian lives next to the person who keeps the rabbit.
