##
## EPITECH PROJECT, 2023
## hackathon_aleph
## File description:
## server.py
##

import flwr as fl
import subprocess


fl.server.start_server(
    server_address="0.0.0.0:8080",
    config=fl.server.ServerConfig(num_rounds=1),
    strategy=fl.server.strategy.FedAvg(),
)

for i in range(10):
    subprocess.run(["./script/clientscript.sh"], shell=True)
