## DREAM

Our group is working on study we call DREAM.  The idea is to repurpose drugs to Alzheimer's disease, or AD, that have been developed and approved for other indications.  To this end our group previously used metabolomics but this talk presents our recent extension of the DREAM study with genomics.  This new line of work begins with the collection of AD genes.  We will distinguish AD risk genes from AD associated genes.  While both type are statistically associated to AD, AD risk genes play mechanistic role in AD pathology, while AD associated genes not necessarily, and in fact most of them do not.

To collect AD genes we use curated knowledge...

...our recently published proteomic study on AD genes...

...public omic data...

...and association resources.

Second, we plan to search for Alzheimer's drug candidates among all approved drugs given our collections of AD genes both by a what we call the shared gene approach taken by Anjali...

...and a network approach taken by me...

Third, we plan to validate those drug candidates with three approaches: (1) in vitro essays  with cell culture based phenotypic screens, (2) pharmacoepidemiology and (3) in a transgenic mouse model for Alzheimer's

## Drug repurposing

The idea of drug repurposing is to take a drug that has been developed and approved for some indication X and use some approach to evaluate its potential for, in the present case, Alzheimer's.

The shared gene approach to repurposing looks at targets of drugs approved for indication X.  These targets are genes associated to X.  If a target is also associated to Alzheimer's then the approach nominates the corresponding drug for repurposing.  An example is drug A and its target t_A1.

This approach is simple and sensitive as it considers thousands of genes that are statistically associated to AD.  Such statistical associations include two classes of genes.  One is a large class of AD associated genes that are without a mechanistic link to Alzheimer's and therefore inefficient for its treatment; examples include genes in linkage disequilibrium with causal variants, or genes mentioned in the context of AD in some corpus of scientific literature. The other, smaller, class of AD associated genes are mechanistically linked to Alzheimer's by either being an AD risk gene or interacting with one.  Targeting these latter class of genes is what we seek.  However, the shared gene approach cannot distinguish between the two classes of genes.

The network approach, in contrast, is designed to make such distinction since it allows us to estimate the strength of a mechanistic link between a drug and AD pathology.  This is done by calculating a network based distance between the drug's targets and the AD risk genes.  The mechanistic insight comes from the fact that distance is defined on the topology of the human gene network also known as the interactome.  This enhances specificity, which in turn helped earlier validation of this approach by pharmacoepidemiology.

I will now let Anjali present her results obtained with the shared gene approach and I will come back afterwards to talk more about the network approach and will present a pilot study.

## Drug repurposing

Let's return to the network approach and see how it quantifies a given drug's repurposing potential for AD!

## Quantifying repurposing potential in a toy network

To demonstrate this we use a toy gene network with three disease genes B, D, E.  The nodes of this network represent genes and the edges represent interactions between genes.  Genes may be connected to each other via paths of one or more edges.  Path length is just the number of edges along the path.  For example the shortest path connecting gene B and E is of length 2.

Suppose a given drug targets both E, itself a disease gene, and J, a gene directly interacting with a disease gene.  Intuitively we expect this drug to have a relatively strong repurposing potential.

This expectation can be quantified by raw distance.  To calculate raw distance we take the length of the shortest path connecting each target to the closest disease gene, then we average these length values across targets.  For target J the path length to the closest gene (which is B) is 1; while for target E it is zero since E is also a disease gene and so its distance to itself is zero.  Therefore the raw distance is 0.5.

Is this distance significantly shorter than randomly picking two other targets in this toy network? To answer that we calculate a Z score that compares the raw distance to the null distribution of distances generated by many random picks of targets.  This standardization removes much of the bias introduced by node degree, that is the number of interaction partners, of the genes involved.  For instance gene B has five interaction partners while gene E only three; thus in principle individual interactions have more impact on E than on B.  The Z score corrects for that.

Once we have the Z score it is straight forward to transform it into a p value.  In the present example p is 0.3.  This suggests that although the raw distance between the drug targets and disease genes is small, it is not small enough relative to the tiny size of the toy network.

Let's take another drug with targets C and H.  Glancing at these new targets they seem to be further away from the red disease genes than the previous targets seem.  Indeed, the raw distance, the z score and p value are all much greater than those for the previous targets, which confirms our intuition.

## The real data

Now let's turn to our real world gene network, the human interactome.  It has nearly quarter of a million interactions (edges) between nearly 20 thousands genes.  As the first approximation to AD risk genes we took AD genes from knowledge bases such as UniProt KB.  Imagine this small set of twenty-six genes in the vast human interactome.  It turns out that their node degree (that is the number of interaction partners) varies greatly: on the one extreme we have APP with more than a thousand interactions, on the other extreme UNC3C with just 4 interactions.  Recall that our network approach takes this into account.

Before we scored drugs given this network and AD risk gene set we arbitrary selected 3 AD genes as positive controls.  The idea is that if there was a drug targeting these 3 AD genes that drug should have a strong repurposing potential and thus should have a significantly small network based distance to AD genes.

## Quantifying repurposing potential in a toy gene network

Next we scored the 3 arbitrary selected AD genes and compared them to seven sets of drug targets in the pilot phase of our network based drug screen.  The first set of genes---TLR7, TLR9 and ACE2---are targeted by Hydroxychloroquine, a drug recently studied by our group.  The remaining six sets of targets each contain a single gene and were implicated by another recent study from our group on the genetics shared by asthma and Alzheimer's disease.

It is important to note that, although they might be statistically associated to Alzheimer's, none of the targets are part of our stringently defined knowledge based AD risk gene set.  Therefore we expect the network approach to give them weaker score than it gives the 3 AD genes.  Indeed this is what we observe: we obtained zero distance, very low z score and p value for the 3 AD genes but not for the rest.

## AD risk genes suggested by several TWAS

In this pilot study we wanted to extend the knowledge based AD risk gene set with likely AD risk genes suggested by recent omic studies.  TWAS or transcriptome wide association studies and other fine mapping methods are designed to identify genes that are causal to disease.  We collected 9 gene sets inferred by various TWAS to play a causal role in Alzheimer's.  The methodological details of these TWAS varied greatly, which explains the small overlap between the resulting AD gene sets.  This is shown by the clustered-heatmap.  To ensure high specificity, we considered further only those AD risk genes that were inferred by two or more studies; these are marked green on the histogram.  We call the set of these high confidence AD risk genes TWAS2+.

## Extending the knowledge based AD risk gene set

The Venn diagram shows the knowledge based and TWAS2+ AD risk gene set.  The third gene set, IAPS is the incipient AD proteomic signature (also called multiomic signature), which our group's latest combined proteomic and transcriptomic study found to be differentially expressed in young APOE carriers.  This suggested that these genes are linked to Alzheimer's pathogenesis.

## Quantifying repurposing potential in a toy gene network

The orange symbols indicate results under the extended AD risk gene set.  We see that the results changed relative to the knowledge only AD risk gene set.  The change is either because one of the TWAS2+ or IAPS genes is closer to the target than any of the knowledge based genes, which decreases raw distance; see ADRB2 for example.  Or, the change is due to the increased AD gene set size and a possibly shifted degree distribution; see ILR6 for instance.

## DREAM

This is where the project stands.  We are working towards scoring all approved drugs in the drug bank...

...to prioritize them for experimental validation.

## Summary

In summary Anjali and I talked about two approaches to evaluating drugs' potential for repurposing to AD.  The shared gene approach is simple and sensitive as it considers thousands of genes statistically associated to AD but its specificity is likely quite low.  The network approach aims at high specificity by focusing on molecular mechanisms.  With the shared gene approach we already obtained some AD drug candidates.  On the other hand, we only completed a pilot study with the network approach and we are now scaling it up for all drugs.

## Acknowledgements

I'd like to thank Madhav, Vijay, Sayantani, Yang, Jackson and Andrew for accepting and supporting me in the CTNS group.  I thank Melissa and Charlee for their help with my onboarding.  Finally I thank our collaborators at the University of Chicago for sharing unpublished TWAS results with us.


## Madhav's suggestions

* Validation
* in vitro esays with cell culture based phenotypic screens; this method is explained in the Science advanced upcoming
* pharmacoepidemiology as mentioned in the DREAM study
* another type of validation: a newly approved study performed in CTNS: PREVENT-AD PREclinical Validation of EMererging and Novel Treatments for AD: we will test the top drugs in transgenic mouse model of AD
* incipient AD multiomic signature
