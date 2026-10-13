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

Output: write a single JSON object to the file /home/user/Puzzle-generation-with-guaranteed-uniqueness/data/llm_tasks/e1_encC/e1_encC_017.out.json with this exact structure
{"puzzles": [{"id": "<puzzle id>", "constraints": [{"clue": 1, "expr": "<expression>"}, ...]}, ...]}
One entry per puzzle and exactly one constraint per numbered clue, in order. Use single quotes inside
expressions so the JSON stays valid.

The puzzles follow.


## Puzzle paraphrase:zebra-00148

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, golf, painting, cooking, chess
- pet: fish, bird, dog, rabbit, horse
- nationality: Spaniard, Dane, Norwegian, Brit, German
- drink: tea, milk, water, juice, coffee

Clues:
1. The bird keeper and the fish keeper do not live next to each other.
2. The chess enthusiast lives next door to the tea drinker.
3. The Spaniard's house has a lower number than the water drinker's.
4. The dog owner plays tennis.
5. The rabbit owner lives immediately left of the golf enthusiast.
6. The coffee drinker does not live in house 3.
7. The Brit and the Dane are not next-door neighbours.
8. The German and the rabbit owner live two houses apart.
9. The fish owner lives directly right of the rabbit keeper.
10. The coffee drinker keeps either the fish or the horse.
11. The Spaniard is the coffee drinker.
12. Painting is the Brit's hobby.
13. The water drinker is the chess enthusiast.
14. The milk drinker keeps either the dog or the rabbit.
15. The tea drinker lives somewhere to the right of the Brit.
16. The tennis enthusiast lives somewhere to the left of the fish owner.

## Puzzle paraphrase:zebra-00177

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, cocoa, tea, juice, coffee
- job: baker, farmer, pilot, doctor, lawyer
- color: purple, yellow, green, red, white
- pet: horse, cat, fish, bird, dog

Clues:
1. The horse owner drinks tea.
2. The red house is house 5.
3. The fish owner lives immediately to the right of the juice drinker.
4. The coffee drinker lives in a lower-numbered house than the white house's occupant.
5. The juice drinker and the occupant of the yellow house have exactly one house between them.
6. The yellow house is at one end of the row.
7. The bird owner and the fish owner are two houses apart.
8. The baker lives in house 2.
9. The purple house's occupant drinks water.
10. One house stands between the dog owner and the tea drinker.
11. The cocoa drinker is the lawyer.
12. The white house is immediately to the left of the pilot's.
13. The doctor and the occupant of the white house live in adjacent houses.

## Puzzle paraphrase:zebra-00137

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Swede, Spaniard, Brit, Norwegian, German
- drink: milk, juice, coffee, cocoa, water
- hobby: cooking, golf, tennis, hiking, painting
- pet: horse, rabbit, fish, bird, cat

Clues:
1. The juice drinker lives directly to the left of the Swede.
2. The Norwegian is the coffee drinker.
3. The German lives directly to the left of the hiking enthusiast.
4. The cooking enthusiast and the hiking enthusiast are two houses apart.
5. The bird owner lives in the second house.
6. The water drinker lives immediately to the right of the German.
7. The rabbit owner is either the Brit or the Spaniard.
8. The cat owner lives somewhere to the right of the Spaniard.
9. The hiking enthusiast and the horse owner live next door to each other.
10. The tennis enthusiast lives in the second house.
11. The milk drinker lives right next to the Spaniard.
12. The Spaniard keeps either the fish or the rabbit.
13. The Swede is the golf enthusiast.

## Puzzle plain:zebra-00098

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: cooking, hiking, golf, chess, painting
- drink: tea, juice, coffee, water, milk
- pet: rabbit, bird, fish, cat, horse
- job: farmer, baker, doctor, teacher, pilot

Clues:
1. The owner of the fish and the teacher live in adjacent houses.
2. The pilot lives in the house just left of the one where the person who keeps the horse lives.
3. The owner of the horse and the water drinker are neighbours.
4. The chess enthusiast drinks water.
5. The person who drinks tea lives directly to the left of the owner of the fish.
6. The coffee drinker lives in one of the two end houses.
7. The owner of the cat and the farmer live two houses apart.
8. The farmer enjoys painting.
9. The person who keeps the bird lives next to the person who drinks milk.
10. The owner of the fish lives in house 3.
11. The doctor and the person who enjoys golf live in adjacent houses.
12. The person who enjoys cooking either works as the baker or works as the teacher.
13. The owner of the cat works as the baker.

## Puzzle paraphrase:zebra-00178

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: yellow, blue, green, purple, red
- job: farmer, doctor, baker, lawyer, teacher
- drink: juice, coffee, cocoa, milk, tea
- pet: cat, fish, rabbit, bird, horse

Clues:
1. The cocoa drinker lives immediately to the right of the farmer.
2. The doctor occupies house 5.
3. The horse is kept by the occupant of the green house.
4. The bird owner and the fish owner live next door to each other.
5. The occupant of the red house keeps either the cat or the horse.
6. The teacher lives immediately to the right of the yellow house's occupant.
7. The bird owner lives somewhere to the right of the teacher.
8. The juice drinker is not a neighbour of the teacher.
9. The occupant of the yellow house drinks either coffee or milk.
10. The coffee drinker lives immediately to the right of the yellow house's occupant.
11. The red house is house 5.
12. The bird owner lives immediately to the right of the lawyer.
13. The cocoa drinker and the purple house's occupant are two houses apart.

## Puzzle paraphrase:zebra-00164

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: hiking, painting, chess, golf, tennis
- drink: coffee, milk, water, cocoa, tea
- nationality: Norwegian, Spaniard, Swede, Dane, Brit
- color: blue, purple, red, white, yellow

Clues:
1. The painter lives in the blue house.
2. One house lies between the milk drinker and the Norwegian.
3. The blue house and the water drinker's house are next to each other.
4. Tea is drunk by whoever lives in the purple house.
5. The hiker lives further left than the Dane.
6. The Swede lives somewhere to the left of the red house's occupant.
7. The tennis player lives in house 4.
8. The Brit and the cocoa drinker are next-door neighbours.
9. The white house is the one in the middle.
10. The water drinker lives immediately to the left of the golfer.
11. The purple house's occupant lives right beside the Swede.
12. The hiker lives directly to the right of the Spaniard.

## Puzzle hard:zebra_hard-00005

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: teacher, doctor, lawyer, pilot, baker
- hobby: chess, golf, painting, tennis, hiking
- color: green, white, red, purple, blue
- pet: dog, rabbit, horse, bird, cat

Clues:
1. Exactly one house separates the owner of the bird from the person who enjoys chess.
2. The right-hand neighbour of the occupant of the blue house keeps the dog.
3. The lawyer and the occupant of the white house are one and the same person.
4. The occupant of the purple house and the teacher are one and the same person.
5. The pilot lives somewhere between the baker and the bird owner.
6. If the person who enjoys painting does not keep the cat, then that person keeps the dog.
7. If the painting enthusiast does not live in the blue house, then that person lives in the white house.
8. The left-hand neighbour of whoever lives in the red house enjoys golf.
9. Whoever lives in the white house lives further to the right than the teacher.
10. If the doctor does not enjoy golf, then that person enjoys tennis.
11. If the doctor does not keep the dog, then that person keeps the horse.
12. The lawyer does not live in the second house from the right.
13. The right-hand neighbour of the person who enjoys painting lives in the purple house.

## Puzzle paraphrase:zebra-00162

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: purple, white, yellow, red, green
- hobby: hiking, cooking, painting, golf, tennis
- pet: horse, dog, bird, cat, rabbit
- drink: juice, cocoa, milk, water, coffee

Clues:
1. The hiker and the juice drinker live in neighbouring houses.
2. The tennis player lives directly to the right of the green house's occupant.
3. The white house is the last one in the row.
4. The purple house is where the hiker lives.
5. The cooking enthusiast lives immediately to the left of the hiker.
6. The rabbit's owner lives in the white house.
7. The dog owner lives next door to the juice drinker.
8. The green house's occupant and the water drinker are neighbours.
9. The green house and the milk drinker's house stand side by side.
10. The hiker keeps either the bird or the cat.
11. The tennis player lives immediately to the right of the cat's owner.
12. The golfer lives in house 5.
13. The milk drinker lives further left in the row than the water drinker.
14. The cocoa drinker lives right next to the hiker.
15. Exactly one house separates the green house from the yellow house.

## Puzzle plain:zebra-00077

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: tennis, hiking, painting, chess, golf
- nationality: Dane, Brit, Swede, Spaniard, Norwegian
- drink: tea, juice, coffee, milk, water
- pet: bird, fish, dog, cat, rabbit

Clues:
1. The Norwegian and the Spaniard are neighbours.
2. The juice drinker lives in a lower-numbered house than the Brit.
3. The Spaniard lives directly to the left of the tea drinker.
4. The painting enthusiast lives immediately to the right of the owner of the rabbit.
5. The person who drinks milk lives next to the tennis enthusiast.
6. The person who keeps the bird and the owner of the rabbit live in adjacent houses.
7. The person who enjoys golf lives next to the hiking enthusiast.
8. The milk drinker either is the Spaniard or is the Swede.
9. The Spaniard enjoys golf.
10. The Dane lives next to the person who drinks milk.
11. The Dane lives in the house just left of the one where the Brit lives.
12. There is exactly one house between the owner of the cat and the hiking enthusiast.
13. The Spaniard either keeps the cat or keeps the fish.
14. The Norwegian drinks coffee.

## Puzzle plain:zebra-00005

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: farmer, lawyer, teacher, pilot, baker
- hobby: painting, tennis, cooking, hiking, chess
- color: purple, green, yellow, white, blue
- pet: fish, rabbit, bird, cat, dog

Clues:
1. The chess enthusiast lives in house 4.
2. The person who enjoys tennis lives in the house just left of the one where the person who enjoys hiking lives.
3. The hiking enthusiast lives directly to the left of the owner of the cat.
4. Whoever lives in the yellow house keeps the rabbit.
5. The person in the white house lives immediately to the right of the person in the green house.
6. The owner of the bird works as the baker.
7. The person in the blue house lives directly to the left of the teacher.
8. The lawyer lives in the white house.
9. The person who keeps the dog lives immediately to the right of the pilot.
10. The dog owner lives immediately to the right of the person who enjoys painting.
11. Whoever lives in the green house works as the farmer.
