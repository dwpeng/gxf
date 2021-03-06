
gxf is a fast gtf/gff parser based pandas.

## GFF/GTF file format

The GFF (General Feature Format) format consists of one line per feature, each containing 9 columns of data, plus optional track definition lines. The following documentation is based on the Version 2 specifications.

The GTF (General Transfer Format) is identical to GFF version 2.

Fields must be tab-separated. Also, all but the final field in each feature line must contain a value; "empty" columns should be denoted with a '.'

- `chr_id` - name of the chromosome or scaffold; chromosome names can be given with or without the 'chr' prefix. Important note: the seqname must be one used within Ensembl, i.e. a standard chromosome name or an Ensembl identifier such as a scaffold ID, without any additional content such as species or assembly. See the example GFF output below.
- `source` - name of the program that generated this feature, or the data source (database or project name)
- `type` - feature type name, e.g. Gene, Variation, Similarity
- `start` - Start position* of the feature, with sequence numbering starting at 1.
- `end` - End position* of the feature, with sequence numbering starting at 1.
- `score` - A floating point value.
- `strand` - defined as + (forward) or - (reverse).
- `phase` - One of '0', '1' or '2'. '0' indicates that the first base of the feature is the first base of a codon, '1' that the second base is the first base of a codon, and so on..
- `attributes` - A semicolon-separated list of tag-value pairs, providing additional information about each feature.
*- Both, the start and end position are included. For example, setting start-end to 1-2 describes two bases, the first and second base in the sequence.

Note that where the attributes contain identifiers that link the features together into a larger structure, these will be used by Ensembl to display the features as joined blocks.

[GFF file format](https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md)


## Usage


### query all lines that type is 'gene'
```python
from gxf import GXF
filename = 'test.gff'

gff = GXF(filename)


gff.filter(type='gene')
```

### Multi-condition query
```python
from gxf import GXF
filename = 'test.gff'

gff = GXF(filename)


gff.filter(type='gene'??? strand=1)
```

You can query not only equality, but also inequality.

The query name is `field_name` + `__` + `oper`, and oper is one of the `ge`???`le`???`eq`???`ne`???`gt`???`lt`.




### query start >= 200
```python
from gxf import GXF
filename = 'test.gff'

gff = GXF(filename)

gff.filter(start__ge=200)
```

### query end < 100

```python
from gxf import GXF
filename = 'test.gff'

gff = GXF(filename)


gff.filter(end__lt=100)
```

### preprocessing data
You can use Inherits `GXF` to rewrite some method to preprocess or Post-process.

the method format is `before/after` + `_handle_` + `field_name`, eg. `after_handle_attributes`, and the method need one arg.


```python
from gxf import GXF
filename = 'test.gff'

class MyGXF(GXF):

    def before_handle_type(self, x):
        return x.lower()

    def after_handle_type(self, x):
        return x.upper()

gff = MyGXF(filename)

gff.filter(type='gene')
```
