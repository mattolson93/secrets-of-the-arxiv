import tarfile
import sys
import arxiv

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
         content = f.read()
         contents.append(content)

print(contents)
#TODO: actually search the contents for comments!
