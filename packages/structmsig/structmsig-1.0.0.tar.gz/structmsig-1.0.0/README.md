# Structured Multi-Signature (StructMSIG)
Structured multi-signature (**StructMSIG**) is a signature protocol that can represent the ***signing structure*** of multiple signers who can only sign the ***specified scope of data***.

## Why StructMSIG?
Firstly, **StructMSIG** can maintain the ***signing structure*** (*i.e.* the way how multiple parties signing data). 

For example, data is generated/signed by Alice, then checked/signed by Bob, and finally published/signed by Charlie. How can a verifier verify this data with understanding the above signing structure?

In this scenario, **StructMSIG** can generate a signature with the signing structure. Thus, a verifier can understand the signing structure while verifying the signature. 

Secondly, a signer can only sign portion of data with **StructMSIG**.

For example, if Bob only checked a portion of data, he can only sign the portion of data by specifying scope. 

## Support Signing Structures
Currently, **StructMSIG** supports the following signing structures.

1. **Nodal Structure**: a signing structrue where only one signer signs data.
2. **Sequential Structure**: a signing structure where multiple signers sign data in a sequential flow.

## Data Model
### Structured Data
In **StructMSIG**, data is modeled as structured data (```StructData```) as
```
{
    "items": [DataItem, ...]
}
```
where ```DataItem``` is modeled as
```
{
    "key": name of data item (str),
    "value": base64-encoded content of data item (str)
}
```

For example,
```json
{
    "items": [
        {
            "key": "hello",
            "value": "aGVsbG8="
        },
        {
            "key": "world",
            "value": "d29ybGQ="
        }
    ]
}
```

### Nodal Signature
The nodal signature (```NodalSig```) is the signature of nodal signing structure and modeled as
```
{
    "signer": name of signer (str),
    "signature": hex signature (str),
    "scope": [key of DataItem, ...] (list[str])
}
```
For example,
```json
{
    "signer": "Signer1",
    "signature": "...",
    "scope": ["hello"]
}
```

### Sequential Signature
The sequential signature (```SeqSig```) is the signature of sequential signing structure and modeled as
```
{
    "signatures":[NodalSig, ...] (list[NodalSig])
}
```
For example,
```json
{
    "signatures": [
        {
            "signer": "Signer1",
            "signature": "...",
            "scope": ["hello"]
        },
        {
            "signer": "Signer2",
            "signature": "...",
            "scope": ["world"]
        }
    ]
}
```

## Usages
### Utilities

**StructMSIG** provides several utilities to help develpoers handling interfaces to files.

#### Create Structured Data

Developers can easily create structred data from texts and files with ```create_struct_data()``` as

```python
from structmsig.utils import create_struct_data

# Create structured data from texts and files
data = create_struct_data(
    texts = {'text1':'hello','text2':'world'},
    files = {'file1':'./text.txt','file2':'./binary.bin'}
)
```

#### Open Nodal and Sequential Signature

Developers can open file-based nodal and sequential signatures with ```open_nodalsig()``` and ```open_seqsig()``` as

```python
from structmsig.utils import open_nodalsig, open_seqsig

# Create nodal signature from file
nodal_sig = open_nodalsig('./signer.nodalsig')

# Create sequential signature from file
seq_sig = open_seqsig('./signer.seqsig')
```

### Nodal Signing Structure
**Step 1.** Import modules
```python
from structmsig.data_model import NodalSig
from structmsig.nodal_struct import sign, verify
from structmsig.utilis import create_struct_data, open_nodalsig
```
**Step 2.** Prepare StructData

Here is the utility to create ```StructData```.
```python
data = create_struct_data(
    texts = {'text1':'hello', 'text2':'world'},
    files = {'file1':'file.txt','file2':'file.bin'}
)
```
**Step 3.** Sign StructData

Signer can sign data by giving name, structured data, private key, scope (***optional, defaults to all***) and flag to output signaure files (***optional, defaults to False***). 
```python
nodal_sig = sign('signer', data, 'signer-priv.pem', scope=['text1','file2'], out=True)
```
Then, signer can send data and nodal signature file (```signer.nodalsig```) to verifier.

**Step 4.** Verify Nodal Signature

Verifier can create ```StructData``` as in Step 2 and open nodal signature file (```signer.nodalsig```) with the utility

```python
nodal_sig = open_nodalsig('signer.nodalsig')
```

Then, verifier can verify nodal signature by giving structured data, nodal signature, and certificate of signer.

```python
result = verify(data, nodal_sig, 'signer-cert.pem')
```

## Sequential Signing Structure
**Step 1.** Import modules
```python
from structmsig.data_model import SeqSig
from structmsig.sequential_structure import sign, verify
from structmsig.utilis import create_struct_data, open_segsig
```
**Step 2.** Prepare StructData

Here is the utility to create ```StructData```.
```python
data = create_struct_data(
    texts = {'text1':'hello', 'text2':'world'},
    files = {'file1':'file.txt','file2':'file.bin'}
)
```
**Step 3.** Sign StructData

Signer 1 can sign data by giving name, structured data, private key, scope (***optional, defaults to all***) and flag to output signaure files (***optional, defaults to False***). 
```python
seq_sig_1 = sign('signer1', data, 'signer1-priv.pem', scope=['text1','file2'], out=True)
```
Then, signer 1 can send data and sequential signature (```singer1.seqsig```) to signer 2.

Signer 2 can create ```StructData``` as in Step 2 and open sequential signature (```signer1.seqsig```) with the utility
```python
seq_sig_1 = open_seqsig('signer1.seqsig')
```

Signer 2 then can sign by giving name, structured data, private key, scope (***optional, defaults to all***), sequential signature of signer 1, and flag to output signaure files (***optional, defaults to False***). 
```python
seq_sigs = sequential_sign('signer2', data, 'signer2-priv.pem', seq_sig=seq_sig_1, scope=['text1','file2'], out=True)
```

Finally, signer 2 can send data and sequential signature file (```signer2.seqsig```) to verifier.

**Step 4.** Verify Sequential Signature

Verifier can create ```StructData``` as in Step 2 and open sequential signature file (```signer2.seqsig```) with the utility

```python
seq_sig = open_seqsig('signer2.seqsig')
```

Then, verifier can verify sequential signature by giving structured data, sequential signature of signer 2, and certificates of signer 1 and signer 2.
```
result = verify(data, seq_sig, ['signer1-cert.pem','signer2-cert.pem'])
```
