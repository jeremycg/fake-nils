import random
from Bio import SeqIO

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
    for i in range(len(nilbreak)):
        factor=len(parental[todo[i]])/nillen
        output.append([nilbreak[i][0]])
        for a in nilbreak[i][1:]:
            output[i]+=[factor*a]
    return(output)

def makenil(parent0,parent1,lenslist,outputfile):
    handle0 = open(parent0, "r")
    parent0 = list(SeqIO.parse(handle0, "fasta"))
    handle1 = open(parent1, "r")
    parent1 = list(SeqIO.parse(handle1, "fasta"))
    filetowrite=open(outputfile, 'a')
    todo=[]
    for i in range(len(parent0)):
        todo+=[i,i]
    for chrom in range(len(lenslist)):
        assert(len(parent0[chrom])==len(parent1[chrom])),"Chromosomes are different lengths"
        chromprint=""
        counter=0
        while len(lenslist[chrom])>0:
            if len(lenslist[chrom])==1:
                if lenslist[chrom][0]==0:
                    print(">",str(parent0[todo[chrom]].id), file=filetowrite,sep='_')
                    print(chromprint,str(parent0[todo[chrom]].seq)[counter:],file=filetowrite,sep='')
                    lenslist[chrom]=[]
                    break
                if lenslist[chrom][0]==1:
                    print(">",str(parent1[todo[chrom]].id), file=filetowrite,sep='_')
                    print(chromprint,str(parent1[todo[chrom]].seq)[counter:],file=filetowrite,sep='')
                    lenslist[chrom]=[]
                    break
            elif lenslist[chrom][0]==0:
                    chromprint+=str(parent0[todo[chrom]].seq)[counter:round(lenslist[chrom][1])]
                    counter=round(lenslist[chrom][1])+1
                    lenslist[chrom][0]=1-lenslist[chrom][0]
                    del(lenslist[chrom][1])
            elif lenslist[chrom][0]==1:
                    chromprint+=str(parent1[todo[chrom]].seq)[counter:round(lenslist[chrom][1])]
                    counter=round(lenslist[chrom][1])+1
                    lenslist[chrom][0]=1-lenslist[chrom][0]
                    del(lenslist[chrom][1])
    handle1.close()
    handle0.close()
    filetowrite.close()
    print("done!")

def cutme(inputfile,mindist,maxdist,outputfile,barcode=""):
    handle = open(inputfile, "r")
    records = list(SeqIO.parse(handle, "fasta"))
    handle.close()
    for chr in records:
        seq=chr.seq.upper()
        counter=-1
        filetowrite=open(outputfile, 'a')
        while counter<len(seq)-3:
            count2=seq.find("TTAA",counter+1)
            if count2==-1:
                break
            if count2-counter > mindist and count2-counter < maxdist:
                if counter==-1:
                    countprint=0
                else:
                    countprint=counter
                print(">",str(chr.id),str(counter),str(count2), file=filetowrite,sep='_')
                print(barcode,seq[countprint:count2+4],file=filetowrite,sep="")
            counter=count2
        filetowrite.close()

def writefastq(infile,outfile,coverage,quality):
    handle = open(infile, "rU")
    records = list(SeqIO.parse(handle, "fasta"))
    handle.close()
    handle = open(outfile, "a")
    for sequence in records:
        rec = sequence
        rec.letter_annotations["phred_quality"] = [quality] * len(sequence.seq)
        for i in range(coverage):
            towrite=rec
            towrite.id=towrite.id+str(i)
            SeqIO.write(towrite, handle, "fastq")
    handle.close()

def parental(tempfa,ref,output):
    handle = open(tempfa, "rU")
    mappedrecords = list(SeqIO.parse(handle, "fasta"))
    handle.close()
    handle = open(ref, "rU")
    refrecords = list(SeqIO.parse(handle, "fasta"))
    handle.close()
    output_handle = open(output, "w")
    for chrom in range(len(mappedrecords)):
        mappedrecords[chrom].seq = mappedrecords[chrom].seq.tomutable()
        for base in range(len(mappedrecords[chrom])):
            if mappedrecords[chrom].seq[base]=="n":
                mappedrecords[chrom].seq[base]=str(refrecords[chrom].seq[base]).upper()
            else:
                mappedrecords[chrom].seq[base]=mappedrecords[chrom].seq[base].upper()
        if len(mappedrecords[chrom])!=len(refrecords[chrom]):
                mappedrecords[chrom]+=refrecords[chrom][len(mappedrecords[chrom]):]
    SeqIO.write(mappedrecords, output_handle, "fasta")
    output_handle.close()
