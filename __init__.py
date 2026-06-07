"""
Compiler-based Distributed NFT System

A revolutionary paradigm shift from Database-centric to Compiler-based
distributed systems with P2P networking, NFT tokenization, and
Proof of Contribution.
"""

__version__ = "0.1.0-alpha"
__author__ = "Distributed System Contributors"

from compiler_nft.core.compiler import MatrixAuthenticatedCompiler
from compiler_nft.network.p2p import P2PCompilerNode
from compiler_nft.nft.tokenizer import NFTTokenAllocator
from compiler_nft.nft.unlocker import ServiceUnlocker

__all__ = [
    'MatrixAuthenticatedCompiler',
    'P2PCompilerNode',
    'NFTTokenAllocator',
    'ServiceUnlocker',
]
