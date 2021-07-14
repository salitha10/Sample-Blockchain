import hashlib

class block:
    def __init__(self,prev_block_hash, transaction_list):
        self.prev_block_hash = prev_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(self.transaction_list) + "-" + self.prev_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


def main():
    block1 = block("Initial_block", ["A2B20", "B2C50"])
    block2 = block(block1.block_hash, ["A2B80", "B2F200"])

    print(block1.block_hash)
    print(block2.block_hash)

# run main function 
if __name__ == "__main__":  
    main()
