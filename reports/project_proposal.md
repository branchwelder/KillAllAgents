# Kill All Agents: An Investigation of Infectious Disease and Agent Based Modeling
Authors: Kathryn Hite, Brenna Manning, Hannah Twigg-Smith, 

### Abstract
We intend to model the spread of infectious disease in humans. The first step of this is to implement a simple agent-based model in a 2D CA modeling a simple disease spread by interpersonal contact, e.g. the common cold. From there, we will add more features, modeling a different, more complicated disease. Modeling the disease to evolve as an agent itself will allow for different strains of a disease to interact within the model.  Including clustering to represent “cities” or social networks in our model will demonstrate how disease spread may be impacted by these factors which exist in the real world. 

### Annotated Bibliography
Liliana Perez, Suzana Dragicevic, "An agent-based approach for modeling dynamics of contagious disease spread" International Journal of Health and Geophysics 2009 – Published 05 August 2009 Link: https://ij-healthgeographics.biomedcentral.com/articles/10.1186/1476-072X-8-50 (Links to an external site.) 
This paper uses an agent-based modelling approach to integrate geographic information about individuals to simulate the spread of contagious disease in an urban setting based on people's daily activities, movement, and geo-spatial interactions between people. The authors' goal was to create a model to show how disease spreads through a network of human interactions, and give people a better understanding of how this occurs in an urban environment. It would be particularly useful for running "what if" scenarios on potential outbreaks.

Azimi, Jomali, Mofrad, “Accounting for Diffusion in Agent Based Models of Reaction-Diffusion Systems with Application to Cytoskeletal Diffusion” Downloaded from http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0025306 (Links to an external site.) In this paper, the authors investigate a computational agent-based model do determine its accuracy in modeling the diffusion of molecules in a three-dimensional solution. They find that their model closely mimics the real behavior of these systems, and they go on to simulate the effects of molecular crowding on effective diffusion.

Andrew T. Crooks, Atesmachew B. Hailegiorgis, "An agent-based modeling approach applied to the spread of cholera" Link: http://www.sciencedirect.com/science/article/pii/S1364815214002515 In this paper, the concept of directly agent based modeling to a specific deisease is explored. The authors' approach will be useful to us when creating a model of a specific disease ourselves. It is especially intereting how they modeled the spread of cholera, which needs a less obvious approach than most diseases.

Kathleen Carley, et al., "BioWar: Acalable Agent-based Model of Bioattacks" Link: http://www.casos.cs.cmu.edu/publications/protected/2005-2006/carley_2006_biowarbioattacks.pdf Looking at the effects that external dynamics such as economics and social networks have on the spread of various diseases

Weidong Gu and Robert Novak, "Agent-based modelling of mosquito foraging behaviour for malaria control" Link: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2818421/ Interesting commentary on ways to factor in the causes of diseases as agents themselves rather than attributes of the agents that could be infected

Azadeh Alimadad, Vahid Dabbaghian, Suraj K. Singhk, and Herbert H. Tsang, “Modeling HIV Spread through Sexual Contact using a Cellular Automaton” Link: http://www.cecm.sfu.ca/~mmonagan/MITACS/papers/VahidHIV.pdf  Models the transmisson of HIV through a population in the context of social connections. 

Chung-Yuan Huang, Chuen-Tsai Sun, Ji-Lung Hsieh, Holin Lin. “Simulating SARS: Small-World Epidemiological Modeling and Public Health Policy Assessments.”  Journal of Artificial Societies and Social Simulation vol. 7, no. 4. 31 October, 2004.
Link: http://jasss.soc.surrey.ac.uk/7/4/2.html  This paper proposes a model of epidemiological scenarios in daily contact social networks using a small-world model. It demonstrates use of 2D automata to model disease spread between social contacts.


### Experiments
Our project will consist of first creating a simple model of a disease spread by interpersonal contact, such as the common cold. The model will be an agent-based two-dimensional cellular automaton with few rules. Agents (representing the humans in this model) will have an attribute that reflects whether they are healthy and not contagious, healthy and contagious, unhealthy and not contagious, and unhealthy and contagious. Additionally, they will have an attribute reflecting their susceptibility to the disease (where a susceptibility of zero indicates immunity) as well as an attribute describing how often they move.
Once we have created this simple model, we will be able to extend it with experiments based on those found in some relevant papers. These experiments range from fairly simple to very complicated, and a full list of them can be found in the extensions section.

### Extensions
After the completion of our initial simple model, there are several possible directions to go deeper. We plan on adding clustering to our model to represent cities. This will allow for us to investigate how the disease might move between groups of people and take social interactions/networks into account. We also plan to incorporate evolution of both the disease and the human agents over time, simulating the disease getting stronger and/or humans becoming immune. Other potential ways we might be able to expand our model once we complete these steps are included in the list below.


- Could the population evolve to become immune if the susceptibility of agents is dependent on that of their parents?
- Could searching for a “cure” and distributing the cure once discovered prevent the entire population from becoming infected?
- How might attributes of the agents affect their susceptibility? Would agents who are very young or old be more susceptible, and how might this affect infection rates?
- What if agents lived in “households”? These could contain a variety of demographics, such as a four-person family, young couple, or roommate pair. They would be more exposed to the agents that they lived with.
- How does clustering (such as in cities) affect the rate of infection?
- How does travel (between cities) affect the rate of infection?
- How does infection affect infected agents? Do they stop moving? Do they eventually die?
- What effect would the antivax movement have on a population that is largely herd-immune?
- Would humans evolve to be resistant to the disease? Could they contract it multiple times, or would they become immune?
- What if our disease was intelligent (and modeled as an agent)? Could it evolve to further its own interests? (By not killing the host or raising its infection rate.)
- How would extroversion/introversion affect infection rates? Would this also affect the motion of the agent?
- How do different types of infection affect the spread of disease? (respiratory, sexually transmitted, non-human carrier)
- hat attributes must the disease have to be able to kill all agents?
- How do different human activities affect the agents involved? (e.g. going to work or school, sports, airports)
- If the disease is genetic, how might we represent that? What would the population look like in thousands of (model) years?

### What Might Possible Results Look Like?/How Do We Plan to Interpret Results?
One possible result representation would be a comparison of the disease spread rate in our simple model with empirical data to validate that we have an accurate foundation to build our extensions on.


Once the extensions are in place, we can create several types of representations of the results based on each extension.  Some of the possibilities include a heat map or grid showing the sick population by location for analyzing travel or social network effects, an overlay comparing the results when changing factors behind disease spread such as doctor accessibility, or the population of disease spreading agents including birds or mosquitoes in comparison to the sick human population.


Our final goal is to create an interactive model that allows users to change health, social, and economic factors before viewing the results of their custom simulation.

### Learning Goals

Hannah: I would like to learn more about numpy by creating a model where I need to largely come up with my own way of modeling things, as opposed to the homework assignments where I could largely copy/modify code written above. I’m also looking forward to working with visualization libraries to create descriptive (and possible interactive) graphs of our results. I also enjoy the freedom that this project gives us in terms of different directions we could take once we have completed our simple model, because I want to learn more about the intricacies of disease spread, and these very specific extensions give me the opportunity to do that.

Katie: Identifying correct models and characteristics to do specific analysis and using numpy.  Because of the broad scope, this project has opportunities for using a variety of different model types in different ways, which will require choosing and implementing the appropriate model for each extension that we want to explore.  We will also use tools such as numpy and matplotlib for modeling and results representation.

Brenna: I originally listed my learning goals to include working with topic relevant to world and learning about agent-based modeling. This project would strongly  fulfill both of those goals. I am interested in exploring how agents interact in a system in a more in depth way, and seeing how these types of models behave in a more complex simulation.  By applying this tool/method to the concept of infectious disease, I will have the opportunity to connect my work to something in the real world, and draw parallels between our simulations and reality.  This project has so much room to grow and expand, and I am very excited about some of the potential extensions to this project, and the opportunities they provide to reach a greater understanding of how these types of models can be made and how they can be both useful and interesting.

