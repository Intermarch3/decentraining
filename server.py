##
## EPITECH PROJECT, 2023
## hackathon_aleph
## File description:
## server.py
##

import flwr as fl
import subprocess

strategy = fl.server.strategy.FedAvg(
    min_available_clients=4
)

fl.server.start_server(
    server_address="0.0.0.0:8080",
    config=fl.server.ServerConfig(num_rounds=4),
    strategy=strategy,
)
