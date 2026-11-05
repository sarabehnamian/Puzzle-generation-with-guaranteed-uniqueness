# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_013.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-05

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- color: green, purple, red, yellow, blue, white
- hobby: golf, tennis, cooking, hiking, painting, chess
- job: teacher, doctor, pilot, lawyer, farmer, baker
- nationality: Norwegian, Brit, German, Spaniard, Dane, Swede
- pet: bird, fish, dog, rabbit, horse, cat
- drink: coffee, juice, cocoa, water, milk, tea

Clues:
1. The tennis enthusiast lives in house 5.
2. The baker and the person who drinks cocoa live in adjacent houses.
3. The Swede lives directly to the left of the milk drinker.
4. The Brit lives directly to the left of the tea drinker.
5. The doctor and the person who keeps the horse are neighbours.
6. The person who keeps the fish lives in the house just left of the one where whoever lives in the yellow house lives.
7. The owner of the horse lives somewhere to the right of the person who drinks cocoa.
8. Whoever lives in the yellow house lives in the house just left of the one where the person who enjoys hiking lives.
9. The owner of the dog enjoys hiking.
10. The person who drinks coffee either enjoys cooking or enjoys tennis.
11. The person who drinks coffee lives in the green house.
12. Whoever lives in the purple house lives in the fifth house.
13. The person who drinks coffee keeps the bird.
14. The German lives directly to the left of the Swede.
15. The doctor does not live next to the person who drinks milk.
16. The baker enjoys golf.
17. The owner of the dog either works as the doctor or works as the pilot.
18. The person who enjoys painting lives in the white house.
19. The occupant of the blue house either drinks juice or drinks tea.
20. The teacher is the Spaniard.
21. The lawyer lives immediately to the right of the person who keeps the rabbit.
22. The owner of the cat works as the teacher.
23. The occupant of the green house is not the Norwegian.
24. The person in the blue house and the milk drinker live two houses apart.
25. The teacher lives next to the pilot.
26. The person who keeps the horse lives directly to the left of the person who keeps the bird.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
