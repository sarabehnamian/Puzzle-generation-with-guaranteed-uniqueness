# Task: solve logic puzzles

Solve each puzzle below by reasoning. Every puzzle has exactly one solution. Work carefully; you
cannot run code. Give a complete answer for every puzzle even if unsure.

Output: write a single JSON object to the file D:\Puzzle-generation-with-guaranteed-uniqueness\data\llm_tasks\e3_solve\e3_zebra_haiku_002.out.json with this exact structure
{"answers": [{"id": "<puzzle id>", "answer": <answer>}, ...]}
where <answer> has the format stated for each puzzle.

The puzzles follow.


## Puzzle zebra-00618

Grid logic puzzle. Deduce which value of each category belongs to each house. Every value is used exactly once.

There are 5 houses in a row, numbered 1 to 5 from left to right. Each house has one occupant. Every occupant has exactly one value from each category below, and no two occupants share a value within a category.
- job: lawyer, doctor, baker, teacher, pilot
- drink: juice, milk, tea, water, cocoa
- nationality: Swede, German, Dane, Norwegian, Brit
- pet: dog, rabbit, fish, cat, horse

Clues:
1. The teacher drinks water.
2. The rabbit owner drinks tea.
3. The Norwegian and the Swede live two houses apart.
4. The dog owner lives immediately to the right of the pilot.
5. The milk drinker lives in the house just left of the one where the Swede lives.
6. The owner of the horse lives next to the owner of the rabbit.
7. The owner of the fish lives next to the person who drinks milk.
8. The doctor lives in the middle house.
9. The person who keeps the horse works as the doctor.
10. The Dane works as the lawyer.
11. The juice drinker lives in the third house.
12. The Brit and the person who keeps the horse live two houses apart.
13. The baker lives immediately to the right of the milk drinker.

Answer format for this puzzle: {"1": {"<category>": "<value>", ...}, "2": {...}, ...} -- one entry per house number, giving the value of every category.
