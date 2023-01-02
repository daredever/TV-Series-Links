def get_int(start: int, end: int, prompt: str) -> int:
    """
    Gets integer value from user input in range [start, end).
    """
    assert isinstance(start, int)
    assert isinstance(end, int)
    assert isinstance(prompt, str)
    
    while True:
        try:
            value = int(input(prompt))
            assert start <= value < end
            return value
        except ValueError:
            print('Value should be an integer')
        except AssertionError:
            print(f'Value should be an integer in range [{start}, {end})')
