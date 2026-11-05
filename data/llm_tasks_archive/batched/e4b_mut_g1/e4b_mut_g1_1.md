# Task: make fair logic puzzles harder for language-model solvers

Each puzzle below is a 6-house logic-grid puzzle with a known unique solution. A language-model
solver attempted it; its mistakes are listed. Propose 2 variants of each puzzle that you expect to
be HARDER for a language-model solver, while staying solvable by pure step-by-step deduction.

You edit puzzles with operations on the formal clue list:
- {"op": "remove", "clue": <clue number>}
- {"op": "add", "clue": {"type": <type>, "args": [...]}}
- {"op": "replace", "clue": <clue number>, "with": {"type": <type>, "args": [...]}}
Use 1 to 4 operations per variant. Clue types (a, b, c are value names; k is a house number):
  same(a,b)        a and b belong to the same person
  not_same(a,b)    a and b belong to different people
  at(a,k)          a is in house k            not_at(a,k)     a is not in house k
  left_of(a,b)     a is directly left of b    next_to(a,b)    a and b are neighbours
  not_next_to(a,b) a and b are not neighbours (they may share a house)
  before(a,b)      a is somewhere left of b   gap2(a,b)       exactly one house between a and b
  end(a)           a is in house 1 or house 6
  or(a,b,c)        a is with b or with c (b and c from the same category)
Every clue you add must be TRUE of the stated solution. A program will apply your edits, add a clue
if the result is no longer unique, and reject variants that need guessing, so focus on what makes the
deduction harder to follow (for example: fewer direct position clues, longer chains of inference,
negative and relative clues, information spread across many clues).

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_mut_g1\e4b_mut_g1_1.out.json with this structure
{"variants": [{"parent": "<puzzle id>", "ops": [<op>, ...], "idea": "<one short sentence>"}, ...]}
with 2 variants per puzzle.

The puzzles follow.


## Puzzle e4b-g0-05

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, yellow, white, red, purple, blue
- job: teacher, farmer, pilot, baker, lawyer, doctor
- drink: cocoa, juice, milk, water, coffee, tea
- pet: horse, dog, bird, fish, rabbit, cat
- nationality: Spaniard, Swede, German, Brit, Dane, Norwegian
- hobby: hiking, golf, tennis, cooking, painting, chess

Formal clues (with their English text):
1. gap2(chess, lawyer)   "There is exactly one house between the chess enthusiast and the lawyer."
2. or(baker, horse, rabbit)   "The baker either keeps the horse or keeps the rabbit."
3. at(german, 6)   "The German lives in house 6."
4. same(blue, juice)   "The person who drinks juice lives in the blue house."
5. gap2(farmer, red)   "The farmer and the person in the red house live two houses apart."
6. left_of(tea, green)   "The tea drinker lives directly to the left of the person in the green house."
7. left_of(yellow, horse)   "The horse owner lives immediately to the right of whoever lives in the yellow house."
8. same(golf, lawyer)   "The lawyer enjoys golf."
9. next_to(norwegian, yellow)   "The Norwegian and the occupant of the yellow house are neighbours."
10. same(brit, white)   "The occupant of the white house is the Brit."
11. left_of(water, swede)   "The water drinker lives in the house just left of the one where the Swede lives."
12. or(rabbit, dane, german)   "The owner of the rabbit either is the Dane or is the German."
13. same(coffee, painting)   "The person who enjoys painting drinks coffee."
14. not_same(coffee, purple)   "The person in the purple house does not drink coffee."
15. same(bird, farmer)   "The farmer keeps the bird."
16. gap2(blue, doctor)   "The person in the blue house and the doctor live two houses apart."
17. left_of(rabbit, horse)   "The rabbit owner lives directly to the left of the owner of the horse."
18. next_to(golf, tea)   "The golf enthusiast and the person who drinks tea are neighbours."
19. next_to(cat, purple)   "The cat owner lives next to the person in the purple house."
20. or(cocoa, doctor, pilot)   "The person who drinks cocoa either works as the doctor or works as the pilot."
21. same(cooking, fish)   "The fish owner enjoys cooking."
22. next_to(green, tennis)   "The person in the green house lives next to the tennis enthusiast."
23. left_of(norwegian, german)   "The Norwegian lives in the house just left of the one where the German lives."
24. or(dog, lawyer, teacher)   "The owner of the dog either works as the lawyer or works as the teacher."
25. same(tennis, white)   "The person in the white house enjoys tennis."

Solution: house 1: brit, dog, tea, teacher, tennis, white; house 2: cat, golf, green, lawyer, spaniard, water; house 3: bird, farmer, hiking, milk, purple, swede; house 4: chess, cocoa, dane, doctor, rabbit, yellow; house 5: baker, coffee, horse, norwegian, painting, red; house 6: blue, cooking, fish, german, juice, pilot
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle e4b-g0-06

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: juice, cocoa, milk, coffee, tea, water
- nationality: Brit, German, Norwegian, Spaniard, Dane, Swede
- pet: dog, cat, horse, fish, bird, rabbit
- color: white, purple, yellow, green, red, blue
- job: farmer, baker, teacher, pilot, lawyer, doctor
- hobby: painting, tennis, hiking, golf, chess, cooking

Formal clues (with their English text):
1. left_of(brit, blue)   "The person in the blue house lives immediately to the right of the Brit."
2. before(teacher, painting)   "The teacher lives in a lower-numbered house than the person who enjoys painting."
3. gap2(cooking, yellow)   "The cooking enthusiast and whoever lives in the yellow house live two houses apart."
4. same(juice, white)   "The person who drinks juice lives in the white house."
5. same(teacher, white)   "The teacher lives in the white house."
6. left_of(dane, farmer)   "The Dane lives directly to the left of the farmer."
7. same(horse, purple)   "The owner of the horse lives in the purple house."
8. same(spaniard, tennis)   "The tennis enthusiast is the Spaniard."
9. not_next_to(bird, fish)   "The person who keeps the bird and the owner of the fish are not neighbours."
10. or(golf, farmer, pilot)   "The person who enjoys golf either works as the farmer or works as the pilot."
11. next_to(coffee, norwegian)   "The person who drinks coffee and the Norwegian live in adjacent houses."
12. at(chess, 2)   "The chess enthusiast lives in house 2."
13. gap2(cocoa, spaniard)   "The cocoa drinker and the Spaniard live two houses apart."
14. left_of(tennis, cooking)   "The tennis enthusiast lives in the house just left of the one where the cooking enthusiast lives."
15. left_of(rabbit, tennis)   "The rabbit owner lives in the house just left of the one where the tennis enthusiast lives."
16. at(bird, 2)   "The bird owner lives in house 2."
17. not_same(dane, milk)   "The Dane and the person who drinks milk are different people."
18. same(golf, swede)   "The Swede enjoys golf."
19. same(doctor, red)   "The occupant of the red house works as the doctor."
20. same(brit, white)   "The Brit lives in the white house."
21. same(dog, german)   "The German keeps the dog."
22. left_of(water, white)   "The occupant of the white house lives immediately to the right of the person who drinks water."
23. same(baker, green)   "The baker lives in the green house."
24. at(golf, 3)   "The golf enthusiast lives in house 3."
25. next_to(doctor, tennis)   "The doctor and the person who enjoys tennis live in adjacent houses."

Solution: house 1: baker, dog, german, green, hiking, water; house 2: bird, brit, chess, juice, teacher, white; house 3: blue, cat, cocoa, golf, pilot, swede; house 4: dane, lawyer, painting, rabbit, tea, yellow; house 5: coffee, farmer, horse, purple, spaniard, tennis; house 6: cooking, doctor, fish, milk, norwegian, red
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00

## Puzzle e4b-g1-03

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- drink: water, milk, juice, cocoa, tea, coffee
- color: purple, white, red, yellow, blue, green
- nationality: German, Dane, Swede, Norwegian, Spaniard, Brit
- hobby: cooking, golf, hiking, chess, painting, tennis
- job: pilot, baker, teacher, doctor, lawyer, farmer
- pet: horse, rabbit, cat, fish, bird, dog

Formal clues (with their English text):
1. next_to(coffee, cocoa)   "The coffee drinker lives next to the cocoa drinker."
2. same(cooking, german)   "The person who enjoys cooking is the German."
3. same(baker, tea)   "The tea drinker works as the baker."
4. same(painting, water)   "The person who drinks water enjoys painting."
5. left_of(norwegian, fish)   "The Norwegian lives directly to the left of the owner of the fish."
6. same(brit, white)   "The occupant of the white house is the Brit."
7. same(pilot, yellow)   "Whoever lives in the yellow house works as the pilot."
8. at(dane, 3)   "The Dane lives in the third house."
9. gap2(bird, lawyer)   "The owner of the bird and the lawyer live two houses apart."
10. before(red, spaniard)   "The Spaniard lives somewhere to the right of the occupant of the red house."
11. next_to(brit, purple)   "The Brit and whoever lives in the purple house are neighbours."
12. left_of(baker, milk)   "The person who drinks milk lives immediately to the right of the baker."
13. gap2(lawyer, milk)   "The lawyer and the person who drinks milk live two houses apart."
14. left_of(blue, brit)   "The occupant of the blue house lives in the house just left of the one where the Brit lives."
15. next_to(chess, doctor)   "The person who enjoys chess and the doctor are neighbours."
16. before(red, rabbit)   "The occupant of the red house lives in a lower-numbered house than the person who keeps the rabbit."
17. or(juice, horse, rabbit)   "The person who drinks juice either keeps the horse or keeps the rabbit."
18. left_of(teacher, blue)   "The teacher lives directly to the left of the occupant of the blue house."
19. same(milk, tennis)   "The person who enjoys tennis drinks milk."
20. next_to(fish, horse)   "The person who keeps the fish and the owner of the horse are neighbours."
21. same(golf, spaniard)   "The Spaniard enjoys golf."
22. or(lawyer, milk, water)   "The lawyer either drinks milk or drinks water."
23. at(cocoa, 5)   "The cocoa drinker lives in house 5."
24. same(dog, water)   "The dog owner drinks water."
25. before(cat, fish)   "The person who keeps the cat lives in a lower-numbered house than the owner of the fish."

Solution: house 1: baker, cat, cooking, german, red, tea; house 2: bird, milk, pilot, swede, tennis, yellow; house 3: dane, green, hiking, juice, rabbit, teacher; house 4: blue, dog, lawyer, norwegian, painting, water; house 5: brit, chess, cocoa, farmer, fish, white; house 6: coffee, doctor, golf, horse, purple, spaniard
Solver mistakes: none - the solver got it fully right
Solver cell accuracy so far: 1.00
