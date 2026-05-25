# BalooJobber
---
Hello my name is sophie and this is my little project for scraping jobs off google/linkedin/indeed and evaluating how well your cv matches each job. the project uses A.I. models (LLMs and Cross Encoders) to evaluate the similarity and the fitness of the job to your cv. I have developed this script due to the frustration my friends have with the current job market.

### Instructions:
all you need to make this repo work is the following python version and libraries :
1. python >=3.14
2. pandas = 2.3.3
3. serpapi = 1.0.2
4. python-dotenv = 1.2.2",
5. python-jobspy = 1.1.82",
6. openai = 2.38.0",
7. torch >= 2.12.0
8. sentence_transformers = 5.5.1

you will also need to get API keys from Deepseek and Serpapi for the full functionality of the script, it works without any API keys by default and will prompt you to enter the desired job title and the city, the default location is Germany and can be changed by changing the scraping scripts.
