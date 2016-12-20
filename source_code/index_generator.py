from glob import glob
import operator
import os
import traceback


CURRENT_DIRECTORY = os.getcwd()
INPUT_FOLDER = path = os.path.join(CURRENT_DIRECTORY,'generated_corpus')
OUTPUT_FOLDER_PATH = path = os.path.join(CURRENT_DIRECTORY,'indexed_terms')


def generate_unigram():
    print "started generating unigrams......"
    inverted_index = {}
    doc_num_of_tokens = {}
    doc_name_map ={} # mapping doc name and ids
    try:
        counter=1
        num_of_files = len(glob(os.path.join(INPUT_FOLDER,'*.txt')))
        for file in glob(os.path.join(INPUT_FOLDER,'*.txt')):
            perc = float((counter/float(num_of_files)))*100
            print "Processing %s - Completed %r%%" %(file[(file.rindex('\\'))+1:],round(perc,2))
            doc_name_map.update({counter:file.split('generated_corpus\\')[1][:-4]})
            doc_id = counter
            doc= open(file, 'r').read()
            doc_num_of_tokens.update({file[(file.rindex('\\'))+1:]:len(doc.split())}) #Storing number of tokens per document
            for term in doc.split():
                if not inverted_index.has_key(term):
                    doc_term_freq ={doc_id:1}
                    inverted_index.update({term:doc_term_freq})
                elif not inverted_index[term].has_key(doc_id):
                    inverted_index[term].update({doc_id:1})
                else:
                    inverted_index[term][doc_id] += 1
            counter+=1
        print doc_num_of_tokens
        generate_table(inverted_index,1)
    except Exception as e:
        print(traceback.format_exc())

def generate_bigram():
    print "started generating bigrams......"
    inverted_index = {}
    doc_num_of_tokens = {}
    doc_name_map ={}# mapping doc name and ids
    try:
        counter=1
        num_of_files = len(glob(os.path.join(INPUT_FOLDER,'*.txt')))
        for file in glob(os.path.join(INPUT_FOLDER,'*.txt')):
            perc = float((counter/float(num_of_files)))*100
            print "Processing %s - Completed %r%%" %(file[(file.rindex('\\'))+1:],round(perc,2))
            doc_name_map.update({counter:file.split('generated_corpus\\')[1][:-4]})
            doc_id = counter
            doc= open(file, 'r').read()
            term_list = doc.split()
            doc_num_of_tokens.update({file[(file.rindex('\\'))+1:]:(len(doc.split())-1)}) #Storing number of tokens per document
            for i in range(len(term_list) - 1):
                term = term_list[i]+" "+term_list[i+1]
                if not inverted_index.has_key(term):
                    doc_term_freq ={doc_id:1}
                    inverted_index.update({term:doc_term_freq})
                elif not inverted_index[term].has_key(doc_id):
                    inverted_index[term].update({doc_id:1})
                else:
                    inverted_index[term][doc_id] += 1
            counter+=1
        print doc_num_of_tokens
        generate_table(inverted_index,2)
    except Exception as e:
        print(traceback.format_exc())

def generate_trigram():
    print "started generating trigrams......"
    inverted_index = {}
    doc_num_of_tokens = {}
    doc_name_map ={}# mapping doc name and ids
    try:
        counter=1
        num_of_files = len(glob(os.path.join(INPUT_FOLDER,'*.txt')))
        for file in glob(os.path.join(INPUT_FOLDER,'*.txt')):
            perc = float((counter/float(num_of_files)))*100
            print "Processing %s - Completed %r%%" %(file[(file.rindex('\\'))+1:],round(perc,2))
            doc_name_map.update({counter:file.split('generated_corpus\\')[1][:-4]})
            doc_id = counter
            doc= open(file, 'r').read()
            term_list = doc.split()
            doc_num_of_tokens.update({file[(file.rindex('\\'))+1:]:(len(doc.split())-2)}) #Storing number of tokens per document
            for i in range(len(term_list) - 2):
                term = term_list[i]+" "+term_list[i+1]+" "+term_list[i+2]
                if not inverted_index.has_key(term):
                    doc_term_freq ={doc_id:1}
                    inverted_index.update({term:doc_term_freq})
                elif not inverted_index[term].has_key(doc_id):
                    inverted_index[term].update({doc_id:1})
                else:
                    inverted_index[term][doc_id] += 1
            counter+=1
        print doc_num_of_tokens
        generate_table(inverted_index,3)
    except Exception as e:
        print(traceback.format_exc())

def generate_table(inverted_index,n):
    print "started generating doc_freq and term_freq tables......"
    term_freq={}
    doc_freq={}
    try:
        for term in inverted_index:
            freq=0
            doc_list =[]
            for doc_id in inverted_index[term].keys():
                doc_list.append(doc_id)
                freq += inverted_index[term][doc_id]
            term_freq.update({term:freq})
            doc_freq.update({term:doc_list})
        sorted_term_freq = sorted(term_freq.items(), key=operator.itemgetter(1), reverse=True)
        write_term_freq_tables(sorted_term_freq,n)
        sorted_doc_freq = sorted(doc_freq.items(), key=operator.itemgetter(0))
        write_doc_freq_tables(sorted_doc_freq,n)
    except Exception as e:
        print(traceback.format_exc())

def write_term_freq_tables(sorted_term_freq,n):
    print "started writing term_freq table in file........"
    try:
        out_file  = open(OUTPUT_FOLDER_PATH+"\\"+ str(n) +"gram-term_freq.txt",'w')
        for item in sorted_term_freq:
            out_file.write(str(item[0])+ ":" + str(item[1]) + "\n")
        out_file.close()
    except Exception as e:
        print(traceback.format_exc())

def write_doc_freq_tables(sorted_doc_freq,n):
    print "started writing doc_freq table in file........"
    try:
        out_file  = open(OUTPUT_FOLDER_PATH+"\\"+ str(n) +"gram-doc_freq.txt",'w')
        for item in sorted_doc_freq:
            out_file.write(str(item[0])+ " " +str(item[1]) + " " + str(len(item[1])) + "\n")
        out_file.close()
    except Exception as e:
        print(traceback.format_exc())


def print_basic_instruction():
    print "======================================"
    print """\tMenu:\n
    \t Unigram - 1
    \t Bigram  - 2
    \t Trigram - 3"""
    print "======================================"


def start():
    try:
        print_basic_instruction()
        ch = raw_input("Enter the choice of n-gram: >\t")
        if ch == str(1):
            generate_unigram()
        elif ch == str(2):
            generate_bigram()
        elif ch == str(3):
            generate_trigram()
        else:
            print "Invalid input"
    except Exception as e:
        print(traceback.format_exc())

start()
