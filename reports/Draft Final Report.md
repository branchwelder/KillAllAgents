
# Kill All Agents: An Investigation of Infectious Disease and Agent Based Modeling
### Kathryn Hite, Brenna Manning, Hannah Twigg-Smith
### Complexity Science 2016
________________________________

## Abstract
In this paper, we investigate the influence that individual people have on human health and disease spread at the scale of larger populations. We perform several smaller experiments using an agent based model of the spread of infectious disease in humans. We first create a simple agent-based model in a two dimensional cellular automata which models the spread of a disease by interpersonal contact, such as the common cold. From there, we add more features to investigate the different human attributes that may alter the spread of disease, including the sociability and immunity of agents. Allowing agent clustering on the cellular automata to represent “cities” or social networks in our model, as well as changing parameters corresponding to other real world situations demonstrates how disease spread may be impacted by these factors as they exist in the real world.
## Experiments
We first create a simple model of a disease such as the flu, which spreads by interpersonal contact. This model is an agent-based two-dimensional cellular automaton with few rules. Once verified against existing models, this simple model is used as the foundation for experiments based on those found in relevant papers. Each of these experiments are focused around changing some parameter in the model that corresponds to a potential real world factor,  seeing how this change impacts the model, and using what we learn from those impacts to draw insights about the world.

## Experiment: The Simple Model

### Question

The purpose of this experiment is to observe how disease spreads through this simulated population of agents with few rules. We determine from this simple model whether our basic simulation is a reasonable enough abstraction of the human population to use as a baseline for future experiments.

### Methodology

In this model, we generate a world that is filled with agents. This world is represented with a 2-D array of cells where each cell corresponds to an agent and its location in space. We initialize this world with dimensions, n (the default number of agents is n * n), and the number of agents that are initially sick. The more sick/contagious agents are adjacent to a healthy agent in space, the higher likelihood there is that that healthy agent will become sick. After becoming sick agents will eventually recover and be immune to catching the sickness again.
In the visual representation linked below, the light orange squares are healthy agents and the dark blue squares represent sick agents. In the animation you can see the disease spreading through the population.

### Results

[Simple Model Animation](https://www.youtube.com/watch?v=FU0oUiNzODU)

As the model runs, the number of agents sick in the population increases until it reaches a peak. After this peak, there were no more newly infected/contagious agents, and the number of sick agents was eventually reduced to zero as the agents recover and move into the healthy state. This aligns with what we would expect, since after an agent has recovered it does not get sick again, essentially becoming immune to the disease. As you can see in the animation, in this run of this model every agent in the array eventually caught the disease. We also observe an interesting pattern of disease spreading in waves traveling across the array.


### Interpretation

After running this simulation several times and observing the animations it generates, we compare our results to figures from articles such as this simulation of H1N1 influenza in Japan in 2009.  
H Yasuda, K Suzuki


Comparing our results to this and similar results in articles and academic papers, we consider our simulation to be a reasonable abstraction and we use it as a foundation for further experimentation. 

## Experiment: Moving Agents vs Still

### Question 
The purpose of this experiment is to learn what impact agents randomly moving around the array has on the spread of disease through the population. People in the real world do not stay in contact with the same 8 neighbors all the time. We are curious how this will impact the "wave" effect we observe in the simple model of disease spread.

### Methodology

In order to simulate individuals moving about in the world and interacting with different groups of people, we had agents move to different positions in the array. We initialized the array with a certain number of empty squares. Every step of the simulation, a randomly selected agent would move to a randomly selected empty location on the grid, giving it a new set of neighbors to interact with. Agents who are healthy or contagious but not sick all have equal likelihood of being selected to move. In this implementation, sick agents remain still.
R: results; what happened when you ran the experiment?


Link to [Still Agents Animation](https://www.youtube.com/watch?v=_897x1_opTI)
Link to [Moving Agents Animation](https://www.youtube.com/watch?v=8e2uW6XcKUQ)


In the still agents with some empty spaces animation, we observe the empty squares acting almost like walls, keeping the disease within a certain area of the grid before allowing it to spread further. This leads to a decrease in the severity of peaks in  how many agents are sick.  Even if the disease was to eventually spread to all or most agents, there is not ever a time where as many are as sick at one time, compared to when there are not empty spaces.

In the moving agents animation we observe the opposite effect. More agents get sick faster, because more agents end up being neighbors with the agents who are sick.  This can be observed in the animation, which was of a simulation where one agent moved each step.

The figure below further shows this effect by increasing the number of agents who move to a new space each time step and showing how the height of the peak of sick agents changes as this increases.  As the number of agents moving each time step increases, the value of the peak number of agents that are sick at one time also increases

This graph shows the number of agents in each health category over time for simulations run where there were between 0-20 agents moving each time step.

This confirms again for us that the more agents move around within the array and the more other agents they are able to interact with, the quicker and higher the number of sick people in the population will spike. Sickness spreads faster and to more people.

### Interpretation

We determine from these results that whether or not an agent moves around a lot in space does have an impact on how disease spreads through that agent’s population. Even if only one agent is moving every time step it makes a pretty significant difference.  Similarly in the real world, people who interact with more other people have a greater chance of getting sick or spreading illness if they are already contagious. 

## Experiment: Health Status Over Time of Introverted Agents vs Extroverted Agents

### Question

In this experiment we determine the effect that the sociability of agents can have on the infection rate of the entire population.  Does the introversion or extroversion of an individual agent change the sickness of the population as a whole?
M: methodology; how did you implement the experiment (at an appropriate level of detail)?
To represent the social attributes of an agent, we give each agent a parameter that ranges between 0 and 1, with 0 being complete introversion and 1 being complete extroversion.  When agents move within the environment, the number of neighbor agents for each of the empty locations that it could move to are compared to the social parameter of the moving agent.  The closest match is found and the agent moves to that location.


TODO FOR FINAL REPORT:  We will be adding another figure set showing the result of a few extremely extroverted agent in a moderately social environment.  We expect this to result in the disease spreading very quickly even though a large part of the population is introverted.  The first two graphs will also be debugged to fix the linear clustering problem.

### Results

The following three figures show the final results of an extremely introverted population vs an extremely extroverted population and how they alter the number of sick agents over the course of time.  An introverted population tends to remain spread across the world in the smallest possible social clusters, while an extroverted population clusters together.


Extremely Introverted Agent Population



Extremely Extroverted Agent Population



### Interpretation

Figure X shows that a higher number of agents are sick for a longer period of time when there is a high number of extroverted agents in the world.  This is due to these agents coming into contact with higher number of their fellow agents and thus being more susceptible to becoming contagious.


TODO FOR FINAL REPORT:  We will be adding another figure set showing the result of a few extremely extroverted agent in a moderately social environment.  We expect this to result in the disease spreading very quickly even though a large part of the population is introverted.  This would show that a single agent can alter the immunity statistics of the entire population.

## Experiment: Immunity Changing Over Time

### Question

How does agent immunity affect disease spread?

### Methodology

All agents are initialized with an immunity attribute. An agent with an immunity of zero is very susceptible to the disease and will definitely get sick if one of their neighbors is sick. Conversely, an agent with immunity set to one will not get sick, regardless of how many of their neighbors are sick. In our current implementation of this model, all agents have the same immunity for each test. In [FIGURES], we sweep the immunity parameter as we run the model for one hundred values between zero and one, and measure the maximum number of sick agents for each run.

### Results

As you can see in [FIGURES], as we increase the the immunity, the maximum number of sick agents decreases. The rate at which it decreases is fairly steady until immunity=0.7, at which point it begins to fall off at a greater rate.

### Interpretation

We do not have an explanation as to why the rate at which max agents sick decreases increases after immunity=0.7. However, we believe that measuring the maximum number of agents sick for each run might not be the ideal tool to relay the effectiveness of agent immunity. These graphs show that an increase in immunity might only serve “flatten” the peak of sick agents and delay it, which tells us that a lower immunity infects a larger population faster. To further investigate this question, we will measure and plot the total fraction of the agent population that is sick at any point during the simulation, rather than the max number that is sick at the same time during the simulation.

## Experiment: Impact of Immunity After Recovery

### Question

Does an agent becoming completely immune to a disease once they have recovered from it prevent a disease from persisting at a catastrophic level in the population?

### Methodology

To answer this question we simply increase the immunity of the agents that have been previously been sick to 100% to prevent them from ever becoming sick again in the future.

### Results

By preventing agents from becoming reinfected, we both drastically slow the infection rate after the peak number of sick agents had been reached and prevent the disease from breaking out again after the majority of the population has previously been infected as shown in Figures X and X.

No Post-Recovery Immunity

Post-Recovery Immunity

### Interpretation

The behavior of the model with full agent immunity after recovery shows that a diseases would not only persist among a population but also continually infect an increasing number of agents if humans were incapable of developing a high immunity to diseases that they had already contracted.

### Results

Based on the experiments above, we show that disease spread is increased in by the mobility and sociability of agents. This is to be expected based on the model of disease spread by the proximity of sick agents, but the more interesting results show that infection rate over the entire population can be affected by a single extroverted agent that travels among many social clusters while contagious. The results of the final experiment also show that a sick agent that ignores its contagiousness and continues to travel through the environment can drastically increase the time that it takes for the number of sick agents to fall from the peak infection number.

We also show that agents developing a resistance or immunity to specific diseases after they have been ill as people do is crucial to the health and survival of humans on large scale.  Without this protection, the entire population of agents quickly become and remain sick rather than the spread of a specific disease peaking and trailing off.  


## Reflection on Learning Goals

### Hannah:

I would like to learn more about numpy by creating a model where I need to largely come up with my own way of modeling things, as opposed to the homework assignments where I could largely copy/modify code written above. I’m also looking forward to working with visualization libraries to create descriptive (and possible interactive) graphs of our results. I also enjoy the freedom that this project gives us in terms of different directions we could take once we have completed our simple model because I want to learn more about the intricacies of disease spread, and these very specific extensions give me the opportunity to do that.

#### Mid-Project checkin: 

I am satisfied that this project is helping me achieve my original learning goals. I’ve enjoyed learning about some of the more hidden numpy features and using them to create graphs of our results, especially as we move into the phase of the project where we’re working on extensions.

#### Final Reflection: 

I believe that this project had helped me satisfy all of my learning goals. I have had many opportunities to work with numpy and matplotlib to create a reasonably complex agent-based model, and I’ve learned a lot about disease spread along the way.

### Katie:

Identifying correct models and characteristics to do specific analysis and using numpy. Because of the broad scope, this project has opportunities for using a variety of different model types in different ways, which will require choosing and implementing the appropriate model for each extension that we want to explore. We will also use tools such as numpy and matplotlib for modeling and results representation.

#### Mid-Project checkin:

I think so far this project has helped me work through my learning goals. We have discussed the applications and advantages of different model types, and I worked with both numpy and matplotlib implementations when we created our initial model. As we add extensions, I will be able to continue with both of these goals.

#### Final Reflection:

This project has been successful in allowing me to explore the characteristics of various models and to see how carefully determining the governing equations in a CA model can create an accurate representation of the world.  I also gained experience creating and debugging implementations that use tools such as numpy.

### Brenna:

I originally listed my learning goals to include working with topic relevant to world and learning about agent-based modeling. This project would strongly fulfill both of those goals. I am interested in exploring how agents interact in a system in a more in depth way, and seeing how these types of models behave in a more complex simulation. By applying this tool/method to the concept of infectious disease, I will have the opportunity to connect my work to something in the real world, and draw parallels between our simulations and reality. This project has so much room to grow and expand, and I am very excited about some of the potential extensions to this project, and the opportunities they provide to reach a greater understanding of how these types of models can be made and how they can be both useful and interesting.

#### Mid-Project checkin: 

I'm happy with how this project has been fulfilling my learning goals so far and am especially excited about delving into more of the extensions of our model.

#### Final reflection: 

This project has met my learning goals. At the start of this project it was important to me to learn more about and get more experience with working with agent based models. Especially in diving into our model’s extensions and developing how agents are affected by each other in this model, I believe I have gotten  the experience I was looking for. I was also interested in doing a project that was relevant to a real world context. Investigating disease spread fulfilled that goal, and I’ve found connecting our model’s results to real world to be an interesting challenge.

### Annotated Bibliography

Liliana Perez, Suzana Dragicevic, "An agent-based approach for modeling dynamics of contagious disease spread" International Journal of Health and Geophysics 2009 – Published 05 August 2009 Link: https://ij-healthgeographics.biomedcentral.com/articles/10.1186/1476-072X-8-50 (Links to an external site.) This paper uses an agent-based modelling approach to integrate geographic information about individuals to simulate the spread of contagious disease in an urban setting based on people's daily activities, movement, and geo-spatial interactions between people. The authors' goal was to create a model to show how disease spreads through a network of human interactions, and give people a better understanding of how this occurs in an urban environment. It would be particularly useful for running "what if" scenarios on potential outbreaks.

Azimi, Jomali, Mofrad, “Accounting for Diffusion in Agent Based Models of Reaction-Diffusion Systems with Application to Cytoskeletal Diffusion” Downloaded from http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0025306 (Links to an external site.) In this paper, the authors investigate a computational agent-based model do determine its accuracy in modeling the diffusion of molecules in a three-dimensional solution. They find that their model closely mimics the real behavior of these systems, and they go on to simulate the effects of molecular crowding on effective diffusion.

Andrew T. Crooks, Atesmachew B. Hailegiorgis, "An agent-based modeling approach applied to the spread of cholera" Link:http://www.sciencedirect.com/science/article/pii/S1364815214002515 In this paper, the concept of directly agent based modeling to a specific deisease is explored. The authors' approach will be useful to us when creating a model of a specific disease ourselves. It is especially intereting how they modeled the spread of cholera, which needs a less obvious approach than most diseases.

Kathleen Carley, et al., "BioWar: Acalable Agent-based Model of Bioattacks" Link: http://www.casos.cs.cmu.edu/publications/protected/2005-2006/carley_2006_biowarbioattacks.pdf Looking at the effects that external dynamics such as economics and social networks have on the spread of various diseases

Weidong Gu and Robert Novak, "Agent-based modelling of mosquito foraging behaviour for malaria control" Link:https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2818421/ Interesting commentary on ways to factor in the causes of diseases as agents themselves rather than attributes of the agents that could be infected

Azadeh Alimadad, Vahid Dabbaghian, Suraj K. Singhk, and Herbert H. Tsang, “Modeling HIV Spread through Sexual Contact using a Cellular Automaton” Link: http://www.cecm.sfu.ca/~mmonagan/MITACS/papers/VahidHIV.pdf Models the transmisson of HIV through a population in the context of social connections.

Chung-Yuan Huang, Chuen-Tsai Sun, Ji-Lung Hsieh, Holin Lin. “Simulating SARS: Small-World Epidemiological Modeling and Public Health Policy Assessments.” Journal of Artificial Societies and Social Simulation vol. 7, no. 4. 31 October, 2004. Link: http://jasss.soc.surrey.ac.uk/7/4/2.html This paper proposes a model of epidemiological scenarios in daily contact social networks using a small-world model. It demonstrates use of 2D automata to model disease spread between social contacts.

Yang, Y., J. D. Sugimoto, M. E. Halloran, N. E. Basta, D. L. Chao, L. Matrajt, G. Potter, E. Kenah, and I. M. Lo ngini. "The Transmissibility and Control of Pandemic Influenza A (H1N1) Virus." Science 326.5953 (2009): 729-33. Web. Link: http://science.sciencemag.org/content/326/5953/729 This paper shows a model of the transmissibility of H1N1 through a population. It has been useful in validating our model's behavior. It is also another resource outlining design of models similar to our own.

Archer, B. N., G. A. Timothy, C. Cohen, S. Tempia, M. Huma, L. Blumberg, D. Naidoo, A. Cengimbo, and B. D. Schoub. "Introduction of 2009 Pandemic Influenza A Virus Subtype H1N1 Into South Africa: Clinical Presentation, Epidemiology, and Transmissibility of the First 100 Cases." Journal of Infectious Diseases 206.Suppl 1 (2012) This was another useful paper containing a flu transmission model we have used to validate our own model.


H Yasuda, K Suzuki. "Measures Against Transmission of Pandemic H1N1 Influenza in Japan in 2009:Simulation Model” Eurosurveillance Rapid Communications, Volume 14, Issue 44. 05 November, 2009.  Link: http://www.eurosurveillance.org/ViewArticle.aspx?ArticleId=19385




