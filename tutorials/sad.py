import h5py
import os
import subprocess
import tensorflow as tf

if not os.path.isfile('data/hg19.ml.fa'):
    subprocess.call('curl -o data/hg19.ml.fa https://storage.googleapis.com/basenji_tutorial_data/hg19.ml.fa', shell=True)
    subprocess.call('curl -o data/hg19.ml.fa.fai https://storage.googleapis.com/basenji_tutorial_data/hg19.ml.fa.fai', shell=True)

if not os.path.isdir('models/lcl'):
    os.mkdir('models/lcl')
if not os.path.isfile('models/lcl/model_human.tf.meta'):
    subprocess.call('curl -o models/lcl/model_human.tf.index https://storage.googleapis.com/basenji_barnyard/tf1/model_human.tf.index', shell=True)
    subprocess.call('curl -o models/lcl/model_human.tf.meta https://storage.googleapis.com/basenji_barnyard/tf1/model_human.tf.meta', shell=True)
    subprocess.call('curl -o models/lcl/model_human.tf.data-00000-of-00001 https://storage.googleapis.com/basenji_barnyard/tf1/model_human.tf.data-00000-of-00001', shell=True)


lines = [['index','identifier','file','clip','sum_stat','description']]
lines.append(['0', 'ENCFF093VXI', 'data/ENCFF093VXI.w5', '32', 'sum', 'DNASE:GM12878'])

samples_out = open('data/lcl_wigs.txt', 'w')
for line in lines:
    samples_out.write('\t'.join(line))
samples_out.close()

