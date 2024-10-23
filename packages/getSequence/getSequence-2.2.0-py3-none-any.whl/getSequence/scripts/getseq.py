#!/usr/bin/env python

# executing script allowing direct input of a protein name to get a graph back
# import stuff for making CLI

import os
import argparse

# import functionality to get a sequence
from getSequence.getseq import getseq as get


def main():
    # Parse command line arguments.
    parser = argparse.ArgumentParser(description='Get a sequence from a protein name or UniProt accession number.')

    parser.add_argument('name', nargs='+', help='Name of the protein.')

    parser.add_argument('-j', '--just_sequence', action='store_true', help='Optional. Use this flag to stop any printed text to the terminal except for the sequence.')

    parser.add_argument('-u', '--uniprot-id', action='store_true', help='Optional. Use this flag to denote that you are putting in a valid Uniprot ID.')

    parser.add_argument('-i', '--ignore-commas', action='store_true', help='Optional. Use this flag to denote that you are inputting a single query that has a comma. This disables the separation of entries by commas.')

    parser.add_argument('-o', '--output', help='Optional. Use this flag to denote that you want to output the sequences to a file.')

    parser.add_argument('-p', '--print_failed_queries', action='store_true', help='Optional. Use this flag to print failed queries when saving the output rather than saving a failed_queries.txt file.')

    # parse the args
    args = parser.parse_args()

    # get True / False values
    # see if we are using a uniprot ID
    if args.uniprot_id:
        use_id=True
    else:
        use_id=False
    # see if you should print the entire uniprot ID to the terminal
    if args.just_sequence:
        print_uniprot=False
    else:
        print_uniprot=True   
    # see if we should ignore commas
    if args.ignore_commas:
        ignore_commas=True
    else:
        ignore_commas=False

    # set save_file to false
    save_file=False
    # check the output path
    if args.output:
        # set save_file to true
        save_file=True
        # set full output path
        full_output_path = args.output
        # get the path and file
        path = os.path.dirname(full_output_path)
        file = os.path.basename(full_output_path)
        if os.path.exists(path)==False:
            raise Exception(f'Path {path} does not exist.')


    # get protein name. It comes as a list, so we 
    # need to pull that out and format it as a string. 
    final_names = ''
    for i in args.name:
        final_names += i
        final_names += ' '

    # set multiple names to False
    multiple_names=False

    # see if we have comma separated names. 
    if ',' in final_names:
        if ignore_commas==False:
            final_names = final_names.split(',')
            multiple_names=True

    # if we have single name, make into a list
    if multiple_names==False:
        final_names = [final_names]

    # list of failures
    failed_queries=[]

    # str to hold file output
    output_values=''

    # iterate through names
    for final_name in final_names:
        # get rid of trailing spaces. 
        if final_name[-1]==' ':
            final_name = final_name[:len(final_name)-1]
        if final_name[0]==' ':
            final_name = final_name[1:]
        
        # try to get query, otherwise print unable to retrieve to user. 
        try:
            # sequence and name
            seq_and_name = get(final_name, uniprot_id=use_id)
        except:
            failed_queries.append(f"Unable to retrieve sequence for the query '{final_name}'")
            continue

        # figure out what to print if anything
        if print_uniprot==True:
            output_values+=f'>{seq_and_name[0]}\n{seq_and_name[1]}\n'
        else:
            output_values+=f'{seq_and_name[1]}\n'

    # either print or write out the output values
    if save_file==True:
        with open(full_output_path, 'w') as f:
            f.write(output_values)
        f.close()
        if multiple_names==True:
            print(f'\nSequences saved to {full_output_path}\n')
        else:
            print(f'\nSequence saved to {full_output_path}\n')
    else:
        print(output_values)

    # print failed queries
    if failed_queries!=[]:
        if len(failed_queries)>1:
            print('Failed queries detected!')
            fail_output='\n\nFailed queries:\n'
        else:
            print('Failed query detected!')
            fail_output='\n\nFailed query:\n'
        for query in failed_queries:
            fail_output+=f'{query}\n'
        fail_output+='\n'
        if save_file==False:
            print(fail_output)
        else:
            if args.print_failed_queries:
                print(fail_output)
            else:
                print(f'\nFailed queries saved to {path}/failed_queries.txt')
                with open(f'{path}/failed_queries.txt', 'w') as f:
                    f.write(fail_output)
                f.close()



