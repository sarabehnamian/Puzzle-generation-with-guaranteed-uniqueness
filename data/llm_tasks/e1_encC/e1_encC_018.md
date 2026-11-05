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

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e1_encC\e1_encC_018.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


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

## Puzzle hard:zebra_hard-00020

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- pet: horse, cat, fish, bird, rabbit
- nationality: Spaniard, Brit, German, Dane, Swede
- drink: water, tea, coffee, cocoa, milk
- color: white, yellow, purple, blue, red

Clues:
1. The person who keeps the bird lives two doors away from the occupant of the purple house.
2. The left-hand neighbour of the cat owner lives in the red house.
3. The person who drinks cocoa and the Dane are one and the same person.
4. The owner of the fish and the person who drinks tea are one and the same person.
5. The person who drinks water has only one neighbour.
6. The Brit lives in the fifth house from the right.
7. Neither the bird owner nor whoever lives in the red house is the Dane.
8. The person who drinks water lives further to the right than the person in the yellow house.
9. The person who drinks coffee and the person in the yellow house are one and the same person.
10. Whoever lives in the blue house lives in the fifth house from the right.
11. The person who drinks milk lives somewhere between the person who drinks water and the occupant of the yellow house.
12. One of the neighbours of the German is the Brit.
13. The Swede lives somewhere between the bird owner and the owner of the horse.

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

## Puzzle paraphrase:zebra-00162

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, white, yellow, red, green
- hobby: hiking, cooking, painting, golf, tennis
- pet: horse, dog, bird, cat, rabbit
- drink: juice, cocoa, milk, water, coffee

Clues:
1. The hiker and the juice drinker live in adjacent houses.
2. The tennis enthusiast lives immediately to the right of the green house's occupant.
3. The white house is the last house.
4. The hiker lives in the purple house.
5. The hiker lives immediately to the right of the cooking enthusiast.
6. The rabbit owner lives in the white house.
7. The dog owner and the juice drinker are next-door neighbours.
8. The green house's occupant and the water drinker are neighbours.
9. The occupant of the green house lives next to the milk drinker.
10. The hiker keeps either the bird or the cat.
11. The tennis enthusiast lives immediately to the right of the cat owner.
12. The golfer lives in house 5.
13. The milk drinker lives in a lower-numbered house than the water drinker.
14. The cocoa drinker lives next door to the hiker.
15. Exactly one house separates the green house from the yellow house.

## Puzzle paraphrase:zebra-00134

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Spaniard, Brit, Norwegian, Swede, Dane
- hobby: golf, chess, cooking, painting, tennis
- job: doctor, farmer, baker, lawyer, teacher
- pet: cat, rabbit, horse, bird, fish

Clues:
1. The painting enthusiast lives directly to the right of the golf enthusiast.
2. The cat owner and the teacher live in adjacent houses.
3. The Brit keeps the rabbit.
4. The Dane is the farmer.
5. The baker and the cat owner live two houses apart.
6. The cooking enthusiast lives immediately to the left of the bird owner.
7. The baker lives directly to the right of the farmer.
8. The Spaniard lives directly to the right of the Dane.
9. The rabbit owner's hobby is tennis.
10. The Swede keeps the horse.
11. The rabbit owner lives immediately to the left of the lawyer.
12. The Swede is the cooking enthusiast.

## Puzzle paraphrase:zebra-00188

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, baker, teacher, pilot, lawyer
- drink: water, tea, coffee, milk, juice
- nationality: Spaniard, Brit, Swede, Norwegian, Dane
- hobby: tennis, hiking, chess, painting, cooking

Clues:
1. The tennis player lives in a lower-numbered house than the teacher.
2. The Brit lives immediately to the right of the juice drinker.
3. The Brit lives next door to the teacher.
4. The Spaniard is the lawyer.
5. The tea drinker lives in the last house.
6. The Norwegian does not live in house 2.
7. The Swede is the hiking enthusiast.
8. One house separates the Brit and the farmer.
9. The lawyer lives immediately to the left of the water drinker.
10. The cooking enthusiast and the Swede live two houses apart.
11. The baker's hobby is tennis.
12. The milk drinker lives immediately to the left of the baker.
13. The lawyer's hobby is chess.

## Puzzle paraphrase:zebra-00155

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, golf, painting, hiking, tennis
- drink: water, milk, coffee, juice, tea
- color: white, yellow, blue, green, purple
- pet: cat, bird, dog, horse, fish

Clues:
1. The hiker drinks coffee.
2. The juice drinker lives in house 4.
3. Exactly one house lies between the green house and the purple house.
4. The blue house's occupant and the tea drinker are neighbours.
5. The bird owner lives immediately to the left of the purple house's occupant.
6. The cooking enthusiast lives next door to the water drinker.
7. The golfer and the tennis player live next to each other.
8. The tennis player doesn't keep the dog.
9. One house sits between the bird's owner and the yellow house's occupant.
10. The juice drinker lives somewhere to the right of the yellow house.
11. The golfer and the horse keeper are not neighbours.
12. The fish owner lives immediately to the left of the cat owner.
13. The painter lives in a lower-numbered house than the hiker.
14. The milk drinker and the tennis player are not next-door neighbours.
15. The white house's occupant enjoys either cooking or painting.
16. The fish owner and the water drinker live next door to each other.
17. The tennis player lives in either the green house or the purple house.

## Puzzle paraphrase:zebra-00191

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: painting, golf, cooking, chess, tennis
- job: pilot, baker, lawyer, teacher, farmer
- pet: horse, bird, fish, cat, dog
- nationality: Norwegian, Swede, Spaniard, Brit, Dane

Clues:
1. The Dane and the dog owner live in neighbouring houses.
2. The horse keeper lives immediately to the right of the chess enthusiast.
3. The tennis enthusiast is a pilot by profession.
4. The cat owner lives next door to the Swede.
5. The Swede lives right before the horse owner's house.
6. The bird owner is the lawyer.
7. The teacher lives somewhere to the right of the pilot.
8. The cooking enthusiast is the farmer.
9. The painting enthusiast keeps the cat.
10. The horse owner lives just to the left of the dog owner.
11. The Spaniard is the cooking enthusiast.
12. The tennis enthusiast keeps the horse.
13. The Brit is the pilot.

## Puzzle plain:zebra-00043

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: cocoa, coffee, tea, water, juice
- job: farmer, teacher, pilot, lawyer, doctor
- color: white, green, yellow, red, purple
- pet: dog, cat, horse, rabbit, fish

Clues:
1. The person who drinks cocoa either lives in the green house or lives in the purple house.
2. The tea drinker either lives in the white house or lives in the yellow house.
3. The person who drinks water lives immediately to the right of the farmer.
4. The pilot and the tea drinker live in adjacent houses.
5. The occupant of the green house and the teacher live in adjacent houses.
6. The person who keeps the horse either works as the farmer or works as the teacher.
7. The owner of the fish works as the doctor.
8. The owner of the fish lives in the yellow house.
9. The person who drinks juice and the person in the white house are neighbours.
10. The person who keeps the rabbit and the tea drinker live two houses apart.
11. The person in the purple house lives somewhere to the left of the owner of the dog.
12. Whoever lives in the white house lives directly to the left of the farmer.
13. The person who keeps the horse lives immediately to the right of the doctor.

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
