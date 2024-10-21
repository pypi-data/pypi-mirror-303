import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch import autograd
import numpy as np
from torch.utils.data import DataLoader


class EWC1:

    def __init__(self, model, crit, lr=0.001, weight=1000000, device="cuda"):
        self.model = model
        self.weight = weight
        self.crit = crit
        self.optimizer = optim.Adam(self.model.parameters(), lr)
        self.device = device

    def _update_mean_params(self):
        for param_name, param in self.model.named_parameters():
            _buff_param_name = param_name.replace('.', '__')
            self.model.register_buffer(_buff_param_name+'_estimated_mean', param.data.clone())

    def _update_fisher_params(self, current_ds, batch_size, num_batch):
        dl = DataLoader(current_ds, batch_size, shuffle=True)
        log_likelihood = torch.FloatTensor([0.]).to(self.device)
        for i, (x, labels, attack_labels, edge_index) in enumerate(dl):
            x, labels, edge_index = [item.float().to(self.device) for item in [x, labels, edge_index]]
            if i > num_batch:
                break
            log_likelihood += F.mse_loss(self.model(x, edge_index), labels, reduction="mean")
        grad_log_likelihood = autograd.grad(log_likelihood, self.model.parameters())
        _buff_param_names = [param[0].replace('.', '__') for param in self.model.named_parameters()]
        for _buff_param_name, param in zip(_buff_param_names, grad_log_likelihood):
            self.model.register_buffer(_buff_param_name+'_estimated_fisher', param.data.clone() ** 2)

    def register_ewc_params(self, dataset, batch_size, num_batches):
        self._update_fisher_params(dataset, batch_size, num_batches)
        self._update_mean_params()

    def _compute_consolidation_loss(self, weight):
        try:
            losses = []
            for param_name, param in self.model.named_parameters():
                _buff_param_name = param_name.replace('.', '__')
                estimated_mean = getattr(self.model, '{}_estimated_mean'.format(_buff_param_name))
                estimated_fisher = getattr(self.model, '{}_estimated_fisher'.format(_buff_param_name))
                losses.append((estimated_fisher * (param - estimated_mean) ** 2).sum())
            return (weight / 2) * sum(losses)
        except AttributeError:
            return 0

    def forward_backward_update(self, input, target, edge_index):
        output = self.model(input, edge_index)
        loss = self._compute_consolidation_loss(self.weight) + self.crit(output, target)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        return loss

    def save(self, filename):
        torch.save(self.model.state_dict(), filename)

    def load(self, filename):
        self.model = torch.load(filename)
