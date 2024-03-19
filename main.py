import matplotlib.pyplot as plt
from Bio import SeqIO

def count_reads_by_length(fastq_file):
    read_lengths = {}
    with open(fastq_file, "r") as handle:
        for record in SeqIO.parse(handle, "fastq"):
            length = len(record.seq)
            if length in read_lengths:
                read_lengths[length] += 1
            else:
                read_lengths[length] = 1
    return read_lengths

def plot_read_counts(read_lengths1, read_lengths2):
    plt.figure(figsize=(10, 6))
    plt.bar(read_lengths1.keys(), read_lengths1.values(), color='blue', alpha=0.7, label='File 1')
    plt.bar(read_lengths2.keys(), read_lengths2.values(), color='red', alpha=0.7, label='File 2')
    plt.xlabel('Length of Reads')
    plt.ylabel('Number of Reads')
    plt.title('Read Counts by Length')
    plt.legend()
    plt.show()

# Substitua 'file1.fastq' e 'file2.fastq' pelos caminhos dos seus arquivos FASTQ
file1 = 'file1.fastq'
file2 = 'file2.fastq'

# Contagem de leituras por comprimento para cada arquivo
read_lengths1 = count_reads_by_length(file1)
read_lengths2 = count_reads_by_length(file2)

# Plotagem e comparação dos resultados
plot_read_counts(read_lengths1, read_lengths2)