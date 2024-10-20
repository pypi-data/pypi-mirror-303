from typing import Text, Dict

from ipakyuli.exception import TransactionFailed
from ipakyuli.integration import BankIntegration


class BankTransaction(BankIntegration):
    """
    Transaction with Ipak Yo'li Bank
    """

    def __init__(
            self, card_data: Dict, **kwargs
    ) -> None:
        super().__init__(**kwargs)
        self.card_data = card_data
        self.transfer_id: Text = ""

    async def transfer_create(self, amount: float, order_id: Text, desc: Text):
        data = {
            "jsonrpc": "2.0",
            "method": "transfer.create",
            "params": {
                "card": self.card_data,
                "details": {
                    "description": desc},
                "order_id": order_id,
                "amount": amount,
            },
        }
        response = self.post(url="/transfer", data=data).json()

        if response.get("result", {}).get("text") == "Transfer created":
            self.transfer_id = response.get("result", {}).get("transfer_id")
        else:
            raise TransactionFailed()

    async def transfer_confirm(self, code: Text):
        data = {
            "jsonrpc": "2.0",
            "method": "transfer.confirm",
            "params": {
                "transfer_id": self.transfer_id,
                "code": code,
            },
        }
        response = self.post(url="/transfer", data=data).json()
        if not response.get("result", {}).get("text") == "Transfer approved":
            raise TransactionFailed()

    async def transfer_cancel(self):
        data = {
            "jsonrpc": "2.0",
            "method": "transfer.cancel",
            "params": {
                "transfer_id": self.transfer_id
            },
        }
        self.post(url="/transfer", data=data)
