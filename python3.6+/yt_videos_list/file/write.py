def update_status(video_number, total_writes, incrementer):
    video_number += incrementer
    total_writes += 1
    return video_number, total_writes
def txt_entry(file, markdown_formatting, selenium_element, newline, spacing, video_number, incrementer, total_writes):
    if markdown_formatting:
        file.write(f'### Video Title:  {selenium_element.get_attribute("title")}{newline}')
        file.write(f'Video Number: {video_number}{newline}')
    else:
        file.write(f'Video Number: {video_number}{newline}')
        file.write(f'Video Title:  {selenium_element.get_attribute("title")}{newline}')
    file.write(f'Video URL:    {selenium_element.get_attribute("href")}{newline}')
    file.write(f'Watched?{spacing}{newline}')
    file.write(f'Watch again later?{spacing}{newline}')
    file.write(f'Notes:{spacing}{newline}')
    file.write('*'*75 + newline)
    return update_status(video_number, total_writes, incrementer)
def csv_entry(writer, selenium_element, video_number, incrementer, total_writes):
    writer.writerow({'Video Number': f'{video_number}', 'Video Title': f'{selenium_element.get_attribute("title")}', 'Video URL': f'{selenium_element.get_attribute("href")}', 'Watched?': '', 'Watch again later?': '', 'Notes': ''})
    return update_status(video_number, total_writes, incrementer)
