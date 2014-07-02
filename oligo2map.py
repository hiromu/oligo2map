#!/usr/bin/env python

import sys

def oligo2map(input_file, output_file):
    line = input_file.readline().split()
    assert line[0] == 'forward', 'The first line should start with `forward`'

    primer = line[1]
    output_file.write('#SampleID\tBarcodeSequence\tLinkerPrimerSequence\tDescription\n')

    for line in input_file.readlines():
        data = line.split()
        assert data[0] == 'barcode', 'Each lines should start with `barcode`'

        barcord, id = data[1:3]
        comments = '\t'.join(data[3:])
        if len(comments) == 0:
            comments = 'N/A'

        output_file.write('%s\t%s\t%s\t%s\n' % (id, barcord, primer, comments))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: %s [input file] [output file]' % sys.argv[0])

    with open(sys.argv[1], 'r') as input:
        with open(sys.argv[2], 'w') as output:
            oligo2map(input, output)
