## DREAM

Our group is working on study we call DREAM.  The idea is to repurpose drugs to Alzheimer's that have been developed and approved for other indications.  To this end our group previously used metabolomics but this talk presents our more recent research project that is driven by genomics.  This new project begins with the collection of AD genes.  We will distinguish AD risk genes from AD associated genes.  While both type are statistically associated to AD, AD risk genes play mechanistic role in AD pathology, while AD associated genes not necessarily, and in fact most of them do not.

To collect AD genes we use curated knowledge...

...our own proteomic studies on AD genes...

...public omic data...

...and association resources.

Second, we plan to search for AD drug candidates among all approved drugs given our collection of AD genes both by a what we call the shared gene approach taken by Anjali...

...and a network approach taken by me...

Third, we plan to validate those drug candidates with in vitro essays and pharmacoepidemiology.

## Drug repurposing

The idea of drug repurposing is to take a drug that has been developed and approved for some indication X and use some approach to evaluate its potential for Alzheimer's.

The shared gene approach to repurposing looks at targets of drugs approved for indication X.  These targets are genes associated to X.  If a target is also associated to AD then the approach nominates the corresponding drug for repurposing to AD.  An example is drug A and its target t_A1.

This approach is simple and sensitive as it considers thousands of genes that are statistically associated to AD.  Such statistical associations include two classes of genes.  One is a large class of AD associated genes that are without a mechanistic link to AD and therefore inefficient for AD treatment; examples include genes in linkage disequilibrium with causal variants, or genes mentioned in the context of AD in the corpus of scientific literature. The other, smaller, class of AD associated genes are mechanistically linked to AD by either being an AD risk gene or interacting with one.  Targeting these latter class of genes is what we seek.  However, the shared gene approach cannot distinguish between the two classes of genes.

The network approach, in contrast, allows us to estimate the strength of a mechanistic link between a drug and AD pathology by calculating the distance between the drug's targets and the AD risk genes.  It emphasizes specificity and was validated by pharmacoepidemiology.  This distance is defined on the topology of the vast gene network of the interactome.

I will now let Anjali present her results obtained with the shared gene approach and I will come back afterwards to talk more about the network approach and present a pilot study.
