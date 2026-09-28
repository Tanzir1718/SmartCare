# Comparison: Human-Written Version vs. AI-Generated Version

| Question | Human version | AI version |
| :--- | :--- | :--- |
| **Easy to understand?** | Yes, very straightforward with basic lists, dictionaries, and simple print statements. | Mostly yes, though AI code sometimes introduces complex helper classes or built-in libraries unnecessarily. |
| **Runs successfully?** | Yes, runs cleanly without requiring external packages. | Yes, provided no overly complex libraries were suggested. |
| **Uses only required features?** | Yes, sticks strictly to variables, lists, dictionaries, and functions. | Sometimes adds extra features like CLI menus, classes, or data validation libraries. |
| **Adds assumptions?** | Minimal; only assumes the basic fields (patient, practitioner, time). | Might assume persistent file storage (JSON/CSV) or interactive command-line loops. |
| **Handles errors?** | Basic check for empty patient names (`ValueError`). | Usually includes more robust exception handling and edge-case validation. |
| **Could I explain it?** | Yes, every single line was written and structured manually. | Yes, after reviewing the generated logic line by line. |