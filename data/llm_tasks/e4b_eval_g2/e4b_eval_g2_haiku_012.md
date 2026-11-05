# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_012.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-04

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, purple, red, yellow, blue, white
- hobby: golf, tennis, cooking, hiking, painting, chess
- job: teacher, doctor, pilot, lawyer, farmer, baker
- nationality: Norwegian, Brit, German, Spaniard, Dane, Swede
- pet: bird, fish, dog, rabbit, horse, cat
- drink: coffee, juice, cocoa, water, milk, tea

Clues:
1. The fish owner lives in the house just left of the one where whoever lives in the yellow house lives.
2. The person in the blue house either drinks juice or drinks tea.
3. The person who drinks milk lives directly to the left of the owner of the dog.
4. The coffee drinker either enjoys cooking or enjoys tennis.
5. The golf enthusiast works as the baker.
6. The doctor does not live next to the milk drinker.
7. The doctor lives next to the person who keeps the horse.
8. Whoever lives in the purple house and whoever lives in the green house live in adjacent houses.
9. The Brit lives directly to the left of the tea drinker.
10. The person who enjoys tennis and the person who enjoys cooking are neighbours.
11. The Spaniard lives in house 3.
12. The Swede lives in the house just left of the one where the milk drinker lives.
13. The lawyer lives immediately to the right of the rabbit owner.
14. The occupant of the yellow house lives directly to the left of the hiking enthusiast.
15. The person in the green house drinks coffee.
16. The person who keeps the horse lives in the house just left of the one where the person who keeps the bird lives.
17. The cocoa drinker lives somewhere to the left of the owner of the horse.
18. The owner of the dog enjoys hiking.
19. The Norwegian works as the farmer.
20. The Norwegian and the occupant of the green house are different people.
21. There is exactly one house between the occupant of the blue house and the milk drinker.
22. The tennis enthusiast lives immediately to the right of the owner of the dog.
23. The dog owner either works as the doctor or works as the pilot.
24. The person in the white house enjoys painting.
25. The baker and the person who drinks cocoa live in adjacent houses.
26. The German lives in the house just left of the one where the Swede lives.
27. The teacher lives in the third house.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
