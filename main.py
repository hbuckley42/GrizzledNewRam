import random
import copy

def draw_allele():
    """Randomly sample the genepool"""

    # Initialize pick variables
    first_pick = ''
    second_pick = ''
    draw_number = 1

    # sort allele picks into genotypes and phenotypes,
    # and record allele sample for next generation
    while draw_number < 11:
        # Draw random alleles from the gene pool
        first_pick = gene_pool[random.randint(0, 19)]
        second_pick = gene_pool[random.randint(0, 19)]
        # Sort the alleles and record the picks
        if first_pick == 'r' and second_pick == 'r':
            geno_pheno['rr'] += 1
            gene_sample.append('r')
            gene_sample.append('r')
            geno_pheno['red'] += 1
        elif first_pick == 'w' and second_pick == 'w':
            geno_pheno['ww'] += 1
            gene_sample.append('w')
            gene_sample.append('w')
            geno_pheno['white'] += 1
        elif first_pick == 'b' and second_pick == 'b':
            geno_pheno['bb'] += 1
            gene_sample.append('b')
            gene_sample.append('b')
            geno_pheno['blue'] += 1
        elif first_pick + second_pick == 'rw' or first_pick + second_pick == 'wr':
            geno_pheno['rw'] += 1
            gene_sample.append('r')
            gene_sample.append('w')
            geno_pheno['red'] += 1
        elif first_pick + second_pick == 'rb' or first_pick + second_pick == 'br':
            geno_pheno['rb'] += 1
            gene_sample.append('r')
            gene_sample.append('b')
            geno_pheno['purple'] += 1
        elif first_pick + second_pick == 'wb' or first_pick + second_pick == 'bw':
            geno_pheno['wb'] += 1
            gene_sample.append('w')
            gene_sample.append('b')
            geno_pheno['blue'] += 1
        draw_number += 1


# Create the gene pool, phenotype dictionary, and a sample list to hold picks
gene_pool = ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
gene_sample = []
geno_pheno = {'rr': 0, 'ww': 0, 'rw': 0, 'rb': 0, 'wb': 0, 'bb': 0, 'red': 0, 'white': 0, 'blue': 0, 'purple': 0}
GENO_PHENO_RESET = {'rr': 0, 'ww': 0, 'rw': 0, 'rb': 0, 'wb': 0, 'bb': 0, 'red': 0, 'white': 0, 'blue': 0,
                        'purple': 0}
num_generations = 1
count_gen = 1

print('*************************************************************')
print('*                                                           *')
print('*                 GENETIC DRIFT SIMULATION                  *')
print('*                                                           *')
print('*************************************************************')
print('This exercise is designed to simulate the effects of genetic drift on a small population.')
print('This simulation will "create" 10 individuals from a gene pool of 20 alleles by randomly selecting')
print('alleles to be passed on to the next generation. Each selection represents the genotype of a fish.')
print('Refer to the exercise handout for additional information and instructions.')



# Ask the user how many generations to simulate
try:
    num_generations = int(input('How many generations would you like to simulate?: '))
except ValueError:
    print('Invalid input. Please enter an integer: ')
    num_generations = int(input('How many generations would you like to simulate?: '))

# Ask the user for a file name to record the output
try:
    file_name = input('Enter a file name for the output file: ')
except ValueError:
    print('Invalid input. Please enter a file name: ')
    file_name = input('Enter a file name for the output file: ')

# Write starting information to file
with open(file_name + '.txt', 'w') as file_object:
    file_object.write('GENETIC DRIFT EXERCISE DATA\n\n')
    file_object.write(f'Initial Alleles in the Gene Pool:\n')
    file_object.write(f'White alleles: {gene_pool.count("w")}\n')
    file_object.write(f'Red alleles: {gene_pool.count("r")}\n')
    file_object.write('********************\n\n')

# Run the function to pick alleles, write results, and
# reset variables for additional generations
while num_generations > 0:
    draw_allele()
    gene_sample.sort()
    gene_pool = copy.deepcopy(gene_sample)
    with open(file_name + '.txt', 'a') as file_object:
        file_object.write(f'Gene pool after generation {count_gen}:\n')
        file_object.write(f'White alleles: {gene_pool.count("w")}\n')
        file_object.write(f'Red alleles: {gene_pool.count("r")}\n\n')

        file_object.write(f'Genotypes and phenotypes (gen {count_gen}):\n')
        file_object.write(f'rr: {geno_pheno["rr"]}\n')
        file_object.write(f'ww: {geno_pheno["ww"]}\n')
        file_object.write(f'rw: {geno_pheno["rw"]}\n')
        file_object.write(f'White phenotype: {geno_pheno["white"]}\n')
        file_object.write(f'Red phenotype: {geno_pheno["red"]}\n\n')
        file_object.write('********************\n')

    # Update variables
    gene_sample = []
    geno_pheno = copy.deepcopy(GENO_PHENO_RESET)
    num_generations -= 1
    count_gen += 1

print('Simulation complete. Refer to the output file for results.\n')

print(geno_pheno)
print(gene_pool)
print(gene_sample)

mut_choice = input('Would you like to run the simulation again with the blue allele mutation?(y/n): ')

while mut_choice != 'y' and mut_choice != 'n':
    print('Invalid input. Please enter a y or n: ')
    mut_choice = input('Enter a file name for the output file: ')

if mut_choice == 'y':
    try:
        print('Enter a file name for the second output file...')
        file_name = input('CAUTION: Use a different file name or your previous output will be overwritten!: ')
    except ValueError:
        print('Invalid input. Please enter a file name: ')
        file_name = input('Enter a file name for the new output file: ')
else:
    end = input('Press enter key to quit.')

try:
    num_generations = int(input('How many generations would you like to simulate?: '))
except ValueError:
    print('Invalid input. Please enter an integer: ')
    num_generations = int(input('How many generations would you like to simulate?: '))

# Reset gene_pool and count_gen to original states, swapping a blue allele for a red allele (mutation)
# geno_pheno has already been reset after all generations have run (line 123), and gene_sample already emptied
gene_pool = ['b', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
count_gen = 1

# Write starting information to file
with open(file_name + '.txt', 'w') as file_object:
    file_object.write('GENETIC DRIFT EXERCISE DATA - BLUE MUTATION\n\n')
    file_object.write(f'Initial Alleles in the Gene Pool:\n')
    file_object.write(f'White alleles: {gene_pool.count("w")}\n')
    file_object.write(f'Red alleles: {gene_pool.count("r")}\n')
    file_object.write(f'Blue alleles: {gene_pool.count("b")}\n')
    file_object.write('********************\n\n')

# Run the function to pick alleles, write results, and
# reset variables for additional generations
while num_generations > 0:
    draw_allele()
    gene_pool = copy.deepcopy(gene_sample)
    #count_gen = 1
    with open(file_name + '.txt', 'a') as file_object:
        file_object.write(f'Gene pool after generation {count_gen}:\n')
        file_object.write(f'White alleles: {gene_pool.count("w")}\n')
        file_object.write(f'Red alleles: {gene_pool.count("r")}\n')
        file_object.write(f'Blue alleles: {gene_pool.count("b")}\n\n')

        file_object.write(f'Genotypes and phenotypes (gen {count_gen}):\n')
        file_object.write(f'rr: {geno_pheno["rr"]}\n')
        file_object.write(f'ww: {geno_pheno["ww"]}\n')
        file_object.write(f'rw: {geno_pheno["rw"]}\n')
        file_object.write(f'rb: {geno_pheno["rb"]}\n')
        file_object.write(f'wb: {geno_pheno["wb"]}\n')
        file_object.write(f'bb: {geno_pheno["bb"]}\n')
        file_object.write(f'White phenotype: {geno_pheno["white"]}\n')
        file_object.write(f'Red phenotype: {geno_pheno["red"]}\n')
        file_object.write(f'Blue phenotype: {geno_pheno["blue"]}\n')
        file_object.write(f'Purple phenotype: {geno_pheno["purple"]}\n')
        file_object.write('********************\n')

    # Update variables for next run through draw_allele
    gene_sample = []
    geno_pheno = copy.deepcopy(GENO_PHENO_RESET)
    num_generations -= 1
    count_gen += 1

print('Simulation complete. Refer to the output file for results.\n\n')
end = input('Press enter key to quit.')