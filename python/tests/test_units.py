from yt_videos_list.program import normalize_whitespace


def main():
    test_normalize_whitespace()

def test_normalize_whitespace():
    test_cases =     test_cases = (
        ('This is a title with no newlines', 'This is a title with no newlines'),
        ('This is a title with one newline \n', 'This is a title with one newline'),
        ('This is a title with two newlines \n\n', 'This is a title with two newlines'),
        ('This is a title with two\n\nnewlines', 'This is a title with two newlines'),
        ('This is a title with\n\ntwo newlines', 'This is a title with two newlines'),
        ('This is a title with one newline \n and one carriage return\r', 'This is a title with one newline and one carriage return'),
        ('This is a title with one newline \n and \rone carriage return', 'This is a title with one newline and one carriage return'),
        ('This is a title with one newline \n\r and one carriage return', 'This is a title with one newline and one carriage return'),
        ('This is a title with one newline \r\n and one carriage return', 'This is a title with one newline and one carriage return'),
        ('This is a title with one newline \r \n and one carriage return', 'This is a title with one newline and one carriage return'),
        ('This is a title with one newline \r \n and one carriage return', 'This is a title with one newline and one carriage return'),
        ('This is a title with multiple newlines \r \n and multiple carriage returns \r\r', 'This is a title with multiple newlines and multiple carriage returns'),
        ('This is a title with multiple newlines \r \n and multiple carriage returns \n\n', 'This is a title with multiple newlines and multiple carriage returns'),
        ('This is a title with multiple newlines \r \n and multiple carriage returns \r\n', 'This is a title with multiple newlines and multiple carriage returns'),
        ('This is a title with multiple newlines \r\n and multiple carriage returns \r\n', 'This is a title with multiple newlines and multiple carriage returns'),
        ('This is a title with multiple newlines \n\r and multiple carriage returns \r\n', 'This is a title with multiple newlines and multiple carriage returns'),
        ('This is a title with one newline \n but a sneaky carriage\rreturn', 'This is a title with one newline but a sneaky carriage return'),
    )
    error_message = '''
    Test case {index} is not properly formatted!
    The raw_text provided was: {raw_text}
    The expected normalized_text is: {normalized_text}
    The actual normalized_text output is: {actual_output_text}
    '''
    for index, (raw_text, normalized_text) in enumerate(test_cases):
        actual_output_text = normalize_whitespace(raw_text)
        if actual_output_text != normalized_text:
            raise ValueError(error_message.format(index=index, raw_text=raw_text, normalized_text=normalized_text, actual_output_text=actual_output_text))


if __name__ == '__main__':
    main()
