class W3Exception(Exception):
    pass

class TransactionFailedException(W3Exception):
    pass

class ReplacementTransactionUnderpricedException(TransactionFailedException):
    pass

class InsufficientFundsException(TransactionFailedException):
    pass

class RPCException(W3Exception):
    pass
