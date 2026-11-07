
def S(cat, qen, qfi, een, efi, cands):
    """cat, question EN, question FI, explanation EN, explanation FI,
    cands = list of (en, fi, belongs)"""
    assert len(cands) == 10, (qen, len(cands))
    n = sum(1 for c in cands if c[2])
    assert 4 <= n <= 6, (qen, n)
    assert len(qen) <= 110 and len(qfi) <= 110, (qen, len(qen), len(qfi))
    assert qen != qfi and een != efi, qen
    out = []
    for en, fi, v in cands:
        assert en and fi, (qen, en, fi)
        out.append([en, fi, fi, 1 if v else 0])
    assert cat in ("Arts & culture", "Sport", "Everyday"), cat
    return [cat, qen, qfi, qfi, een, efi, efi, out]
