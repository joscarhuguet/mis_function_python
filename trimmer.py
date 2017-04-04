from Bio.SeqIO.QualityIO import FastqGeneralIterator
import sys
#if  (len(sys.argv < 3) ):
#	sys.stderr.write("E: usage file name cut from 3 cut forom5")
#	sys.stderr.flush();
#	exit( 2 );
#else:
file = sys.argv[1]
trim = int(sys.argv[2])
end = int(sys.argv[3])

#trim = 10
#end = 10
for title, seq, qual in FastqGeneralIterator(open(file, 'r')) :
	print("@" + str(title) + "\n" + str(seq[trim:(len(seq) - end)]) + "\n" + "+" + "\n" + str(qual[trim : (len(qual) - end)]))
