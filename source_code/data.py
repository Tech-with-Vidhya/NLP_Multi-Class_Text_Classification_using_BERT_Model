import torch


class TextDataset(torch.utils.data.Dataset):

    def __init__(self, tokens, labels):
        self.tokens = tokens
        self.labels = labels

    def __len__(self):
        return len(self.tokens)

    def __getitem__(self, idx):
        return self.labels[idx], self.tokens[idx]
