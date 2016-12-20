import matplotlib.pyplot as p
import traceback
import os
from glob import glob


CURRENT_DIRECTORY = os.getcwd()
INPUT_FOLDER = path = os.path.join(CURRENT_DIRECTORY,'indexed_terms')

def get_unigram_term_freq():
    sorted_term_freq = []
    try:
        for filename in glob(os.path.join(INPUT_FOLDER,'1*t*.txt')):
            with file(filename) as f:
                for line in f:
                    tup = line.split(':')
                    tup[1] = int(tup[1])
                    sorted_term_freq.append(tup)
        return sorted_term_freq
    except Exception as e:
        print(traceback.format_exc())

def get_bigram_term_freq():
    sorted_term_freq = []
    try:
        for filename in glob(os.path.join(INPUT_FOLDER,'2*t*.txt')):
            with file(filename) as f:
                for line in f:
                    tup = line.split(':')
                    tup[1] = int(tup[1])
                    sorted_term_freq.append(tup)
        return sorted_term_freq
    except Exception as e:
        print(traceback.format_exc())

def get_trigram_term_freq():
    sorted_term_freq = []
    try:
        for filename in glob(os.path.join(INPUT_FOLDER,'3*t*.txt')):
            with file(filename) as f:
                for line in f:
                    tup = line.split(':')
                    tup[1] = int(tup[1])
                    sorted_term_freq.append(tup)
        return sorted_term_freq
    except Exception as e:
        print(traceback.format_exc())

def plotgraph(sorted_term_freq,n):
    try:
        total_words = 0
        for item in  sorted_term_freq:
            total_words+=item[1]
        freq = [float(x[1]/float(total_words)) for x in sorted_term_freq]
        ax1 = p.subplot2grid((1,1),(0,0))
        if n == 1:
            ax1.plot(range(len(sorted_term_freq)),freq, label="Unigram")
        elif n == 2:
            ax1.plot(range(len(sorted_term_freq)),freq, label="Bigram")
        else:
            ax1.plot(range(len(sorted_term_freq)),freq, label="Trigram")
        p.ylabel('Probability\n(no. of occurence)')
        p.xlabel('Rank\n(decreasing frequency)')
        ax1.set_yscale('log')
        ax1.set_xscale('log')
        p.subplots_adjust(bottom=0.15,right=0.94,left=0.17,wspace=0.2,hspace=0.1)
        p.legend()
        p.title('Zipf\'s law\n(This is a log-log plot of Zipf\'s law)')
        p.show()
    except Exception as e:
        print(traceback.format_exc())

def plotallgraph(sorted_term_freq1,sorted_term_freq2,sorted_term_freq3):
    try:
        total_words1 = 0
        for item in  sorted_term_freq1:
            total_words1+=item[1]
        freq1 = [float(x[1]/float(total_words1)) for x in sorted_term_freq1]
        total_words2 = 0
        for item in  sorted_term_freq2:
            total_words2+=item[1]
        freq2 = [float(x[1]/float(total_words2)) for x in sorted_term_freq2]
        total_words3 = 0
        for item in  sorted_term_freq3:
            total_words3+=item[1]
        freq3 = [float(x[1]/float(total_words3)) for x in sorted_term_freq3]
        ax1 = p.subplot(1,1,1)
        ax2 = p.subplot(1,1,1)
        ax3 = p.subplot(1,1,1)
        ax1.plot(range(len(sorted_term_freq1)),freq1, label="Unigram")
        ax2.plot(range(len(sorted_term_freq2)),freq2, label="Bigram")
        ax3.plot(range(len(sorted_term_freq3)),freq3, label="Trigram")
        ax1.set_yscale('log')
        ax1.set_xscale('log')
        ax2.set_yscale('log')
        ax2.set_xscale('log')
        ax3.set_yscale('log')
        ax3.set_xscale('log')
        p.ylabel('Probability\n(no. of occurence)')
        p.xlabel('Rank\n(decreasing frequency)')
        p.subplots_adjust(bottom=0.15,right=0.94,left=0.17,wspace=0.2,hspace=0.1)
        p.legend()
        p.title('Zipf\'s law\n(This is a log-log plot of Zipf\'s law)')
        p.show()
    except Exception as e:
        print (traceback.format_exc())

def print_basic_instruction():
    print "======================================================"
    print """\tMenu:\n
    \t To Plot graph for only Unigram - 1
    \t To Plot graph for only Bigram  - 2
    \t To Plot graph for only Trigram - 3
    \t To Plot graph for n-grams      - 4"""
    print "======================================================"

def plotstart():
    try:
        print_basic_instruction()
        ch = raw_input("Enter your choice: >\t")
        if ch == str(1):
            sorted_term_freq = get_unigram_term_freq()
            plotgraph(sorted_term_freq,1)
        elif ch == str(2):
            sorted_term_freq = get_bigram_term_freq()
            plotgraph(sorted_term_freq,2)
        elif ch == str(3):
            sorted_term_freq = get_trigram_term_freq()
            plotgraph(sorted_term_freq,3)
        elif ch == str(4):
            sorted_term_freq1 = get_unigram_term_freq()
            sorted_term_freq2 = get_bigram_term_freq()
            sorted_term_freq3 = get_trigram_term_freq()
            plotallgraph(sorted_term_freq1,sorted_term_freq2,sorted_term_freq3)
        else:
            print "Invalid Input"
    except Exception as e:
        print(traceback.format_exc())

plotstart()
