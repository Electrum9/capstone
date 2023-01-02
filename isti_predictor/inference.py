import numpy as np
import os
import sys
import math
import argparse
import random
import glob
import json
from datetime import datetime
import torch
import torch.nn as nn
import torchvision
from torchvision import models
import torch.optim as optim
from tqdm import tqdm

from model.network import Merge_LSTM as net_model
from dataloader.dataloader import thermaldataset


def main():
    """ Performs inference using given model, on given input video.

    Example usage:

    $ python dataloader.py ../data/test_label ../data/mat_files ../data/sync_data 

    """
    label_name, ir_vid_name, sync_sig_name = sys.argv[1:]

    print(label_name, ir_vid_name)
    label    = "{}/".format(label_name)
    ir_video = "{}/".format(ir_vid_name)
    print(label, ir_video)

    train_dataset = thermaldataset(
            label    = "{}/".format(label_name), 
            ir_video = "{}/".format(ir_vid_name), 
            sync_sig = "{}/".format(sync_sig_name), 
            phase    = 'test' # NOTE: Change to correct name
    )
    
    frame_rate = 15; in_dim = frame_rate*2048; h_dim = frame_rate*30; num_l = 6
    print("Initializing Network")
    model  = net_model(in_dim, h_dim, num_l, frame_rate)

    model.eval()
    trainloader = torch.utils.data.DataLoader(train_dataset,batch_size=1,shuffle=True,num_workers=1)
    for data in trainloader:
        try:
                inputs = data['data'].cuda().float()
                labels = data['label']
        except:
                print("Data read error, corrupted data")
                continue
        print("Test input: ", inputs.shape, "label: ", labels.shape, iteration)
        b_size, num_frames, ch, h, w = inputs.shape


    #import pdb;pdb.set_trace()

if __name__=='__main__':
    main()
