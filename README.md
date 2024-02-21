## This repository contains Minerva, a classroom simulator which won 1st place at HackUMass2023. We have productionized this prototype into a softawre as a service targeting sales team, which can be found [here](https://minervai.co)
# MinervAI
![output-onlinepngtools](https://github.com/dmavani25/MinervAI/assets/107078090/8413ebde-629f-4307-bfba-ca26f8a41b7c)
![demo](demo.png)

Empowering teachers through interactions with realistic simulated classrooms. MinervAI combines AI agent students with various backgrounds and proficiencies to help educators better understand students and the ways in which they think.

In this beta version of MinervAI,  language models serve as AI agents in the classroom: each is initialized with a distinct personality (ex: “confident”), background (ex: “liberal arts student with math training”) and weight factor (which varies the scale of the 2 prior features’ impact) which influences their understanding of topics.

Users can upload a “lecture file” containing important information. The text is interpreted by the professor agent, which lectures the students, who then internalize the new data and generate new questions depending on their background. The professor then provides sample answers specific to each student’s needs and knowledge gaps.

The final output of this tool is a summary file listing Q+A conversations and summary statistics regarding question types (commonly asked questions, question frequency, recurring “keyword” concepts and more).

## API and Frontend

The API is built partially with SemanticKernel to manage different contexts and connections to LLM providers (we use OpenAI's chat-gpt-3.5 and chat-gpt-4-turbo). You can test this out by running `python3 server.py`.

Also included is a websocket web server which allows for asynchronous connection to the API, to stream results. This server is built with FastAPI and Uvicorn, which can be executed by `uvicorn server:app --reload`.

Finally, the front-end server can be started by calling `npm run dev`, more information is found in the `frontend` directory.

Use **uvicorn server:app --reload** to run the web server, and **npm run dev** to run the frontend.

<h2>Requirements for running</h2>

The required packages needed to run MinervAI are included in the ***requirements.txt*** file.

All packages can be installed using `pip3 install -r requirements.txt` command. 

## MinervAI - Team Contributions

MinervAI is an innovative educational tool designed to empower teachers through interactions with AI-simulated classrooms. This project was developed as part of the HackUMass XI Hackathon, where it was awarded the **Grand Overall Prize**.

We would like to firstly thank Taichi Kato (one of our pivotal founding members) for giving an awesome introduction to Semantic Kernels, and making pivotal contributions to the project with us!!

### Team Members & Contributions

Developed by Taichi Kato, Tina Zhang, Dhyey Mavani, Seb Brown, Muhammad Ahsan Tahir, and Sawyer Pollard. All are current students of Amherst College.
