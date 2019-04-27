#!/usr/bin/env bash

. ../../../.env1/bin/activate

cp ../../datasets/generic2semantic/trees_txt/* ./data/

python utils/txt2jsonl.py --txt1 ./data/allformulas_generic_trees.txt --txt2 ./data/allformulas_semantic_trees.txt --out ./data/trees.jsonl

python utils/split_train_val.py --input ./data/trees.jsonl

python build_snli_vocab.py --data ./data/trees.jsonl --vocab-size 1100 --out ./data/vocab.p

#python dump_snli_reader.py --data ./data/trees.jsonl --vocab ./data/vocab.p --max-length 1000 --out ./data/trees.p
python dump_snli_reader.py --data ./data/trees.jsonl.train --vocab ./data/vocab.p --max-length 1000 --out ./data/trees.p.train
python dump_snli_reader.py --data ./data/trees.jsonl.val --vocab ./data/vocab.p --max-length 1000 --out ./data/trees.p.val

echo Start training...

python train_nli.py --word-dim 400 --hidden-dim 300 --tracking-dim 300 --clf-hidden-dim 300 --clf-num-layers 1 --train-data ./data/trees.p.train --valid-data ./data/trees.p.val --batch-size 4 --max-epoch 100 --trans-loss-weight .5 --save-dir ./data/checkpoint.model #--gpu


