"""Utility for splitting an FML file into separate floors.
"""
import os
import sys
import json
import argparse


def create_parser() -> argparse.ArgumentParser:
    """Method to create an arguments parser.
    
    Returns:
        An ArgumentParser.
    """
    parser = argparse.ArgumentParser(description='Split FML file into separate floor')
    parser.add_argument("INPUT", help='Input .fml file')
    parser.add_argument("OUTPUT", nargs='?', help='Output .fml file format (default: INPUT_#.fml)')
    return parser


def main():
    """Entry point of the application.
    """
    
    # Arguments parsing and validation
    parser = create_parser()
    args = parser.parse_args()
    
    input = args.INPUT
    output = args.OUTPUT
    if output is None:
        output = '{}_#.fml'.format(input)
    
    if '#' not in output:
        print('*** ERR: provided OUTPUT argument ({}) does not contain # placeholder'
            .format(output),
            file=sys.stderr
        )
        sys.exit(-1)
    
    if not os.path.exists(input) or not os.path.isfile(input):
        print('*** ERR: provided INPUT argument ({}) is not a file'
            .format(input),
            file=sys.stderr
        )
        sys.exit(-2)
    
    
    # Read input
    print('Reading file... {}'.format(input))
    with open(input, 'r') as fh:
        fml = json.load(fh)
    
    floors = fml.get('floors')
    
    if not floors:
        print('*** ERR: no floors found in {}'
            .format(input),
            file=sys.stderr
        )
        sys.exit(-3)
    
    
    # Process each floor
    for lvl, floor in enumerate(floors):
        with open(output, 'w') as fh:
            # Replace floors in FML with a single floor
            floor['level'] = 0
            fml['floors'] = [floor]
            
            # Then write the results
            dst = output.replace('#', str(lvl), 1)
            print('Writing file... {}'.format(dst))
            with open(dst, 'w') as fh:
                json.dump(fml, fh)
                
    
    print('\nDone.')
    
if __name__ == '__main__':
    main()
