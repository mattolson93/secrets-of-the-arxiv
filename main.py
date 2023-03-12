import tarfile
import sys
import arxiv
from numpy import loadtxt


url = sys.argv[1]

if "arxiv" not in url: exit("bad url")

arxiv_id = url.split("/")[-1]
arxiv_id = arxiv_id.split(".")[:2]
arxiv_id = f"{arxiv_id[0]}.{arxiv_id[1]}"

paper = next(arxiv.Search(id_list=[arxiv_id]).results())
# Download the archive to the PWD with a default filename.
paper.download_source(filename="cur_download.tar.gz")
tar = tarfile.open("cur_download.tar.gz", "r:gz")
contents = []
for member in tar.getmembers():
    f = tar.extractfile(member)
    if f is not None and member.name.endswith(".tex"):
        #breakpoint()
        content = f.readlines()
        content = [c.decode("utf-8").strip() for c in content]

        contents.extend([c for c in content if c.startswith("%")])


######### bad word identification ##################
f = open('badwords.txt', 'r+')
badwords = [line for line in f.readlines()]
f.close()

output = []
for line in contents:
    for bad in badwords:
        if bad in line:
            output.append(line)

if len(output) == 0: print("no bad words hidden in this paper")

for o in output: print(o)
######### end bad word search #################
