#!/usr/bin/env python3
"""Mira review-only Git-blob identity kernel and synthetic audit fixtures.

GEN/DERIVED software mathematics.  This does not approve, open, or extract any
real intake PDF and does not modify the production extractor or allowlist.

Git's SHA-1 object name for byte payload P is

    SHA1(b"blob " + ascii_decimal(len(P)) + b"\\0" + P).

The kernel couples that repository identity to an optional independent SHA-256
digest.  Byte count is checked separately so failure reports remain typed.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, getcontext
import hashlib
from typing import Iterable


@dataclass(frozen=True)
class Identity:
    size: int
    git_blob_sha1: str
    content_sha256: str


@dataclass(frozen=True)
class Verdict:
    accepted: bool
    reason: str
    observed: Identity


def git_blob_header(size: int) -> bytes:
    if size < 0:
        raise ValueError("size must be nonnegative")
    return b"blob " + str(size).encode("ascii") + b"\0"


def identity_bytes(payload: bytes) -> Identity:
    git_sha1 = hashlib.sha1(git_blob_header(len(payload)) + payload).hexdigest()
    sha256 = hashlib.sha256(payload).hexdigest()
    return Identity(len(payload), git_sha1, sha256)


def identity_chunks(chunks: Iterable[bytes], total_size: int) -> Identity:
    """Hash one pass over chunks while retaining Git's required size header."""
    if total_size < 0:
        raise ValueError("total_size must be nonnegative")
    git_sha1 = hashlib.sha1()
    git_sha1.update(git_blob_header(total_size))
    sha256 = hashlib.sha256()
    seen = 0
    for chunk in chunks:
        if not isinstance(chunk, bytes):
            raise TypeError("chunks must yield bytes")
        seen += len(chunk)
        if seen > total_size:
            raise ValueError("stream exceeds declared size")
        git_sha1.update(chunk)
        sha256.update(chunk)
    if seen != total_size:
        raise ValueError(f"stream size {seen} != declared size {total_size}")
    return Identity(seen, git_sha1.hexdigest(), sha256.hexdigest())


def verify(
    payload: bytes,
    expected_size: int,
    expected_git_blob_sha1: str,
    expected_content_sha256: str | None = None,
) -> Verdict:
    """Typed fail-closed comparison against pinned repository metadata."""
    observed = identity_bytes(payload)
    if observed.size != expected_size:
        return Verdict(False, "hold_size_mismatch", observed)
    if observed.git_blob_sha1 != expected_git_blob_sha1.lower():
        return Verdict(False, "hold_git_blob_identity_mismatch", observed)
    if (
        expected_content_sha256 is not None
        and observed.content_sha256 != expected_content_sha256.lower()
    ):
        return Verdict(False, "hold_sha256_identity_mismatch", observed)
    return Verdict(True, "review_identity_verified_not_content_approved", observed)


def collision_union_bound(n: int, bits: int) -> Decimal:
    """Rigorous birthday union bound: P(any collision) <= C(n,2)/2^bits.

    This is only an accidental-uniform-hash model.  It is not an adversarial
    security claim, especially for SHA-1.
    """
    if n < 0 or bits <= 0:
        raise ValueError("require n>=0 and bits>0")
    return Decimal(n * (n - 1)) / (Decimal(2) ** (bits + 1))


def chunked(payload: bytes, width: int) -> Iterable[bytes]:
    if width <= 0:
        raise ValueError("width must be positive")
    for start in range(0, len(payload), width):
        yield payload[start:start + width]


def main() -> None:
    getcontext().prec = 80

    original = b"ABCDEFGHIJ"
    same_size_mutation = b"abcdeFGHIJ"
    shorter_mutation = b"ABCDE"
    pinned = identity_bytes(original)

    print("pinned", pinned)
    assert pinned.git_blob_sha1 == "7074bbccf568292d27cc8fd52958804dd366ad48"

    fixtures = (
        ("original", original),
        ("same_size_mutation", same_size_mutation),
        ("shorter_mutation", shorter_mutation),
    )
    for name, payload in fixtures:
        size_only_accepts = len(payload) == pinned.size
        result = verify(
            payload,
            pinned.size,
            pinned.git_blob_sha1,
            pinned.content_sha256,
        )
        print(
            f"{name}: size_only_accepts={size_only_accepts} "
            f"accepted={result.accepted} reason={result.reason} "
            f"git_blob_sha1={result.observed.git_blob_sha1}"
        )

    # The decisive negative control: equal byte count passes the old size-only
    # predicate but fails repository object identity.
    assert len(same_size_mutation) == pinned.size
    assert not verify(
        same_size_mutation,
        pinned.size,
        pinned.git_blob_sha1,
        pinned.content_sha256,
    ).accepted

    # Raw SHA-1(P) is not Git SHA-1("blob <len>\\0" || P).  This catches a
    # common identity-format substitution.
    raw_sha1 = hashlib.sha1(original).hexdigest()
    raw_confusion = verify(original, pinned.size, raw_sha1)
    print(
        f"raw_sha1={raw_sha1} git_blob_sha1={pinned.git_blob_sha1} "
        f"raw_hash_as_git_expected={raw_confusion.reason}"
    )
    assert raw_sha1 != pinned.git_blob_sha1
    assert raw_confusion.reason == "hold_git_blob_identity_mismatch"

    # Standard empty Git blob fixture and one-pass chunking invariance.
    empty = identity_bytes(b"")
    print(f"empty_git_blob_sha1={empty.git_blob_sha1}")
    assert empty.git_blob_sha1 == "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"
    for width in (1, 3, 7, 65536):
        streamed = identity_chunks(chunked(original, width), len(original))
        print(f"chunk_width={width} identity_equal={streamed == pinned}")
        assert streamed == pinned

    # Declared-length controls reject both truncation and overrun.
    for bad_size in (len(original) - 1, len(original) + 1):
        try:
            identity_chunks(chunked(original, 3), bad_size)
        except ValueError as exc:
            print(f"declared_size={bad_size} rejected={exc}")
        else:
            raise AssertionError("bad declared size was accepted")

    # Mira's checkpoint records 245 distinct pending blob identities.  Under
    # the explicitly limited uniform-accidental model, report rigorous bounds.
    n = 245
    b160 = collision_union_bound(n, 160)
    b256 = collision_union_bound(n, 256)
    print(f"n={n} sha1_union_bound={b160:.12E}")
    print(f"n={n} sha256_union_bound={b256:.12E}")

    assert verify(
        original,
        pinned.size,
        pinned.git_blob_sha1,
        pinned.content_sha256,
    ).accepted
    print("checks: PASS")
    print("boundary: identity verified != citation cleared or content approved")


if __name__ == "__main__":
    main()
