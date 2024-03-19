from random import choice, randint
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

# Função para gerar uma sequência de DNA aleatória com um comprimento específico
def generate_random_sequence(length):
    bases = 'ATGC'
    return ''.join(choice(bases) for _ in range(length))

# Função para gerar pontuações de qualidade fictícias
def generate_quality_scores(length):
    return [choice(range(40, 70)) for _ in range(length)]  # Pontuações aleatórias entre 40 e 70

# Definindo os comprimentos das leituras para cada arquivo
read_lengths_file1 = [randint(50, 100) for _ in range(100)]  # 100 leituras de comprimento aleatório entre 50 e 100
read_lengths_file2 = [randint(50, 100) for _ in range(150)]  # 150 leituras de comprimento aleatório entre 50 e 100

# Gerando as sequências de DNA e pontuações de qualidade para cada arquivo
sequences_file1 = [SeqRecord(Seq(generate_random_sequence(length)), id=f'read{i}', description='',
                             letter_annotations={'phred_quality': generate_quality_scores(length)}) for i, length in enumerate(read_lengths_file1, start=1)]
sequences_file2 = [SeqRecord(Seq(generate_random_sequence(length)), id=f'read{i}', description='',
                             letter_annotations={'phred_quality': generate_quality_scores(length)}) for i, length in enumerate(read_lengths_file2, start=1)]

# Escrevendo os arquivos FASTQ
with open('file1.fastq', 'w') as handle:
    SeqIO.write(sequences_file1, handle, 'fastq')

with open('file2.fastq', 'w') as handle:
    SeqIO.write(sequences_file2, handle, 'fastq')
