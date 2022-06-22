from domain import BlockChain
from domain import Block

wallets = [
    {
        "nombre": "Dairo",
        "id": 100000000000,
        "cantidad": 100,
    },
    {
        "nombre": "Antonio",
        "id": 100000000001,
        "cantidad": 100,
    },
    {
        "nombre": "Juan",
        "id": 1000000000002,
        "cantidad": 100,
    },
    {
        "nombre": "Jose",
        "id": 100000000003,
        "cantidad": 100,
    },
    {
        "nombre": "Daniela",
        "id": 100000000004,
        "cantidad": 100,
    },
    {
        "nombre": "Pepito",
        "id": 100000000005,
        "cantidad": 100,
    }
]

t1 = "Daniela sends 15 coin to Pepito"
t2 = "Jose sends 20 coin to James"
t3 = "Juan sends 5 coin to Daniela"
t4 = "Juan sends 5 coin to Noah"


block1 = Block('genesis', [t1, t2])
