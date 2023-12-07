# RQ4: How does the datatype of the input and output variables
affect LLM4TDD?
Conclusion: 
- String-based methods require less prompts, as they often in-
volve similar high-level steps to solve. If unique string manipu-
lations are needed, then that should be represented in the first
test to avoid ChatGPT starting off in the wrong direction.
- Integers based problems are notably vulnerable to accidentally
ambiguous test cases. In addition, names of tests could help
narrow the space of possible Integer operations to help Chat-
GPT find the right series of steps needed to solve the problem
<img width="513" alt="image" src="https://github.com/SanyogitaPiya/LLM4TDD/assets/85206339/d8ffbaf3-655d-4fe9-97be-98acf5c8571c">
