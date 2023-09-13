```
function GENETIC-ALGORITHM(populationSize, generations) returns a solution state
    population <- INITIALIZE-POPULATION(populationSize)
    
    for gen = 1 to generations do
        fitnessValues <- EVALUATE-POPULATION(population)
        selectedParents <- SELECT-PARENTS(population, fitnessValues)
        offspring <- RECOMBINE(selectedParents)
        offspring <- MUTATE(offspring)
        population <- SELECT-NEXT-GENERATION(population, offspring)
    
    return BEST-INDIVIDUAL(population)

function INITIALIZE-POPULATION(populationSize) returns a population of individuals
    population <- []
    repeat populationSize times:
        individual <- RANDOM-INDIVIDUAL()
        population.append(individual)
    return population

function EVALUATE-POPULATION(population) returns a list of fitness values
    fitnessValues <- []
    for individual in population do:
        fitness <- FITNESS-FUNCTION(individual)
        fitnessValues.append(fitness)
    return fitnessValues

function SELECT-PARENTS(population, fitnessValues) returns a list of selected parents
    selectedParents <- []
    totalFitness <- sum(fitnessValues)
    
    repeat len(population) times:
        parent1 <- RANDOM-SELECT(population, fitnessValues, totalFitness)
        parent2 <- RANDOM-SELECT(population, fitnessValues, totalFitness)
        selectedParents.append((parent1, parent2))
    
    return selectedParents

function RECOMBINE(selectedParents) returns a list of offspring
    offspring <- []
    for parent1, parent2 in selectedParents do:
        child1, child2 <- CROSSOVER(parent1, parent2)
        offspring.append(child1)
        offspring.append(child2)
    return offspring

function MUTATE(offspring) returns a list of mutated offspring
    mutatedOffspring <- []
    for child in offspring do:
        if RANDOM() < MUTATION-PROBABILITY then:
            mutatedChild <- MUTATION(child)
            mutatedOffspring.append(mutatedChild)
        else:
            mutatedOffspring.append(child)
    return mutatedOffspring

function SELECT-NEXT-GENERATION(population, offspring) returns the next generation of individuals
    combinedPopulation <- population + offspring
    sortedPopulation <- SORT-BY-FITNESS(combinedPopulation)
    nextGeneration <- TOP-N(sortedPopulation, populationSize)
    return nextGeneration

function BEST-INDIVIDUAL(population) returns the individual with the highest fitness
    bestIndividual <- population[0]
    bestFitness <- FITNESS-FUNCTION(bestIndividual)
    
    for individual in population do:
        fitness <- FITNESS-FUNCTION(individual)
        if fitness > bestFitness then:
            bestIndividual <- individual
            bestFitness <- fitness
    
    return bestIndividual
```
