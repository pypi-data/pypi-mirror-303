# Cysteine Counter Package

This package can be used to identify unique cysteine sites observed in mass spec data.

## Installation
Install with the command 
```pip install cysteine_counter```
There might also be some dependencies I have yet to include in the pip installation. 

## Quick Start
To analyze cysteine counts and coverage from a given diann tsv file:
```
from cysteine_counter import *

# Load the diann file
dl = DataLoader()
# Must include stripped sequence to count cysteines
data_container = dl.load_data(<path_to_file>, include_stripped_sequence=True)

# Instantiate the counter and collection builder
cc = CysteineCounter()
pcb = ProteinCollectionBuilder(ProteinLoader(), ProteinProcessor())

# Build the protein collection
proteins_by_id = pcb.load_protein_by_id(data_container.raw_df)

# Count cystienes
proteins_by_id = cc.count_cysteines(proteins_by_id)

# Get the results in a dataframe
result = cc.get_result_dataframe(proteins_by_id)

# Print a summary of the results
report = cc.get_coverage_report(result)
print(report)
```

## Using an encyclopeDIA file
To use an encyclopeDIA file, there are some extra steps needed to make it look like a diann file.
```
from cysteine_counter import *

# Load the encyclopedia file
dl = DataLoader()
data_container = dl.load_data(<path_to_file>)

# Instantiate a PeptideProcessor and convert the encyclopedia file to diann
p = PeptideProcessor()
data_container = p._convert_encyclopedia_file(data_container)
data_container.raw_df = data_container.raw_df.rename(columns={"Precursor.Id": "Stripped.Sequence"})

# Instantiate the counter and collection builder
cc = CysteineCounter()
pcb = ProteinCollectionBuilder(ProteinLoader(), ProteinProcessor())

# Build the protein collection
proteins_by_id = pcb.load_protein_by_id(data_container.raw_df)

# Strip modification annotations from peptide sequences
proteins_by_id = pcb.processor.strip_all_peptide_sequences(proteins_by_id)

## Then proceed with counting
```

# Cysteine Analysis

The purpose of this notebook is to answer two primary questions:

1. How many cysteine sites are we able to detect with mass spec?
2. Do transcription factors tend to have more cysteine residues than non-TF protiens?

## Part 1: Detecting Cysteine Sites
### Purpose
This analysis aims to quantify our ability to observe cysteine sites MS. There are two ways to think of this:
1. How many cysteine sites are we able to detect out of all the cysteine sites that exist?
2. How many cysteine sites are we able to detect out of the cysteine sites that could theoretically be seen with mass spec?

### Method
This notebook looks at three datsets:
1. THP-1 data on AWS
2. Anborn screen data
3. Data from all screens on AWS

#### Constructing a protein sequence hashmap
Using the fasta file and the make_seq_id_map.py script, I constucted a hashmap that makes the protein ID to it's peptide sequence. This hashmap contains all proteins in the human proteome. It is stored as sequence_by_ids.json to avoid reconstructing it each time this script is run. 

#### Comparing peptide sequences
Each cysteine-containg peptide in the tsv file is compared to its protein sequence to find the exact location to the cysteine it contains. This means that if there are two peptides that "overlap" and have a shared sequence containing a cysteine, this cysteine will not be counted twice. 

#### Ovbservable vs. total cysteine sites
We expect there to be some cysteine sites that cannot be observedby mass spec. Perhaps they are contained in a very large peptide that cannot be properly analyzed. In addition to determining how many cysteine sites we see out of all that exist, it is also useful to understand how many we see out of those that are possible to see. 

Each protein was trypsin digested *in silico* allowing for some miscleaves. This produced a library of every peptide that we could reasonably expect to produce with a trypsin digest for each protein. Of these peptides, only those containg a cysteine residue are of interest. For simplicity, the "observable" peptides are peptides that are between 7 and 40 amino acids long. This is of course an over simplification, but it is useful as an approximation. 

It turns out that there is significant overlap between the set of peptides that contain a cysteine residue and the set of peptides that contain a cysteine residue *and* are between 7 and 40 amino acids long. 95% of all cysteine residues are "observable" by this criterion. For this reason, the results of this analysis are almost identical for the total number of cysteine residues and the total number of "observable" cysteine residues.

### Results
Using the THP-1 data, we observe about 25% of the cysteine residues. 
Anborn data - we observe ~ 35% of the cysteine residues.
Overall, we observe about 25% of the cysteine residues.


## Part 2: Testing for Cysteine Enrichment in Transcription Factors

### Purpose
Preliminary analyses suggest that transcription factor proteins may contain more cysteine residues compared to non-transcription factor proteins. This analysis aims to perform a similar analysis on a per protein basis (as opposed to per population) and confirm that any observed enrichment is a real effect.

### Methods

This section of the notebook uses two external datasets:
1. Gene, sequence, and protein ID data for the entire human proteome, curated by UniProt
2. A list of human genes that encode transcription factors according to [Lambert et al. 2018, table S1](https://www.cell.com/cell/fulltext/S0092-8674(18)30106-5?_returnURL=https%3A%2F%2Flinkinghub.elsevier.com%2Fretrieve%2Fpii%2FS0092867418301065%3Fshowall%3Dtrue#supplementaryMaterial)

#### Labeling TFs
In addition to the id-to-sequence map generated in part 1, I generated a map of gene IDs to protein IDs which I used to create a list of protein IDs for transcription factors. The proteome was compared to this list to label each protein as either a transcription factor or not.

#### Determining Cysteine Composition
For each protein in the proteome, I counted the number of cysteine residues in the peptide sequence and divided this by the number of amino acids in the protein to determine the cysteine percentage in each protein.

### Comparing Cysteine Composition
I split the proteome into two groups: TFs and non-TFs. I then compared the average cysteine composition in each group.

As a control, I randomly split the proteome into two groups with the same number of proteins in each group as the TF and non-TF split. I then looked at the average cystein composition in the smaller group (which represents the TF group). I repeated this 1000 to gather a distribution of cysteine percentages in a random subset of the proteome. I then used a one-sample, one-tailed t test to test if the mean of the random distribution was significantly different the the average cysteine composition in transcription factors.

### Results
Transcription factors are enriched for cysteine compared to non-TF proteins (p<<<0.01).


*Prepared by Lilly Tatka on 8/20/2024*
