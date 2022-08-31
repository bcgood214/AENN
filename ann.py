import math, random

class AND:
    def __init__(self, x1, x2, w1, w2, w3, theta):
        self.x1 = x1
        self.x2 = x2
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.theta = theta

    def is_and(self):
        if self.x1 and self.x2:
            return 1
        return 0
    
    def run(self):
        sum = 0
        sum += self.x1 * self.w1
        sum += self.is_and() * self.w2
        sum += self.x2 * self.w3

        if sum < self.theta:
            return False
        return True

class EA:
    def __init__(self, gens, poolsize, mutrate):
        self.gens = gens
        self.mutrate = mutrate
        self.poolsize = poolsize
    
    def genind(self, submats):
        ind = []

        for i in range(submats):
            whole = ['0' for x in range(5)]
            decimal = ['0' for x in range(5)]

            for i in range(len(whole)):
                if random.random() > 0.5:
                    whole[i] = '1'
            
            for i in range(len(decimal)):
                if random.random() > 0.5:
                    decimal[i] = '1'
        
            ind.append([whole, decimal])
        
        return ind
    
    def genind_nodec(self, submats):
        ind = []

        for i in range(submats):
            whole = ['0' for x in range(5)]

            for i in range(len(whole)):
                if random.random() > 0.5:
                    whole[i] = '1'
        
            ind.append(whole)
        
        val = self.eval(ind)
        ind.append(val)
        return ind
    
    def genpool(self):
        self.pool = [self.genind_nodec(4) for i in range(self.poolsize)]
    
    def decode(self, s):
        val = 0
        for i in range(len(s)):
            if s[i] == '1':
                val += 2**(4-i)
        
        return val
    
    def eval(self, genotype):
        w1 = self.decode(genotype[0])
        w2 = self.decode(genotype[1])
        w3 = self.decode(genotype[2])
        theta = self.decode(genotype[3])
        ann = AND(0, 0, w1, w2, w3, theta)
        fitness = 0

        result = ann.run()
        if not result:
            fitness += 50

        ann.x1 = 1
        result = ann.run()

        if result:
            fitness += 50
        
        ann.x1 = 0
        ann.x2 = 1
        result = ann.run()

        if result:
            fitness += 50
        
        ann.x1 = 1
        result = ann.run()

        if not result:
            fitness += 50
        
        return fitness
    
    def random_ts(self):
        group = random.choices(self.pool, k=len(self.pool)//5)

        fittest = None
        second_fittest = None
        fittest_val = None
        second_fittest_val = None

        for ind in group:
            if fittest is None:
                fittest = ind
                fittest_val = ind[-1]
            elif second_fittest is None:
                second_fittest = ind
                second_fittest_val = ind[-1]
            else:
                if ind[-1] > fittest_val:
                    second_fittest = fittest
                    second_fittest_val = fittest_val
                    fittest = ind
                    fittest_val = ind[-1]
                elif ind[-1] > second_fittest_val:
                    second_fittest = ind
                    second_fittest_val = ind[-1]

        return [fittest, second_fittest]
    
    def recombine(self, p1, p2):
        child = []
        for i in range(4):
            co_point = random.randint(0, 4)
            child.append(p1[i][:co_point]+p2[i][co_point:])
        
        val = self.eval(child)
        child.append(val)
        return child
    
    def fittest(self):
        fittest = self.pool[0]
        fittest_val = self.pool[0][-1]
        for ind in self.pool:
            if ind[-1] > fittest_val:
                fittest = ind
                fittest_val = ind[-1]
        
        return fittest


    def run(self):
        # TODO include fitness value in pool
        self.genpool()

        for g in range(self.gens):
            next_gen = []
            for j in range(len(self.pool)-1):
                parents = self.random_ts()
                children = self.recombine(parents[0], parents[1])
                next_gen.append(children)
            
            next_gen.append(self.fittest())
            self.pool = next_gen

        return self.fittest()
            

if __name__ == "__main__":
    ea = EA(10, 30, 0.05)
    one = ea.genind_nodec(4)
    two = ea.genind_nodec(4)
    print(ea.run())

    
