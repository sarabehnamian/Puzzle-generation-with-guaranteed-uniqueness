# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e4b_eval_g2\e4b_eval_g2_haiku_014.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle e4b-g2-10

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 6 houses in a row, numbered 1 to 6 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- hobby: chess, golf, tennis, hiking, painting, cooking
- pet: horse, fish, rabbit, cat, bird, dog
- job: teacher, pilot, lawyer, baker, farmer, doctor
- color: yellow, blue, white, purple, green, red
- nationality: Brit, Norwegian, Swede, Spaniard, Dane, German
- drink: juice, milk, cocoa, tea, coffee, water

Clues:
1. The person in the green house and the Norwegian live in adjacent houses.
2. The person who enjoys golf lives in one of the two end houses.
3. The baker keeps the dog.
4. The German lives somewhere to the left of the owner of the fish.
5. The person who keeps the dog lives next to the doctor.
6. The person who keeps the cat lives in the red house.
7. The tennis enthusiast drinks milk.
8. The occupant of the green house works as the lawyer.
9. The person in the blue house lives in one of the two end houses.
10. The cat owner lives in the house just left of the one where the teacher lives.
11. The person who keeps the dog either drinks water or drinks tea.
12. The hiking enthusiast lives immediately to the right of the doctor.
13. The person in the green house does not live next to the tennis enthusiast.
14. The Brit lives in the first house.
15. The juice drinker lives immediately to the right of the person in the white house.
16. The farmer lives somewhere to the left of the lawyer.
17. Whoever lives in the purple house lives in the house just left of the one where the German lives.
18. The Dane and the dog owner live in adjacent houses.
19. The owner of the horse and the person who drinks milk live two houses apart.
20. The person who enjoys golf lives in the house just left of the one where the chess enthusiast lives.
21. The rabbit owner is the Swede.
22. The person in the white house lives somewhere to the right of whoever lives in the yellow house.
23. The person who drinks cocoa and the milk drinker live two houses apart.
24. The cat owner lives next to the person who drinks tea.
25. The person who keeps the fish works as the doctor.
26. The cooking enthusiast and the person in the white house live two houses apart.
27. The occupant of the red house lives somewhere to the right of the baker.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
