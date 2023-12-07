# LLM4TDD: Best Practices for Test Driven Development Using LLMs
Welcome to the GitHub page dedicated to our research on Test-Driven Development (TDD) using large language models, specifically focusing on ChatGPT. In this repository, we explore the intersection of large language models with software testing methodologies, providing guidelines and recommendations for effective TDD practices when leveraging large language models like ChatGPT.

## Features and Key Components

- To evaluate the efficacy of TDD with ChatGPT, we selected a set of problems from LeetCode, a platform renowned for its algorithmic challenges. 
- Our experiments leverage the GPT-3.5 architecture,a state-of-the-art language model developed by OpenAI, to analyze and generate test cases. 
- We explore various software testing strategies like Input Space Partitioning techniques to ensure thorough testing coverage across different input domains

<img width="378" alt="Flowchart2" src="https://github.com/SanyogitaPiya/LLM4TDD/assets/85206339/19b5c743-a23f-486e-af5d-9a9638766112">


## Tech

This research uses a number of open source projects and tools:

- [LeetCode] - The online platform for coding and algorithmic problems intended for users of different skill set
- [Pynguin] - Pynguin is a command line tool written in Python that allows to automatically generate unit tests for Python programs.
- [GPT-3.5] - A set of models that improve on GPT-3 and can understand as well as generate natural language or code
- [Pytest] - Pytest is a Python testing framework that originated from the PyPy project. It can be used to write various types of software tests, including unit tests, integration tests, end-to-end tests, and functional tests. 


## Contents

This research addresses number of research questions:

- [RQ1] - What is the performance of LLM4TDD?
- [RQ2] - What attributes of the test cases impact LLM4TDD?
- [RQ3] - Are manual or automatic test suites better for LLM4TDD?
- [RQ4] - How does the datatype of the input and output variables affect LLM4TDD?
- [RQ5] - How does the test prompt template impact the performance of LLM4TDD?
- [RQ6] - When the same failing code is repeated for multiple iterations, is the source of these code snippets traceable to solution blogs
or discussion group posts?
- [RQ7] -How does ChatGPT’s performance differ for LeetCode problems before and after its knowledge cutoff? 

   [RQ1]: <https://github.com/SanyogitaPiya/LLM4TDD/tree/main/RQ1>
   [RQ2]: <https://github.com/SanyogitaPiya/LLM4TDD/tree/main/RQ2>
   [RQ3]: <https://github.com/SanyogitaPiya/LLM4TDD/tree/main/RQ3>
   [RQ4]: <https://github.com/SanyogitaPiya/LLM4TDD/tree/main/RQ4>
   [RQ5]: <https://github.com/SanyogitaPiya/LLM4TDD/tree/main/RQ5>
   [RQ6]: <https://github.com/SanyogitaPiya/LLM4TDD/tree/main/RQ6>
   [RQ7]: <https://github.com/SanyogitaPiya/LLM4TDD/tree/main/RQ7>
   [LeetCode]: <https://leetcode.com/>
   [Pynguin]: <https://www.pynguin.eu/>
   [GPT-3.5]:<https://platform.openai.com/docs/models>
   [Pytest]: <https://docs.pytest.org/en/7.4.x/>
