SRUC programmers challenge 3


One of the main challenges of using genotypes for genomic evaluations is to ensure data quality and validating that genotypes belong to the right animals. When an animal and its offspring are genotyped we can do parentage verification. When we get negative result we need to run parentage discovery.  This is very computationally demanding for large datasets. There are 108 Single Nucleotide Polymorphisms (SNPs) identified for cattle which give high accuracy for checking parent-offspring relationship. 

The method that we use to assign parentage is via exclusion. The genotypes of parent and offspring are compared, and if they do not match (i.e an animal with genotype AA cannot be the parent of an animal with genotype BB at the same marker)
The 108 SNP panel has been chosen because these SNPs are highly variable within the population, and so you wouldn't expect the genotypes to match just by chance. The genotypes provided are coded as 0 (homozygous reference e,g AA) 1 (heterozygous e.g AB) and 2(alternate homozygous e.g BB). 

Use the list of SNPs (file: parentageSNPs.txt) and find possible sires for all animals. Simulated data can be found in file mMatrixFileSimulated_54609_1000_1.dat. All animals have been genotyped using Illumina 50k V2 chip (file: Illumina50kV2map.txt).  
	
Deliverables:

Week 1 - Provide a flowchart of your solution. Please do not start coding until we finalise it during our next meeting. You can use http://www.gliffy.com/ 

Week 2 (this week) - Write a sub function to read in and parse the original, large files into a useable format. Bonus challenge! Can you extract the 108 sites of interest? 
	

Final goal: Write software which takes input files in fixed format and outputs a list of possible sires for every animal.

Requirements:
1.	It should be possible to change the names of your input files without altering the code.
2.	Use functions and/or procedures.
3.	Use UML naming convention.




********
To download all files for week 3 please hit the "download as zip" button to the right¬!! -->>
********
