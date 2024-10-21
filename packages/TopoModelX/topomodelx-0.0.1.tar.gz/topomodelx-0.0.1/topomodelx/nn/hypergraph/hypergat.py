"""HyperGat Layer."""

import torch

from topomodelx.nn.hypergraph.hypergat_layer import HyperGATLayer


class HyperGAT(torch.nn.Module):
    """Neural network implementation of Template for hypergraph classification [1]_.

    Parameters
    ----------
    in_channels : int
        Dimension of the input features.
    hidden_channels : int
        Dimension of the hidden features.
    n_layers : int, default = 2
        Amount of message passing layers.
    layer_drop : float, default = 0.2
        Dropout rate for the hidden features.
    **kwargs : optional
        Additional arguments for the inner layers.

    References
    ----------
    .. [1] Ding, Wang, Li, Li and Huan Liu.
        EMNLP, 2020.
        https://aclanthology.org/2020.emnlp-main.399.pdf
    """

    def __init__(
        self,
        in_channels,
        hidden_channels,
        n_layers=2,
        layer_drop=0.2,
        **kwargs,
    ):
        super().__init__()

        self.layers = torch.nn.ModuleList(
            HyperGATLayer(
                in_channels=in_channels if i == 0 else hidden_channels,
                hidden_channels=hidden_channels,
                **kwargs,
            )
            for i in range(n_layers)
        )
        self.layer_drop = torch.nn.Dropout(layer_drop)

    def forward(self, x_0, incidence_1):
        """Forward computation through layers, then linear layer, then global max pooling.

        Parameters
        ----------
        x_0 : torch.Tensor, shape = (n_nodes, channels_nodes)
            Node features.
        incidence_1 : torch.Tensor, shape = (n_nodes, n_edges)
            Boundary matrix of rank 1.

        Returns
        -------
        x_0 : torch.Tensor
            Output node features.
        x_1 : torch.Tensor
            Output hyperedge features.
        """
        for layer in self.layers:
            x_0, x_1 = layer.forward(x_0, incidence_1)
            x_0 = self.layer_drop(x_0)

        return x_0, x_1
