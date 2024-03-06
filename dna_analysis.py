from Bio import SeqIO
import matplotlib.pyplot as plt

def plot_nucleotide_frequencies(seq_id, nucleotide_counts):
    labels = list(nucleotide_counts.keys())
    values = list(nucleotide_counts.values())

    plt.bar(labels, values)
    plt.xlabel('Nucleotides')
    plt.ylabel('Frequency')
    plt.title(f'Nucleotide Frequencies for {seq_id}')
    plt.show()

def plot_gc_content(gc_contents):
    labels = list(gc_contents.keys())
    values = list(gc_contents.values())

    plt.bar(labels, values)
    plt.xlabel('Sequence ID')
    plt.ylabel('GC Content (%)')
    plt.title('GC Content across Sequences')
    plt.xticks(rotation=45)  # Rotates the sequence IDs for better readability
    plt.show()


def count_nucleotides(dna_sequence):
    return {
        'A': dna_sequence.count('A'),
        'C': dna_sequence.count('C'),
        'G': dna_sequence.count('G'),
        'T': dna_sequence.count('T')
    }

def main():
    for seq_record in SeqIO.parse('domestic_cat/ncbi_dataset/data/GCF_018350175.1/GCF_018350175.1_F.catus_Fca126_mat1.0_genomic.fna', 'fasta'):
        nucleotide_counts = count_nucleotides(str(seq_record.seq))
        plot_nucleotide_frequencies(seq_record.id, nucleotide_counts)
        # Optional: Calculate and plot GC content
        # gc_content = calculate_gc_content(str(seq_record.seq))
        # plot_gc_content(seq_record.id, gc_content)

if __name__ == "__main__":
    main()
