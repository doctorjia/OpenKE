import os
import pandas as pd
import numpy as np
import random
import shutil

entity_dict_file = '../benchmarks/WN18RR/entity2id.txt'
relation_dict_file = '../benchmarks/WN18RR/relation2id.txt'

entity_df = pd.read_table(entity_dict_file, header=None)
entity_dict = dict(zip(entity_df[0], entity_df[1]))
n_entity = len(entity_dict)
entities = list(entity_dict.values())
print(6186301 in entity_dict)
print('#entity: {}'.format(n_entity))
print('-----Loading relation dict-----')
relation_df = pd.read_table(relation_dict_file, header=None)
relation_dict = dict(zip(relation_df[0], relation_df[1]))
n_relation = len(relation_dict)

training_file = 'train.txt'
validation_file = 'valid.txt'
test_file = 'test.txt'
print('-----Loading training triples-----')
training_df = pd.read_table(training_file, header=None)
training_triples = list(zip([entity_dict[h] for h in training_df[0]],
                            [entity_dict[t] for t in training_df[1]],
                            [relation_dict[r] for r in training_df[2]]))
n_training_triple = len(training_triples)
np.savetxt("train2id.txt", training_triples,fmt='%d',delimiter=' ')
print('#training triple: {}'.format(n_training_triple))
print('-----Loading validation triples-----')
validation_df = pd.read_table(validation_file, header=None)
validation_triples = list(zip([entity_dict[h] for h in validation_df[0]],
                              [entity_dict[t] for t in validation_df[1]],
                              [relation_dict[r] for r in validation_df[2]]))
n_validation_triple = len(validation_triples)
np.savetxt("validation2id.txt", validation_triples,fmt='%d',delimiter=' ')
print('#validation triple: {}'.format(n_validation_triple))
print('-----Loading test triples------')
test_df = pd.read_table(test_file, header=None)
test_triples = list(zip([entity_dict[h] for h in test_df[0]],
                        [entity_dict[t] for t in test_df[1]],
                        [relation_dict[r] for r in test_df[2]]))
n_test_triple = len(test_triples)
np.savetxt("test2id.txt", test_triples,fmt='%d',delimiter=' ')

i = 0

entity_id = 40942
relation_id = 17

if os.path.exists("train_2.txt"):
    os.remove("train_2.txt")
shutil.copyfile("train.txt", "train_2.txt")

output_file = open("train_2.txt", "a")
entity_file = open("entity2id_add.txt", "a")

new_entities = [32786788,
                63833825,
                88613461,
                32911214,
                43333422]

while i < 5:
    generate_entity = new_entities[i]
    entity_id += 1
    entity_dict[generate_entity] = entity_id
    # entity_file.write(str(generate_entity) + "\t" + str(entity_id) + "\n")
    i += 1
    a = [260881, 260622, 1332730]
    for b in a:
        relation_temp = list(relation_dict.keys())[random.randint(0, 17):]
        output_file.write(str(generate_entity) + "\t" + str("%08d" % b) + "\t" + relation_temp[0] + "\n")
        training_df.append([generate_entity, b, relation_temp[0]])

output_file.close()


training_file = 'train_2.txt'
validation_file = 'valid.txt'
test_file = 'test.txt'
print('-----Loading training triples-----')
training_df = pd.read_table(training_file, header=None)
training_triples_2 = list(zip([entity_dict[h] for h in training_df[0]],
                            [entity_dict[t] for t in training_df[1]],
                            [relation_dict[r] for r in training_df[2]]))
np.savetxt("train2id_add.txt", training_triples_2,fmt='%d',delimiter=' ')
n_training_triple = len(training_triples)
print('#training triple: {}'.format(n_training_triple))
print('-----Loading validation triples-----')
validation_df = pd.read_table(validation_file, header=None)
validation_triples = list(zip([entity_dict[h] for h in validation_df[0]],
                              [entity_dict[t] for t in validation_df[1]],
                              [relation_dict[r] for r in validation_df[2]]))
n_validation_triple = len(validation_triples)
print('#validation triple: {}'.format(n_validation_triple))
print('-----Loading test triples------')
test_df = pd.read_table(test_file, header=None)
test_triples = list(zip([entity_dict[h] for h in test_df[0]],
                        [entity_dict[t] for t in test_df[1]],
                        [relation_dict[r] for r in test_df[2]]))
n_test_triple = len(test_triples)