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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encB\e1_encB_026.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00160

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, dog, cat, rabbit, horse
- job: lawyer, teacher, baker, doctor, farmer
- hobby: chess, cooking, tennis, golf, painting
- drink: juice, water, coffee, cocoa, milk

Clues:
1. Whoever enjoys tennis drinks juice.
2. The cat owner and the painting enthusiast live next door to each other.
3. The golfer doesn't drink milk.
4. The lawyer occupies the middle house.
5. The chess player lives immediately to the left of the painting enthusiast.
6. The bird keeper is the doctor.
7. The dog owner drinks milk.
8. The farmer does not live in house 2.
9. The golfer is the baker.
10. The farmer and the water drinker are next-door neighbours.
11. The rabbit owner lives in house 1.
12. The cocoa drinker's hobby is either painting or tennis.
13. The water drinker lives immediately to the left of the coffee drinker.

## Puzzle plain:zebra-00066

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Brit, Spaniard, Norwegian, Dane
- job: lawyer, baker, doctor, pilot, farmer
- color: purple, yellow, white, green, blue
- hobby: tennis, painting, chess, cooking, golf

Clues:
1. The lawyer and whoever lives in the white house live in adjacent houses.
2. The farmer lives next to the person in the purple house.
3. The occupant of the yellow house either is the Brit or is the Norwegian.
4. The chess enthusiast lives in the blue house.
5. The golf enthusiast lives next to the person in the white house.
6. The Norwegian lives next to the Swede.
7. The farmer lives in house 2.
8. The baker and the person who enjoys painting live in adjacent houses.
9. The golf enthusiast lives somewhere to the right of whoever lives in the green house.
10. Whoever lives in the yellow house lives directly to the left of the doctor.
11. The person who enjoys cooking and the Dane live two houses apart.
12. The person who enjoys painting and the Spaniard live two houses apart.
13. The cooking enthusiast and the baker are different people.

## Puzzle hard:zebra_hard-00044

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, tea, juice, coffee, cocoa
- job: teacher, doctor, pilot, farmer, baker
- pet: dog, fish, cat, rabbit, horse
- color: purple, green, yellow, white, red

Clues:
1. Exactly 4 houses lie to the left of the home of the cocoa drinker.
2. The doctor and the tea drinker are one and the same person.
3. The baker lives somewhere between the person who drinks juice and the water drinker.
4. The person who keeps the cat is not the same person as the pilot.
5. The owner of the horse and the teacher are one and the same person.
6. The occupant of the green house and the person who drinks juice are one and the same person.
7. The pilot lives somewhere between the owner of the rabbit and the water drinker.
8. If the occupant of the yellow house does not drink coffee, then that person drinks tea.
9. One of the neighbours of the pilot keeps the dog.
10. The owner of the dog lives two doors away from whoever lives in the purple house.
11. The doctor lives somewhere between the owner of the rabbit and the occupant of the white house.
12. The dog owner does not live to the right of the cat owner.

## Puzzle hard:zebra_hard-00099

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: doctor, lawyer, teacher, pilot, farmer
- drink: water, milk, tea, cocoa, juice
- pet: rabbit, cat, horse, dog, fish
- nationality: German, Dane, Norwegian, Spaniard, Swede

Clues:
1. One of the neighbours of the rabbit owner is the Spaniard.
2. One of the neighbours of the Dane is the Spaniard.
3. Exactly 0 houses lie to the left of the home of the dog owner.
4. Exactly one house separates the person who keeps the cat from the person who keeps the rabbit.
5. The doctor lives two doors away from the person who drinks milk.
6. The right-hand neighbour of the cocoa drinker is the German.
7. The person who drinks cocoa lives in the second house from the right.
8. One of the neighbours of the Swede works as the teacher.
9. The farmer lives two doors away from the person who drinks tea.
10. The fish owner and the lawyer are one and the same person.
11. Exactly one house separates the Norwegian from the water drinker.
12. At least one house separates the Norwegian from the Swede.
13. The German and the person who drinks tea are one and the same person.
14. One of the neighbours of the pilot works as the teacher.

## Puzzle plain:zebra-00018

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: pilot, doctor, teacher, lawyer, farmer
- nationality: Dane, Brit, Norwegian, German, Swede
- drink: juice, water, tea, coffee, cocoa
- hobby: golf, tennis, painting, chess, cooking

Clues:
1. The person who drinks water lives in one of the two end houses.
2. The golf enthusiast and the juice drinker are not neighbours.
3. The Brit and the Dane are not neighbours.
4. The coffee drinker and the cooking enthusiast live two houses apart.
5. The person who enjoys cooking works as the doctor.
6. The Norwegian lives somewhere to the right of the person who drinks cocoa.
7. The teacher is the Norwegian.
8. The person who drinks juice lives next to the Norwegian.
9. The teacher lives at one end of the row.
10. The person who enjoys painting lives directly to the left of the Swede.
11. The person who drinks tea works as the lawyer.
12. The Brit and the painting enthusiast live two houses apart.
13. The person who enjoys tennis lives in the house just left of the one where the Dane lives.
14. The farmer does not live in house 3.
15. There is exactly one house between the person who drinks juice and the pilot.

## Puzzle hard:zebra_hard-00030

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: tea, cocoa, juice, water, milk
- color: white, red, blue, yellow, green
- job: lawyer, teacher, pilot, farmer, doctor
- nationality: Swede, Dane, Norwegian, Brit, German

Clues:
1. The occupant of the white house has only one neighbour.
2. The occupant of the yellow house lives somewhere between the person who drinks milk and the person in the red house.
3. The juice drinker and the occupant of the yellow house are one and the same person.
4. The doctor is not the same person as the person who drinks tea.
5. The left-hand neighbour of the pilot is the Brit.
6. None of the neighbours of the person in the red house lives in the green house.
7. The Brit and the person who drinks tea are one and the same person.
8. The water drinker lives further to the right than the Norwegian.
9. Whoever lives in the red house lives in the fifth house from the right.
10. The Dane and the teacher are one and the same person.
11. The Dane and the person in the yellow house are one and the same person.
12. One of the neighbours of the doctor is the German.
13. The left-hand neighbour of the lawyer lives in the yellow house.
14. The right-hand neighbour of the person who drinks juice drinks water.

## Puzzle hard:zebra_hard-00077

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, chess, painting, tennis, golf
- pet: rabbit, fish, dog, bird, horse
- job: pilot, teacher, baker, lawyer, doctor
- nationality: Spaniard, German, Brit, Dane, Swede

Clues:
1. The Dane lives further to the right than the person who enjoys painting.
2. The pilot lives somewhere between the doctor and the Swede.
3. The person who keeps the dog and the lawyer are one and the same person.
4. Exactly one house separates the lawyer from the painting enthusiast.
5. The person who enjoys golf and the Swede are one and the same person.
6. Exactly 0 houses lie to the left of the home of the Brit.
7. Exactly 2 houses lie to the left of the home of the Spaniard.
8. The person who keeps the rabbit lives somewhere between the doctor and the hiking enthusiast.
9. The right-hand neighbour of the painting enthusiast enjoys golf.
10. The Spaniard lives further to the right than the lawyer.
11. One of the neighbours of the person who enjoys painting works as the baker.
12. One of the neighbours of the person who keeps the bird enjoys hiking.
13. None of the neighbours of the owner of the fish enjoys golf.
14. The doctor and the tennis enthusiast are one and the same person.

## Puzzle hard:zebra_hard-00039

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: bird, rabbit, cat, dog, fish
- nationality: Brit, German, Dane, Norwegian, Swede
- color: green, red, blue, purple, yellow
- drink: water, cocoa, coffee, tea, milk

Clues:
1. The right-hand neighbour of the fish owner keeps the cat.
2. The water drinker lives in the rightmost house.
3. The left-hand neighbour of the fish owner lives in the yellow house.
4. The person who drinks coffee lives somewhere between the occupant of the purple house and the Swede.
5. The person who keeps the rabbit is not the same person as whoever lives in the red house.
6. The dog owner lives two doors away from the milk drinker.
7. The occupant of the purple house and the tea drinker are one and the same person.
8. The left-hand neighbour of the person in the red house is the German.
9. One of the neighbours of the person who keeps the bird is the Brit.
10. The person who keeps the rabbit lives in the rightmost house.
11. The left-hand neighbour of the person in the green house lives in the yellow house.
12. The Dane lives two doors away from the rabbit owner.

## Puzzle paraphrase:zebra-00107

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, hiking, tennis, cooking
- pet: bird, dog, fish, rabbit, cat
- nationality: German, Dane, Brit, Swede, Spaniard
- job: lawyer, teacher, doctor, pilot, baker

Clues:
1. The Brit is the teacher.
2. The Dane lives next door to the Spaniard.
3. The Swede lives immediately to the left of the fish owner.
4. The hiker lives in the last house.
5. The fish owner lives next door to the lawyer.
6. The golf enthusiast lives immediately to the right of the cooking enthusiast.
7. One house separates the cat owner from the hiker.
8. One house lies between the pilot and the tennis enthusiast.
9. The hiker lives next door to the Spaniard.
10. The doctor lives immediately to the left of the lawyer.
11. The Dane keeps the bird.
12. The chess enthusiast lives in the fourth house.
13. The doctor and the rabbit owner are neighbours.

## Puzzle plain:zebra-00072

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, cooking, hiking, painting, chess
- pet: fish, rabbit, dog, cat, horse
- drink: milk, juice, coffee, tea, water
- color: blue, yellow, purple, green, white

Clues:
1. The owner of the horse either drinks tea or drinks water.
2. The occupant of the purple house keeps the fish.
3. Whoever lives in the green house lives next to the rabbit owner.
4. The tea drinker and the person who enjoys tennis live two houses apart.
5. The owner of the cat lives at one end of the row.
6. There is exactly one house between whoever lives in the blue house and the juice drinker.
7. The occupant of the blue house enjoys hiking.
8. The owner of the dog lives in the fourth house.
9. The person in the white house lives in a lower-numbered house than the person who enjoys painting.
10. The milk drinker lives in a lower-numbered house than whoever lives in the white house.
11. The water drinker lives in house 3.
12. The chess enthusiast and the person who drinks water live in adjacent houses.
13. The person in the yellow house lives in the house just left of the one where the person who enjoys tennis lives.
