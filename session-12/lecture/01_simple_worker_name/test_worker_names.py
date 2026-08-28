from worker_names import get_formatted_worker_name                          # <1>

def test_simple_worker_name():                                              # <2> 
    """
    Test that simple worker names (first and last) are formatted correctly.
    Example: Clara Barton
    """
    formatted_name = get_formatted_worker_name('clara', 'barton')          # <3>
    assert formatted_name == 'Clara Barton' 