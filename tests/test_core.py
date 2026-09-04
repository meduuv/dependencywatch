from dependencywatch import diff


def test_diff():
    assert diff(["a==1", "b"], ["a==2", "c"]) == {
        "added": ["c"], "removed": ["b"], "changed": ["a"]
    }
