# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_opus_007.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00704-L1aug

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- nationality: Brit, Dane, German, Spaniard, Norwegian
- color: red, yellow, green, white, purple
- drink: coffee, cocoa, tea, milk, water
- pet: dog, bird, cat, horse, fish

Clues:
1. The tea drinker and whoever lives in the white house are not neighbours.
2. The coffee drinker lives in house 3.
3. The occupant of the purple house does not keep the horse.
4. The Norwegian and whoever lives in the red house are not neighbours.
5. The horse owner lives somewhere to the right of the Dane.
6. The person who keeps the dog lives in the red house.
7. The dog owner and the person who keeps the fish live in adjacent houses.
8. The cat owner lives in the second house.
9. The Norwegian lives in the purple house.
10. The person who keeps the fish drinks coffee.
11. The person in the purple house does not drink water.
12. The person who drinks tea is the German.
13. The person in the yellow house either drinks cocoa or drinks water.
14. The cocoa drinker lives directly to the left of whoever lives in the green house.
15. The person who drinks coffee and the person in the yellow house are neighbours.
16. There is exactly one house between the fish owner and the person who drinks milk.
17. Whoever lives in the white house does not keep the cat.
18. The occupant of the purple house is not the Spaniard.
19. Whoever lives in the green house does not live next to the person who drinks water.
20. The owner of the fish lives in the white house.
21. The water drinker lives in a lower-numbered house than the person who keeps the dog.
22. The occupant of the yellow house lives in a lower-numbered house than the Brit.
23. Whoever lives in the red house lives in the fourth house.
24. The cocoa drinker is the Brit.
25. The Spaniard drinks water.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
