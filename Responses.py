import requests


def sample_responses(input_link):
    user_message = str(input_link).lower()

    k = user_message.split("//")
    if "tapas.io" in k[1]:
        image_url = get_image_url(user_message)
        return image_url


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
    line = lines[531]

    temp_link = line.split("\"")
    print(temp_link[1])

    return temp_link[1]
