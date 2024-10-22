import subprocess

__all__ = [
    "KeyPair",
]


class KeyPair:
    _pubkey: str
    _private_key: str

    def __init__(self, private_key: str | None = None, *, pubkey: str | None = None) -> None:
        if private_key is not None and pubkey is not None:
            self._pubkey = pubkey
            self._private_key = private_key
        elif private_key is not None and pubkey is None:
            self._private_key = private_key
            self._pubkey = self._generate_pubkey(self._private_key)
        elif private_key is None and pubkey is None:
            self._pubkey, self._private_key = self._generate_key_pair()
        else:
            raise ValueError("Invalid arguments")

    def _generate_key_pair(self) -> tuple[str, str]:
        private_key = (subprocess
                       .run(["wg", "genkey"], capture_output=True, text=True)
                       .stdout
                       .replace("\n", "")
                       )
        public_key = self._generate_pubkey(private_key)
        return public_key, private_key

    @staticmethod
    def _generate_pubkey(private_key: str) -> str:
        return (subprocess
                .run(["wg", "pubkey"], capture_output=True, text=True, input=private_key)
                .stdout
                .replace("\n", "")
                )

    @property
    def pubkey(self) -> str:
        return self._pubkey

    @property
    def private_key(self) -> str:
        return self._private_key

    def __str__(self) -> str:
        return f'KeyPair(pubkey="{self._pubkey}", private_key="{self._private_key}")'
