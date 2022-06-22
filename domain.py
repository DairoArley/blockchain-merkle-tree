import hashlib


def updateWallets(wallets, walletSentModifiqued,  walletRecievedModifiqued):
    idWallets = map(lambda wallet: wallet.id, wallets)
    idSent = idWallets.index(walletSentModifiqued.id)
    idRecieved = idWallets.index(walletRecievedModifiqued.id)

    wallets.insert(idSent, walletSentModifiqued)
    wallets.insert(idRecieved, walletRecievedModifiqued)

    return wallets


class BlockChain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

        self.block = []
        self.wallets = []

    def generateGenesisBlock(self):
        self.chain.append(Block("first", ['Genesis Block']))

    def create_block_from_transaction(self, transactions):
        previousBlockHash = self.lastBlock.block_hash
        self.chain.append(Block(previousBlockHash, transactions))

    def showChain(self):
        for i in range(len(self.chain)):
            print(
                f"Data {i + 1}: {self.chain[i].block_data} \n Hash {i + 1}: {self.chain[i].block_hash}\n\n")

    def lastBlock(self):
        return self.chain[-1]

    def addWallet(wallet, self):
        idWallets = map(lambda wallet: wallet.id, self.wallets)
        if(wallet.id not in idWallets):
            self.wallets.append(wallet)
            print(f'Wallet added {wallet}')
        else:
            raise ValueError(f'Wallet exits in blockchain {wallet}')


class Block:
    def __init__(self, prevBlockHash, transactions):

        self.prevBlockHash = prevBlockHash
        self.transactions = transactions

        self.blockData = f"{'#'.join(transactions)} # {prevBlockHash}"
        self.blockHash = hashlib.sha256(self.block_data.encode()).hexdigest()

    def makeTransaction(walletSent, walletRecieved, cantidad, wallets):
        if(walletSent.id == walletRecieved.id):
            raise ValueError(f'The same Wallet {walletSent.id }')
        elif(walletSent.cantidad < cantidad):
            raise ValueError(
                f'Insufficient Money {walletSent.cantidad} < {cantidad}')
        else:
            idWallets = map(lambda wallet: wallet.id, wallets)
            if(walletSent.id not in idWallets):
                raise ValueError(f'Wallet is not register {walletSent.id }')
            elif(walletRecieved not in idWallets):
                raise ValueError(
                    f'Wallet is not register {walletRecieved.id }')
            else:
                walletSentModifiqued = {
                    "nombre": walletSent.nombre,
                    "id": walletSent.id,
                    "cantidad": walletSent.cantidad - cantidad
                }
                walletRecievedModifiqued = {
                    "nombre": walletRecieved.nombre,
                    "id": walletRecieved.id,
                    "cantidad": walletRecieved.cantidad + cantidad
                }
                transaction = f'{walletSent.nombre} le envia {cantidad} a {walletRecieved.nombre}'

                walletsModifiqueds = updateWallets(
                    wallets, walletSentModifiqued,  walletRecievedModifiqued)

                # modificar wallets originales
                return walletsModifiqueds, transaction

            print(f'The same Wallet {walletSent.id }')
        return transaction

    def transactionToHash(transaction):
        # hast de transaction
        return hashed

    def hashTwoHash(hash1, hash2):
        return hashed

    def makeProofOfWork(cantidyNumber, number):
        return nonce
