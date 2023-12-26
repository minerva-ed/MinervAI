# MinervAI
![output-onlinepngtools](https://github.com/dmavani25/MinervAI/assets/107078090/8413ebde-629f-4307-bfba-ca26f8a41b7c)

Empowering teachers through interactions with realistic simulated classrooms. MinervAI combines AI agent students with various backgrounds and proficiencies to help educators better understand students and the ways in which they think.

In this beta version of MinervAI,  language models serve as AI agents in the classroom: each is initialized with a distinct personality (ex: “confident”), background (ex: “liberal arts student with math training”) and weight factor (which varies the scale of the 2 prior features’ impact) which influences their understanding of topics.

Users can upload a “lecture file” containing important information. The text is interpreted by the professor agent, which lectures the students, who then internalize the new data and generate new questions depending on their background. The professor then provides sample answers specific to each student’s needs and knowledge gaps.

The final output of this tool is a summary file listing Q+A conversations and summary statistics regarding question types (commonly asked questions, question frequency, recurring “keyword” concepts and more).

<h2>Requirements for running</h2>

The required packages needed to run MinervAI are included in the ***requirements.txt*** file.

The semantic kernel package can be installed using the command ***python3 -m pip install semantic-kernel***.

Other packages can be installed using ***pip3 install ...***. 

Use **uvicorn server:app --reload** to run the web server, and **npm run dev** to run the frontend.