import os
import pandas as pd
import numpy as np
import random
import shutil

# default_repo = '/export/data/zjiaad/OpenKE/benchmarks/WN18RR/'
default_repo = '../../benchmarks/WN18RR/'
out_repo = '../../benchmarks/WN18RR_1/'

entity_dict_file = default_repo + 'entity2id.txt'
relation_dict_file = default_repo + 'relation2id.txt'

entity_df = pd.read_csv(entity_dict_file, header=0, sep='\t')
entity_df.columns = ["A","B"]
entity_dict = dict(zip(entity_df["A"], entity_df["B"]))
n_entity = len(entity_dict)
entities = list(entity_dict.values())
#print(6186301 in entity_dict)
print('#entity: {}'.format(n_entity))
print('-----Loading relation dict-----')
relation_df = pd.read_csv(relation_dict_file, header=0, sep='\t')
relation_df.columns = ["A", "B"]
relation_dict = dict(zip(relation_df["A"], relation_df["B"]))
n_relation = len(relation_dict)

training_file = default_repo + 'train.txt'
validation_file = default_repo + 'valid.txt'
test_file = default_repo + 'test.txt'
print('-----Loading training triples-----')
training_df = pd.read_table(training_file, header=None)
training_triples = list(zip([entity_dict[h] for h in training_df[0]],
                            [entity_dict[t] for t in training_df[1]],
                            [relation_dict[r] for r in training_df[2]]))
n_training_triple = len(training_triples)
with open(default_repo + "train2id.txt", "w") as f:
    f.write(str(n_training_triple)+'\n')
f.close()
with open(default_repo + "train2id.txt", "ab") as f:
    np.savetxt(f, training_triples, fmt='%d', delimiter=' ')
f.close()
print('#training triple: {}'.format(n_training_triple))

print('-----Loading validation triples-----')
validation_df = pd.read_table(validation_file, header=None)
validation_triples = list(zip([entity_dict[h] for h in validation_df[0]],
                              [entity_dict[t] for t in validation_df[1]],
                              [relation_dict[r] for r in validation_df[2]]))
n_validation_triple = len(validation_triples)
with open(default_repo + "valid2id.txt", "w") as f:
    f.write(str(n_validation_triple)+'\n')
f.close()
with open(default_repo + "valid2id.txt", "ab") as f:
    np.savetxt(f, validation_triples, fmt='%d', delimiter=' ')
f.close()
shutil.copyfile(default_repo + "valid2id.txt", out_repo + "valid2id.txt")
print('#validation triple: {}'.format(n_validation_triple))

print('-----Loading test triples------')
test_df = pd.read_table(test_file, header=None)
test_triples = list(zip([entity_dict[h] for h in test_df[0]],
                        [entity_dict[t] for t in test_df[1]],
                        [relation_dict[r] for r in test_df[2]]))
n_test_triple = len(test_triples)
with open(default_repo + "test2id.txt", "w") as f:
    f.write(str(n_test_triple)+'\n')
f.close()
with open(default_repo + "test2id.txt", "ab") as f:
    np.savetxt(f, test_triples, fmt='%d', delimiter=' ')
f.close()
shutil.copyfile(default_repo + "test2id.txt", out_repo + "test2id.txt")

i = 0

entity_id = 40942
relation_id = 17

if os.path.exists(out_repo + "train.txt"):
    os.remove(out_repo + "train.txt")
# shutil.copyfile(default_repo + "train.txt", out_repo + "train.txt")
with open(default_repo+"train.txt", "r") as f1:
    lines_default = f1.readlines()
lines_default[0] = lines_default[0].replace(lines_default[0], "141455\n")
with open(out_repo+"train.txt", "w") as f2:
    for line in lines_default:
        f2.write(line)
f1.close()
f2.close()

if os.path.exists(out_repo + "entity2id.txt"):
    os.remove(out_repo + "entity2id.txt")
# shutil.copyfile(default_repo + "entity2id.txt", out_repo + "entity2id.txt")
with open(default_repo+"entity2id.txt", "r") as f1:
    lines_default = f1.readlines()
lines_default[0] = lines_default[0].replace(lines_default[0], "40948\n")
with open(out_repo+"entity2id.txt", "w") as f2:
    for line in lines_default:
        f2.write(line)
f1.close()
f2.close()

output_file = open(out_repo + "train.txt", "a")
entity_file = open(out_repo + "entity2id.txt", "a")

new_entities = [32786788,
                63833825,
                88613461,
                32911214,
                43333422]

while i < 5:
    generate_entity = new_entities[i]
    entity_id += 1
    entity_dict[generate_entity] = entity_id
    entity_file.write(str(generate_entity) + "\t" + str(entity_id) + "\n")
    i += 1
    a = [260881, 260622, 1332730]
    for b in a:
        relation_temp = list(relation_dict.keys())[random.randint(0, 17):]
        output_file.write(str(generate_entity) + "\t" + str("%08d" % b) + "\t" + relation_temp[0] + "\n")
        training_df.append([generate_entity, b, relation_temp[0]])

output_file.close()

training_file = open(out_repo + 'train.txt', 'r')
print('-----Loading training triples-----')
tot = (int)(training_file.readline())
training_df = pd.read_csv(training_file, header=0, sep='\t')
training_df.columns = ["A","B","C"]
training_triples_2 = list(zip([entity_dict[h] for h in training_df["A"]],
                              [entity_dict[t] for t in training_df["B"]],
                              [relation_dict[r] for r in training_df["C"]]))
n_training_new = len(training_triples_2)
with open(out_repo + "train2id.txt", "w") as f:
    f.write(str(n_training_new)+'\n')
f.close()
with open(out_repo + "train2id.txt", "ab") as f:
    np.savetxt(f, training_triples_2, fmt='%d', delimiter=' ')
f.close()
print('#training triple: {}'.format(n_training_new))
