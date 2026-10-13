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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encA/e1_encA_022.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00124

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: white, red, yellow, blue, purple
- pet: rabbit, horse, fish, bird, cat
- drink: juice, cocoa, milk, coffee, tea
- job: farmer, pilot, lawyer, teacher, doctor

Clues:
1. The purple house's occupant lives right beside the teacher.
2. The cat owner lives directly to the right of the fish owner.
3. The bird owner lives somewhere to the right of the farmer.
4. The pilot keeps either the cat or the fish.
5. The rabbit owner drinks either coffee or tea.
6. The juice drinker lives next door to the purple house.
7. The pilot lives next door to the yellow house.
8. The farmer lives directly to the right of the cat owner.
9. The coffee drinker lives in the first house.
10. The farmer and the rabbit owner are next-door neighbours.
11. One house lies between the blue house and the pilot.
12. The doctor lives somewhere to the right of the cocoa drinker.
13. The bird owner does not live next door to the purple house.
14. The red house's occupant is the pilot.

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

## Puzzle plain:zebra-00094

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, chess, golf, painting, tennis
- color: green, yellow, purple, blue, red
- nationality: Dane, Swede, Spaniard, Brit, Norwegian
- drink: milk, water, coffee, cocoa, tea

Clues:
1. The occupant of the red house either drinks cocoa or drinks milk.
2. Whoever lives in the red house enjoys tennis.
3. The painting enthusiast is the Swede.
4. The Brit lives immediately to the right of whoever lives in the green house.
5. The Spaniard either drinks milk or drinks water.
6. The Dane lives in house 5.
7. The person who enjoys hiking lives next to the person in the yellow house.
8. The golf enthusiast lives directly to the left of the Norwegian.
9. The coffee drinker either is the Dane or is the Norwegian.
10. The Swede lives in the house just left of the one where the person in the red house lives.
11. The hiking enthusiast drinks cocoa.
12. The occupant of the blue house lives in house 1.

## Puzzle paraphrase:zebra-00150

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, German, Spaniard, Swede
- job: pilot, lawyer, doctor, farmer, teacher
- hobby: golf, tennis, cooking, painting, chess
- color: white, purple, green, yellow, blue

Clues:
1. There are exactly two houses between the teacher and the occupant of the yellow house, which is to say they are two doors apart.
2. The Brit and the Spaniard are next-door neighbours.
3. Painting is the Swede's hobby.
4. The tennis player lives in either the green house or the yellow house.
5. The green house is one of the two houses at the ends of the row.
6. The farmer's house lies somewhere to the right of the painter's.
7. The white house sits directly to the left of the lawyer's home.
8. One house separates the Dane from the resident of the purple house.
9. The German and the green house's occupant live two houses apart.
10. The chess player lives immediately to the left of the doctor.
11. The Spaniard's house is the yellow one.
12. The farmer's hobby is chess.
13. The Brit's favourite pastime is golf.

## Puzzle hard:zebra_hard-00098

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: cat, horse, rabbit, bird, dog
- color: blue, white, yellow, purple, green
- drink: milk, tea, water, cocoa, coffee
- nationality: Norwegian, Swede, German, Brit, Dane

Clues:
1. The Dane lives two doors away from the person who drinks water.
2. Neither whoever lives in the blue house nor the Norwegian drinks milk.
3. The right-hand neighbour of the tea drinker is the Dane.
4. Exactly 0 houses lie to the left of the home of the occupant of the blue house.
5. The Brit and the person who drinks coffee are one and the same person.
6. Exactly one house separates the person in the blue house from whoever lives in the green house.
7. Exactly 0 houses lie to the left of the home of the owner of the rabbit.
8. The left-hand neighbour of the owner of the bird is the Norwegian.
9. The German lives in the fifth house from the right.
10. Exactly one house separates the Norwegian from whoever lives in the purple house.
11. One of the neighbours of the dog owner keeps the horse.
12. One of the neighbours of the horse owner keeps the cat.
13. The Brit and the person who keeps the dog are one and the same person.
14. The Norwegian and the occupant of the white house are one and the same person.

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

## Puzzle paraphrase:zebra-00117

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, cocoa, water, juice, coffee
- pet: rabbit, dog, bird, cat, fish
- hobby: hiking, painting, chess, cooking, tennis
- job: lawyer, pilot, teacher, baker, farmer

Clues:
1. The chess enthusiast lives in house 5.
2. The baker is the tea drinker.
3. The cooking enthusiast lives immediately to the right of the cocoa drinker.
4. The bird owner drinks either coffee or water.
5. The cat keeper and the pilot are two houses apart.
6. The bird owner lives directly to the right of the fish owner.
7. The farmer drinks either coffee or juice.
8. The fish owner lives immediately to the right of the dog keeper.
9. The coffee drinker and the hiking enthusiast have exactly one house between them.
10. The lawyer lives directly to the left of the pilot.
11. The baker is the tennis enthusiast.
12. The teacher does not live in the third house.
13. The bird owner is a hiking enthusiast.

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

## Puzzle plain:zebra-00089

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, baker, pilot, doctor, farmer
- color: red, blue, green, yellow, white
- drink: tea, cocoa, water, milk, juice
- nationality: Swede, Dane, Brit, Spaniard, German

Clues:
1. Whoever lives in the yellow house either drinks cocoa or drinks tea.
2. The German lives directly to the left of the person in the green house.
3. The farmer and the Spaniard are not neighbours.
4. The baker lives immediately to the right of the pilot.
5. The person who drinks juice lives next to the lawyer.
6. The doctor lives in the blue house.
7. The baker lives in the second house.
8. The person who drinks cocoa lives directly to the left of the person who drinks juice.
9. The German drinks tea.
10. The farmer and the person in the red house are not neighbours.
11. The Dane lives in house 2.
12. The German lives in the house just left of the one where the Brit lives.
13. The German and the person who drinks milk live two houses apart.
14. The occupant of the white house lives in house 1.
