import polars as pl
from dataclasses import dataclass
import json
from pyteomics.parser import cleave
from warnings import warn
import pkg_resources
import pandas as pd
import numpy as np
import textwrap
import requests
import re

from z_score_target_engagement import ProcessUtils, DataLoader



@dataclass
class Protein():
    """ A class to store information about a single protein.
    """
    gene_id: str            # The protein's gene ID
    protein_id: str         # The protein's unitprot ID
    sequence: str           # The protein's amino acid sequence
    is_tf: bool = False     # If the protein is a transcription factor
    
    c_idx: set = None           # All existing cysteine sites
    ms_c_sites: set = None      # All existing observable cysteine sites
    
    total_coverage: float = 0.0 # Portion of ALL cysteine sites observed
    ms_coverage: float = 0.0    # Portion of OBSERVABLE cysteine observed

    all_possible_peptides: set = None  # Possible peptides with trypsin digest
    all_possible_ms_peptides: set = None   # Peptides that can be seen with MS
    portion_observable_sites: float = 0.0  # Observable/Total peptides

    found_peptides: list = None # Peptides found in the mass spec experiment
    c_found: set = None         # All found cysteine sites

    def __post_init__(self) -> None:
        """
        Post init for a Protein. Enumerates cysteine sites, generates 
        list of all possible peptides and those that are observable by MS.
        """

        # Initialze sets and get the indexes of cysteines in the protein
        self.c_found = set()
        self.all_possible_ms_peptides = set()
        self.ms_c_sites = set()
        self.get_c_idx()
    
    def get_c_idx(self) -> set:
        """
        Find the indices of all cysteines in the amino acid sequence

        Returns:
            set: locations of all cysteines in the amino acid
        """
        # Find ALL indices where character C occurs in sequence string, 
        self.c_idx = set([i for i, ltr in enumerate(self.sequence) \
                          if ltr == 'C'])
        return self.c_idx

    def to_dict(self) -> dict:
        """
        Convert the Protein object to a dictionary

        Returns:
            dict: Dictionary of protein with attributes as keys and values
        """

        return {
            'gene_id': self.gene_id,
            'is_tf': self.is_tf,
            'c_idx': list(self.c_idx),
            'c_found': list(self.c_found),
            'ms_c_sites': list(self.ms_c_sites),
            "total_c_sites": len(self.c_idx),
            'total_c_found': len(self.c_found),
            'total_ms_sites': len(self.ms_c_sites),
            'total_coverage': self.total_coverage,
            'ms_coverage': self.ms_coverage,
            'portion_observable_sites': self.portion_observable_sites,
        }
    
    
@dataclass
class ProteinLoader():
    """Collection of functions related to instantiating the Protein class
    and finding the amino acid sequence of a given protein.

    Attributes:
        process_utils (ProcessUtils): An instance of the ProcessUtils class 
        needed for identifying if a protein is a transcription factor or not
        seq_by_protein_id (dict): A dictionary containing protein amino acide
        sequences with uniprot protein IDs as the keys.

    """
    process_utils = ProcessUtils()
    seq_by_protein_id: dict = None

    def __post_init__(self):
        """
        Post initialize ProteinLoader. Load the sequence by protein ID dict.
        """
        self.seq_by_protein_id = self.load_seq_by_protein_id()

    def load_protein(self, target: str, protein_string: str) -> Protein:
        """Instantiate a protein object and get sequence information and 
        transcription factor status for a given gene.

        Args:
            target (str): Gene ID
            protein_string (str): Protein ID string

        Returns:
            Protein: Instance of protein for the given protein ID.
        """
        sequence = self.get_sequence(target, protein_string)
        if not sequence:
            print(f"Could not find sequence for protein {target}.")
            return None
        protein = Protein(target, 
                          self.process_protein_id(protein_string),
                          sequence)
        protein.is_tf = self.process_utils._is_tf(target)
        return protein

    @staticmethod
    def load_seq_by_protein_id() -> dict:
        """
        Load a dictionary of protein sequence information

        Returns:
            dict: Dictionary with uniprot protein IDs as keys and peptide 
            sequence string as values.
        """
        path = pkg_resources.resource_filename('cysteine_counter',
                                'data/sequence_by_protein_id.json')
        
        with open(path, "r") as file:
            seq_by_protein_id = json.load(file)

        return seq_by_protein_id

    def get_sequence(self, target: str, protein_string: str) -> str:
        """ Get the amino acid sequence for a given protein.

        Args:
            target (str): Gene ID for the protein
            protein_string (str): Protein ID string

        Returns:
            str: amino acid sequence
        """
        if target is None:
            return

        proteins = self.process_protein_id(protein_string)
        for protein in proteins:
            if protein in self.seq_by_protein_id.keys():
                return self.seq_by_protein_id[protein]
        
        # If it's not in either dictionary, try looking it up online
        for protein in proteins:
            sequence = self.lookup_protein_sequence(protein)
            if sequence:
                return sequence


    def process_protein_id(self, protein_string: str) -> list:
        """An annoying way of splitting up multiple protein IDs in search of a 
        sequence match. This is necessary for genes that have a different name
        in diann vs uniprot but may have matching protein ids.
        
        Takes a string such as 'Q8WUQ7;Q8WUQ7-2;ABCD;XYDF-3' and returns
        ['Q8WUQ7', 'XYDF', 'ABCD']"""
        proteins = protein_string.split(";")
        proteins = [protein.split("-")[0] for protein in proteins]
        return list(set(proteins))
    
    def lookup_protein_sequence(self, protein_id: str) -> str:
        """Last resort method of getting the amino acid sequence from 
        the uniprot website

        Args:
            protein_id (str): Protein id string

        Returns:
            str: amino acid sequence
        """
        # Last resort: just lookup the protein sequence in uniprot
        url = f"https://www.uniprot.org/uniprot/{protein_id}.fasta"
        try:
            response = requests.get(url)
        
            fasta_data = response.text
            # Extract the sequence from the FASTA format
            lines = fasta_data.strip().split("\n")
            sequence = ''.join(lines[1:]) 
            return sequence
        except:
            return



@dataclass
class ProteinProcessor():
    """Houses functions to process protein sequences to find cysteine sites,
    get theoretical peptides, and determine which cysteine sites could be
    observed by mass spec.

    Attributes:
        min_peptide_len (int) = 7: The minimum number of amino acids required
        for a peptide to be considered mass spec observable.
        max_peptide_len (int) = 40: The maximum number of amino acids for 
        a peptide to be considered mass spec observable.
    """
    min_peptide_len: int = 7
    max_peptide_len: int = 40

    def process_protein_sequence(self, protein: Protein) -> Protein:
        """Process a protein's amino acid sequence to determine how many 
        peptides are mass spec observable and what cysteine sites these 
        correspond to.

        Args:
            protein (Protein): An instance of a protein to process
        Returns:
            Protein: the processed protein
        """

        # Cleave the protein to get all possible peptides
        protein = self.cleave_sequence(protein)  

        # Isolate theoretic peptides that are "MS observable" AND contain cys
        protein = self.get_ms_peptides(protein)  

        # Get the location of these cystine sites
        protein = self.locate_ms_c_sites(protein)

        # Calculate what portion of all cysteines we could theoretically 
        # see with mass spec
        protein = self.calculate_portion_observable_sites(protein)

        return protein
    
    def cleave_sequence(self, protein: Protein) -> Protein:
        """ Trypsin digest a protein to get a list of all possible peptides.

        Args:
            protein (Protein): protein to cleave

        Returns:
            Protein: protein with all possible peptide information
        """
        protein.all_possible_peptides = cleave(protein.sequence, 'Trypsin/P', 2)
        return protein
    
    def get_ms_peptides(self, protein: Protein) -> Protein:
        """Take the list of all possible peptides and identify only those that 
        are observable by MS (as determined by their size) and that have a 
        cysteine residue

        Args:
            protein (Protein): A protein that has been "digested"

        Returns:
            Protein: The protein with observable peptide information
        """
        protein.all_possible_ms_peptides = \
            [pep for pep in protein.all_possible_peptides \
                if (self.min_peptide_len <= len(pep) \
                <= self.max_peptide_len) and 'C' in pep]
        return protein
    
    def locate_ms_c_sites(self, protein: Protein) -> Protein:
        """Get the indices of all cysteines that could theoretically be 
        observed by mass spec

        Args:
            protein (Protein): protein with MS peptide information

        Returns:
            Protein: Protein with indices for all MS observable cysteines
        """
        found = set()

        for peptide in protein.all_possible_ms_peptides:
            found_sites = CysteineCounter.map_c_sites(protein, peptide)
            found.update(found_sites)

        protein.ms_c_sites = found

        return protein
    
    def calculate_portion_observable_sites(self, protein: Protein) -> Protein:
        """Calculate the portion of cysteine sites that could theoretically
        be observed by mass spec.

        Args:
            protein (Protein): A protein with peptide and ms peptide information

        Returns:
            Protein: A protein with portion observable sites information
        """
        try: 
            protein.portion_observable_sites = \
                len(protein.ms_c_sites) / len(protein.c_idx)
        except:
            protein.portion_observable_sites = np.nan
        return protein 
    
    def strip_peptide_sequences(self, protein: Protein) -> Protein:
        """Peptides from EncyclopeDIA pipelines will often have modification
        info embedded of the sequence. This function strips that information.

        For example: 'GPHGC[+57.021464]HSP' -> 'GPHGCHSP'

        Args:
            protein (Protein): A protein with the found_peptides attribute 
            populated.

        Returns:
            Protein: The protein with found_peptides stripped of modification
            annotations.
        """
        protein.found_peptides = [re.sub(r'[^a-zA-Z]', '', peptide) \
                                  for peptide in protein.found_peptides]
        return protein
    
    def strip_all_peptide_sequences(self, proteins_by_id: dict) -> dict:
        """Apply the strip_peptide_sequences function to all proteins in 
        a collection to strip any modification annotations fround found
        peptides.

        Args:
            protiens_by_id (dict): A dictionary of Protein objects by 
            their IDs.

        Returns:
            dict: The Protein dictionary with each protein's peptides 
            stripped.
        """
        for protein_id, protein in proteins_by_id.items():
            proteins_by_id[protein_id] = self.strip_peptide_sequences(protein)
        return proteins_by_id


@dataclass
class ProteinCollectionBuilder():
    """Builds a collection of Protein objects from a pr_matrix dataframe.

    Attributes:
        loader (ProteinLoader): An instance of the ProteinLoader class to
        load a protein and it's sequence information
        processor (ProteinProcessor): An instance of the ProteinProcessor class
        to process the proteins sequence information and cysteine indices.
    """

    loader: ProteinLoader=None
    processor: ProteinProcessor=None

    
    def load_protein_by_id(self, df: pd.DataFrame) -> dict:
        """Create a dictionary of proteins that have sequences and information
        about their cysteine sites and possible peptides

        Args:
            df (pd.DataFrame): A pr_matrix dataframe resulting from DIANN

        Returns:
            dict: A dictionary of proteins with the gene ID as keys and 
            instances of the Protein class as values
        """
        not_found = set()  # avoid looking for targets if they're not there

        protein_by_id = {}
        for target, protein_string in zip(df["Genes"], df["Protein.Ids"]):
            if target not in protein_by_id.keys() and target not in not_found:
                protein = self.loader.load_protein(target, protein_string)
                if protein:
                    protein = self.processor.process_protein_sequence(protein)
                    protein_by_id[target] = protein
                else: 
                    # If it's not in either dict and can't be found track
                    # it to avoid looking for it again
                    not_found.add(target)
        protein_by_id = self.get_found_peptides(df, protein_by_id)
        return protein_by_id

    def get_found_peptides(self, df: pd.DataFrame, protein_by_id: dict) -> dict:
        """Gather the peptides observed and store them with their respective
        proteins

        Args:
            df (pd.DataFrame): A pr_matrix dataframe resulting from DIANN
            protein_by_id (dict): A dictionary of proteins with the gene 
            ID as keys and instances of the Protein class as values

        Returns:
            dict: The protein_by_id dictionary updated with the peptides
            observed in the dataframe.
        """
        found_peptides = df.groupby("Genes")["Stripped.Sequence"].unique()
        for protein_id, protein in protein_by_id.items():
            if protein_id in found_peptides:
                protein.found_peptides = found_peptides[protein_id]
        return protein_by_id

@dataclass
class CysteineCounter():
    """A class for counting the unique cysteine sites observed in a collection
    of peptides.
    """


    def count_cysteines(self, protein_by_id: dict) -> dict:
        """For each protein, find the indices of the cysteines of the observed
        peptides.

        Args:
            protein_by_id (dict): A dictionary of proteins with the gene 
            ID as keys and instances of the Protein class as values

        Returns:
            dict: A dictionary of proteins with the gene 
            ID as keys and instances of the Protein class as values with each
            Protein updated with cysteine count and index information.
        """
        for protein_id, protein in protein_by_id.items():
            protein = self.locate_cysteines(protein)
            protein = self.calculate_coverages(protein)
            protein_by_id[protein_id] = protein
        return protein_by_id


    def get_result_dataframe(self, protein_by_id: dict) -> pd.DataFrame:
        """Produce a dataframe summarizing the results.

        Args:
            protein_by_id (dict): A dictionary of proteins with the gene 
            ID as keys and instances of the Protein class as values with each
            Protein updated with cysteine count and index information.

        Returns:
            pd.DataFrame: A dataframe summarizing cysteine count and 
            coverage information
        """
        for protein_id, protein in protein_by_id.items():
            protein = self.calculate_coverages(protein)
            protein_by_id[protein_id] = protein

        protein_data = [protein_by_id[key].to_dict() \
                        for key in protein_by_id.keys()]
        return pd.DataFrame(protein_data)


    @staticmethod
    def find(s: str, start_idx: int) -> list:
        """Correct the cysteine indices for a peptide by adding the starting 
        index to each index.

        For example, if the peptide ABC begins at index 10 of an
        amino acid sequence, then this function corrects the index of C from 2
        to 12.

        Args:
            s (str): A peptide amino acid sequence
            start_idx (int): The index of a protein amino acid sequence where
            the peptide substring occurs
        Returns:
            list: A list of the corrected indices of the cysteines in the 
            peptide
        """
        # Get list of indices where C occurs in s, the substring
        idx = [i for i, ltr in enumerate(s) if ltr == 'C']  

        # Add starting idx to each c index to get it's location in the
        # protein seq 
        return [x+start_idx for x in idx]  

    @staticmethod
    def map_c_sites(protein: Protein, peptide: str) -> set:
        """Given a peptide with at least one cysteine, find the index of
        the cysteine(s) in the protein amino acid sequence.

        Args:
            protein (Protein): The Protein the peptide belongs to
            peptide (str): The peptide amino acid sequence

        Raises:
            ValueError: If the protein sequence is None (ie it was not found)

        Returns:
            set: The indices of the cysteines in the peptide
        """


        if protein.sequence is None:
            raise ValueError(f"Sequence for protein {protein.gene_id} is None")
        
        found_sites = set()
        
        # Slide the peptide along the protein sequence until we find the 
        # region of the protein sequence that matches the peptide
        for start_idx in range(0, len( protein.sequence) - len(peptide) + 1):
            sub_seq = protein.sequence[start_idx: start_idx + len(peptide)]
            if sub_seq == peptide:
                # When we've found the matching region, get the indices of the 
                # cysteines we've found in the protein sequence
                found_idx =  CysteineCounter.find(sub_seq, start_idx)
                for i in found_idx: # Add these indices to the set of found Cys.
                    found_sites.add(i)
        return found_sites
    

    def locate_cysteines(self, protein: Protein) -> Protein:
        """Locate the indices for all cysteines for all peptides found for a 
        given protein.

        Args:
            protein (Protein): The protein containing a list of found peptides

        Returns:
            Protein: The protein updated with the indices of the found 
            cysteines.
        """
        found = set()

        for peptide in [pep for pep in protein.found_peptides if "C" in pep]:
            found_sites = CysteineCounter.map_c_sites(protein, peptide)
            found.update(found_sites)

        protein.c_found = found
        return protein

    def calculate_coverages(self, protein: Protein) -> Protein:
        """Calculate the coverage of a protein, how many cysteines were found 
        out of the total number of cysteines and out of the number of cysteines
        observable by mass spec.

        Args:
            protein (Protein): The protein with the indices of the cysteines 
            for all found peptides

        Returns:
            Protein: The protein updated with coverage information
        """
        try:
            protein.total_coverage = len(protein.c_found) / len(protein.c_idx)
        except:
            protein.total_coverage = np.nan
        try:
            protein.ms_coverage =  \
                len(protein.c_found) / len(protein.ms_c_sites)
        except:
            protein.ms_coverage = np.nan
        return protein


    def get_coverage_report(self, coverage_df: pd.DataFrame,
                            write_out_path: str=None) -> str:
        """ Summarize a results dataframe.

        Args:
            coverage_df (pd.DataFrame): A dataframe with the cysteine count
            results
            write_out_path (str): Optional - the path to save the summary 
            report
        
        Returns:
            str: A summary of the results dataframe.
        """

        observe_portion = coverage_df['portion_observable_sites'].mean()
        num_complete = len(coverage_df.loc[coverage_df["c_found"]== \
                                       coverage_df["total_c_sites"]])
        total_proteins = coverage_df["gene_id"].nunique()

        mean_total_coverage = coverage_df["total_coverage"].mean()
        mean_ms_coverage = coverage_df["ms_coverage"].mean()
        
        total_sites_observed = coverage_df["c_found"].apply(len).sum()
        total_sites = coverage_df["total_c_sites"].sum()
        total_ms = coverage_df["total_ms_sites"].sum()

        report = textwrap.dedent(f"""\
            --------------------------------------------------------
            Total proteins analyzed: {total_proteins}
            Proteins with all cysteines identified: {num_complete}
            --------------------------------------------------------
            Mean percent observable cysteine sites: {observe_portion*100:.2f}%
            --------------------------------------------------------
            Mean percent coverage: {mean_total_coverage*100:.2f}%
            Mean observable coverage: {mean_ms_coverage*100:.2f}%
            --------------------------------------------------------
            Total cysteine sites: {total_sites}
            Total observable sites: {total_ms}
            Total sites observed: {total_sites_observed}
        """)

        if write_out_path:
            with open(write_out_path, "x") as f:
                f.write(report)
        return report
