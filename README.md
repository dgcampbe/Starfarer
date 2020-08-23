#tp2p
Later this will be completely written in rust.
Currently, it is completely broken and not worth your time.
### Below are just random notes I made long ago. They are currently incomprehensible.
Blockchains are expendable.
Public key encryption is used to verify identities of people.
Token is passed to a key that was derived using hardened derivation.
Lockscript language is Turing complete.

Timelock - lock until Unix Epoch timestamp
In bitcoin a transaction cannot be distributed if it is timelocked.
This allows the possibility of double spending.
Instead maybe allow it to be added to the blockchain but its outputs can't be spent until it is unlocked
also maybe allow it so that only some outputs have this, so change can be spent immediately
maybe different ways to express time available instead of just Unix Epoch

extra field for the "payload" - what the block is supposed to record

token abilities:
revoke
expire
grant
access
