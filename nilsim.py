import random

def makeparent(x,y,z): #function to make the parentals
        return([[[z]*x]*2]*y) #making a list of loci

#so parents are [[[c1l1s1,c1l2s1],[c1l1s2,c1l2s2].....],[[c2l1s1,c2l2s1]...]]
#for now looks like [[[0,0],[0,0]]...]

def makegametes(parent):#function to make gametes from individual
        gamete=[]#blanks the gamete
        for chromo in parent:#for each chromosome
                startingchr=random.randint(0,1)#choose the starting chromosome
                breakpoint=random.randint(1,len(chromo[0])-1)#set the breakpoint
                gamete+=[chromo[startingchr][0:breakpoint]+chromo[1-startingchr][breakpoint:]]
                #above makes the gamete - starting from the startingchr until the breakpoint
                #then continuing to the end
        return(gamete)#returns the made gamete

def combinegametes(gamete1,gamete2):#makes new individual from two gametes
        offspring=[]#blanks offspring
        for chromo in range(0,len(gamete1)):#for each
                offspring+=[[gamete1[chromo],gamete2[chromo]]]#add the two chromos to be sisters
        return(offspring)#give back the offspring

#perfect! no we just have to loop the above in a sensible way
#lets write a function to do it
#the below function is recursive - it takes a list of crosses to carry out, does the first one, then
#deletes it off the list, and returns the offspring and the list to the same function.



#ok! so now we can call cross on a list, where 0 is a backcross to parent0 and 1 to 1, an "s" is a sibling mating
#NILs were cross([1,1,1,1,1,1,"sib","sib","sib","sib","sib","sib"],parent0)
#or cross([1,1,1,1,1,1,"self","self","self","self","self","self"],parent0)
#new ones will be cross([1,0,1,0,1,"sib","sib","sib","sib","sib"],parent0)
#some measure of composition?

def percentageril(ril):#function of individual
        oneflat=[item for sublist in ril for item in sublist]#flattens one level
        flatlist=[item for sublist in oneflat for item in sublist]#flattens one more level
        return(sum(flatlist)/(len(flatlist)))#finds percentage

#repeats it to give a number of percentages out
def repril(repeats,crosslist,initparent):#function of crosslist, number of repeats
        d=[]#clears holder
        for i in range(1,repeats):#loops by num repeats
                x=cross(crosslist,initparent,initparent)#cross
                d+=[percentageril(x)]#finds percentage
        return(d)#returns percent

#finds the introgressions size as a list - len() to give number, max() to give maximum
def introgressions(individ,vartocount):#function of individual, then 0 or 1
        d=0#clears counter
        e=[]#clears list of counts
        for chr in individ:#for each chromosome
                for sister in chr:#and each sister
                        for loci in sister:#for each locus
                                if loci==vartocount:#if it's a match
                                        d+=1#increase the counter
                                elif loci!=vartocount:#otherwise
                                        if d != 0:#if the counter isnt 0
                                                e+=[d]#add it to the list
                                        d=0#reset the counter for next introgression
                        if d!=0:#checks for introgression at end of chr
                                e+=[d]#adds to list
                        d=0#resets counter for next
        return(e)#returns the list

def crosschrom(individual):
    out=[]
    for chrom in individual:
        for sister in chrom:
            breaks=[sister[0]]
            for i in range(1,len(sister)):
                if sister[i]!=sister[i-1]:
                    breaks.append(i)
            out+=[breaks]
    return(out)

def convertlens(nilbreak,parental,nillen):
    output=[]
    todo=[]
    for i in range(len(parental)):
        todo+=[i,i]
    print(todo)
    for i in range(len(nilbreak)):
        factor=len(parental[todo[i]])/nillen
        output.append([nilbreak[i][0]])
        for a in nilbreak[i][1:]:
            output[i]+=[factor*a]
    return(output)
