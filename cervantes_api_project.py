from urllib.request import urlopen
import json
print("This program gives you the links to new free downloadable tracks.")
while True:
    link_list = []
    track_list = []
    url = 'https://api.soundcloud.com/tracks?client_id=e5651410a19ca352f913924d71712e96'
    req = urlopen(url)
    encoding = req.headers.get_content_charset()
    data = json.loads(req.read().decode(encoding))
    for i in range(len(data)):
        d = data[i]
        for key in d:
            if key == "downloadable" and d["downloadable"] is True:
                track = d["title"]
                link = d["permalink_url"]
                track_list.append(track)
                link_list.append(link)
    for l in range(len(link_list)):
        link_num = l + 1
        print('''track %s: %s
%s''' % (link_num, track_list[l], link_list[l]))
    m = int(input('''Do you want to run again? Yes(1) No(2)
'''))
    if m == 2:
        break
 
