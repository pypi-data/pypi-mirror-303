from jupygcc.utils import handle_metadata


def test_handle_metadata():
    metadata_dict, code = handle_metadata(
        """//| stdin: 10
int n;
printf("Combien de lignes? ")
scanf("%d", &n);
printf("%d lignes", n);
"""
    )

    assert metadata_dict.get("stdin") == "10"

    assert (
        code
        == """int n;
printf("Combien de lignes? ")
scanf("%d", &n);
printf("%d lignes", n);
"""
    )
