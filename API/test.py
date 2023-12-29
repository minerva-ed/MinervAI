from agents.CustomerAgent import CustomerAgent                                               
from agents.SalesAgent import SalesAgent
import asyncio

s = SalesAgent()
s.transcript = """Sales Representative: Good morning everyone! Thank you for joining me today. I'm excited to introduce you to our innovative sales training software. Now, let's dive right in and explore what makes our product stand out from the competition.

First, let's talk about our product definition. Our sales training software combines advanced AI simulations with effective pedagogy principles. It's designed specifically for high-stakes customer interactions, allowing sales professionals like yourselves to practice and refine your skills in a risk-free environment. Our platform offers a unique interface where you can engage with a variety of simulated customers, each presenting different questions and scenarios. This means you can experience the real-world diversity of B2B software sales, pharmaceutical sales, and even VC pitches, all from the comfort of your own training space.

Now, let's move on to the key features of our software. One of the standout features is the ability to interact with a range of AI-generated customers. These customers have distinct queries and behaviors, simulating the diversity you encounter in real-life customer profiles. This ensures that you're prepared for any type of customer interaction.

Our training process consists of two stages. First, you'll go through an initial learning phase where you'll watch an AI simulated sales or client interaction. This sets the foundation for your training. Then, you'll move on to practical simulations where you'll receive live feedback. This hands-on approach allows you to apply what you've learned and receive immediate guidance.

But what sets us apart is our data-driven customization. We gather data during the simulations to continually refine and personalize the training material. This ensures that the training realistically portrays your clients and targets the specific needs of your business. We believe in a homogenized product approach, meaning our software provides a standardized yet adaptable training experience suitable for businesses of all sizes and types. This scalability is crucial in meeting the diverse needs of our market.

Speaking of our market, let's define it. Our primary market includes businesses of various sizes and industries that are looking to enhance their sales team's performance through sales and client handling training. We understand the needs of this market, and that's why we've developed a product that addresses these needs head-on.

In summary, our product offers a sophisticated blend of multi-agent AI simulation and pedagogically informed training methods. It provides a realistic and diverse simulation environment for sales training, while also ensuring continual improvement and customization through data-driven insights. We're here to meet the growing demand for effective, risk-free, and adaptive sales training.

Thank you for your attention so far. Now, let's open the floor for any questions or further discussion.
Could you elaborate on how the AI simulations are tailored to reflect the specific sales scenarios and client profiles that are relevant to our industry?
Could you elaborate on how the AI simulations are tailored to reflect the specific customer interaction scenarios encountered in the fast food industry, particularly for a company like ours that primarily sells burgers?
Could you please clarify how the data-driven customization process ensures that the training material is specifically tailored to the needs of a retail company focused primarily on grocery sales?
Could you elaborate on how the AI-generated customer profiles are developed and how they ensure a realistic representation of our specific client base?
SALES prompt: Provide a detailed answer to the following question received after receiving the sales transcribed as: "Sales Pitch Transcript:

Sales Representative: Good morning everyone! Thank you for joining me today. I'm excited to introduce you to our innovative sales training software. Now, let's dive right in and explore what makes our product stand out from the competition.

First, let's talk about our product definition. Our sales training software combines advanced AI simulations with effective pedagogy principles. It's designed specifically for high-stakes customer interactions, allowing sales professionals like yourselves to practice and refine your skills in a risk-free environment. Our platform offers a unique interface where you can engage with a variety of simulated customers, each presenting different questions and scenarios. This means you can experience the real-world diversity of B2B software sales, pharmaceutical sales, and even VC pitches, all from the comfort of your own training space.

Now, let's move on to the key features of our software. One of the standout features is the ability to interact with a range of AI-generated customers. These customers have distinct queries and behaviors, simulating the diversity you encounter in real-life customer profiles. This ensures that you're prepared for any type of customer interaction.

Our training process consists of two stages. First, you'll go through an initial learning phase where you'll watch an AI simulated sales or client interaction. This sets the foundation for your training. Then, you'll move on to practical simulations where you'll receive live feedback. This hands-on approach allows you to apply what you've learned and receive immediate guidance.

But what sets us apart is our data-driven customization. We gather data during the simulations to continually refine and personalize the training material. This ensures that the training realistically portrays your clients and targets the specific needs of your business. We believe in a homogenized product approach, meaning our software provides a standardized yet adaptable training experience suitable for businesses of all sizes and types. This scalability is crucial in meeting the diverse needs of our market.

Speaking of our market, let's define it. Our primary market includes businesses of various sizes and industries that are looking to enhance their sales team's performance through sales and client handling training. We understand the needs of this market, and that's why we've developed a product that addresses these needs head-on.

In summary, our product offers a sophisticated blend of multi-agent AI simulation and pedagogically informed training methods. It provides a realistic and diverse simulation environment for sales training, while also ensuring continual improvement and customization through data-driven insights. We're here to meet the growing demand for effective, risk-free, and adaptive sales training.

Thank you for your attention so far. Now, let's open the floor for any questions or further discussion." Your customer Google described as "An internet company which builds serach engines. Most of its revenue comes from ads.": Could you elaborate on how the AI simulations are tailored to reflect the specific sales scenarios and client profiles that are relevant to our industry?? Answer concisely.
SALES prompt: Provide a detailed answer to the following question received after receiving the sales transcribed as: "Sales Pitch Transcript:

Sales Representative: Good morning everyone! Thank you for joining me today. I'm excited to introduce you to our innovative sales training software. Now, let's dive right in and explore what makes our product stand out from the competition.

First, let's talk about our product definition. Our sales training software combines advanced AI simulations with effective pedagogy principles. It's designed specifically for high-stakes customer interactions, allowing sales professionals like yourselves to practice and refine your skills in a risk-free environment. Our platform offers a unique interface where you can engage with a variety of simulated customers, each presenting different questions and scenarios. This means you can experience the real-world diversity of B2B software sales, pharmaceutical sales, and even VC pitches, all from the comfort of your own training space.

Now, let's move on to the key features of our software. One of the standout features is the ability to interact with a range of AI-generated customers. These customers have distinct queries and behaviors, simulating the diversity you encounter in real-life customer profiles. This ensures that you're prepared for any type of customer interaction.

Our training process consists of two stages. First, you'll go through an initial learning phase where you'll watch an AI simulated sales or client interaction. This sets the foundation for your training. Then, you'll move on to practical simulations where you'll receive live feedback. This hands-on approach allows you to apply what you've learned and receive immediate guidance.

But what sets us apart is our data-driven customization. We gather data during the simulations to continually refine and personalize the training material. This ensures that the training realistically portrays your clients and targets the specific needs of your business. We believe in a homogenized product approach, meaning our software provides a standardized yet adaptable training experience suitable for businesses of all sizes and types. This scalability is crucial in meeting the diverse needs of our market.

Speaking of our market, let's define it. Our primary market includes businesses of various sizes and industries that are looking to enhance their sales team's performance through sales and client handling training. We understand the needs of this market, and that's why we've developed a product that addresses these needs head-on.

In summary, our product offers a sophisticated blend of multi-agent AI simulation and pedagogically informed training methods. It provides a realistic and diverse simulation environment for sales training, while also ensuring continual improvement and customization through data-driven insights. We're here to meet the growing demand for effective, risk-free, and adaptive sales training.

Thank you for your attention so far. Now, let's open the floor for any questions or further discussion." Your customer McDonalds described as "A fast food company which sells burgers. Most of its revenue comes from selling burgers.": Could you elaborate on how the AI simulations are tailored to reflect the specific customer interaction scenarios encountered in the fast food industry, particularly for a company like ours that primarily sells burgers?? Answer concisely.
SALES prompt: Provide a detailed answer to the following question received after receiving the sales transcribed as: "Sales Pitch Transcript:

Sales Representative: Good morning everyone! Thank you for joining me today. I'm excited to introduce you to our innovative sales training software. Now, let's dive right in and explore what makes our product stand out from the competition.

First, let's talk about our product definition. Our sales training software combines advanced AI simulations with effective pedagogy principles. It's designed specifically for high-stakes customer interactions, allowing sales professionals like yourselves to practice and refine your skills in a risk-free environment. Our platform offers a unique interface where you can engage with a variety of simulated customers, each presenting different questions and scenarios. This means you can experience the real-world diversity of B2B software sales, pharmaceutical sales, and even VC pitches, all from the comfort of your own training space.

Now, let's move on to the key features of our software. One of the standout features is the ability to interact with a range of AI-generated customers. These customers have distinct queries and behaviors, simulating the diversity you encounter in real-life customer profiles. This ensures that you're prepared for any type of customer interaction.

Our training process consists of two stages. First, you'll go through an initial learning phase where you'll watch an AI simulated sales or client interaction. This sets the foundation for your training. Then, you'll move on to practical simulations where you'll receive live feedback. This hands-on approach allows you to apply what you've learned and receive immediate guidance.

But what sets us apart is our data-driven customization. We gather data during the simulations to continually refine and personalize the training material. This ensures that the training realistically portrays your clients and targets the specific needs of your business. We believe in a homogenized product approach, meaning our software provides a standardized yet adaptable training experience suitable for businesses of all sizes and types. This scalability is crucial in meeting the diverse needs of our market.

Speaking of our market, let's define it. Our primary market includes businesses of various sizes and industries that are looking to enhance their sales team's performance through sales and client handling training. We understand the needs of this market, and that's why we've developed a product that addresses these needs head-on.

In summary, our product offers a sophisticated blend of multi-agent AI simulation and pedagogically informed training methods. It provides a realistic and diverse simulation environment for sales training, while also ensuring continual improvement and customization through data-driven insights. We're here to meet the growing demand for effective, risk-free, and adaptive sales training.

Thank you for your attention so far. Now, let's open the floor for any questions or further discussion." Your customer Walmart described as "A retail company which sells groceries. Most of its revenue comes from selling groceries.": Could you please clarify how the data-driven customization process ensures that the training material is specifically tailored to the needs of a retail company focused primarily on grocery sales?? Answer concisely.
SALES prompt: Provide a detailed answer to the following question received after receiving the sales transcribed as: "Sales Pitch Transcript:

Sales Representative: Good morning everyone! Thank you for joining me today. I'm excited to introduce you to our innovative sales training software. Now, let's dive right in and explore what makes our product stand out from the competition.

First, let's talk about our product definition. Our sales training software combines advanced AI simulations with effective pedagogy principles. It's designed specifically for high-stakes customer interactions, allowing sales professionals like yourselves to practice and refine your skills in a risk-free environment. Our platform offers a unique interface where you can engage with a variety of simulated customers, each presenting different questions and scenarios. This means you can experience the real-world diversity of B2B software sales, pharmaceutical sales, and even VC pitches, all from the comfort of your own training space.

Now, let's move on to the key features of our software. One of the standout features is the ability to interact with a range of AI-generated customers. These customers have distinct queries and behaviors, simulating the diversity you encounter in real-life customer profiles. This ensures that you're prepared for any type of customer interaction.

Our training process consists of two stages. First, you'll go through an initial learning phase where you'll watch an AI simulated sales or client interaction. This sets the foundation for your training. Then, you'll move on to practical simulations where you'll receive live feedback. This hands-on approach allows you to apply what you've learned and receive immediate guidance.

But what sets us apart is our data-driven customization. We gather data during the simulations to continually refine and personalize the training material. This ensures that the training realistically portrays your clients and targets the specific needs of your business. We believe in a homogenized product approach, meaning our software provides a standardized yet adaptable training experience suitable for businesses of all sizes and types. This scalability is crucial in meeting the diverse needs of our market.

Speaking of our market, let's define it. Our primary market includes businesses of various sizes and industries that are looking to enhance their sales team's performance through sales and client handling training. We understand the needs of this market, and that's why we've developed a product that addresses these needs head-on.

In summary, our product offers a sophisticated blend of multi-agent AI simulation and pedagogically informed training methods. It provides a realistic and diverse simulation environment for sales training, while also ensuring continual improvement and customization through data-driven insights. We're here to meet the growing demand for effective, risk-free, and adaptive sales training.

Thank you for your attention so far. Now, let's open the floor for any questions or further discussion."""
c = CustomerAgent("Google","An internet company which builds serach engines. Most of its revenue comes from ads.")
asyncio.run(s.answer_question(c, "How do you get the data for the customers?"))