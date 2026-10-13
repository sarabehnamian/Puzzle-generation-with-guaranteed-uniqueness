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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encA/e1_encA_013.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle paraphrase:zebra-00140

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, tennis, hiking, painting, golf
- drink: tea, water, milk, cocoa, juice
- color: white, red, green, yellow, purple
- pet: cat, bird, horse, fish, rabbit

Clues:
1. The resident of the yellow house is no tennis player.
2. Cocoa is what the person in the white house drinks.
3. House 2 belongs to the water drinker.
4. Hiking is the pastime of whoever owns the rabbit.
5. Whoever paints lives in one of the two end houses.
6. The horse lives with the occupant of the red house.
7. The tea drinker is not the one who keeps the horse.
8. The purple house and the tennis enthusiast's home stand side by side.
9. The juice drinker is the golf fan.
10. The chess player does not live in the yellow house.
11. The cat owner lives right next door to the right of the tennis enthusiast.
12. The bird keeper lives in the house directly right of the juice drinker's.
13. The rabbit belongs to the occupant of the white house.
14. The horse owner lives in house 5.

## Puzzle plain:zebra-00014

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: coffee, juice, cocoa, water, milk
- job: pilot, teacher, doctor, farmer, baker
- pet: fish, horse, cat, rabbit, dog
- hobby: hiking, cooking, painting, chess, tennis

Clues:
1. There is exactly one house between the baker and the person who drinks milk.
2. The pilot lives at one end of the row.
3. The person who drinks coffee enjoys tennis.
4. The juice drinker either keeps the horse or keeps the rabbit.
5. The person who drinks water works as the pilot.
6. The owner of the cat works as the baker.
7. The person who keeps the rabbit enjoys hiking.
8. The person who enjoys chess lives in one of the two end houses.
9. The coffee drinker lives at one end of the row.
10. The teacher lives in the third house.
11. The doctor lives immediately to the right of the person who keeps the rabbit.
12. The person who enjoys cooking does not live in the fourth house.
13. The person who enjoys tennis lives directly to the left of the dog owner.

## Puzzle plain:zebra-00052

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: cat, rabbit, fish, bird, horse
- color: blue, white, green, yellow, purple
- drink: milk, juice, cocoa, tea, water
- hobby: hiking, golf, chess, painting, tennis

Clues:
1. Whoever lives in the purple house lives directly to the left of the person in the blue house.
2. The cocoa drinker lives directly to the left of the tennis enthusiast.
3. The chess enthusiast lives immediately to the right of the cat owner.
4. The painting enthusiast lives in the leftmost house.
5. The person who drinks tea lives immediately to the right of the chess enthusiast.
6. The owner of the fish lives next to the person who drinks milk.
7. There is exactly one house between the occupant of the green house and the person who drinks juice.
8. There is exactly one house between the golf enthusiast and the person who enjoys hiking.
9. The occupant of the green house either enjoys golf or enjoys painting.
10. The bird owner lives immediately to the right of the painting enthusiast.
11. The person who keeps the fish and the person in the yellow house are neighbours.
12. The occupant of the white house lives in the first house.
13. The milk drinker keeps the horse.

## Puzzle hard:zebra_hard-00071

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: golf, tennis, cooking, chess, hiking
- nationality: Norwegian, Dane, Swede, Brit, Spaniard
- color: red, yellow, blue, green, white
- drink: coffee, cocoa, water, juice, milk

Clues:
1. If the person in the green house does not enjoy cooking, then that person enjoys golf.
2. The Brit lives two doors away from the person who drinks water.
3. Neither the Brit nor the water drinker lives in the red house.
4. One of the neighbours of the person in the blue house is the Spaniard.
5. The chess enthusiast and the Norwegian are one and the same person.
6. The right-hand neighbour of the hiking enthusiast is the Norwegian.
7. The person who enjoys cooking is not the same person as the Spaniard.
8. The chess enthusiast lives further to the right than the person in the red house.
9. One of the neighbours of the occupant of the yellow house enjoys tennis.
10. The milk drinker lives somewhere between the person who drinks cocoa and the Dane.
11. The Brit and the person who drinks coffee are one and the same person.
12. If the person in the green house does not drink coffee, then that person drinks milk.
13. The Brit and the person who enjoys hiking are one and the same person.
14. One of the neighbours of the person who enjoys tennis is the Dane.

## Puzzle hard:zebra_hard-00092

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, farmer, baker, pilot, lawyer
- color: red, purple, blue, yellow, white
- drink: water, milk, juice, tea, cocoa
- hobby: painting, chess, hiking, golf, tennis

Clues:
1. The pilot and the person in the purple house are one and the same person.
2. The person who enjoys chess lives two doors away from the person who drinks cocoa.
3. One of the neighbours of the hiking enthusiast works as the lawyer.
4. The right-hand neighbour of the person who enjoys painting drinks juice.
5. The right-hand neighbour of the person who drinks tea works as the doctor.
6. The baker lives somewhere between the occupant of the purple house and the tennis enthusiast.
7. The right-hand neighbour of the tennis enthusiast lives in the blue house.
8. The baker and the milk drinker are one and the same person.
9. The right-hand neighbour of the person in the white house drinks cocoa.
10. The person in the yellow house lives somewhere between whoever lives in the blue house and the person who drinks milk.
11. The right-hand neighbour of the person who drinks water drinks juice.

## Puzzle hard:zebra_hard-00023

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, teacher, farmer, lawyer, baker
- color: red, yellow, purple, green, white
- drink: juice, tea, milk, coffee, cocoa
- pet: fish, bird, horse, dog, rabbit

Clues:
1. The teacher lives further to the right than the person in the red house.
2. One of the neighbours of the person who drinks milk lives in the green house.
3. The lawyer lives two doors away from the person who drinks tea.
4. Whoever lives in the green house and the rabbit owner are one and the same person.
5. The cocoa drinker and the owner of the fish are one and the same person.
6. The person in the green house has only one neighbour.
7. The farmer lives in the second house from the right.
8. The dog owner does not live to the right of the person who keeps the fish.
9. The person who keeps the fish and whoever lives in the yellow house are one and the same person.
10. The person who keeps the bird lives in the fourth house from the right.
11. The tea drinker and the occupant of the white house are one and the same person.
12. The right-hand neighbour of the baker drinks cocoa.
13. If whoever lives in the red house does not drink cocoa, then that person drinks coffee.

## Puzzle hard:zebra_hard-00090

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Norwegian, Dane, Swede, German, Spaniard
- color: yellow, green, blue, red, white
- job: farmer, pilot, teacher, lawyer, baker
- drink: water, coffee, milk, juice, cocoa

Clues:
1. The pilot lives somewhere between the juice drinker and the lawyer.
2. One of the neighbours of the occupant of the red house drinks coffee.
3. The left-hand neighbour of the German drinks water.
4. Neither the person in the blue house nor the cocoa drinker works as the baker.
5. If the cocoa drinker is not the German, then that person is the Norwegian.
6. One of the neighbours of the cocoa drinker drinks coffee.
7. The right-hand neighbour of the Norwegian is the Swede.
8. Whoever lives in the green house and the teacher are one and the same person.
9. The occupant of the green house does not live in the second house from the right.
10. The right-hand neighbour of the coffee drinker is the Norwegian.
11. Exactly 4 houses lie to the left of the home of the lawyer.
12. Neither the baker nor the person in the green house is the Spaniard.
13. The right-hand neighbour of the baker drinks water.
14. The German and the person in the white house are one and the same person.

## Puzzle paraphrase:zebra-00129

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, cocoa, water, tea, coffee
- hobby: chess, painting, cooking, tennis, golf
- color: purple, blue, yellow, red, green
- job: lawyer, doctor, pilot, farmer, baker

Clues:
1. The doctor lives directly to the left of the red house.
2. The tea drinker lives immediately to the right of the milk drinker.
3. The baker lives directly to the left of the yellow house.
4. The coffee drinker and the tennis enthusiast have exactly one house between them.
5. The coffee drinker does not live next door to the golf enthusiast.
6. The green house stands immediately to the left of the yellow house.
7. The yellow house's occupant is the lawyer.
8. The coffee drinker lives somewhere to the left of the blue house.
9. The golf enthusiast lives in either the purple house or the yellow house.
10. The pilot lives further to the left than the farmer.
11. The cocoa drinker lives next door to the cooking enthusiast.
12. The coffee drinker lives immediately to the right of the water drinker.
13. The blue house is at one end of the row.
14. The painting enthusiast lives directly to the left of the milk drinker.

## Puzzle paraphrase:zebra-00125

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, juice, coffee, water, milk
- pet: rabbit, horse, dog, fish, bird
- color: red, green, blue, yellow, white
- hobby: hiking, golf, cooking, chess, tennis

Clues:
1. The milk drinker is the bird keeper.
2. The green house stands immediately to the right of the milk drinker.
3. The tea drinker lives somewhere to the left of the dog keeper.
4. The coffee drinker lives directly to the left of the white house.
5. The white house's occupant keeps either the dog or the rabbit.
6. The golf enthusiast keeps the rabbit.
7. The occupant of the white house enjoys hiking.
8. The cooking enthusiast lives next door to the hiking enthusiast.
9. The rabbit owner drinks coffee.
10. The blue house stands immediately to the right of the green house.
11. The tennis enthusiast lives directly to the left of the rabbit owner.
12. The yellow house's occupant is not the fish owner.
13. The fish owner drinks water.
