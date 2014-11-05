import random

nloci = 1000#number of loci per chromosome
nchro = 6 #number of chromosomes per worm


def makeparent(x,y,z): #function to make the parentals
	return([[[z]*x]*2]*y) #making a list of loci



#so parents are [[[c1l1s1,c1l2s1],[c1l1s2,c1l2s2].....],[[c2l1s1,c2l2s1]...]]
#for now looks like [[[0,0],[0,0]]...]

def makegametes(parent):#function to make gametes from individual
        gamete=[]#blanks the gamete
        for chromo in parent:#for each chromosome
                startingchr=random.randint(0,1)#choose the starting chromosome
                breakpoint=random.randint(1,nloci-1)#set the breakpoint
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
#the siblings are a hack - we need sibling mating.
#By checking the list[2] and making an if else it could be fixed. - do if it gets too long to run
def cross(list1,parent,sibling):#function of croses to do, the parent and a sibling
        if len(list1)==0:#if all our crosses are done, return the offspring
                return(parent)
        elif(list1[0])==1:#if the cross is 1, backcross to parent 1
                return(cross(list1[1:],combinegametes(makegametes(parent),makegametes(parent1)),combinegametes(makegametes(parent),makegametes(parent1))))
        elif(list1[0])==0:#if the cross is 0, backcross to parent 0
                return(cross(list1[1:],combinegametes(makegametes(parent),makegametes(parent0)),combinegametes(makegametes(parent),makegametes(parent0))))
        elif(list1[0])=="sib":#if the cross is sib, sib mate
                return(cross(list1[1:],combinegametes(makegametes(parent),makegametes(sibling)),combinegametes(makegametes(parent),makegametes(sibling))))
        elif(list1[0])=="self":#if the cross is self, self
                return(cross(list1[1:],combinegametes(makegametes(parent),makegametes(parent)),combinegametes(makegametes(parent),makegametes(parent))))

#ok! so now we can call cross on a list, where 0 is a backcross to parent0 and 1 to 1, an "s" is a sibling mating
#NILs were cross([1,1,1,1,1,1,"sib","sib","sib","sib","sib","sib"],parent0)
#or cross([1,1,1,1,1,1,"self","self","self","self","self","self"],parent0)
#new ones will be cross([1,0,1,0,1,"sib","sib","sib","sib","sib"],parent0)
#some measure of composition?

def percentageril(ril):#function of individual
        oneflat=[item for sublist in ril for item in sublist]#flattens one level
        return(sum([item for sublist in oneflat for item in sublist])/(2*nloci*nchro))#flattens another level, finds percentage

#repeats it to give a number of percentages out
def repril(repeats,crosslist):#function of crosslist, number of repeats
        d=[]#clears holder
        for i in range(1,repeats):#loops by num repeats
                x=cross(crosslist,parent0,parent0)#cross
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
