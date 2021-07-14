# Network based drug repurposing for Alzheimer's disease


## 1. Introduction

We recently announced the Drug Repurposing for Effective Alzheimer's Medicines (DREAM) study, in which we plan to find and test repurposable drugs for Alzheimer's disease.  Here we present our proposal for prioritizing drugs for AD based on the following sources of information:
* our novel proteomics study that describes the *incipient AD proteomic signature*
* transcriptome-wide association studies, TWAS, on AD
* curated knowledge on established AD genes
* a network based drug repurposing approach


## 2. The network based approach

We choose the approach to drug repurposing developed by Cheng et al based on their earlier work, which showed that disease genes tend to form clusters, so-called *disease modules*, in the human protein-protein interactome (PPI).

The figure shows two disease modules: a red module for coronary artery disease (CAD) and a purple module for cardiovascular disease (CVD).  Cheng et al found only a few drugs approved for non-cardiovascular indications that are proximal to the CAD  module. Hydroxychloroquine is one of those drugs.  Cheng et al also found further support for Hydroxychloroquine's protective effect on CAD using pharmaco-epidemiology and an in vitro assay. This shows the utility of the network based approach.

## 3. Quantifying proximity of drug targets to disease genes

The network based approach defines the proximity, d, between some drug targets (blue genes) a disease module (red genes).  We interpret the definition as the average length of the shortest paths taken from all targets to the disease genes.

The left and right figures show the same toy network and disease module in red but different drug targets in blue.  On the left: target C is one protein-protein interaction away from the disease module, while target H is two interactions away, so the proximity is d = (1 +3) / 2 = 3/2.  On the right: target J is one interaction away from the disease module, while target E is part of the disease module, hence zero interactions away; this means proximity d = (1 + 0) / 2 = 1/2.

The approach also evaluates the standardized proximity, z, according to which drugs/targets can be prioritized for a given disease.

## 4. Planned workflow

The network based approach will evaluate drug targets' proximity to AD genes (near bottom) and thereby prioritize drugs for AD.  One of the inputs to this step is the set of AD genes, which are not fully known.  Therefore we will predict AD genes from high confidence gene sets (top).

## 5. High confidence AD gene sets

We have already compiled three high confidence AD gene sets, counting 108 genes in total:

* AD genes in knowledge bases such as UniProt
* AD genes whose expression is causal to AD inferred from transcriptome-wide association studies
* the incipient AD proteomic signature from our recent work

Next we will use these AD genes as seed to our upcoming AD candidate gene prioritization (see 4. Planned workflow).

Once our workflow is completed we will perform experimental validation as part of the DREAM prevent AD studies.  Furthermore, the present network based approach might also clarify some patho-mechanisms of comorbidities at the molecular systems level. 
