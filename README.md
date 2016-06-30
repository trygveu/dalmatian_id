# 101 Dalmatian ID

After Roger and Anita decide to keep all the 101 dalmatians, they move to a house in the countryside. They soon realize that they need a system to make sure that all the puppies are healthy and develop as they should, and they contact you to help them design a novel health supervision system for dalmatians.

The system will be installed in the kitchen door, and at every pass a camera takes a series of images of the passing puppy. The system monitors the health of each puppy, by estimating it's growth and it will also look for signs of injury. This will help Roger and Anita making sure that all the puppies are happy and healthy at any time.

A requirement of this system, is that it needs to learn the spot pattern of each puppy, and adapt as the puppies grow. There is no prior data as none of the puppies have names yet - there's such a chaos that it will take Roger and Anita months to make all of them apart. We need to help them ;)

## Discussion
This may sound like a constructed and corny problem. But it has in fact a very strong relevance to problems that we work with in Agricultural Robotics and with industry clients. We would like to have a case like this, to understand how you think and reason.

Depending on your specialty and interest, we would like to hear your opinion on any of these questions:

1. What type of problem would you say that this is? Would you say that it is a hard problem?
2. What benefits do you think such a system could give to Roger and Anita?
3. How would you design the actual imaging system? (Lights, cameras, processing unit, positions, guiding of the dogs, etc.)
4. How would you represent the spot pattern in a data-structure?
5. If you are given the "ground truth" knowledge of all the puppies' spot patterns, names and information - How would you solve the identification problem?
6. If you are given no prior. You don't even know how many puppies there are, only that they will normally pass three times a day - How would you approach the problem?
7. What sources of noise and  uncertainty would you expect in an observation of the spot pattern?
8. How would you design the user interface and front-end? Which use-cases would you design for?
9. What additional data would you like to include and estimate?


## Spot images
The puppies pass the camera normally three times a day to get food. 
The camera system detect the shoulder part, and capture the spot pattern. 
Each observation will carry noise, so each position and size might vary. 
Some spots may not be detected at all. 

The first 7 puppies looks like this:

Pongo

![Pongo](./population/001-Pongo.svg?raw=true "Pongo")

Perdi

![Perdi](./population/002-Perdita.svg?raw=true "Perdi")

Patch

![Patch](./population/003-Patch.svg?raw=true "Patch")

Lucky

![Lucky](./population/004-Lucky.svg?raw=true "Lucky")

Rolly

![Rolly](./population/005-Rolly.svg?raw=true "Rolly")

Penny

![Penny](./population/006-Penny.svg?raw=true "Penny")

Freckles

![Freckles](./population/007-Freckles.svg?raw=true "Freckles")


