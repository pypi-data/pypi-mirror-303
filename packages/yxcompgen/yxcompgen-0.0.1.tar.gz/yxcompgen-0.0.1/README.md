# yxcompgen
Xu Yuxing's personal comparative genomics tools

## Installation
```
pip install yxcompgen
```

## Usage

### Example for orthogroups analysis

orthogroups tsv file: The format which OrthoFinder outputs (`Orthogroups.tsv`), with the first column as orthogroup ID and the rest columns as gene IDs from different species, separated by tab (`\t`) and gene IDs separated by a comma and a space (`, `). File have a header line, which first column is `Orthogroup` and the rest columns are species names.

read a orthogroups file:
```python
from yxcompgen import OrthoGroups
OGs = OrthoGroups(OG_tsv_file="/path/to/Orthogroups.tsv")
# get orthogroup information
OGs.get(('OG0000000', 'Ath'))
```

species info file: An Excel file with columns `sp_id`, `taxon_id`, `species_name`, `genome_file`, `gff_file`, `pt_file`, `cDNA_file`, `cds_file`. `sp_id` is the species ID, `taxon_id` is the taxon ID, `species_name` is the species name, `genome_file` is the genome file path, `gff_file` is the GFF file path, `pt_file` is the protein sequence file path, `cDNA_file` is the cDNA sequence file path, `cds_file` is the CDS sequence file path.

read a species info file:
```python
from yxcompgen import read_species_info
ref_xlsx = '/path/to/species_info.xlsx'
sp_info_dict = read_species_info(ref_xlsx)
```


### Example for synteny blocks building

1. input: gff file and gene pair file

gff file should be in gff3 format, and gene pair file should be a tab-delimited file with two columns, each row is a gene pair from two species.
```
Cca_Gene1 Sly_Gene1
Cca_Gene2 Sly_Gene2
...
```

```python
sp1_id = 'Cca'
sp1_gff = '/path/to/Cca.gff3'
sp2_id = 'Sly'
sp2_gff = '/path/to/Sly.gff3'
gene_pair_file = '/path/to/gene_pair.txt'
```

2. build synteny blocks
    
```python
from yxcompgen import GenomeSyntenyBlockJob
sb_job = GenomeSyntenyBlockJob(
    sp1_id, sp1_gff, sp2_id, sp2_gff, gene_pair_file)
sb_job.build_synteny_blocks()
```

3. write synteny blocks to file

output file is in MCScan format

```python
mcscan_output_file = "/path/to/collinearity_output.txt"
sb_job.write_mcscan_output(mcscan_output_file)
```

4. Or you can read synteny blocks from file
    
```python
sb_job = GenomeSyntenyBlockJob(
    sp1_id, sp1_gff, sp2_id, sp2_gff)
sb_job.read_mcscan_output(mcscan_output_file)
```

5. You can also work with only one genome

```python
sb_job = GenomeSyntenyBlockJob(
    sp1_id, sp1_gff, gene_pair_file=gene_pair_file)
```

### Example for synteny blocks plot

```python
sb_job.plot()
highlight_sb_list = [65, 178, 237, 331]
sb_job.plot(mode='loci', reverse=True, highlight_synteny_blocks=highlight_sb_list)
```

