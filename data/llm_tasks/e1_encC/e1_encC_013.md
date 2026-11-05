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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encC\e1_encC_013.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00169

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: fish, cat, horse, bird, rabbit
- job: baker, lawyer, teacher, doctor, farmer
- drink: cocoa, juice, coffee, milk, water
- nationality: Norwegian, Spaniard, Swede, Dane, Brit

Clues:
1. The baker lives next door to the rabbit owner.
2. The coffee drinker lives immediately to the right of the water drinker.
3. The cocoa drinker lives in house 5.
4. Exactly one house lies between the Dane and the doctor.
5. One house separates the Norwegian from the Swede.
6. The cat owner and the fish owner live in adjacent houses.
7. The cat owner lives immediately to the right of the farmer.
8. The Dane lives next door to the rabbit owner.
9. The cocoa drinker and the farmer are neighbours.
10. The Spaniard keeps either the cat or the horse.
11. The teacher drinks water.
12. Exactly one house lies between the bird keeper and the cat owner.
13. The cocoa drinker lives somewhere to the right of the doctor.
14. The rabbit owner is the Swede.
15. The doctor lives next door to the milk drinker.

## Puzzle hard:zebra_hard-00094

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, German, Dane, Brit, Norwegian
- drink: coffee, water, milk, tea, juice
- job: doctor, pilot, teacher, baker, lawyer
- hobby: hiking, tennis, chess, golf, cooking

Clues:
1. One of the neighbours of the German works as the lawyer.
2. Exactly one house separates the milk drinker from the teacher.
3. The baker lives two doors away from the pilot.
4. If the Dane does not enjoy golf, then that person enjoys tennis.
5. The Brit and the person who drinks juice are one and the same person.
6. The person who drinks milk and the Spaniard are one and the same person.
7. The person who enjoys chess lives further to the right than the German.
8. Exactly one house separates the coffee drinker from the golf enthusiast.
9. The milk drinker lives in the fifth house from the right.
10. Exactly 4 houses lie to the left of the home of the person who enjoys tennis.
11. The person who drinks juice lives further to the right than the pilot.
12. One of the neighbours of the water drinker enjoys golf.
13. The person who enjoys hiking lives in the third house from the right.

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

## Puzzle paraphrase:zebra-00159

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, cooking, golf, chess, hiking
- pet: cat, bird, horse, fish, dog
- drink: juice, milk, water, cocoa, coffee
- color: blue, green, white, purple, red

Clues:
1. The cocoa drinker and the golfer live two houses apart.
2. The milk drinker lives in house 5.
3. The purple house is house 2.
4. The painter drinks either coffee or water.
5. The red house is the third house.
6. The fish keeper and the water drinker live two houses apart.
7. The cat's owner lives in the third house.
8. The chess player keeps the fish.
9. The dog owner lives in the green house.
10. The cocoa drinker keeps the cat.
11. The fish owner and the white house's occupant live two houses apart.
12. The horse owner drinks either cocoa or juice.
13. The cocoa drinker lives in a lower-numbered house than the cooking enthusiast.

## Puzzle plain:zebra-00058

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, chess, tennis, painting, cooking
- job: teacher, lawyer, farmer, doctor, baker
- pet: fish, dog, cat, horse, bird
- color: purple, red, yellow, green, white

Clues:
1. The occupant of the purple house lives directly to the left of the bird owner.
2. The bird owner and the farmer are not neighbours.
3. The farmer and the person who keeps the horse live two houses apart.
4. The person in the red house and the person who enjoys tennis live two houses apart.
5. The painting enthusiast either lives in the white house or lives in the yellow house.
6. The doctor and whoever lives in the green house live two houses apart.
7. The occupant of the white house enjoys hiking.
8. The owner of the fish lives in the second house.
9. There is exactly one house between the baker and the farmer.
10. The person who keeps the cat enjoys chess.
11. The baker either enjoys hiking or enjoys tennis.
12. The teacher lives in the green house.
13. Whoever lives in the white house lives in house 2.
14. The person in the red house lives in a lower-numbered house than the owner of the bird.

## Puzzle paraphrase:zebra-00140

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, tennis, hiking, painting, golf
- drink: tea, water, milk, cocoa, juice
- color: white, red, green, yellow, purple
- pet: cat, bird, horse, fish, rabbit

Clues:
1. The yellow house's resident does not play tennis.
2. Cocoa is drunk by whoever lives in the white house.
3. House 2 is home to the water drinker.
4. Whoever owns the rabbit loves hiking.
5. The painting enthusiast lives in one of the two end houses.
6. The red house's occupant keeps a horse.
7. The tea drinker is not the one who keeps the horse.
8. The purple house and the tennis player are next-door neighbours.
9. Whoever drinks juice enjoys golf.
10. The chess enthusiast is not the person living in the yellow house.
11. The cat owner lives directly to the right of the tennis player.
12. The bird keeper lives right next to the juice drinker, on the right side.
13. The white house's occupant keeps the rabbit.
14. The horse owner lives in house 5.

## Puzzle plain:zebra-00099

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, water, cocoa, coffee, tea
- job: pilot, farmer, lawyer, teacher, baker
- color: red, purple, white, blue, yellow
- hobby: golf, hiking, tennis, painting, chess

Clues:
1. The tea drinker lives in the house just left of the one where the occupant of the yellow house lives.
2. The person who drinks coffee lives next to the person who enjoys painting.
3. Whoever lives in the blue house and whoever lives in the red house are neighbours.
4. The water drinker enjoys chess.
5. The person in the purple house lives in a lower-numbered house than the painting enthusiast.
6. The person in the yellow house works as the farmer.
7. The baker and the cocoa drinker live in adjacent houses.
8. The person who drinks cocoa and the teacher live two houses apart.
9. The tennis enthusiast lives in the second house.
10. The cocoa drinker lives in the fourth house.
11. The person in the red house either drinks cocoa or drinks juice.
12. The lawyer drinks cocoa.
13. The person who enjoys chess and the tea drinker are not neighbours.
14. The hiking enthusiast and the water drinker live two houses apart.
15. The farmer and the person in the purple house live two houses apart.

## Puzzle hard:zebra_hard-00038

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, purple, white, yellow, red
- drink: water, coffee, cocoa, tea, juice
- pet: horse, bird, dog, rabbit, fish
- hobby: hiking, cooking, golf, tennis, painting

Clues:
1. If the person in the white house does not drink cocoa, then that person drinks tea.
2. The right-hand neighbour of the cooking enthusiast drinks tea.
3. One of the neighbours of the golf enthusiast drinks juice.
4. The person who keeps the bird and the coffee drinker are one and the same person.
5. The horse owner and the person who drinks tea are one and the same person.
6. The person who enjoys painting and the person who drinks tea are one and the same person.
7. If whoever lives in the yellow house does not keep the fish, then that person keeps the horse.
8. Whoever lives in the red house has only one neighbour.
9. If the occupant of the red house does not keep the horse, then that person keeps the rabbit.
10. Whoever lives in the white house lives further to the right than the owner of the horse.
11. The left-hand neighbour of whoever lives in the yellow house enjoys hiking.
12. The juice drinker lives somewhere between the occupant of the purple house and the person in the white house.
13. One of the neighbours of whoever lives in the red house lives in the purple house.

## Puzzle paraphrase:zebra-00186

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Dane, German, Brit, Swede, Spaniard
- pet: rabbit, bird, fish, dog, cat
- drink: juice, tea, milk, cocoa, coffee
- hobby: golf, painting, tennis, chess, cooking

Clues:
1. The German does not live beside the painter.
2. The chess player and the Spaniard live two houses apart.
3. The Spaniard has the dog.
4. The juice drinker is the painter.
5. The cooking enthusiast lives in one of the end houses.
6. One house lies between the fish owner and the juice drinker.
7. The dog's owner drinks cocoa.
8. The Swede drinks tea.
9. The juice drinker and the tennis player have exactly one house between them.
10. The bird is in house 2.
11. The German lives at one of the two ends of the row.
12. The milk drinker lives immediately to the left of the juice drinker.
13. The Dane and the tennis player live two houses apart.
14. The rabbit owner lives in a lower-numbered house than the Swede.
15. The chess enthusiast lives somewhere to the right of the Dane.

## Puzzle paraphrase:zebra-00136

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: milk, cocoa, juice, coffee, tea
- job: lawyer, baker, pilot, farmer, doctor
- color: red, purple, white, yellow, green
- pet: fish, bird, dog, rabbit, horse

Clues:
1. The white house's occupant is not the baker.
2. The green house is right next to the red house.
3. The fish owner lives directly to the right of the cocoa drinker.
4. One house separates the dog owner from the purple house.
5. One house lies between the doctor and the pilot.
6. The coffee drinker lives in house 1.
7. The horse owner lives immediately to the left of the doctor.
8. The purple house is next door to the tea drinker.
9. The horse owner is the lawyer.
10. The green house lies somewhere to the right of the doctor.
11. The rabbit owner lives immediately to the left of the farmer.
12. The dog owner and the lawyer are not neighbours.
13. The green house is directly to the right of the cocoa drinker.
14. The doctor does not own the rabbit.
15. One house lies between the green house and the milk drinker.
