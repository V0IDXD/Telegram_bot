import requests


def get_image_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(url, headers=headers)

    with open('source.txt', 'w', encoding='utf-8') as f:
        f.write('{}\n'.format(result.content.decode()))

    # Open the source file for reading
    with open('source.txt', 'r') as f:
        lines = f.readlines()

    # Get the desired line (line 532 in this example)
    name = lines[512]
    line = lines[531]
    line_sc = lines[546]

    start_index = name.index('"') + 1
    end_index = name.index('"', start_index)
    title = name[start_index:end_index]
    temp_link = line.split("\"")
    temp_sc = line_sc.split("\"")

    print(temp_link[1])
    print(temp_sc[1])
    print(title)

    return title, temp_link[1], temp_sc[1]

